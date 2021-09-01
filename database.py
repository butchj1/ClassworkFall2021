print("This is the database.py module")
print("Its name is {}".format(__name__))

import blood_calculator as bc

answer = bc.HDL_analysis(55)
print("The analysis of 55 HDL is {}".format(answer))

answer2 = bc.LDL_analysis(200)
print("The analysis of 200 LDL is {}".format(answer2))

