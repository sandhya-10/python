import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def addition(n1,n2):
   return (n1+n2)

# DO NOT TOUCH THE BELOW CODE
class TestAddition(unittest.TestCase):

    def test_01(self):
        self.assertEqual(addition(3,2), 5)

    def test_02(self):
        self.assertEqual(addition(3,-5), -2)

    def test_03(self):
        self.assertEqual(addition(0,3), 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
