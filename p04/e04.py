import json

# collect data
def collect_data(single):
    # create new list for data sets
    data_set = []
    # set add another to True to collect first set of data
    add_another = True

    # while add_another is true, ask user for input
    while add_another:
        # store ahv_number to variable to use as key
        ahv_number = input("Please enter AHV-Number: ")

        # collect data by input as dictionary
        data_collection = {}

        data_collection["ahv_number"] = ahv_number

        data_collection["patient_name"] = input("Please enter name: ")
        data_collection["date_of_birth"] = input("Please enter date of birth (YYYY-MM-DD): ")
        data_collection["patient_temperature"] = float(input("Please enter temperature: "))
        data_collection["heart_rate"] = input("Please enter heart rate: ")
        data_collection["blood_pressure"] = input("Please enter blood pressure (e.g. 120/80): ")

        # add current data dictionary to data_set list
        data_set.append(data_collection)

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
    return data_set

# collect data, False means, we collect multiple data
patient_information = collect_data(False)

# print pretty data by using json.dumps()
print(json.dumps(patient_information, sort_keys=False, indent=4))
