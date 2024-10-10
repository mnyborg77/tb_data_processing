import unittest
from reading import read_tb_functions
from utils import count_orf_clas, orfs_w_protein_hydro, calc_multiple_m


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Obtains the dictionary to be used in the tests.
        print("Creating dictionaries")
        cls.cl, cls.func = read_tb_functions('data/tb_functions.pl')

    def test_count_orf_clas(self):
        print("Starting test_count_orf_clas")
        # Obtains result from function
        orf_pr_clas = count_orf_clas(self.cl, self.func)
        # Test no. ORFs pr class.
        self.assertEqual(orf_pr_clas['1,1,0,0'], 0)
        self.assertEqual(orf_pr_clas['1,1,4,0'], 4)
        self.assertEqual(orf_pr_clas['2,1,8,0'], 8)

    def test_orfs_w_protein_hydro(self):
        print("Starting test_orfs_w_protein_hydro")
        # Obtains result from function.
        prot, hydro = orfs_w_protein_hydro(self.func)
        # Test all keys in prot dictionary starts with `tb`.
        self.assertEqual(len([x for x in prot.keys() if not x.startswith('tb')]), 0)
        # Test ORFs (keys) has right class(value).
        self.assertEqual(prot['tb1909'], '1,10,1,0')
        self.assertEqual(hydro['tb1731'], '1,1,1,0')
        # Test that all keys in hydro include the word hydro in description.
        self.assertEqual(len([k for k, v in hydro.items()
                              if 'hydro' not in self.func[v][k][1]]), 0)

    def test_calc_multiple_m(self):
        print("Starting test_calc_multiple_m")
        # Obtains result from function.
        ms = calc_multiple_m(self.cl)
        # Test counted values for different m.
        self.assertEqual(ms[9], 3)
        self.assertEqual(ms[7], 19)


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUtils))
unittest.TextTestRunner(verbosity=2).run(suite)