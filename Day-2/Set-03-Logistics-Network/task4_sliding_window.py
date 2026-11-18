
parcels = [
    35, 40, 38, 45, 60, 75,
    80, 95, 110, 125, 130, 120,
    115, 105, 100, 90, 85, 80,
    70, 65, 55, 50, 45, 40
]

window_size = 4

current_sum = sum(parcels[:window_size])

maximum_sum = current_sum
best_start = 0

for i in range(1, len(parcels) - window_size + 1):

    current_sum += parcels[i + window_size - 1]
    current_sum -= parcels[i - 1]

    if current_sum > maximum_sum:

        maximum_sum = current_sum
        best_start = i


average = maximum_sum / window_size

print("HOURLY PARCEL COUNTS")
print(parcels)

print("\nHIGHEST AVERAGE 4-HOUR WINDOW")

print("Starting hour:", best_start)
print("Ending hour:", best_start + window_size)

print("Total parcels:", maximum_sum)
print("Average parcels per hour:", round(average, 2))
