
"""
Day 1 - Set 3 - Task 3
Detect Double-Booked Hospital Appointment Slots

Duplicate condition:
Same patient ID and same appointment slot.
"""

from collections import defaultdict


appointments = [
    {"patient_id": "PAT001", "slot": "09:00 AM", "doctor": "Dr. Kumar"},
    {"patient_id": "PAT002", "slot": "09:30 AM", "doctor": "Dr. Priya"},
    {"patient_id": "PAT003", "slot": "10:00 AM", "doctor": "Dr. Kumar"},
    {"patient_id": "PAT001", "slot": "09:00 AM", "doctor": "Dr. Kumar"},
    {"patient_id": "PAT004", "slot": "10:30 AM", "doctor": "Dr. Priya"},
    {"patient_id": "PAT002", "slot": "09:30 AM", "doctor": "Dr. Priya"},
    {"patient_id": "PAT001", "slot": "11:00 AM", "doctor": "Dr. Kumar"},
    {"patient_id": "PAT005", "slot": "11:30 AM", "doctor": "Dr. Priya"},
    {"patient_id": "PAT003", "slot": "10:00 AM", "doctor": "Dr. Kumar"},
]


def detect_double_bookings(data):
    # Store the first appointment for each patient and slot.
    booking_map = {}
    duplicates = []

    for appointment in data:
        key = (
            appointment["patient_id"],
            appointment["slot"].strip().upper()
        )

        if key in booking_map:
            duplicates.append({
                "original": booking_map[key],
                "duplicate": appointment
            })
        else:
            booking_map[key] = appointment

    return duplicates


def main():
    print("=" * 70)
    print("HOSPITAL APPOINTMENT DESK - DOUBLE BOOKING DETECTION")
    print("=" * 70)

    print(f"\nTotal appointments checked: {len(appointments)}")

    duplicates = detect_double_bookings(appointments)

    print("\n--- DOUBLE-BOOKED APPOINTMENTS ---")

    if duplicates:
        for number, pair in enumerate(duplicates, start=1):
            original = pair["original"]
            duplicate = pair["duplicate"]

            print(f"\nDuplicate Booking {number}")
            print(f"Patient ID:       {duplicate['patient_id']}")
            print(f"Appointment Slot: {duplicate['slot']}")
            print(f"Doctor:           {duplicate['doctor']}")
            print(
                "Original booking: "
                f"{original['patient_id']} - {original['slot']}"
            )
            print(
                "Duplicate booking: "
                f"{duplicate['patient_id']} - {duplicate['slot']}"
            )
    else:
        print("No double-booked appointments found.")

    print(f"\nTotal duplicate bookings: {len(duplicates)}")

    print("\n--- DATA STRUCTURE ---")
    print("Used: Dictionary (Hash Table)")
    print("Key: (Patient ID, Appointment Slot)")
    print("Average lookup/insert: O(1)")
    print("Overall time complexity: O(n)")
    print("Space complexity: O(n)")

    print("\nTask 3 completed successfully.")


if __name__ == "__main__":
    main()
