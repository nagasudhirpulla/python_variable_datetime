import calendar
import datetime as dt
from typing import Optional

import pandas as pd


class VarTime:
    absoluteTime: Optional[dt.datetime] = None
    offsetDays: Optional[int] = None
    offsetMonths: Optional[int] = None
    offsetYears: Optional[int] = None
    offsetHrs: Optional[int] = None
    offsetMins: Optional[int] = None
    offsetSecs: Optional[int] = None

    def getDateObj(self) -> Optional[dt.datetime]:
        resultTime: Optional[dt.datetime] = dt.datetime.now()

        # Add offsets to current time as per the settings
        if not pd.isna(self.offsetYears):
            resultTime = VarTime.addMonths(resultTime, 12*self.offsetYears)

        if not pd.isna(self.offsetMonths):
            resultTime = VarTime.addMonths(resultTime, self.offsetMonths)

        if not pd.isna(self.offsetDays):
            resultTime = resultTime + dt.timedelta(days=self.offsetDays)

        if not pd.isna(self.offsetHrs):
            resultTime = resultTime + dt.timedelta(hours=self.offsetHrs)

        if not pd.isna(self.offsetMins):
            resultTime = resultTime + dt.timedelta(minutes=self.offsetMins)

        if not pd.isna(self.offsetSecs):
            resultTime = resultTime + dt.timedelta(seconds=self.offsetSecs)

        if pd.isna(self.offsetYears) or pd.isna(self.offsetMonths) or pd.isna(self.offsetDays) or pd.isna(self.offsetHrs) or pd.isna(self.offsetMins) or pd.isna(self.offsetSecs):
            # check if we require absolute component but the absolute component is None
            if pd.isna(self.absoluteTime):
                return None

        # Set absolute time settings to the result time
        if pd.isna(self.offsetYears):
            resultTime = resultTime.replace(year=self.absoluteTime.year)

        if pd.isna(self.offsetMonths):
            resultTime = resultTime.replace(month=self.absoluteTime.month)

        if pd.isna(self.offsetDays):
            resultTime = resultTime.replace(day=self.absoluteTime.day)

        if pd.isna(self.offsetHrs):
            resultTime = resultTime.replace(hour=self.absoluteTime.hour)

        if pd.isna(self.offsetMins):
            resultTime = resultTime.replace(minute=self.absoluteTime.minute)

        if pd.isna(self.offsetSecs):
            resultTime = resultTime.replace(second=self.absoluteTime.second)

        return resultTime

    @staticmethod
    def addMonths(inpDt: dt.datetime, mnths: int) -> dt.datetime:
        tmpMnth = inpDt.month - 1 + mnths

        # Add floor((input month - 1 + k)/12) to input year component to get result year component
        resYr = inpDt.year + tmpMnth // 12

        # Result month component would be (input month - 1 + k)%12 + 1
        resMnth = tmpMnth % 12 + 1

        # Result day component would be minimum of input date component and max date of the result month (For example we cant have day component as 30 in February month)
        # Maximum date in a month can be found using the calendar module monthrange function as shown below
        resDay = min(inpDt.day, calendar.monthrange(resYr, resMnth)[1])

        # construct result datetime with the components derived above
        resDt = dt.datetime(resYr, resMnth, resDay, inpDt.hour,
                            inpDt.minute, inpDt.second, inpDt.microsecond)

        return resDt
