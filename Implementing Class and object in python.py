class MyClass:
    def __init__(self, data):
        self.data = data

    def display_data(self):
        print("Data:", self.data)


# Creating an object of MyClass and initializing it with data
my_object = MyClass("Hello, World!")

# Accessing class data and calling class functions using the object
print("Accessing class data:", my_object.data)
my_object.display_data()
