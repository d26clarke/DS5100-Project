<h1 align="center">
<img src="img/chanceRollersLogoFINAL.png" width="300">
</h1><br>



Chance Rollers is die rolling simulator package.

- **Source code:** https://github.com/d26clarke/DS5100-Project/tree/main


The Features:

- Generate multiface die with die specific weights
- Alter die specific weights
- Die can be rolled one (1) to n times per game
- Display game results to include jackpot results
- Computes how many times a given face is rolled in each event
- Computes the distinct combinations of faces rolled, along with their counts
- Computes the distinct permutations of faces rolled, along with their counts
- Computes how many times a given face is rolled in each event

Synopsis:

Installation:

    At your system command prompt,
    pip install chanceRollers
        result:
            Obtaining ChanceRollers
        Installing build dependencies ... done
        Checking if build backend supports build_editable ... done
        Getting requirements to build editable ... done
        Preparing editable metadata (pyproject.toml) ... done
        Requirement already satisfied: numpy in /Users/ddclarke/.pyenv/versions/3.12.7/lib/python3.12/site-packages (from Chance-Rollers==3.0) (2.1.3)
        Requirement already satisfied: pandas in /Users/ddclarke/.pyenv/versions/3.12.7/lib/python3.12/site-packages (from Chance-Rollers==3.0) (2.2.3)
        Requirement already satisfied: python-dateutil>=2.8.2 in /Users/ddclarke/.pyenv/versions/3.12.7/lib/python3.12/site-packages (from pandas->Chance-Rollers==3.0) (2.9.0.post0)
        .............
        Successfully built Chance-Rollers
        Installing collected packages: Chance-Rollers
        Successfully installed Chance-Rollers-3.0

    import required modules
        For Example: Let's play a game where we create three die, give the three die the same weight
                        and roll the three die ten (10) times.  You will be able to review the results and see if 
                        you hit any jackpots!  You will also be able to see differing combinations and permutations
                        of your die rolls.

        In a file called chanceRollersDemo.py, use the following code sample

            from theDie.die import Die
            from analyze.analyzer import Analyzer
            from game.game import Game

            # The Die
            listDieOne: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            listDieTwo: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            listDieThree: np.array = np.array(['1', '2', '3', '4', '5', '6'], dtype=str)
            
            dieOneInstance: Die = Die(listDieOne)
            dieTwoInstance: Die = Die(listDieTwo)
            dieThreeInstance: Die = Die(listDieThree)
            
            #Manage Die weighting
            dieOneInstance.change_die_weight('2', .20)
            dieTwoInstance.change_die_weight('2', .20)
            dieThreeInstance.change_die_weight('2', .20)

            diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance]

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



API description
----------------------

