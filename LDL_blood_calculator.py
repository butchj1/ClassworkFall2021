# LDL Blood Calculator

def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            LDL_Driver()      
    print(choice)
    return(choice)

def LDL_Driver():
    LDL_value = ldl_input()
    LDL_character = LDL_analysis(LDL_value)
    ldl_output(LDL_value, LDL_character)
    
def ldl_input():
    ldl_value = int(input(("Enter LDL Value: ")))
    return ldl_value

def LDL_analysis(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 159:
        return "Borderline High"
    elif 160 <= LDL_value < 189:
        return "High"
    else:
        return "Very High"
        
def ldl_output(LDL_value, LDL_answer):
    print("The LDL value of {} is considered {}".format(LDL_value, LDL_answer))
    return   
    
interface()
