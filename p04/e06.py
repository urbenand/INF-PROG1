import p04_helpers as helper


# Collect data, to search for after
data_collection = helper.collect_data(True)

# print empty line, weil schön. und übersicht. :-)
print("---")

# Retrieve and analyze patient data
result = helper.retrieve_and_analyze_patient_data(data_collection, input("Search for data, enter AHV number: "))

# print empty line, weil schön. und übersicht. :-)
print("---")

# iterate through result
for data in result.items():
    # translate given values, data[0] is the key, data[1] is the value
    print(helper.translate_key(data[0], data[1]))
