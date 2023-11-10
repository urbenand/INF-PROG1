# Import helper functions from p04_helpers.py
import p04_helpers as helper

# analyse values, data gets directly collected
heart_rate = helper.analyse_heart_rate(int(input("Enter heart rate: ")), helper.calculate_age(input("Enter date of birth (YYYY-MM-DD): ")))
blood_pressure = helper.analyse_blood_pressure(int(input("Enter systolic value: ")), int(input("Enter diastolic value: ")))

# output results
print(heart_rate)
print(blood_pressure)
