#Defining and Calling Functions
# def say_hello():
#     print("Hello, Tara!")
# say_hello()


#Functions with Parameters
# def greet(name):
#     print("Welcome,", name)
# greet("Tara")


#Return Values
# def square(num):
#     return num * num
# result = square(5)
# print(result)  # 25


#Default Parameters
# def greet(name="Guest"):
#     print("Hello,", name)
# greet()          # Hello, Guest
# greet("Tara")    # Hello, Tara


#Scope: Local vs Global Variables
x = 10
def test():
    x = 5
    print(x)  # local x = 5
test()
print(x)      # global x = 10
