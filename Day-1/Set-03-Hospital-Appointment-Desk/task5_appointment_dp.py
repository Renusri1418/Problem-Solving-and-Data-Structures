
from bisect import bisect_right
from time import perf_counter


# Appointment data:
# patient_id, start time, end time
appointments = [
    ("PAT001", 9, 12),    # 3 hours
    ("PAT002", 9, 10),    # 1 hour
    ("PAT003", 10, 11),   # 1 hour
    ("PAT004", 11, 12),   # 1 hour
    ("PAT005", 12, 14),   # 2 hours
    ("PAT006", 10, 13),   # 3 hours
    ("PAT007", 13, 14),   # 1 hour
    ("PAT008", 14, 16),   # 2 hours
    ("PAT009", 15, 17),   # 2 hours
    ("PAT010", 16, 18),   # 2 hours
]


def appointment_duration(appointment):
    return appointment[2] - appointment[1]


# Sort appointments by finishing time
sorted_appointments = sorted(appointments, key=lambda x: x[2])

# Store the ending times for binary search
end_times = [appointment[2] for appointment in sorted_appointments]

# Find the previous compatible appointment for each appointment
previous = []

for i in range(len(sorted_appointments)):
    compatible_index = bisect_right(
        end_times, sorted_appointments[i][1], 0, i
    ) - 1
    previous.append(compatible_index)


# Dynamic Programming
def maximum_appointments_dp():
    n = len(sorted_appointments)

    # dp[i] = maximum appointments among the first i appointments
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        include = 1 + dp[previous[i - 1] + 1]
        exclude = dp[i - 1]

        dp[i] = max(include, exclude)

    # Reconstruct the selected appointments
    selected = []
    i = n

    while i > 0:
        include = 1 + dp[previous[i - 1] + 1]

        if include > dp[i - 1]:
            selected.append(sorted_appointments[i - 1])
            i = previous[i - 1] + 1
        else:
            i -= 1

    selected.reverse()
    return dp[n], selected


# Greedy approach: choose the appointment that finishes earliest
def maximum_appointments_greedy():
    selected = []
    last_end_time = -1

    for appointment in sorted_appointments:
        if appointment[1] >= last_end_time:
            selected.append(appointment)
            last_end_time = appointment[2]

    return len(selected), selected


# Run Dynamic Programming
start = perf_counter()
dp_count, dp_selected = maximum_appointments_dp()
dp_time = perf_counter() - start

# Run Greedy
start = perf_counter()
greedy_count, greedy_selected = maximum_appointments_greedy()
greedy_time = perf_counter() - start


print("=" * 55)
print("HOSPITAL APPOINTMENT SCHEDULING")
print("=" * 55)

print("\nAvailable Appointments:")
for patient, start_time, end_time in appointments:
    print(
        f"{patient}: {start_time}:00 - {end_time}:00 "
        f"({end_time - start_time} hour(s))"
    )

print("\nDynamic Programming Result:")
print("Maximum appointments:", dp_count)
for appointment in dp_selected:
    print(appointment)

print("\nGreedy Result (Earliest Finishing Time):")
print("Maximum appointments:", greedy_count)
for appointment in greedy_selected:
    print(appointment)

print("\nPerformance Comparison:")
print(f"Dynamic Programming Time: {dp_time:.8f} seconds")
print(f"Greedy Time:              {greedy_time:.8f} seconds")

print("\nVerification:")
print("Both approaches produce the same maximum:",
      dp_count == greedy_count)

print("\nComplexity:")
print("Dynamic Programming: O(n log n) time, O(n) space")
print("Greedy:              O(n log n) time, O(n) space")
print("=" * 55)
