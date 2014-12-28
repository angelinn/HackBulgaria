from functools import reduce


class GenerateTests:
    TEST_TEMPLATE = 'test_template.txt'

    def __init__(self, file_name):
        self.test_file = file_name

    def load_template(self):
        template_file = open(self.TEST_TEMPLATE)
        output = template_file.read()
        template_file.close()

        return output

    def load_input(self):
        input_file = open(self.test_file, 'r')
        content = input_file.read().split('\n')
        input_file.close()

        return content

    def is_import(self, line):
        if line[:6] == 'import' or line[:4] == 'from':
            return True

        return False

    def concat(self, one, other):
        return one + other

    def make_class_name(self):
        without_extension = self.test_file[:-4]



    def go(self):
        output = self.load_template()
        test_file = self.load_input()

        res = reduce(self.concat, filter(self.is_import, test_file), '')

        output = output.replace('{imports}', res)
        output = output.replace('{class_name}', self.test_file)
        print(output)

GenerateTests('is_prime_test.dsl').go()
