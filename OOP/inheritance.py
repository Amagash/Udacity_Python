class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("Last name : " + self.last_name)
        print ("Eye color : " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print ("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        # print ("Last name : " + self.last_name)
        # print ("Eye color : " + self.eye_color)
        super().show_info()
        print ("Number of toys : " + str(self.number_of_toys))


olivier = Parent("Leplus", "brown")
# print (olivier.last_name)

katoun = Child("Leplus Souterre", "green", 5)
# print (katoun.last_name)
# print (katoun.number_of_toys)

# olivier.show_info()
katoun.show_info()