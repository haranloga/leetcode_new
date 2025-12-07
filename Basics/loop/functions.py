# def name(params):
class Person:
    def hello(self):
        print("Hi there!")
    
    def addNums(self, a, b):
        c = a + b
        self.numberValid(c*c)
        print(c)

    def numberValid(self,num):
        print(num) 
    




person = Person() # Object Create 
person.hello() # function calling
person.addNums(5, 8) # function with parameters 
