# collect data
def collect_data(single):
    data_collection = {}
    # set add another to True to collect first set of data
    add_another = True

    # while add_another is true, ask user for input
    while add_another:
        # store ahv_number to variable to use as key
        ahv_number = input("Please enter AHV-Number: ")

        # create new dictionary with ahv_number as key
        data_collection[ahv_number] = {}

        # collect data by input
        # Template: data_collection[ahv_number].update({"key": input(value)})
        data_collection[ahv_number].update({"ahv_number": ahv_number})
        data_collection[ahv_number].update({"patient_name": input("Please enter name: ")})
        data_collection[ahv_number].update({"date_of_birth": input("Please enter date of birth (YYYY-MM-DD): ")})
        data_collection[ahv_number].update({"patient_temperature": float(input("Please enter temperature: "))})
        data_collection[ahv_number].update({"heart_rate": input("Please enter heart rate: ")})
        data_collection[ahv_number].update({"blood_pressure": input("Please enter blood pressure (e.g. 120/80): ")})

        # if single is True, we only collect one set of data
        if single:
            # Set add_another to False, so loop while add_another will end
            add_another = False

        # check, if add_another is True, if True, ask user if he wants to add another set of data
        if add_another:
            # if user does not enter "n", set add_another to False and therefore the while loop ends
            if input("Do you want do add another dataset? y/n: ") == "n":
                add_another = False

    # return dictionary data_collection (not print!)
    return data_collection


# Calculate current age by date of birth
def calculate_age(date_of_birth):
    from datetime import date

    # define/get today's date
    today = date.today()

    # split up date into year, month prepare values
    year, month, day = [int(item) for item in date_of_birth.split("-")]

    # convert date of birth into date
    date_of_birth = date(year, month, day)

    # A bool that represents if today's day/month precedes the birthday/month
    one_or_zero = ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

    # Calculate the difference in years from the date object's components
    year_difference = today.year - date_of_birth.year
    age = year_difference - one_or_zero

    return age


# blood pressure analyser
def analyse_blood_pressure(systolic, diastolic):
    condition = "Optimal"

    if systolic in range(120, 129) or diastolic in range(80, 84):
        condition = "Normal"
    elif systolic in range(130,139) or diastolic in range(85,89):
        condition = "Highnormal"
    elif systolic in range(140, 159) or diastolic in range(90,99):
        condition = "hypertension stage I "
    elif systolic in range(160,179) or diastolic in range(100,109):
        condition = "hypertension stage II "
    elif systolic in range(180, 300) or diastolic in range(110,300):
        condition = "hypertension stage III"

    message = f"The calculated blood pressure condition with given values is {condition}. Given values: {systolic}/{diastolic} mmHg"

    return message


# heart rate analyser
def analyse_heart_rate(heart_rate, patient_age):
    condition = "Normal"

    # Newborn
    if patient_age in range(0, 1):
        if heart_rate in range(0, 120):
            condition = "too low"
        elif heart_rate in range(140,250):
            condition = "too high"

    # Children < 8
    if patient_age in range(2,8):
        if heart_rate in range(0, 100):
            condition = "too low"
        elif heart_rate in range(120, 250):
            condition = "too high"

    # Children, teenagers
    if patient_age in range(9, 19):
        if heart_rate in range(0, 80):
            condition = "too low"
        elif heart_rate in range(100, 250):
            condition = "too high"

    # Adolescents
    if patient_age in range(20,119):
        if heart_rate in range(0, 60):
            condition = "too low"
        elif heart_rate in range(80, 250):
            condition = "too high"

    message = f"Heart rate is {condition} for a patient at the age of {patient_age}. Given value: {heart_rate} bpm"

    return message


# translate keys / values from list
def translate_key(key, value):
    # set output
    output = ""

    # check key, e.g. ahv_number
    # translate value into readable output-string by key
    if key == "ahv_number":
        output = f"AHV Number: {value}"
    elif key == "patient_name":
        output = f"Patient Name: {value}"
    elif key == "patient_temperature":
        output = f"Patient Temperature: {value}°C"
    elif key == "date_of_birth":
        output = f"Age: {calculate_age(value)}"
    elif key == "heart_rate":
        output = f"Heart Rate: {value}"
    elif key == "blood_pressure":
        output = f"Blood pressure: {value}"
    else:
        output = f"{value}"

    return output


def retrieve_and_analyze_patient_data(data_collection, ahv_number):
    result = {}

    # check if given ahv_number is in data collection
    if ahv_number in data_collection:
        # prepare data from collection
        patient_age = calculate_age(data_collection[ahv_number]["date_of_birth"])
        blood_pressure = data_collection[ahv_number]["blood_pressure"].split("/")
        heart_rate = data_collection[ahv_number]["heart_rate"]

        # template: result.update({"": })
        result.update({"patient_name": data_collection[ahv_number]["patient_name"]})

        # call blood pressure analyzer
        result.update({"blood_pressure": analyse_blood_pressure(int(blood_pressure[0]), int(blood_pressure[1]))})

        # call heart rate analyzer
        result.update({"heart_rate": analyse_heart_rate(int(heart_rate), int(patient_age))})
    else:
        # ahv number is not in list, add "Patient Data not found" as result
        result.update({"message": f"Patient data not found for AHV Number: {ahv_number}"})

    return result

# The actual part of the program


# Collect data, to search for after
data_collection = collect_data(False)

# print empty line, weil schön. und übersicht. :-)
print("---")

# start asking for AHV number
ahv_entry = input("Please enter AHV number (or 'quit' to exit): ")

# print empty line, weil schön. und übersicht. :-)
print("---")

# while repeat is not quit, ask for AHV number and analyse data
while ahv_entry != "quit":
    # Retrieve and analyze patient data
    result = retrieve_and_analyze_patient_data(data_collection, ahv_entry)

    # iterate through result
    for data in result.items():
        # translate given values, data[0] is the key, data[1] is the value
        print(translate_key(data[0], data[1]))

    # print empty line, weil schön. und übersicht. :-)
    print("---")
    ahv_entry = input("Please enter AHV number (or 'quit' to exit): ")
else:
    # print empty line, weil schön. und übersicht. :-)
    print("---")
    # be sad, because user does not need you anymore :-(
    print("Ok, bye :'(")
