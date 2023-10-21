# Create list
heart_rates = [58, 65, 78, 72, 110, 89, 94]

# create variable for counting the amount of normal heart rates
normal_rates = 0

for heart_rate in heart_rates:
    if 60 < heart_rate < 110:
        normal_rates += 1

# output
print(f"{normal_rates} heart rates are within the normal range")
