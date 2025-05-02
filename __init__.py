#Project Version Number
#This number will change for each release

__version__ = "0.3.0"

candidateId: str = "thq3hn"
print(f"Welcome Chance Rollers!  Powered By UVA MSDS Candidate: {candidateId}")

from .chanceRollers.theDie.die import Die
from .chanceRollers.game.game import Game
from .chanceRollers.analyze.analyzer import Analyzer