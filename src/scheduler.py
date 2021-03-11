from dataclasses import dataclass
from typing import Dict, Text, Union

import datetime


@dataclass
class TimeControl:
  clock: int
  increment: int


@dataclass
class Level:
  name: Text
  min_elo: int = None
  max_elo: int = None


@dataclass
class Arena:
  level: Level
  time_control: TimeControl
  start_date: datetime.datetime

  duration: int = 120
  min_rated: int = 10
  
  def prepare_request(self) -> Dict[Text, Union[Text, int, bool]]:
    return {
      'name': '{} {}+{} Chess960'.format(
        self.level.name, self.time_control.clock, self.time_control.increment),
      'clockTime': self.time_control.clock,
      'clockIncrement': self.time_control.increment,
      'minutes': self.duration,
      'variant': 'chess960',
      'description': 'Daily Chess960 Arena. Times cycle daily so that everyone'
        'gets a chance to play their favorite time control. Please put all'
        'suggestions in the forum! Have fun :)',
      'conditions.teamMember.teamId': 'chess960',
      'conditions.minRating.rating': self.level.min_elo,
      'conditions.maxRating.rating': self.level.max_elo,
      'conditions.nbRatedGame.nb': self.min_rated,
    }
  

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