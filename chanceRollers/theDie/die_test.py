from die import Die
import unittest
import numpy as np


# Create variable to capture results when necessary
results: str = ""

class DieTestSuite(unittest.TestCase):
  
  def test_1_check_distinct_die_weights(self): 

    with self.assertRaises(ValueError):
      #Generate ValueError by passing numpy array argument that contains a set of non-distinct items  
      theDie: np.array = np.array(['1', '1', '3', '4', '5', '6'], dtype=str)
      Die(theDie)

  def test_2_change_die_weight(self): 

    with self.assertRaises(IndexError):
      theDie: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
      myInstance: Die = Die(theDie)
      #Generate IndexError by passing a non-existent face_name argument
      myInstance.change_die_weight('9', .30)

  def test_3_change_die_weight(self): 

    
    with self.assertRaises(TypeError):
      theDie: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
      myInstance: Die = Die(theDie)
      #Generate TypeError by passing new_weight argument as a string
      myInstance.change_die_weight('3', '30')


    
    
        

  
                

if __name__ == '__main__':
    unittest.main(verbosity=3)