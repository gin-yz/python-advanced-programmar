class Company(object):
    def __init__(self, list_demo):
        self.list_demo = list_demo

    def __str__(self):
        return ",".join(self.list_demo)

    def __repr__(self):
        return ",".join(self.list_demo)


company = Company(["1", '2', '3'])
print(company)