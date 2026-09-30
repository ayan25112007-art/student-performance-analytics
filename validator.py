def get_valid_grade(prompt):
    while True:
        try:
            user_input = input(prompt)
            value = float(user_input)
            if value >= 0 and value <= 100:
                return value
            else:
                print("Error: Grade must be between 0 and 100")
        
        except:
            print("Error: Enter a valid number")

def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        else:
            print("Error: Input cannot be empty")