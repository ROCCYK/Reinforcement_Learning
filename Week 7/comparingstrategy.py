# Program to compare two strategies based on their discounted rewards
import numpy as np

# Given rewards
exp_rewards_strategy_1 = np.array([10, 5, 2, 1])
exp_rewards_strategy_2 = np.array([1, 2, 5, 10])

# Discount factor
discount_factor = 0.9

# Function to calculate discounted rewards
def discounted_rewards(exp_rewards, discount_factor):
    discounted_sum = 0
    for i in range(len(exp_rewards)):
        discounted_sum += exp_rewards[i] * (discount_factor ** i)
    return discounted_sum

# Calculating discounted rewards for both strategies
discounted_rewards_strategy_1 = discounted_rewards(exp_rewards_strategy_1, discount_factor)
discounted_rewards_strategy_2 = discounted_rewards(exp_rewards_strategy_2, discount_factor)

# Comparing the discounted rewards
if discounted_rewards_strategy_1 > discounted_rewards_strategy_2:
    print("Strategy 1 has higher discounted rewards.")
else:
    print("Strategy 2 has higher discounted rewards.")
