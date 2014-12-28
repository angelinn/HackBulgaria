from functools import reduce
from tools import Tools
from file_format_exception import FileFormatException


class GenerateTests:
    TEST_TEMPLATE = 'test_template.txt'

    def __init__(self, file_name):
        self.test_name = file_name
        self.output = self.load_template()
        self.test_file = self.load_input()

    def load_template(self):
        template_file = open(self.TEST_TEMPLATE)
        output = template_file.read()
        template_file.close()

        return output

    def load_input(self):
        input_file = open(self.test_name, 'r')
        content = input_file.read().split('\n')
        input_file.close()

        return content

    def set_imports(self):
        imports = reduce(Tools.concat, filter(Tools.is_import, self.test_file), '')
        self.output = self.output.replace('{imports}', imports)

    def set_class_name(self):
        self.output = self.output.replace('{class_name}', Tools.make_class_name(self.test_name))

    def set_comments(self):
        comment = list(filter(Tools.is_comment, self.test_file))
        if len(comment) < 1:
            return

        self.output = self.output.replace('{comments}', comment[0])

    def set_test_cases(self):
        result = ''
        cases = list(filter(Tools.is_test_case, self.test_file))

        for i, case in enumerate(cases):
            if case[0] != '"':
                raise FileFormatException

            result += Tools.TEST_CASE_BODY.format(i, Tools.build_case(case))

        self.output = self.output.replace('{test_cases}', result)

    def go(self):
        try:
            self.set_imports()
            self.set_class_name()
            self.set_comments()
            self.set_test_cases()

        except FileFormatException:
            print('There was a problem with the .dsl file format.')

        return self.output

if __name__ == '__main__':
    data = GenerateTests('is_prime_test.dsl').go()
    print(data)
