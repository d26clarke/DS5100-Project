import pandas as pd

import numpy as np

from theDie.die import Die
from game.game import Game

class Analyzer:
    """
    A class that provides descriptive statistical properties about a game object


    Attributes:
       
        None
    
    Methods:
        jackpots() 
        dieFaceCounter()
        dieComboCounter()
        diePermutationCounter()
    """

    def __init__(self, theGame: Game) -> None:
        """Initializes Analyzer Class with a Game object, as a single paramter

            self.theGame = theGame

        Args:
            theGame (Game):  Game object with game results

        Raises:
            ValueError: If the parameter is not a Game object

        Returns:
            None
        """
        
        print(f"The Inital Type: {type(theGame)}")

        #Must be type Game
        if not type(theGame) is Game:
            raise ValueError("The parameter must be of type Game!") 
        
        self.theGame = theGame

        print(f"Game Results (WideFormat): \n{self.theGame.playResults()}")
        print(f"Game Results (NarrowFormat): \n{self.theGame.playResults("n")}")


    
    def jackpots(self) -> int:
        
        """Computes how many times the game resulted in a jackpot 

            A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die



        Args:
            None

        Raises:
            None

        Returns:
            None
        """

        print(f"Entering method jackpots... \n")

        numberOfJackpots: int = 0

        #Load play Results
        diePlayResultsFrame: pd.DataFrame = self.theGame.playResults("w")
        print(f"The DataFrame to examine for jackpot notifications: \n{diePlayResultsFrame}")

        #Check all rows in this dataframe
        rowsInDataFrame: int = len(diePlayResultsFrame)
        #print(f"Number of Rows in DataFrame: {rowsInDataFrame}")
        #Use the following for Loop to get to each Series 
        for rowIdx in range(1,rowsInDataFrame + 1):
            #print(f"Row Index: {rowIdx}")
            #Use the series duplicated function to determine if there is a jackpot
            #If the number of duplicates plus one matches the len of the series then 
            #we have a jackpot.  NOTE:  We have to add one to the number of duplicates since the first element 
            #in the series is not seen as a duplicate.
            #print(f"**********************")
            #print(f"DATA: \n{type(diePlayResultsFrame.loc[rowIdx])}")
            #print(f"Length of the Series: {len(diePlayResultsFrame.loc[rowIdx])}")
            #print(f"**********************")

            duplicates: pd.Series = diePlayResultsFrame.loc[rowIdx].duplicated()
            #print(f"The Duplicates \n{duplicates}")
            num_duplicates: np.int64 = duplicates.sum()
            #print(f"The Number of Duplicates \n{num_duplicates}")
            #print(f"Corrected Offset: {num_duplicates + 1}")

            if len(diePlayResultsFrame.loc[rowIdx]) == num_duplicates + 1:
                #We have a jackpot
                numberOfJackpots += 1
        
        return numberOfJackpots

    def dieFaceCounter(self) -> pd.DataFrame:
        
        """Computes how many times a given face is rolled in each event.
           
            For Example:
            If a roll of five dice has all sixes, 
            then the counts for this roll would be 5 for the face value 6 and 0 for the other faces


        Args:
            None

        Raises:
            None

        Returns:
            pd.DataFrame of results
        """

        print(f"Entering dieFaceCounter...")


        print(f"DEBUG TEST: \n {self.theGame.playResults("w").apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)}")

        
        df_ForFaceCounts: pd.DataFrame = self.theGame.playResults("w").apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)

        #Set Index Name
        df_ForFaceCounts.index.name = "RollNum"
        
        #print(f"Reset: {diePlayResultsFrame.reset_index()}")
        #print(f"Face Counts DataFrame: \n{df_ForFaceCounts}")

        return df_ForFaceCounts


    def dieComboCounter(self) -> pd.DataFrame:
        
        """Computes the distinct combinations of faces rolled, along with their counts
           
            NOTE:  Combinations are order-independent and may contain repetitions
                   The data frame should have a MultiIndex of distinct combinations and a column for the associated counts


        Args:
            None

        Raises:
            None

        Returns:
            pd.DataFrame of results
        """

        print(f"Entering dieComboCounter...") 

         #Load play Results
        diePlayResultsFrame: pd.DataFrame = self.theGame.playResults("w")

       
        dfMultiIndex: pd.DataFrame = diePlayResultsFrame.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('Occurrence')
        dfMultiIndex.index.names = ["DieValue:"+str(i) for i in range(1, len(diePlayResultsFrame.columns.to_list())+1)]

        return dfMultiIndex
    

    def diePermutationCounter(self) -> pd.DataFrame:
        
        """Computes the distinct permutations of faces rolled, along with their counts
           
            NOTE:  Permutations are order-dependent and may contain repetitions
                   The data frame should have a MultiIndex of distinct permutations and a column for the associated counts


        Args:
            None

        Raises:
            None

        Returns:
            pd.DataFrame of results
        """

        print(f"Entering diePermutationCounter...") 

        #Load play Results
        diePlayResultsFrame: pd.DataFrame = self.theGame.playResults("w")

        dfMultiIndex = diePlayResultsFrame.set_index(diePlayResultsFrame.columns.to_list(), append=True)
        dfMultiIdxPermCnt = dfMultiIndex.groupby(diePlayResultsFrame.columns.to_list()).size().to_frame("Occurence")

        #new_names = ["#"+str(i)+" die's value" for i in range(1, len(self._game._list_of_die)+1)]
        #temp_df = self._game.show_result()
        #temp_df.columns = new_names
        #x = list(range(len(self._game._list_of_die)))
        #return temp_df.set_index(new_names).sort_index().groupby(level=x).size().to_frame("Occurence")

        return dfMultiIdxPermCnt

       

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
    dieOneInstance.change_die_weight('2', .20)
    dieTwoInstance.change_die_weight('2', .20)
    dieThreeInstance.change_die_weight('2', .20)


    #diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance, dieFourInstance]
    diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance]

    myErrorInstance: list = list(diceList)
    myInstance: Game = Game(diceList)

    #Let it roll!
    myInstance.play(10)

    myAnalyzerInstance: Analyzer = Analyzer(myInstance) 
    #myAnalyerErr: Analyzer = Analyzer(myErrorInstance)

    #Jackot Information
    print(f"Did I hit any jackpots? \n{myAnalyzerInstance.jackpots()}")

    print(f"Play Results(Wide Format): \n{myAnalyzerInstance.dieFaceCounter()}")

    #print(f"Play Results(Narrow Format): \n{myInstance.playResults("x")}")

    print(f"Play Results(Wide Format): \n{myAnalyzerInstance.dieComboCounter()}")

    print(f"Play Results(Wide Format): \n{myAnalyzerInstance.diePermutationCounter()}")
