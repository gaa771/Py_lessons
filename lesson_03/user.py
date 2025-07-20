class User:

    def __init__(self, first_name, last_name):
        self.username = first_name
        self.usersurname = last_name

    def sayName(self):
        print("мое имя", self.username)

    def saySurname(self):
        print("моя фамилия", self.usersurname)

    def sayFullName(self):
        print("меня зовут", self.username, self.usersurname)
