
daily_claims = [
    85, 120, 135, 110, 95, 130,
    145, 160, 90, 105, 115, 125
]

longest = 0
current = 0

best_start = 0
current_start = 0

for day, claims in enumerate(daily_claims, start=1):

    if claims > 100:

        if current == 0:
            current_start = day

        current += 1

        if current > longest:
            longest = current
            best_start = current_start

    else:
        current = 0

print("DAILY INSURANCE CLAIMS:")
print(daily_claims)

print("\nLongest consecutive run:")
print(longest, "days")

if longest > 0:
    print("Starting day:", best_start)
    print("Ending day:", best_start + longest - 1)
else:
    print("No consecutive days found.")
