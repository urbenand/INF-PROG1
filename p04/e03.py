import p04_helpers as helper


def patient_analysis():
    result = {}
    # collect data
    patient_name = input("Enter patient name: ")
    patient_heart_rate = int(input("Enter heart rate: "))
    patient_age = int(helper.calculate_age(input("Enter date of birth (YYYY-MM-DD): ")))
    patient_blood_pressure = input("Enter blood pressure (e.g. 120/80): ")

    blood_pressure = patient_blood_pressure.split("/")
    systolic = int(blood_pressure[0])
    diastolic = int(blood_pressure[1])

    # call functions
    result.update({"patient_name": f"Patient Name: {patient_name}"})
    result.update({"heart_rate": f"Heart rate analysis: {helper.analyse_heart_rate(patient_heart_rate, patient_age)}"})
    result.update({"blood_pressure": f"Blood pressure analysis: {helper.analyse_blood_pressure(systolic, diastolic)}"})

    return result


analysis_result = patient_analysis()

# read out values in analysis results
for value in analysis_result.items():
    print(value[1])
