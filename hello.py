#Create a function that takes a name as an argument and returns a new string that says Hello and then the name 
#above is the argument
#Then use the function and ask the user for their name and tell them hello

print ("Jhon")

name = "John"
print(name)

print("Hello", name)
print("Hello" + " " +name)
hello_jhon = "Hello" + " " + name
print(hello_jhon)

def say_hello_print(the_users_name):
    print("Hello " + the_users_name)

print("Using our function with the print statement inside")
say_hello_print("Jhon")
print(say_hello_print("Jhon"))
#This function by default will return none. Above has value of none. 

def say_hello_return(the_users_name):
    return "Hello " + the_users_name

print("Using our function with the return statement inside and not printing")
print(say_hello_return("Steve") == "Hello Steve")

 #Nothing is the output because we returned a value, shows 

print(say_hello_return("Steve"))
hello_Steve = say_hello_return("Steve")
print(hello_Steve)


users_name = input("What is your name? ")
#print(users_name)
#print(type(users_name))
#user_name is a string
print(say_hello_return(users_name))

