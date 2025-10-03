import numpy as np
transaction_volumes = np.random.randint(100, 1000, size=(4 ,6))
print("Transaction Volumes:\n", transaction_volumes)

totals_per_branch = transaction_volumes.sum(axis=1)
print("Total Transactions per Branch:", totals_per_branch)

highest_branch = np.argmax(totals_per_branch) + 1
print(f"Branch {highest_branch} has the highest total transactions:", totals_per_branch[highest_branch-1])

avg_monthly = transaction_volumes.mean(axis=0)
print("Average Monthly Transaction Volume:", avg_monthly)

reshaped_array = transaction_volumes.reshape(3, 8)
print("Reshaped Array :\n", reshaped_array)