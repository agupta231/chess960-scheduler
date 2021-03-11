from pytz import timezone
import scheduler
import unittest

import datetime


class SchedulerTestCase(unittest.TestCase):
  def test_arena_request_overall(self):
    clock = 5
    increment = 3
    min_elo = 69
    max_elo = 420

    start_datetime = datetime.datetime(
      2020, 4, 20, 4, 20, 0, 
      tzinfo=datetime.timezone(-datetime.timedelta(hours=4)))
    start_timestamp = 1587370800 # https://www.epochconverter.com/
    
    a = scheduler.Arena(
      scheduler.Level('name', min_elo, max_elo),
      scheduler.TimeControl(clock, increment), start_datetime)
    r = a.prepare_request()
    
    self.assertEqual(r['clockTime'], clock)
    self.assertEqual(r['clockIncrement'], increment)
    self.assertEqual(r['minutes'], 120)
    self.assertEqual(r['startDate'], start_timestamp)

  def test_arena_no_min_elo(self):
    start_datetime = datetime.datetime(2020, 4, 20, 4, 20, 0)
    a = scheduler.Arena(
      scheduler.Level('name', None, 500), scheduler.TimeControl(0, 1), 
      start_datetime)
    r = a.prepare_request()

    self.assertNotIn('conditions.minRating.rating', r)
    self.assertEqual(r['conditions.maxRating.rating'], 500)

  def test_arena_no_max_elo(self):
    start_datetime = datetime.datetime(2020, 4, 20, 4, 20, 0)
    a = scheduler.Arena(
      scheduler.Level('name', 500, None), scheduler.TimeControl(0, 1), 
      start_datetime)
    r = a.prepare_request()

    self.assertNotIn('conditions.maxRating.rating', r)
    self.assertEqual(r['conditions.minRating.rating'], 500)


if __name__ == '__main__':
  unittest.main()