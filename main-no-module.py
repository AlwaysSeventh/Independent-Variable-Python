# Scenario 1 Ski Club

# Business A:
# $50/day

# Business B:
# $40/day, $200 Registration

# X amount of months

total_a = None
total_b = None
indepedent_var_a = None
dependent_var_a = 50
indepedent_var_b = 200
dependent_var_b = 40
timeForBoth = None

def repeat_function():
    while True: # repeats the function
        indepedent_var_a = int(input("What is the registration fee? (dollars) ")) # asks for input in (int)
        timeForBoth = int(input("What is the time period? (months) "))
        if (indepedent_var_a != None):
                total_b = indepedent_var_b + timeForBoth * dependent_var_b # calculates fee + monthly * time period
                total_a = indepedent_var_a + dependent_var_a * timeForBoth # calculates independent + dependent * time period
                converted_a = str(total_a) # converts total_a and total_b to strings for print()
                converted_b = str(total_b)
                convertedTime = str(timeForBoth)
                print("You pay business A " + "$" + converted_a + " " + "over a period of " + convertedTime + " " + "months.") # prints a messsage to the console
                print("You pay business B " + "$" + converted_b + " " + "over a period of " + convertedTime + " " + "months.")
                if (total_a > total_b):
                    print("You pay more with Business A")
                else:
                    print("You pay more with Business B")
        else:
            print("ERROR: Enter an integer!")
repeat_function() # calls the function
