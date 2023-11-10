import p04_helpers as helper

# Collect data, to search for after
data_collection = helper.collect_data(False)

# print empty line, weil schön. und übersicht. :-)
print("---")

# start asking for AHV number
ahv_entry = input("Please enter AHV number (or 'quit' to exit): ")

# print empty line, weil schön. und übersicht. :-)
print("---")

# while repeat is not quit, ask for AHV number and analyse data
while ahv_entry != "quit":
    # Retrieve and analyze patient data
    result = helper.retrieve_and_analyze_patient_data(data_collection, ahv_entry)

    # iterate through result
    for data in result.items():
        # translate given values, data[0] is the key, data[1] is the value
        print(helper.translate_key(data[0], data[1]))

    # print empty line, weil schön. und übersicht. :-)
    print("---")
    ahv_entry = input("Please enter AHV number (or 'quit' to exit): ")
else:
    # print empty line, weil schön. und übersicht. :-)
    print("---")
    # be sad, because user does not need you anymore :-(
    print("Ok, bye :'(")
