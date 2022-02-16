PIN = '4567'
attempts = 1
while attempts <= 3:
    supplied_pin = input('Enter your PIN: ')
    if supplied_pin != PIN:
         # input('Enter your PIN: ')
         print("Incorrect, attempts remaining:", int(3 - attempts))
         attempts += 1

        # elif supplied_pin == PIN:
        #     print('correct')
    else:
        print('correct')
        break

