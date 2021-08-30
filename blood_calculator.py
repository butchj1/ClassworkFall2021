# Blood Calculator

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
            HDL_Driver()
            
            
    print(choice)
    return(choice)



def HDL_Driver():
    HDL_value = hdl_input()
    hdl_analysis(HDL_Value)
    hdl_output(hdl_value, hdl_character)

def hdl_input():
    hdl_value = int(input(("Enter HDL Value: ")))
    return hdl_value

def hdl_analysis():
    if hdl_value >= 60:
        return "Normal"
    elif 40 < hdl_value < 60:
        return "Borderline Low"
    else hdl_value < 40:
        return "Low"
        
def hdl_output(hdl_value, hdl_answer):
    
interface()