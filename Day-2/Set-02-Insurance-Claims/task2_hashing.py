
claims = [
    ("POL-101", "2026-10-12", "C001"),
    (" pol-101 ", "2026-10-12", "C002"),
    ("POL-202", "2026-10-13", "C003"),
    ("pol-202", "2026-10-13", "C004"),
    ("POL-303", "2026-10-14", "C005")
]


def normalize(text):
    return "".join(text.lower().split())


claim_map = {}
duplicates = []

for policy, date, claim_id in claims:

    key = (normalize(policy), date.strip())

    if key in claim_map:
        duplicates.append(
            (claim_map[key], claim_id)
        )
    else:
        claim_map[key] = claim_id


print("INSURANCE CLAIM RECORDS")

for claim in claims:
    print(claim)

print("\nDUPLICATE CLAIMS")

for first, second in duplicates:
    print(second, "matches", first)

print("\nCollision Explanation:")
print("Different keys may map to the same hash bucket.")
print("Chaining stores multiple entries in that bucket.")
print("Key equality checks distinguish different claims.")
