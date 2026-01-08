import unittest
from Archive.calculator import Calculator

class TestOperations(unittest.TestCase):
    
   # def test_sum(self):
    #    calc = Calculator(8,2)
     #   answer = calc.get_sum()
      #  print(f"The answer was {answer}. \n Test Results:")
       # self.assertEqual(answer, 10, "The answer wasn't 10.")

    #def test_product(self):
     #   calc = Calculator(8,2)
      #  answer = calc.get_product()
       # print(f"The answer was {answer}. \n Test Results:")
        #self.assertEqual(answer, 16, "The answer wasn't 16.")

    def test_division(self):
        calc = Calculator(64,12)
        answer = calc.get_division()
        print(f"The answer was {answer}. \n Test Results:")
        self.assertEqual(answer, 5, "The answer wasn't 5.")

   # def test_difference(self):
    #    calc = Calculator(8,2)
     #   answer = calc.get_difference()
      #  print(f"The answer was {answer}. \n Test Results:")
       # self.assertEqual(answer, 6, "The answer wasn't 6.")

if __name__ == "__main__":
    unittest.main()