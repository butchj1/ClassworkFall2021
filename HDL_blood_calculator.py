# HDL Blood Calculator

def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver() 
        elif choice == 2:
            LDL_Driver
    print(choice)
    return(choice)

def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = HDL_analysis(HDL_value)
    hdl_output(HDL_value, HDL_character)
    
def hdl_input():
    hdl_value = int(input(("Enter HDL Value: ")))
    return hdl_value

def HDL_analysis(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"
        
def hdl_output(HDL_value, HDL_answer):
    print("The HDL value of {} is considered {}".format(HDL_value, HDL_answer))
    return   

if __name__ == "__main__"
    interface()
