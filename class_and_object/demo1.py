class Day(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "{x}/{y}/{z}".format(x=self.x, y=self.y, z=self.z)

    # @staticmethod
    # def format_date(str1):
    #     x, y, z = tuple(str1.split('-'))
    #     return Day(x, y, z)

    @classmethod
    def string_decode(cls, str1):
        x, y, z = str1.split('-')
        return cls(x, y, z)


str_day = '1111-2222-3333'
day = Day.string_decode(str_day)

print(day)

