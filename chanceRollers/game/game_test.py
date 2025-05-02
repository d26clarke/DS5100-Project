
from game import Game
import unittest
import numpy as np

from theDie.die import Die



# Create variable to capture results when necessary
results: str = ""

class GameTestSuite(unittest.TestCase):
  
    def test_1_check_is_container_list(self): 

        with self.assertRaises(TypeError):
        #Generate TypeError by passing a set object
            listDieOne: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)

            dieOneInstance: Die = Die(listDieOne)

            diceList: set = ((dieOneInstance))
            Game(diceList)

    def test_2_check_if_die_object(self): 

        with self.assertRaises(TypeError):
        #Generate TypeError by passing a set object
            listDieOne: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            listDieTwo: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            listDieThree: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)

            diceList: set = [listDieOne, listDieTwo, listDieThree]
            Game(diceList)


    def test_3_change_die_weight(self): 

    
        with self.assertRaises(ValueError):
            #Generate ValueError by passing an invalid option for narrow or wide
            listDieOne: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            listDieTwo: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            listDieThree: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)

            dieOneInstance: Die = Die(listDieOne)
            dieTwoInstance: Die = Die(listDieTwo)
            dieThreeInstance: Die = Die(listDieThree)


            #Manage Die weighting
            dieOneInstance.change_die_weight('2', .40)
            dieTwoInstance.change_die_weight('2', .30)
            dieThreeInstance.change_die_weight('2', .20)

            diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance]
            myInstance: Game = Game(diceList)

            #Let it roll!
            myInstance.play(2)

            #The Results
            myInstance.playResults("x")

    
    def test_4_check_die_faces(self): 

    
        with self.assertRaises(ValueError):
            
            #Generate ValueError if all die have the same faces
            
            # The Die
            listDieOne: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            listDieTwo: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            listDieThree: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            listDieFour: np.array = np.array(['1', '2'], dtype=str)

            dieOneInstance: Die = Die(listDieOne)
            dieTwoInstance: Die = Die(listDieTwo)
            dieThreeInstance: Die = Die(listDieThree)
            dieFourInstance: Die = Die(listDieFour)

            #Manage Die weighting
            dieOneInstance.change_die_weight('2', .40)
            dieTwoInstance.change_die_weight('2', .30)
            dieThreeInstance.change_die_weight('2', .20)

            diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance, dieFourInstance]
            myInstance: Game = Game(diceList)

            #Let it roll!
            myInstance.play(2)

            #The Results
            myInstance.playResults("x")



    
    
        

  
                

if __name__ == '__main__':
    unittest.main(verbosity=3)