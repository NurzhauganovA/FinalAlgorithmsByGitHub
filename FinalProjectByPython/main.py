def displayMenu():
    print('\n********** Welcome to ErenArminMikasa *********\n')
    print(''
          '1 - Login page\n'
          '2 - Posts\n'
          '3 - My subscribers\n'
          '4 - My subscriptions\n'
          '0 - Quit'
          '\n')

    choose = input('Choose menu: ')
    if choose == '1':
        return LoginPage()
    elif choose == '2':
        return PostPage()


def LoginPage():
    user_data = [
        {
            'email': '',
            'password': '',
            'name': '',
            'surname': '',
            'age': '',
            'gender': '',
            'phone_number': ''
        }
    ]

    status = ''

    def displayUserMenu():
        status = input('\n1 - Register\n2 - Sign In\n3 - Quit\n')
        if status == '1':
            newUser()
        elif status == '2':
            oldUser()
        else:
            return displayMenu()

    def newUser():
        create_email = input('\nCreate user email address: \n')
        test = False

        for user in user_data:
            if create_email in user['email']:
                print('\n********** Email address already exists: ' + create_email + ' **********')
                displayUserMenu()
        create_password = input('\nCreate user password: (password must have greater than 8 and less than 20)\n')
        if 8 <= len(create_password) <= 20:
            test = True
        else:
            print('\n********** Password must be greater than 8 and less than 20!!! **********')
            test = False
            newUser()
        create_name = input('\nCreate user name: \n')
        if create_name.isalpha():
            test = True
        else:
            print('\n********** Enter your name correctly!!! **********')
            test = False
            newUser()
        create_surname = input('\nCreate user surname: \n')
        if create_surname.isalpha():
            test = True
        else:
            print('\n********** Enter your surname correctly!!! **********')
            test = False
            newUser()
        create_age = input('\nCreate user age: \n')
        if create_age.isnumeric():
            test = True
        else:
            print('\n********** Age must be number!!! **********')
            test = False
            newUser()
        create_gender = input('\nCreate user gender: (Gender must be Male or Female)\n')
        if create_gender in 'Male' or create_gender in 'Female':
            test = True
        else:
            print('\n********** Gender must be Male or Female!!! **********')
            test = False
            newUser()
        create_phone_number = input('\nCreate user phone number: \n')
        if create_phone_number.isdigit() or create_phone_number.isnumeric():
            test = True
        else:
            print('\n********** Phone number must be a number!!! **********')
            test = False
            newUser()
        if test:
            print(
                '\n******************\nUser created: \n' + f'Email address: {create_email}' + "\n" + f'Password: {create_password}' + "\n" + f'Name: {create_name}' + "\n" + f'Surname: {create_surname}' + "\n" + f'Age: {create_age}' + "\n" + f'Gender: {create_gender}' + "\n" + f'Phone number: {create_phone_number}' + '\n*******************')

            create_user = {
                'email': create_email,
                'password': create_password,
                'name': create_name,
                'surname': create_surname,
                'age': create_age,
                'gender': create_gender,
                'phone_number': create_phone_number
            }
            user_data.append(create_user)
            return displayMenu()

    def oldUser():
        email = input('Enter your email address: \n')
        password = input('Enter your password: \n')
        test = True

        for user in user_data:
            if email in user['email'] and password in user['password']:
                print('\nLogin successful!')
                test = False
        if test:
            print("\n********** User doesn't exist or wrong email/password **********")
        else:
            return displayMenu()
    return displayUserMenu()


def PostPage():
    print('Hello')


if __name__ == '__main__':
    displayMenu()