class Die(builtins.object)
 |  Die(theDie: <built-in function array>) -> None
 |
 |  A class representing a Die (2-Face: Die of type Coin or 6-Face Die )
 |
 |  Attributes:
 |
 |      _privateDataFrame (pd.DataFrame): Used to hold both die face and weight data points
 |
 |  Methods:
 |      __init__():
 |      change_die_weight()
 |      roll_die()
 |      die_state()
 |
 |  Methods defined here:
 |
 |  __init__(self, theDie: <built-in function array>) -> None
 |      Initializes Die Class
 |         Initializes the weights to 1 for each die face
 |         Saves die faces and weights _privateDataFrame with die faces in the index
 |
 |      Args:
 |          theDie (np.array):  NumPy array of Die faces where array dtype(strings|numbers)
 |
 |      Raises:
 |          ValueError: If die faces are not distinct values
 |          TypeError: If die is not of type NumPy Array
 |
 |      Returns:
 |          None
 |
 |  change_die_weight(self, face_name: str, new_weight: float) -> None
 |      Takes two arguments: face_name  new_weight
 |      Checks:
 |          face_name: must exist in die array (If not, raises an IndexError)
 |          new_weight: must be of type float and castable as numeric (If not, raises a TypeError)
 |
 |      Actions:
 |          If new weight is of type float, subtract 1 from new weight to obtain the percentage which will be distributed among the
 |          remaining die faces
 |
 |          If new weight is of type int, convert integer to float  then subtract 1 from generated float to obtain the percentage which will be distributed among the
 |          remaining die faces
 |
 |      Note(s):  Weights must sum to 1
 |
 |  die_state(self) -> list
 |      Takes no arguments
 |
 |      Returns a copy of the private data frame
 |
 |  roll_die(self, how_many_times: int = 1) -> list
 |      Simulates a dice roll with weighted probabilities for each face.
 |
 |      Arg Checks:
 |          how_many_times: number of requested die rolls; default is 1 roll
 |
 |      Returns:
 |          a python list of outcomes
 |



 |  Game(theDice: list[theDie.die.Die]) -> None
 |
 |  A class representing a game of rolling one or more similar dice (Die objects) one or more times
 |  Game objects have a behavior to play a game, i.e. to roll all of the dice a given number of times
 |  Game objects only keep the results of their most recent play
 |
 |
 |  Attributes:
 |
 |      self._privateGameDataFrame (pd.DataFrame): a private variable Used to hold game results
 |
 |  Methods:
 |      play()
 |      playResults()
 |
 |  Methods defined here:
 |
 |  __init__(self, theDice: list[theDie.die.Die]) -> None
 |      Initializes Game Class with Python list, as a single paramter, that contains one or more dice
 |
 |          self.theDice = theDice
 |          self._privateGameDataFrame = pd.DataFrame = pd.DataFrame(emptyDict)
 |
 |
 |      Args:
 |          theDice (list):  NumPy array of Die faces where array dtype(strings|numbers)
 |
 |      Raises:
 |          TypeError: If container for Die objects is not of type list
 |          TypeError: If list item is not a Die object
 |
 |      Returns:
 |          None
 |
 |  play(self, how_many_rolls: int) -> None
 |      Takes an integer parameter to specify how many times the dice should be rolled and
 |          saves the result of the play to self._privateGameDataFrame
 |
 |          Using the playResults methond, self._privateGameDataFrame will be returned
 |          in wide format unless narrow form (n) is requested.
 |
 |
 |      Args:
 |          how_many_rolls (int):  How many times to roll dice
 |
 |      Raises:
 |          None
 |
 |      Returns:
 |          None
 |
 |  playResults(self, df_frame_type: str = 'w') -> pandas.core.frame.DataFrame
 |      Returns a copy of self._privateGameDataFrame in wide form (w) (DEFAULT) to the user
 |         unless narrow form (n) is requested.
 |
 |          Using the playResults methond, self._privateGameDataFrame will be returned
 |          in wide format unless narrow form (n) is requested.
 |
 |
 |      Args:
 |          df_frame_type (str):  parameter to return the data frame in narrow (n) or wide (w) form where wide is DEFAULT
 |
 |      Raises:
 |          ValueError: if the user passes an invalid option for narrow or wide
 |
 |      Returns:
 |          None




class Analyzer(builtins.object)
 |  Analyzer(theGame: game.game.Game) -> None
 |
 |  A class that provides descriptive statistical properties about a game object
 |
 |
 |  Attributes:
 |
 |      None
 |
 |  Methods:
 |      jackpots()
 |      dieFaceCounter()
 |      dieComboCounter()
 |      diePermutationCounter()
 |
 |  Methods defined here:
 |
 |  __init__(self, theGame: game.game.Game) -> None
 |      Initializes Analyzer Class with a Game object, as a single paramter
 |
 |          self.theGame = theGame
 |
 |      Args:
 |          theGame (Game):  Game object with game results
 |
 |      Raises:
 |          ValueError: If the parameter is not a Game object
 |
 |      Returns:
 |          None
 |
 |  dieComboCounter(self) -> pandas.core.frame.DataFrame
 |      Computes the distinct combinations of faces rolled, along with their counts
 |
 |          NOTE:  Combinations are order-independent and may contain repetitions
 |                 The data frame should have a MultiIndex of distinct combinations and a column for the associated counts
 |
 |
 |      Args:
 |          None
 |
 |      Raises:
 |          None
 |
 |      Returns:
 |          pd.DataFrame of results
 |
 |  dieFaceCounter(self) -> pandas.core.frame.DataFrame
 |      Computes how many times a given face is rolled in each event.
 |
 |          For Example:
 |          If a roll of five dice has all sixes,
 |          then the counts for this roll would be 5 for the face value 6 and 0 for the other faces
 |
 |
 |      Args:
 |          None
 |
 |      Raises:
 |          None
 |
 |      Returns:
 |          pd.DataFrame of results
 |
 |  diePermutationCounter(self) -> pandas.core.frame.DataFrame
 |      Computes the distinct permutations of faces rolled, along with their counts
 |
 |          NOTE:  Permutations are order-dependent and may contain repetitions
 |                 The data frame should have a MultiIndex of distinct permutations and a column for the associated counts
 |
 |
 |      Args:
 |          None
 |
 |      Raises:
 |          None
 |
 |      Returns:
 |          pd.DataFrame of results
 |
 |  jackpots(self) -> int
 |      Computes how many times the game resulted in a jackpot
 |
 |          A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die
 |
 |
 |
 |      Args:
 |          None
 |
 |      Raises:
 |          None
 |
 |      Returns:
 |          None
 |
