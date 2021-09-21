class Patient:

    def __init__(self, input_name, id_no, age):
        self.name = name
        self.id_no = id_no
        self.age = age
        self.tests = []
        
        
def class_work():
    new_patient = Patient("Ann Ables", 120, 36)
    print(new_patient.id_no)
    print(new_patient.name)
    x = Patient("Bob Boyes", 24, 33)
    print(x.name)


def create_database_entry(patient_name, id_no, age):
    new_patient = {"name": patient_name, "id_no": id_no, 
                    "age": age, "tests": []}
    return new_patient


def print_database(db):
    locations = ["Room 1", "Room 4", "ER", "Post-Op"]
    for patient, location in zip(db, locations):
        print("{} - {}".format(patient, location))


def main():
    class_work()
    return
    
    db = {}
    x = create_database_entry("Ann Ables", 1, 30)
    db[x["id_no"]] = x
    x = create_database_entry("Bob Byles", 2, 31)
    db[x["id_no"]] = x
    x = create_database_entry("Chris Chou", 3, 33)
    db[x["id_no"]] = x
    x = create_database_entry("David Dinkins", 4, 34)
    db[x["id_no"]] = x
    print(db)
    
    patient_id_tested = 24
    test_done = ("HDL", 65)
    
    patient = get_patient(db, patient_id_tested)
    patient["tests"].append(test_done)
    print(db)
    
    print_database(db)


def print_patients_over_age(age, db):
    for patient in db:
        if patient["age"] > age:
            print(patient[0])


def get_patient(db, id_no):
    patient = db[id_no]
    #for patient in db:
      #  if patient["id_no"] == id_no:
       #     return patient
    return patient

            
if __name__ == "__main__":
    main()