#a = "The sky is blue"
#print(a)

#for letter in a:
#    print(letter)


def function_name():
    x = "hello"
    
    try:
        y = int(x)
    except ValueError:
        print("This is a string")
    

def main():
    function_name()


if __name__ == "__main__":
    main()