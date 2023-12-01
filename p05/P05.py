import csv


# Exercise 2: Read Patient Data
def read_patient_records(filename):
    # TODO: Exercise 2 - Implement reading records from CSV file
    # Try to find file, if not found, quit program
    try:
        # open file
        with open(filename, 'r', newline='') as file:
            # read rows
            records = csv.DictReader(file)
            # open empty dict
            rows = {}

            # write records into rows dict
            for record in records:
                rows.update({record["Patient ID"]: record})

            # return rows
            return rows
    except:
        # File not found, print out message to user
        print(f"ERROR: File {filename} not found!")
        quit()


# Exercise 3: View Patient Records
def view_patient_records(records):
    # TODO: Exercise 3 - Implement displaying the patient records
    if records:
        # Header row, graphical stuff
        nice_line = "+-----------------+----------------------+-----------------+-----------------+-----------------+"
        header_row = "| {:15} | {:20} | {:15} | {:15} | {:15} |".format("Patient ID",
                                                                        "Name", "Date of Birth", "Height", "Weight")
        print(nice_line)
        print(header_row)
        print(nice_line)

        # Print contents in a beauuuutiful way. :-)
        for key, val in records.items():
            record_row = "| {:15} | {:20} | {:15} | {:15} | {:15} |".format(key, val["Name"],
                                                                            val["Date of Birth"] + " BBY", val["Height"] + " cm",
                                                                            val["Weight"] + " kg")
            print(record_row)
            print(nice_line)
    else:
        # tell user, if no data available
        print("ERROR: No data available.")


# Exercise 4: Add Patient Record
def add_patient_record(records):
    # TODO: Exercise 4 - Implement adding a new patient record
    # ask for patient id first
    patient_id = input("Please enter patient ID: ")

    # check if patient id already exists
    if patient_id in records.keys():
        print(f"ERROR: Patient with ID {patient_id} already exists")
    else:
        # patient id does not exist, prompt user to input new values
        patient = {patient_id: {
                        "Patient ID": patient_id,
                        "Name": input("Please enter patient name: "),
                        "Date of Birth": input("Please enter date of birth: "),
                        "Height": input("Please enter patient height in cm: "),
                        "Weight": input("Please enter patient weight in kg: ")}}
        # update records dictionary
        records.update(patient)


# Exercise 5: Update Patient Record
def update_patient_record(records):
    # TODO: Exercise 5 - Implement updating an existing patient record
    patient_id = input("Please enter patient ID to update: ")

    # check if patient id exists
    if patient_id in records.keys():
        # prompt user to change data or use existing value
        patient_name = input("Please enter patient name: ") or records[patient_id]["Name"]
        patient_dob = input("Please enter date of birth: ") or records[patient_id]["Date of Birth"]
        patient_height = input("Please enter patient height in cm: ") or records[patient_id]["Height"]
        patient_weight = input("Please enter patient weight in kg: ") or records[patient_id]["Weight"]

        # create patient object with given values
        patient = {patient_id: {
                "Patient ID": patient_id,
                "Name": patient_name,
                "Date of Birth": patient_dob,
                "Height": patient_height,
                "Weight": patient_weight}
        }

        # update and return records dictionary
        records.update(patient)
        return records
    else:
        # tell user, if patient does not exist
        print(f"ERROR: Patient with ID {patient_id} does not exist")


# Exercise 6: Delete Patient Record
def delete_patient_record(records):
    # TODO: Exercise 6 - Implement deleting a patient record
    patient_id = input("Please enter patient ID to delete:")

    # check if patient ID exists
    if patient_id in records.keys():
        # if exists, remove item from dict by using pop(key)
        if records.pop(patient_id):
            print(f"Patient with ID {patient_id} has been deleted")
        return records
    else:
        # tell user, that patient does not exist
        print(f"ERROR: Patient with ID {patient_id} does not exist")


# General: Writing Data Back to CSV
def write_patient_records(filename, records):
    # TODO: Implement writing records to CSV file (Refer to Exercises 4, 5, and 6)
    # open CSV file
    with open(filename, 'w', newline='') as file:
        # define fieldnames (header)
        fieldnames = ["Patient ID", "Name", "Date of Birth", "Height", "Weight"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # write header
        writer.writeheader()

        # iterate through records and write each row into csv
        for key, val in records.items():
            writer.writerow(val)


# Main function with the menu system
def main():
    records = read_patient_records("patient_records.csv")
    while True:
        print("\nPatient Records Management System")
        print("1. Add Patient Record")
        print("2. View Patient Records")
        print("3. Update Patient Record")
        print("4. Delete Patient Record")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '2':
            view_patient_records(records)
        elif choice == '3':
            update_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '4':
            delete_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
