
orders = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

gift_card = 60

left = 0
right = len(orders) - 1

pairs = []

while left < right:

    total = orders[left] + orders[right]

    if total == gift_card:
        pairs.append((orders[left], orders[right]))
        left += 1
        right -= 1

    elif total < gift_card:
        left += 1

    else:
        right -= 1

print("ORDER VALUES:", orders)
print("GIFT CARD VALUE:", gift_card)

print("\nMATCHING PAIRS:")

for first, second in pairs:
    print(first, "+", second, "=", gift_card)

if not pairs:
    print("No matching pairs found.")
