import unittest
from testing.matematika_test import (
    TestKelilingLingkaran,
    TestRadianKeDerajat,
    TestDiameterLingkaran,
    TestPersamaanLinear,
    TestRataRata,
    TestFaktorial,
    TestPermutasi,
    TestKombinasi,
    TestFPB,
    TestFaktorPrima,
    TestMatriksTranspose,
)

if __name__ == "__main__":
    testing_matematika = unittest.TestLoader().loadTestsFromTestCase(
        TestKelilingLingkaran,
        TestRadianKeDerajat,
        TestDiameterLingkaran,
        TestPersamaanLinear,
        TestRataRata,
        TestFaktorial,
        TestPermutasi,
        TestKombinasi,
        TestFPB,
        TestFaktorPrima,
        TestMatriksTranspose,
    )
    all_tests = unittest.TestSuite([testing_matematika])

    unittest.TextTestRunner(verbosity=2).run(all_tests)
