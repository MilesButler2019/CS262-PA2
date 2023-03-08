import unittest
import subprocess
import os
import time
import datetime
import pandas as pd


main = []

class TestCreate(unittest.TestCase):
    def runTest(self):
        try:
            result = subprocess.run(['python', 'init.py'],capture_output=True, text=True)
        except:
            self.assertIn(result,"""Connected to: 127.0.0.1:60485 \n
            Connected to: 127.0.0.1:60486 \n
            Connected to: 127.0.0.1:60487""")

class CheckFileCreation(unittest.TestCase):
    def runTest(self):
        now = datetime.datetime.now()
        one_minute_ago = now - datetime.timedelta(minutes=1)
        time_stamp = one_minute_ago.strftime('%H:%M')
        main.append(time_stamp)
        self.assertTrue(os.path.exists('logs/log-1-expiriemental--{}.csv'.format(time_stamp)))
        self.assertTrue(os.path.exists('logs/log-2-expiriemental--{}.csv'.format(time_stamp)))
        self.assertTrue(os.path.exists('logs/log-3-expiriemental--{}.csv'.format(time_stamp)))


class TestClockSpeed(unittest.TestCase):
    def runTest(self):
        df1 = pd.read_csv("logs/log-1-expiriemental--{}.csv".format(main[0]))
        self.assertIn(df1.columns[1], 'Clock Speed')
        df2 = pd.read_csv("logs/log-2-expiriemental--{}.csv".format(main[0]))
        self.assertIn(df1.columns[1], 'Clock Speed')
        df3 = pd.read_csv("logs/log-3-expiriemental--{}.csv".format(main[0]))
        self.assertIn(df1.columns[1], 'Clock Speed')




if __name__ == '__main__':
    unittest.main()











