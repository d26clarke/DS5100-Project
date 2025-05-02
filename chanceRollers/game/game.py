import pandas as pd

import numpy as np

from theDie import Die

class Game:
    """
    A class representing a game of rolling one or more similar dice (Die objects) one or more times
    Game objects have a behavior to play a game, i.e. to roll all of the dice a given number of times
    Game objects only keep the results of their most recent play


    Attributes:
       
        self._privateGameDataFrame (pd.DataFrame): a private variable Used to hold game results
    
    Methods:
        play() 
        playResults()
    """

    def __init__(self, theDice: list[Die]) -> None:
        """Initializes Game Class with Python list, as a single paramter, that contains one or more dice

            self.theDice = theDice
            self._privateGameDataFrame = pd.DataFrame = pd.DataFrame(emptyDict)


        Args:
            theDice (list):  NumPy array of Die faces where array dtype(strings|numbers)

        Raises:
            TypeError: If container for Die objects is not of type list 
            TypeError: If list item is not a Die object

        Returns:
            None
        """
        
        #print(f"The Inital Type: {type(theDice)}")

        #Must be type list
        if not type(theDice) is list:
            raise TypeError("The container for the dice must be of type list!") 

        #List items must be Die Objects
        for item in theDice:
            if not isinstance(item, Die):
                raise TypeError(f"List element: {item} is not of type {Die.__name__} !")
            #dieStateDataFrame: pd.DataFrame = item.die_state()
            #print(f"Length of each Die: {len(item.die_state())}")
        
        self.theDice = theDice

        #Use this empty dictionay object for private pandas dataFrame
        emptyDict = {'RollNum': [],
        'DieId': [],
        'DieValue': []}

        self._privateGameDataFrame: pd.DataFrame = pd.DataFrame(emptyDict)

        
        #All Die objects in list must have the same number of faces
        checkCoinFaces: bool = all(len(x.die_state()) == 2 for x in theDice)   #Two Face Coin
        checkDieFaces: bool = all(len(x.die_state()) == 6 for x in theDice)   #Six Face Die
        checkAlphaDieFaces: bool = all(len(x.die_state()) == 26 for x in theDice)   #Alphabet Face Die

        #print(f"Staus of checkCoinFaces: {checkCoinFaces}\n")
        #print(f"Staus of checkDieFaces: {checkDieFaces}\n")

        #Raise error if die objects do not have the same number of faces
        if checkCoinFaces == False and checkDieFaces == False and checkAlphaDieFaces == False:
            #print(f"DEBUG1:We have an issue!\n")
            raise ValueError(f"All Die objects in list must have the same number of faces!")
        else:
            print(f"We are good to go!\n")
    
    
    def play(self, how_many_rolls: int) -> None:
        
        """Takes an integer parameter to specify how many times the dice should be rolled and 
            saves the result of the play to self._privateGameDataFrame

            Using the playResults methond, self._privateGameDataFrame will be returned 
            in wide format unless narrow form (n) is requested. 


        Args:
            how_many_rolls (int):  How many times to roll dice

        Raises:
            None

        Returns:
            None
        """

        print(f"Entering method play: Number of requested rolls ({how_many_rolls})\n")

        print(f"Number of Die in play: {len(self.theDice)}")

        ## Add a new row to df_empty
        #df_empty.loc[len(df_empty)] = [1, 1, 'Face2']

        allDieRollResults: list = []

        dieID: int = 1
        for item in self.theDice:
            #print(f"DEBUG Die ID: {dieID}")
            dieRoll: list = item.roll_die(how_many_rolls)
            #print(f"DEBUG AAA: {dieRoll}")
            dieRollResults: list = [(i + 1, dieID, dieRoll[i]) for i in range(len(dieRoll))]
            allDieRollResults = allDieRollResults + dieRollResults
            dieID += 1

        #Save Results to private Dataframe with newly generated list
        self._privateGameDataFrame = pd.DataFrame(allDieRollResults, columns=['RollNum', 'DieId', 'DieValue'])



    def playResults(self, df_frame_type: str = 'w') -> pd.DataFrame:
        
        """Returns a copy of self._privateGameDataFrame in wide form (w) (DEFAULT) to the user 
           unless narrow form (n) is requested.

            Using the playResults methond, self._privateGameDataFrame will be returned 
            in wide format unless narrow form (n) is requested. 


        Args:
            df_frame_type (str):  parameter to return the data frame in narrow (n) or wide (w) form where wide is DEFAULT

        Raises:
            ValueError: if the user passes an invalid option for narrow or wide

        Returns:
            None
        """

        #print(f"Entering playResults...Requested Frame Type: {df_frame_type}")

        if (df_frame_type != "w") and (df_frame_type != "n"):
            raise ValueError(f"invalid option for (n)arrow or (w)ide: {df_frame_type}\n")

        if df_frame_type == "w":
            #Wide Format (DEFAULT)
            #print("Wide format DataFrame:\n", df_wide)
            return self._privateGameDataFrame.pivot(index='RollNum', columns='DieId', values='DieValue')
        elif df_frame_type == "n":
            #Narrow Format
            #return pd.MultiIndex.from_frame(self._privateGameDataFrame)
            return self._privateGameDataFrame.set_index(['RollNum', 'DieId'])
            

if __name__ == '__main__':

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
    dieOneInstance.change_die_weight('2', .40)
    dieTwoInstance.change_die_weight('2', .30)
    dieThreeInstance.change_die_weight('2', .20)


    #diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance, dieFourInstance]
    diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance]
    myInstance: Game = Game(diceList)

    #Let it roll!
    myInstance.play(3)

    #The Results
    print(f"Play Results(Wide Format): \n{myInstance.playResults()}")

    #print(f"Play Results(Narrow Format): \n{myInstance.playResults("n")}")

    #print(f"Play Results(Narrow Format): \n{myInstance.playResults("x")}")