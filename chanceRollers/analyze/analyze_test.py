
import unittest
import numpy as np

from theDie.die import Die
from game.game import Game
from analyze.analyzer import Analyzer

# Create variable to capture results when necessary
results: str = ""

class AnalyzeTestSuite(unittest.TestCase):
  
    def test_1_check_is_game_object(self): 

        with self.assertRaises(ValueError):
            #Generate ValueError by passing an invalid game object
            # The Die
            listDieOne: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            listDieTwo: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            listDieThree: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            #listDieFour: np.array = np.array([1.0, 2.0], dtype=float)

            dieOneInstance: Die = Die(listDieOne)
            dieTwoInstance: Die = Die(listDieTwo)
            dieThreeInstance: Die = Die(listDieThree)
            #dieFourInstance: Die = Die(listDieFour)

            #Manage Die weighting
            dieOneInstance.change_die_weight('2', .20)
            dieTwoInstance.change_die_weight('2', .20)
            dieThreeInstance.change_die_weight('2', .20)

            diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance]

            myErrorInstance: list = list(diceList)
            
            myAnalyerErr: Analyzer = Analyzer(myErrorInstance)

                    

if __name__ == '__main__':
    unittest.main(verbosity=3)