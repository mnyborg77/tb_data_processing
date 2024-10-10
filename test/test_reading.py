import unittest
from reading import read_tb_functions, read_tb_data


class TestReading(unittest.TestCase):

    def test_read_tb_functions(self):
        print("Starting test_read_tb_functions")
        # Obtains result from function
        cl, func = read_tb_functions('data/tb_functions.pl')
        # Test class dictionary has 123 classes.
        self.assertEqual(len(cl), 123)
        # Test key-value pairs for class dictionary.
        self.assertEqual(cl['1,1,3,0'], "Fatty acids ")
        # Test number of orfs for class in function dictionary.
        self.assertEqual(len(func['1,1,1,0']), 22)

    def test_read_tb_data(self):
        print("Starting test_read_tb_data")
        # Obtains result from function
        data = read_tb_data('data/orfs/')
        # Test number of related orfs.
        self.assertEqual(len(data['tb5']), 18)
        self.assertEqual(len(data['tb11']), 9)


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestReading))
unittest.TextTestRunner(verbosity=2).run(suite)
