N = int(input())
toppings = input().split()
cheeses = set()
for topping in toppings:
    if topping.endswith('Cheese'):
        cheeses.add(topping)
print('yummy' if len(cheeses) >= 4 else 'sad')