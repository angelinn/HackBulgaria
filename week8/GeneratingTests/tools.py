class Tools:
    TEST_CASE_BODY = '\tdef testCase{}(self):\n\t\t{}\n\n'
    _ASSERT_TRUE = 'self.assertTrue({}, {})'
    _ASSERT_FALSE = 'self.assertFalse({}, {})'
    _ASSERT_EQUAL = 'self.assertEqual({}, {}, {})'

    @staticmethod
    def is_test_case(line):
        if '->' in line:
            return True

        return False

    @staticmethod
    def is_comment(line):
        if line[:1] == '"' and line[-1:] == '"':
            return True

        return False

    @staticmethod
    def make_class_name(file_name):
        result = list(file_name[:-4])
        result[0] = result[0].upper()

        for i in range(len(result)):
            if result[i] == '_':
                result[i] = ''

                if i < len(result) - 1:
                    result[i + 1] = result[i + 1].upper()

        return ''.join(result)

    @staticmethod
    def is_import(line):
        if line[:6] == 'import' or line[:4] == 'from':
            return True

        return False

    @staticmethod
    def concat(one, other):
        return one + other

    @classmethod
    def build_case(cls, case):
        raw = case.split(' -> ')
        message = raw[0]
        condition = raw[1].split(' == ')

        if condition[1] == 'True':
            return cls._ASSERT_TRUE.format(condition[0], message)
        if condition[1] == 'False':
            return cls._ASSERT_FALSE.format(condition[0], message)
        else:
            return cls._ASSERT_EQUAL.format(condition[0], condition[1], message)
