
# ==========================================
# TASK 5: GREEDY ALGORITHM AND DYNAMIC PROGRAMMING
# ==========================================

# 1. Greedy Algorithm

def greedy_coin_change(amount, denominations):

    denominations = sorted(denominations, reverse=True)

    coins_used = []

    for coin in denominations:

        while amount >= coin:
            amount -= coin
            coins_used.append(coin)

    if amount != 0:
        return None

    return coins_used


# 2. Dynamic Programming Algorithm

def dp_coin_change(amount, denominations):

    # dp[i] stores the minimum coins needed for amount i
    dp = [float("inf")] * (amount + 1)

    # Store the coin selected for each amount
    selected_coin = [0] * (amount + 1)

    dp[0] = 0

    for current_amount in range(1, amount + 1):

        for coin in denominations:

            if coin <= current_amount:

                if dp[current_amount - coin] + 1 < dp[current_amount]:

                    dp[current_amount] = dp[current_amount - coin] + 1

                    selected_coin[current_amount] = coin

    if dp[amount] == float("inf"):
        return None, None

    # Reconstruct the optimal coin combination
    result = []
    remaining = amount

    while remaining > 0:

        coin = selected_coin[remaining]

        result.append(coin)

        remaining -= coin

    return result, dp[amount]


# 3. Main Program

if __name__ == "__main__":

    # Refund amount
    refund_amount = 6

    # Available denominations
    denominations = [1, 3, 4]

    print("========== REFUND DETAILS ==========")

    print("Refund Amount:", refund_amount)
    print("Available Denominations:", denominations)

    # Greedy approach
    greedy_result = greedy_coin_change(
        refund_amount, denominations
    )

    print("\n========== GREEDY APPROACH ==========")

    if greedy_result is not None:

        print("Coins Used:", greedy_result)
        print("Number of Coins:", len(greedy_result))

    # Dynamic Programming approach
    dp_result, minimum_coins = dp_coin_change(
        refund_amount, denominations
    )

    print("\n========== DYNAMIC PROGRAMMING ==========")

    if dp_result is not None:

        print("Optimal Coins:", dp_result)
        print("Minimum Number of Coins:", minimum_coins)

    # Compare both approaches
    print("\n========== COMPARISON ==========")

    if greedy_result is not None and dp_result is not None:

        print("Greedy Coin Count:", len(greedy_result))
        print("DP Coin Count:", minimum_coins)

        if len(greedy_result) > minimum_coins:
            print("Greedy failed to find the optimal solution!")

        else:
            print("Greedy found an optimal solution.")

    print("\n========== COMPLEXITY ==========")

    print("Greedy: O(k log k + c)")
    print("Dynamic Programming: O(amount * k)")
    print("DP Space Complexity: O(amount)")

    print("\nRefund calculation completed successfully!")
