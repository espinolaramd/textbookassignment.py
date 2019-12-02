class person():

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def description(self):
        author = (f"This person is called {self.first + self.last} and is {self.age} years of age.")
        return author
