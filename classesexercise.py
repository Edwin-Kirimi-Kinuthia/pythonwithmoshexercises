class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def talk(self):
        print(f"Hello, I am {self.firstname} {self.lastname}. {self.firstname} {self.lastname} is a dedicated and skilled professional with a multifaceted background encompassing medicine, research, and software development.")


edwin = Person('Edwin', 'Kirimi')
edwin.talk()
