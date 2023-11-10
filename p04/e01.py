import p04_helpers as helper


# retrieve patient data
def retrieve_patient_data(data_collection):

    # iterate through user_data dictionary
    for data_set_keys, data_set_values in data_collection.items():
        for key, value in data_set_values.items():
            print(helper.translate_key(key, value))


# collect data, function defined in p04_helpers.py
data_collection = helper.collect_data(True)


# retrieve data
retrieve_patient_data(data_collection)
