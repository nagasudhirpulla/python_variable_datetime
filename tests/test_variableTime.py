import unittest
import datetime as dt
from variableTime import VarTime
import numpy as np
import pandas as pd


class TestVariableTime(unittest.TestCase):

    def test_case1(self) -> None:
        t1 = VarTime()
        # t1.absoluteTime = dt.datetime.now()
        t1.offsetYears = 0
        t1.offsetMonths = 0
        t1.offsetDays = 0
        t1.offsetHrs = 0
        t1.offsetMins = 0
        # t1.offsetSecs = 0
        self.assertIsNone(t1.getDateObj())

        # check for numpy nan along with None
        t1.offsetSecs = np.nan
        self.assertIsNone(t1.getDateObj())

    def test_case2(self) -> None:
        t1 = VarTime()
        t1.absoluteTime = dt.datetime.now()
        t1.offsetYears = 0
        t1.offsetMonths = 0
        t1.offsetDays = 0
        t1.offsetHrs = 0
        # t1.offsetMins = 0
        # t1.offsetSecs = 0
        self.assertIsNotNone(t1.getDateObj())

    def test_case3(self) -> None:
        t1 = VarTime()
        # t1.absoluteTime = dt.datetime.now()
        t1.offsetYears = 0
        t1.offsetMonths = 0
        t1.offsetDays = 0
        t1.offsetHrs = 0
        t1.offsetMins = 0
        t1.offsetSecs = 0
        self.assertIsNotNone(t1.getDateObj())

        # check for numpy nan along with None
        t1.absoluteTime = np.nan
        self.assertIsNotNone(t1.getDateObj())

        # check for numpy nat along with None
        t1.absoluteTime = pd.NaT
        self.assertIsNotNone(t1.getDateObj())

    def test_case4(self) -> None:
        t1 = VarTime()
        nowTime = dt.datetime.now()
        t1.absoluteTime = nowTime
        self.assertIsNotNone(t1.getDateObj())
        self.assertTrue((t1.getDateObj() - nowTime).total_seconds() == 0)
