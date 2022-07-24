class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + " " + lastname
        self.email = (firstname+"."+lastname).lower()+"@company.com"
        # Complete the code!


class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = '{} {}'.format(firstname, lastname)
        self.email = '{}.{}@company.com'.format(firstname, lastname).lower()
