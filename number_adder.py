#Create a function that will add up all the numbers in a list of numbers
#List of numbers that was given as an argument
#Use this function to ask the user for aseries of number
#and then show the user the sum of all the numbers
#that were given by the user

#          0,1,2,3, 4
my_nums = [1,7,9,12,15]

print(my_nums)
print(my_nums[3])
print(my_nums[4])
print(type(my_nums[0]))

my_total = 0
my_total = my_total + my_nums[0]
my_total = my_total + my_nums[1]
my_total = my_total + my_nums[2]
my_total = my_total + my_nums[3]
my_total = my_total + my_nums[4]
print(my_total)
#only good for in the index in range (cannot go up to 5)

print(sum(my_nums)) 

#use a foor loop, see below
new_total = 0
for num in my_nums:
    new_total = new_total + num
print(new_total) #this is same as above

def total_my_list(my_list):
    total = 0
    for num in my_list:
        total = total + num
    return total

print(total_my_list(my_nums)) #from line 8
print(total_my_list([1,8,9,10,15]))
print("="*25)

#now we need to ask
#using while loop next line

x = 12    #Look up 20:14 in pre-work video for explanation below
while x != "quit":
    print("the valute of x is", x)
    x = x + 1
    if x == 15:
        x = "quit"


user_num = input("Tell me a number?")
print(user_num)
print(type(user_num))
#next convert string to integer
user_num = int(user_num)
print(type(user_num))

#how do we add num to list of num? see below (Append)

my_test_list = [100, 101, 102, 103]
print(my_test_list)
my_test_list.append(104)
print(my_test_list)

#The following is the code to answer the top function
a_number = input("Give me a number to add to your total or type 'quit' to quit ")
num_list = [] #list to hold all numbers
while a_number != "quit":
    num_list.append(int(a_number)) #adding integer
    a_number = input("Give me a number to add to your total or type 'quit' to quit ")

print("The total of your list is", total_my_list(num_list))
