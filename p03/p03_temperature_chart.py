# import helper functions
from statistics import mean

# define list with weekday and avg temparture
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# define average body temperature per day
avg_bodytemp_per_day = [36.8, 37.2, 36.9, 37.5, 38.0, 37.4, 36.6]

# calculate average body temperature and round to 2 decimals
avg_body_temp = mean(avg_bodytemp_per_day)

# print avg body temp with given temperatures
print(f"The average temperature for the week is: {avg_body_temp:.2f}°C")

# count amount of weekdays
weekday_count = len(weekdays)

# count amount of temperatures
temperature_count = len(avg_bodytemp_per_day)

# Define list of body_temp_over_avg
body_temp_over_avg = []

# only go through iteration if weekday_count is equal to temperature_count to avoid error:
if weekday_count == temperature_count:
    
    # take length of weekdays list and loop:
    for x in range(weekday_count):

        # check if avg_bodytemp_per_day on index x is greater than avg_body_temp
        if avg_bodytemp_per_day[x] > avg_body_temp:
            # if yes, append to list body_temp_over_avg
            body_temp_over_avg.append(weekdays[x])

    # define weekday_output
    weekday_output = ', '.join(body_temp_over_avg)

    # Print string
    print(f"Days with above-average temperatures: {weekday_output}")
else:
    print(f"The amount of given temperatures is not equal to the amount of days")
