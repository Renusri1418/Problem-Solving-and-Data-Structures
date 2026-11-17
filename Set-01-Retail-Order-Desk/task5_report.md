
# Task 5 – Greedy Algorithm and Dynamic Programming

## Objective
Calculate the minimum number of coins required for a
refund using Greedy and Dynamic Programming.

## Input

Refund Amount: 6

Available Denominations: [1, 3, 4]

## 1. Greedy Algorithm

The Greedy algorithm selects the largest available
denomination that does not exceed the remaining amount.

Steps:
1. Select coin 4. Remaining amount = 2.
2. Select coin 1. Remaining amount = 1.
3. Select coin 1. Remaining amount = 0.

Result: [4, 1, 1]

Total Coins: 3

## 2. Dynamic Programming

Dynamic Programming calculates the minimum number
of coins needed for every smaller amount.

It uses previously calculated results to determine
the optimal solution.

Optimal Result: [3, 3]

Minimum Coins: 2

## 3. Comparison

| Method | Coin Combination | Number of Coins |
|---|---|---:|
| Greedy | [4, 1, 1] | 3 |
| Dynamic Programming | [3, 3] | 2 |

## 4. Complexity Analysis

Greedy:
- Time: O(k log k + c)
- Space: O(c) for the returned coin list.

Dynamic Programming:
- Time: O(A × k)
- Space: O(A)

Where:
- A = Refund amount
- k = Number of denominations
- c = Number of selected coins

## Conclusion

The Greedy algorithm does not always produce
the minimum number of coins.

For amount 6 and denominations [1, 3, 4],
Greedy requires three coins, whereas Dynamic
Programming finds the optimal solution using two.

Dynamic Programming is more reliable when the
denomination system does not guarantee that
Greedy will produce an optimal solution.
