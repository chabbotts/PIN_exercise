password_number = 4321
max_number_of_attempts = 3
user_number_of_attempts = 0

while user_number_of_attempts < max_number_of_attempts:
    supplied_pin = input("Enter your PIN: ")
    if supplied_pin == str(password_number):
        print("You have access to your account.")
        break
    else:
        user_number_of_attempts += 1
        print("Incorrect! You have used", user_number_of_attempts, 'out of', max_number_of_attempts, 'attempts.')
        if user_number_of_attempts == max_number_of_attempts:
            print("You have no more attempts left. You are blocked from your account.")
