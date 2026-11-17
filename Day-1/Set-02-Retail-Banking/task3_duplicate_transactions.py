
"""
Day 1 - Set 2 - Task 3
Duplicate Banking Transaction Detection using Hashing

Duplicate conditions:
1. Same account number
2. Same amount
3. Same merchant
4. Within 60 seconds
"""

from datetime import datetime
from collections import defaultdict


transactions = [
    {
        "transaction_id": "TXN001",
        "account": "ACC1001",
        "amount": 2500,
        "merchant": "Amazon",
        "timestamp": "2026-11-17 09:00:00"
    },
    {
        "transaction_id": "TXN002",
        "account": "ACC1001",
        "amount": 2500,
        "merchant": "Amazon",
        "timestamp": "2026-11-17 09:00:35"
    },
    {
        "transaction_id": "TXN003",
        "account": "ACC1002",
        "amount": 1200,
        "merchant": "Flipkart",
        "timestamp": "2026-11-17 09:05:00"
    },
    {
        "transaction_id": "TXN004",
        "account": "ACC1001",
        "amount": 2500,
        "merchant": "Amazon",
        "timestamp": "2026-11-17 09:01:10"
    },
    {
        "transaction_id": "TXN005",
        "account": "ACC1003",
        "amount": 500,
        "merchant": "Swiggy",
        "timestamp": "2026-11-17 09:10:00"
    },
    {
        "transaction_id": "TXN006",
        "account": "ACC1002",
        "amount": 1200,
        "merchant": "Flipkart",
        "timestamp": "2026-11-17 09:07:00"
    },
    {
        "transaction_id": "TXN007",
        "account": "ACC1001",
        "amount": 2500,
        "merchant": "Amazon",
        "timestamp": "2026-11-17 09:10:00"
    }
]


def detect_duplicates(data):
    # Dictionary groups transactions by account, amount and merchant.
    groups = defaultdict(list)

    for transaction in data:
        key = (
            transaction["account"],
            transaction["amount"],
            transaction["merchant"].strip().lower()
        )

        timestamp = datetime.strptime(
            transaction["timestamp"], "%Y-%m-%d %H:%M:%S"
        )

        groups[key].append((timestamp, transaction))

    duplicate_pairs = []

    # Sort each group by timestamp and check nearby transactions.
    for key, records in groups.items():
        records.sort(key=lambda item: item[0])

        left = 0

        for right in range(len(records)):
            while (
                records[right][0] - records[left][0]
            ).total_seconds() > 60:
                left += 1

            # Every earlier transaction in this 60-second window
            # is a duplicate candidate for the current transaction.
            for i in range(left, right):
                first = records[i][1]
                second = records[right][1]

                duplicate_pairs.append((first, second))

    return duplicate_pairs


def main():
    print("=" * 70)
    print("RETAIL BANKING - DUPLICATE TRANSACTION DETECTION")
    print("=" * 70)

    print(f"\nTotal transactions checked: {len(transactions)}")

    duplicates = detect_duplicates(transactions)

    print("\n--- DUPLICATE TRANSACTIONS ---")

    if duplicates:
        for number, (first, second) in enumerate(duplicates, start=1):
            print(f"\nDuplicate Pair {number}")
            print(f"Transaction 1: {first['transaction_id']}")
            print(f"Transaction 2: {second['transaction_id']}")
            print(f"Account:       {first['account']}")
            print(f"Amount:        {first['amount']}")
            print(f"Merchant:      {first['merchant']}")

            time1 = datetime.strptime(
                first["timestamp"], "%Y-%m-%d %H:%M:%S"
            )
            time2 = datetime.strptime(
                second["timestamp"], "%Y-%m-%d %H:%M:%S"
            )

            difference = abs((time2 - time1).total_seconds())
            print(f"Time difference: {difference:.0f} seconds")
    else:
        print("No duplicate transactions found.")

    print(f"\nTotal duplicate pairs detected: {len(duplicates)}")
    print("\nTask 3 completed successfully.")


if __name__ == "__main__":
    main()
