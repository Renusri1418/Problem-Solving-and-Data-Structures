
def check_palindrome(route):

    # Remove separators and convert to lowercase
    cleaned = ""

    for character in route:

        if character.isalnum():
            cleaned += character.lower()

    left = 0
    right = len(cleaned) - 1

    while left < right:

        if cleaned[left] != cleaned[right]:
            return False

        left += 1
        right -= 1

    return True


routes = [
    "CHN-BLR-CHN",
    "CHN / BLR / MUM",
    "A-B-C-B-A",
    "DEL-PUN-DEL"
]

print("DELIVERY ROUTE PALINDROME CHECK")

for route in routes:

    result = check_palindrome(route)

    print("\nRoute:", route)

    if result:
        print("Result: Palindrome")
    else:
        print("Result: Not a palindrome")
