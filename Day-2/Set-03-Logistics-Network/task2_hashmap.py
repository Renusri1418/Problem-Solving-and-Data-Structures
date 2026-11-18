
parcels = {
    "TRK1001": ["CHN", "BLR"],
    "TRK1002": ["CHN", "CHN", "HYD"],
    "TRK1003": ["MUM", "PUN"],
    "TRK1004": ["DEL", "DEL"],
    "TRK1005": ["BLR", "HYD"]
}

print("PARCEL TRACKING SYSTEM")

for tracking, hubs in parcels.items():
    print(tracking, ":", hubs)

print("\nDUPLICATE SCAN DETECTION")

found = False

for tracking, hubs in parcels.items():

    visited_hubs = set()
    duplicates = set()

    for hub in hubs:

        if hub in visited_hubs:
            duplicates.add(hub)

        visited_hubs.add(hub)

    if duplicates:
        found = True

        print(
            tracking,
            "scanned multiple times at:",
            sorted(duplicates)
        )

if not found:
    print("No duplicate scans found.")

# Search for a parcel
search_id = "TRK1003"

print("\nPARCEL LOOKUP")
print(search_id, ":", parcels.get(search_id, "Not found"))
