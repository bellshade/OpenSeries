import unittest
from testing.matematika_testing import TestKelilingLingkaran

if __name__ == "__main__":
    testing_keliling_lingkaran = unittest.TestLoader().loadTestsFromTestCase(
        TestKelilingLingkaran
    )
    semua_testing = unittest.TestSuite(testing_keliling_lingkaran)

    unittest.TextTestRunner(verbosity=2).run(semua_testing)
