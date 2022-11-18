class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def cal(self):
        print(f"{self.year}/{self.month}/{self.day}")

    @classmethod
    def pre_handle(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        t_date = cls(year, month, day)
        return t_date


date = Date.pre_handle("2022-10-21")
date.cal()