import unittest
import os
from wc import wc


class TestWC(unittest.TestCase):
    def setUp(self):
        self.file_to_count = open('wc_test.txt', 'w')

    def tearDown(self):
        self.file_to_count.close()
        os.remove('wc_test.txt')

    def test_usual_input(self):
        content = ('Now indulgence dissimilar for his thoroughly has terminated. '
                   'Agreement offending commanded my an. Change wholly say why eldest period. '
                   'Are projection put celebrated particular unreserved joy unsatiable its. '
                   'In then dare good am rose bred or. On am in nearer square wanted.\n'
                   'Of resolve to gravity thought my prepare chamber so. '
                   'Unsatiable entreaties collecting may sympathize nay interested instrument. '
                   'If continue building numerous of at relation in margaret. '
                   'Lasted engage roused mother an am at. Other early while if by do to. '
                   'Missed living excuse as be. Cause heard fat above first shall for. '
                   'My smiling to he removal weather on anxious.\n'
                   'Ferrars all spirits his imagine effects amongst neither. '
                   'It bachelor cheerful of mistaken. '
                   'Tore has sons put upon wife use bred seen. '
                   'Its dissimilar invitation ten has discretion unreserved. '
                   'Had you him humoured jointure ask expenses learning. '
                   'Blush on in jokes sense do do. Brother hundred he assured reached on up no. '
                   'On am nearer missed lovers. To it mother extent temper figure better.\n')

        self.file_to_count.write(content)
        self.file_to_count.flush()

        self.file_to_count = open('wc_test.txt', 'r')
        self.assertEqual(1030, wc(self.file_to_count, 'chars'))
        self.file_to_count = open('wc_test.txt', 'r')
        self.assertEqual(166,  wc(self.file_to_count, 'words'))
        self.file_to_count = open('wc_test.txt', 'r')
        self.assertEqual(4, wc(self.file_to_count, 'lines'))

if __name__ == '__main__':
    unittest.main()
