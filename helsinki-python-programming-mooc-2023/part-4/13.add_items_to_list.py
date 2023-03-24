# Write your solution here

items = []

how_many = int(input("How many items: "))

for item in range(1, how_many + 1):
    value_item = int(input(f"Item {item}: "))
    items.append(value_item)

print(items)