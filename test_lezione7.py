import unittest
from lezione7 import CSVFile
class testgetdata(unittest.TestCase):
    def test_linee(self):
        elemento=CSVFile('shampoo_sales.csv')
        controllo_file= elemento.get_data()[0]
        self.assertEqual(controllo_file, ['01-01-2012', '266.0'])