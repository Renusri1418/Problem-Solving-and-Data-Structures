
requests = [
    120, 95, 80, 75, 70, 90,
    150, 210, 260, 300, 280, 250,
    230, 220, 240, 310, 350, 330,
    290, 260, 200, 180, 150, 130
]

window_size = 3

current_sum = sum(requests[:window_size])
maximum_sum = current_sum
best_start = 0

for i in range(1, len(requests) - window_size + 1):

    current_sum += requests[i + window_size - 1]
    current_sum -= requests[i - 1]

    if current_sum > maximum_sum:
        maximum_sum = current_sum
        best_start = i

print("REQUESTS PER HOUR:")
print(requests)

print("\nBUSIEST 3-HOUR WINDOW")

print("Starting hour:", best_start)
print("Ending hour:", best_start + window_size)
print("Total requests:", maximum_sum)

print("Average requests per hour:",
      round(maximum_sum / window_size, 2))
