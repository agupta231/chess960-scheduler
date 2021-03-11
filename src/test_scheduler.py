#from . import scheduler
import scheduler
import unittest

import datetime


class SchedulerTestCase(unittest.TestCase):
  def test_arena_request_overall(self):
    clock = 5
    increment = 3
    min_elo = 69
    max_elo = 420

    start_datetime = datetime.datetime(2020, 4, 20, 4, 20, 0)
    start_timestamp = 1587370800 # https://www.epochconverter.com/
    
    a = scheduler.Arena(
      scheduler.Level(min_elo, max_elo),
      scheduler.TimeControl(clock, increment), start_datetime)
    r = a.prepare_request()
    
    self.assertEqual(r['clockTime'], clock)
    self.assertEqual(r['clockIncrement'], increment)
    self.assertEqual(r['minutes'], 120)
    self.assertEqual(r['startDate'], start_timestamp)


if __name__ == '__main__':
  unittest.main()