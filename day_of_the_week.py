from datetime import datetime
days = ['Monday','Tuesday','wednesday','Thursday','Friday','Saturday','Sunday']

class Solution(object):
    def dayOfTheWeek(year, month, day):
       return days[datetime(year, month, day).weekday()]
    
if __name__ == "__main__":
   print(Solution.dayOfTheWeek(2023, 9, 23))