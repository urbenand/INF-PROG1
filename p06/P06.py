import random
import psycopg


def count_patients():
    # Implement the query and return an integer
    # Connect to an existing database
    with psycopg.connect("dbname=P06 user=postgres") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # SELECT statement
            results = cur.execute("""SELECT COUNT(p.id) as patient_count FROM patients p""")
            # Fetch row zero
            counts = results.fetchone()[0]

            # return count
            return int(counts)


def get_patients_by_blood_group(blood_group):
    # Implement the query and return a list
    # Example: return [{'name': 'Luke Skywalker', 'age': 53, 'planet': 'Tatooine'}]
    with psycopg.connect("dbname=P06 user=postgres") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            results = cur.execute("""SELECT p.name, p.age, p.planet FROM patients p JOIN blood_groups b ON p.blood_group_id = b.id WHERE b.type = %s""", [blood_group])
            results = results.fetchall()
            patients = []
            for result in results:
                patients.append({'name': result[0], 'age': result[1], 'planet': result[2]})
                # patients.update(result)

            # print out value for debugging
            # print(f"{blood_group}:")
            # print(f"{patients}:")

            return patients


def insert_patient(name, age, planet, blood_group):
    # Implement the query and return the ID of the newly created patient
    # Example: return 1234

    with psycopg.connect("dbname=P06 user=postgres") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # get blood_group_id
            blood_group_id = cur.execute("""SELECT id AS blood_group_id FROM blood_groups WHERE type = %s""", [blood_group])
            blood_group_id = blood_group_id.fetchone()[0]

            # insert new patient into table
            result = cur.execute("""INSERT INTO patients (name, age, planet, blood_group_id) VALUES (%s, %s, %s, %s) RETURNING id; """,
            (name, age, planet, blood_group_id))
            new_id = result.fetchone()[0]

            return new_id



def verify_count(result):
    if isinstance(result, int):
        print("Success: Count is an integer, as expected.")
    else:
        print("Error: Count should be an integer.")


def verify_patient_list(result):
    if isinstance(result, list) and all(isinstance(item, dict) for item in result):
        print("Success: Patient list is a list of dictionaries, as expected.")
    else:
        print("Error: Patient list should be a list of dictionaries.")


def verify_insertion(result):
    if isinstance(result, int):
        print("Success: Inserted patient ID is an integer, as expected.")
    else:
        print("Error: Inserted patient ID should be an integer.")


def main():
    # !!! DO NOT MODIFY THIS FUNCTION !!!
    # ALL YOUR WORK SHOULD BE DONE IN THE 3 FUNCTIONS ABOVE

    # Possible new patients
    potential_new_patients = [
        {'name': 'Obi-Wan Kenobi', 'age': 57, 'planet': 'Stewjon', 'blood_group': 'A+'},
        {'name': 'Anakin Skywalker', 'age': 45, 'planet': 'Tatooine', 'blood_group': 'B+'},
        {'name': 'Padme Amidala', 'age': 46, 'planet': 'Naboo', 'blood_group': 'AB+'},
        {'name': 'Mace Windu', 'age': 64, 'planet': 'Haruun Kal', 'blood_group': 'O-'},
        {'name': 'Qui-Gon Jinn', 'age': 60, 'planet': 'Coruscant', 'blood_group': 'A-'}
    ]

    chosen_patient = random.choice(potential_new_patients)

    # Call and verify the functions
    count_result = count_patients()
    verify_count(count_result)

    blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    chosen_blood_group = random.choice(blood_groups)
    patient_list_result = get_patients_by_blood_group(chosen_blood_group)
    verify_patient_list(patient_list_result)

    insert_result = insert_patient(**chosen_patient)
    verify_insertion(insert_result)


if __name__ == '__main__':
    main()
