import unittest
from testing.matematika_test import TestKelilingLingkaran

if __name__ == "__main__":
    testing_keliling_lingkaran = unittest.TestLoader().loadTestsFromTestCase(
        TestKelilingLingkaran
    )
    all_tests = unittest.TestSuite([testing_keliling_lingkaran])

    unittest.TextTestRunner(verbosity=2).run(all_tests)
