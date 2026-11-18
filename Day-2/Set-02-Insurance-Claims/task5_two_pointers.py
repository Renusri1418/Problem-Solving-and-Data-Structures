
north_claims = [101, 108, 115, 130, 145, 160]

south_claims = [103, 110, 120, 125, 150]

i = 0
j = 0

merged = []

while i < len(north_claims) and j < len(south_claims):

    if north_claims[i] <= south_claims[j]:

        merged.append(north_claims[i])
        i += 1

    else:

        merged.append(south_claims[j])
        j += 1


# Append remaining elements
merged.extend(north_claims[i:])
merged.extend(south_claims[j:])

print("NORTH REGION:", north_claims)
print("SOUTH REGION:", south_claims)

print("\nMERGED SORTED CLAIM LIST:")
print(merged)
