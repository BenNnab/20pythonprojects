foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----------------YOUR CART---------------")

for food, price in zip(foods, prices):
    print(f"{food}: ${price:.2f}")

total = sum(prices)
print()
print(f"Your total is: ${total:.2f}")
