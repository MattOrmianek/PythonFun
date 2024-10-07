import unittest

def disemvowel(string_):
    fixed_string = ''
    vowels = 'aeiou'
    for char in string_:
        if char.lower() in vowels:
            continue
        fixed_string += char

    return fixed_string


def basic_tests():
    suite = unittest.TestSuite()

    def test_fixed_1():
        assert disemvowel('test_fixed_1') == 'tst_fxd_1'

    def test_fixed_2():
        assert disemvowel('test_fixed_2') == 'tst_fxd_2'

    def test_fixed_3():
        assert disemvowel('test_fixed_3') == 'tst_fxd_3'

    suite.addTest(unittest.FunctionTestCase(test_fixed_1))
    suite.addTest(unittest.FunctionTestCase(test_fixed_2))
    suite.addTest(unittest.FunctionTestCase(test_fixed_3))

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    basic_tests()