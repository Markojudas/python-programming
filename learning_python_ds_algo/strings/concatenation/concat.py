message = "the price of the stock is:"
print(id(message))

price = "$1100"
message = message + " " + price
print(id(message))

# strings are immutable; a reassignment of "message" will create a new string object
