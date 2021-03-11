from dataclasses import dataclass
from typing import Dict, Text, Union

import datetime
import dotenv
import os
import pathlib
import requests


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
  start_datetime: datetime.datetime

  duration: int = 120
  min_rated: int = 10
  
  def prepare_request(self) -> Dict[Text, Union[Text, int, bool]]:
    request = {
      'name': '{} {}+{} Chess960'.format(
        self.level.name, self.time_control.clock, self.time_control.increment),
      'clockTime': self.time_control.clock,
      'clockIncrement': self.time_control.increment,
      'minutes': self.duration,
      'startDate': int(self.start_datetime.timestamp()),
      'variant': 'chess960',
      'description': 'Daily Chess960 Arena. Times cycle daily so that everyone'
        'gets a chance to play their favorite time control. Please put all '
        'suggestions in the forum! Have fun :)',
      'conditions.teamMember.teamId': 'chess960',
      'conditions.nbRatedGame.nb': self.min_rated,
    }

    if self.level.min_elo:
      request['conditions.minRating.rating'] = self.level.min_elo

    if self.level.max_elo:
      request['conditions.maxRating.rating'] = self.level.max_elo

    return request

  def register(self):
    headers = {'Authorization': 'Bearer {}'.format(os.getenv('TOKEN'))}
    data = self.prepare_request()
    return requests.post('https://lichess.org/api/tournament', 
                         headers=headers, data=data)


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


def make_daily_arenas(day: datetime.datetime):
  start = datetime.datetime(day.year, day.month, day.day, 0, 0, 0)
  days = (start - datetime.datetime(1970, 1, 1, 0, 0, 0)).days
  
  time_index = days % len(TIME_CONTROLS)
  
  arenas = []
  for i in range(4): 
    for j in range(3): 
      arenas.append(Arena(
        LEVELS[j], TIME_CONTROLS[(time_index + i + j) % 4], start))

      start += datetime.timedelta(hours=2)

  return arenas


if __name__ == '__main__':
  src = pathlib.Path(__file__).resolve().parent
  dotenv.load_dotenv(src / '.env')
  print(os.getenv('TOKEN'))

  # tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
  # arenas = make_daily_arenas(tomorrow)