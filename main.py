from js import document

    onreg = document.getElementById("onreg").value
    medclear = document.getElementById("medclear").value
    
if onreg == "Yes":
    if medclear == "Yes":

        grade = int(input("What grade"))

        section = input("what section?")

        if section == "Emerald":
            if grade == 7:
                print("green hornet")

            elif grade == 10:
                print("green hornet")

            elif grade == 8:
                print("red bulldogs")

            elif grade == 9:
                print("red bulldogs")

            else:
                print("invalid output")

        elif section == "Ruby":
            if grade == 7:
                print("Yellow tigers")

            elif grade == 10:
                print("Yellow tigers")

            elif grade == 8:
                print("blue bears")

            elif grade == 9:
                print("blue bears")

            else:
                print("invalid output")

        else:
            print("invalid output")

    else:
        print("Please get a Medical Clearance.")

else:
    print("Please Register.")