

print("Challenge 3.1: Debug code snippets")

print()

print("Code Snippet 1:")

a = 2
b = 1
c = (a > b)

print("The value of c is True since a is greater than b.")

print()

print("Code Snippet 2:")

d = (True or (5 > 7) or not (8 < 20))

print("The value of d is False since 5 is not greater than 7 and 8 is not greater than 20.")

print()


print("Code Snippet 3:")

m = "GOAT"
n = "goat"

o = (m == n)

print ("The value of o is False becausep Python is case-insensitive.")

print()

print("Code Snippet 4:")

u = 5
v = 2

if u * v == 10:
    print("The product of a and b is 10")
else:
    print("The product of a and b is not 10")

print()

print("Code Snippet 5:")
x = 15
y = 25

z = 30

if z < x:
    print("z is less than x")

elif z > x and z < y:
    print("z is between x and y")

else:
    print("z is greater than y")


print()
print()
print()

print("Challenge 3.2: Playing with the stock market")

print()

print("Challenge 3.2.1: Creating variables")
# Create variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amzn = 3000
# TODO: Create a variable here for the stock price of Apple = 100
appl = 100
# TODO: Create a variable here for the stock price of Facebook = 250
fb = 250
# TODO: Create a variable here for the stock price of Google = 1400
goog = 1400
# TODO: Create a variable here for the stock price of Microsoft = 200
msft = 200
print()


print("Challenge 3.2.2: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input('What is your name?')
print(name)
# TODO: Write code to ask the client his savings and save it to another variable.
investment = int(input('What is your investment?'))
print(investment)
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print(stock)

# print("Challenge 3.2.3: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
if stock == 'amzn':
	current_price = 3000
	num_shares = investment/amzn 
	print(num_shares) 
elif stock == 'appl':
	current_price = 100
	num_shares = investment/appl
	print(investment/appl)
elif stock == 'fb':
	current_price = 250
	num_shares = investment/fb
	print(investment/fb)
elif stock == 'goog':
	current_price = 1400
	num_shares = investment/goog
	print(investment/goog)
else:
	current_price = 200
	num_shares = investment/msft
	print(investment/msft)

# Your code should look like this:



# print("Challenge 3.2.4: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

print(f'{name} has ${investment} in savings and he can buy {num_shares} shares of at the current price of ${current_price}')















