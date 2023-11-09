def collect_data():
    data_set = {}

    # store ahv_number to variable to reuse as key
    ahv_number = input("Please enter AHV-Number: ")

    # collect data by input
    data_set["ahv_number"] = ahv_number
    data_set["patient_name"] = input("Please enter patient name: ")
    data_set["patient_temperature"] = float(input("Please enter temperature: "))
    data_set["date_of_birth"] = input("Please enter date of birth (YYYY-MM-DD): ")
    data_set["heart_rate"] = input("Please enter patient heart rate: ")
    data_set["blood_pressure"] = input("Please enter patient blood pressure (Systolic/Diastolic, e.g. 120/80): ")

    return data_set


def retrieve_patient_data(data_set):
    # iterate through user_data dictionary
    for key, value in data_set.items():
        print(translate_key(key, value))
        # iterate through user data set


# translate keys / values from list
def translate_key(key, value):
    output = ""
    if key == "ahv_number":
        output = f"AHV Number: {value}"
    elif key == "patient_name":
        output = f"Patient Name: {value}"
    elif key == "patient_temperature":
        output = f"Patient Temperature: {value}°C"
    elif key == "date_of_birth":
        output = f"Age: {calculate_age(value)}"
    elif key == "heart_rate":
        output = f"Heart Rate: {value} bpm"
    elif key == "blood_pressure":
        output = f"Blood pressure: {value} mmHg"

    return output


# Calculate current age by date of birth
def calculate_age(date_of_birth):
    from datetime import date

    # todays date
    today = date.today()

    # split up date into year, month, day
    year, month, day = [int(item) for item in date_of_birth.split("-")]

    # convert date of birth into date
    date_of_birth = date(year, month, day)

    # A bool that represents if today's day/month precedes the birth day/month
    one_or_zero = ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

    # Calculate the difference in years from the date object's components
    year_difference = today.year - date_of_birth.year
    age = year_difference - one_or_zero

    return age


# collect data
data_set = collect_data()


# retrieve data
retrieve_patient_data(data_set)

