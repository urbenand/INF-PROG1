# create empty list, we use this list to define the hours, where patient should take medicines
medical_hours = [0]

# define hourly interval of medical intake, in this example it's every 4 hours
intake_interval = 4

# define intake_timestamp, we start at 0
intake_timestamp = 0

# define length of intake period, in this case its 24 hours
intake_period = 24

# As long as intake_timestamp is less than defined value:
while intake_timestamp < intake_period:
    # increase intake_timestamp by intake_interval
    intake_timestamp += intake_interval

    # and add the newly defined intake_timestamp to our list medical_hours
    medical_hours.append(intake_timestamp)

# for loop in range of 0 to intake_period (hours)
for current_hour in range(0, intake_period):

    # if current hour is in list medical_hours, print out the reminder
    if current_hour in medical_hours:
        print(f"Hour {current_hour}: Take your medication")
    # else print current hour, but no reminder
    else:
        print(f"Hour {current_hour}: ")
