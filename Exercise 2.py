# Exercise 2 shopping cart program

item = input("What would you like to buy?: ")
price = float(input("What price is it?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"That will be ${total}.")

