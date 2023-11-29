#if line is empty return an empty message
#if line has names print message with names
#Pseudocode
#condition if empty return empty message
#condition: if has name, return message with name and indexed




def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently: " + " ".join(f"{index + 1}. {name}" for index, name in enumerate(katz_deli))
        print(line_str)

# Example usage
line(["Oscar", "Ronnie", "Lyn"])

def take_a_number(katz_deli, name):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        for index, customer_name in enumerate(katz_deli):
            if customer_name == name:
                print(f"Welcome, {name}. You are number {index + 1} in line.")
                



take_a_number(["Ronnie", "Ochieng", "John", "ochieng", "Thomas"], "Ochieng")




def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        for index, name in enumerate(katz_deli):
            if name == katz_deli[-1]:
                print(f"Currently serving {name}.")
                updated_deli = katz_deli[:-1]
                return updated_deli
                

now_serving(["Ronnie", "Ochieng", "John", "ochieng"])







