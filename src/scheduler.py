from dataclasses import dataclass
from typing import Text

@dataclass
class TimeControl:
  clock: int
  increment: int


@dataclass
class Level:
  name: Text
  min_elo: int = None
  max_elo: int = None


TIME_CONTROLS = [
  TimeControl(3, 2),
  TimeControl(5, 3),
  TimeControl(7, 5),
  TimeControl(10, 0),
]

LEVELS = [
  Level('Beginner', None, 1500),
  Level('Intermediate', 1400, 1700),
  Level('Master', 1600, None),
]