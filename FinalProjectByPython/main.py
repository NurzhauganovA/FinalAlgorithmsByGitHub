import datetime

user_data = []
post_data = []
comment_post_data = []
post_id = 0
like_post = [
    {
        'user_id': '',
        'post_id': ''
    }
]
request_user = ''
request_post = ''
global choose


def displayMenu():
    global post_id
    global choose
    print('\n********** Welcome to ErenArminMikasa *********\n')
    print(''
          '1 - Login page\n'
          '2 - Posts\n'
          '3 - My subscribers\n'
          '4 - My subscriptions\n'
          '5 - Show all users\n'
          '0 - Quit'
          '\n')

    choose = input('Choose menu: ')
    if choose == '1':
        return LoginPage()
    elif choose == '2':
        return PostPage()
    elif choose == '5':
        print(user_data)


def LoginPage():

    def displayUserMenu():
        status = input('\n'
                       '1 - Register\n'
                       '2 - Sign In\n'
                       '0 - Quit\n')
        if status == '1':
            newUser()
        elif status == '2':
            oldUser()
        elif status == '0':
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
            create_password = input('\nCreate user password: \n')
        create_name = input('\nCreate user name: \n')
        if create_name.isalpha():
            test = True
        else:
            print('\n********** Enter your name correctly!!! **********')
            create_name = input('\nCreate user name: \n')
        create_surname = input('\nCreate user surname: \n')
        if create_surname.isalpha():
            test = True
        else:
            print('\n********** Enter your surname correctly!!! **********')
            create_surname = input('\nCreate user surname: \n')
        create_age = input('\nCreate user age: \n')
        if create_age.isnumeric():
            test = True
        else:
            print('\n********** Age must be number!!! **********')
            create_age = input('\nCreate user age: \n')
        create_gender = input('\nCreate user gender: (Gender must be Male or Female)\n')
        if create_gender in 'Male' or create_gender in 'Female':
            test = True
        else:
            print('\n********** Gender must be Male or Female!!! **********')
            create_gender = input('\nCreate user gender: \n')
        create_phone_number = input('\nCreate user phone number: \n')
        if create_phone_number.isdigit() or create_phone_number.isnumeric():
            test = True
        else:
            print('\n********** Phone number must be a number!!! **********')
            create_phone_number = input('\nCreate user phone number: \n')
        if test:
            user_created_data = datetime.datetime.now()
            print(
                '\n******************\nUser created: \n' + f'Email address: {create_email}' + "\n" + f'Password: {create_password}' + "\n" + f'Name: {create_name}' + "\n" + f'Surname: {create_surname}' + "\n" + f'Age: {create_age}' + "\n" + f'Gender: {create_gender}' + "\n" + f'Phone number: {create_phone_number}' + '\n\n' + f'User created data: {user_created_data}' + '\n' + '*******************')

            create_user = {
                'email': create_email,
                'password': create_password,
                'name': create_name,
                'surname': create_surname,
                'age': create_age,
                'gender': create_gender,
                'phone_number': create_phone_number,
                'user_created_data': user_created_data
            }
            user_data.append(create_user)
            return displayMenu()

    def oldUser():
        global request_user
        email = input('Enter your email address: \n')
        password = input('Enter your password: \n')
        test = True

        for user in user_data:
            if email == user['email'] and password == user['password']:
                print('\nLogin successful!\n')
                test = False
        if test:
            print("\n********** User doesn't exist or wrong email/password **********")
            return LoginPage()
        else:
            request_user = email
            print('Requesting user: ' + request_user)
            return displayMenu()
    return displayUserMenu()


def PostPage():
    global post_id
    global choose

    if request_user == '':
        print('\nYou must sign in to account!\n'
              '1 - Continue\n'
              '0 - Quit\n')
        choose = input('Enter your choice: ')
        if choose == '1':
            return LoginPage()
        elif choose == '0':
            return PostPage()
    else:

        def displayPostMenu():
            global choose

            print('\n'
                  '1 - Post list\n'
                  '2 - Create post\n'
                  '3 - Delete post\n'
                  '0 - Quit'
                  '\n')

            choose = input('Choose post menu: ')
            if choose == '1':
                return ViewListPost()
            elif choose == '2':
                return CreatePost()
            elif choose == '3':
                return DeletePost()
            elif choose == '0':
                return displayMenu()

        def ViewListPost():
            global choose
            if len(post_data) < 1:
                print('\n********** Post data is empty! You can create a new post! **********\n')
                print('1 - Continue\n0 - Quit\n')
                choose = input('Enter your choice: ')
                if choose == '1':
                    return CreatePost()
                elif choose == '0':
                    return PostPage()
            else:
                if len(like_post) > 1:
                    for post in post_data:
                        for like in like_post:
                            for user in user_data:
                                if post['post_id'] == like['post_id'] and like['user_id'] == user['email']:
                                    print("\n" +
                                          f'Post id: {post["post_id"]}\n'
                                          f'Post title: {post["post_title"]}\n'
                                          f'Post description: {post["post_description"]}\n'
                                          f'Post created date: {post["post_created_date"]}\n'
                                          f'Post count of like: {len(like)}'
                                          "\n")
                else:
                    for post in post_data:
                        print("\n" +
                              f'Post id: {post["post_id"]}\n'
                              f'Post title: {post["post_title"]}\n'
                              f'Post description: {post["post_description"]}\n'
                              f'Post created date: {post["post_created_date"]}'
                              "\n")
                print('********** You can view post detail **********\n')
                print('1 - Continue\n0 - Quit\n')
                choose = input('Enter your choice: ')
                if choose == '1':
                    for post in post_data:
                        print("\n" +
                              f'Post id: {post["post_id"]}\n'
                              f'Post title: {post["post_title"]}\n'
                              f'Post description: {post["post_description"]}\n'
                              f'Post created date: {post["post_created_date"]}' +
                              "\n")
                    choose = int(input('\nChoose which post you want to see in detail: '))
                    for post in post_data:
                        if choose == post['post_id']:
                            return DetailPost(post['post_id'])
                elif choose == '0':
                    return PostPage()
                else:
                    return PostPage()

        def CreatePost():
            global post_id
            global choose
            if request_user == '':
                print('\nYou must sign in to account!\n'
                      '1 - Continue\n'
                      '0 - Quit\n')
                choose = input('Enter your choice: ')
                if choose == '1':
                    return LoginPage()
                elif choose == '0':
                    return PostPage()
            else:
                post_id += 1
                post_title = input('Post title: \n')
                post_description = input('Post description: \n')
                post_created_data = datetime.datetime.now()
                post_author = request_user

                print('Post created:\nPost id: ' + str(post_id) + '\nPost author: ' + post_author + '\nPost title: ' + post_title + '\nPost description: ' + post_description + '\nPost created date: ' + str(post_created_data))

                create_post = {
                    'post_id': post_id,
                    'post_author': post_author,
                    'post_title': post_title,
                    'post_description': post_description,
                    'post_created_date': post_created_data
                }

                post_data.append(create_post)
                return displayPostMenu()

        def DeletePost():
            global choose
            my_post = []
            print('\n'
                  'You can only delete your posts.\n'
                  'Select the post you want to delete.'
                  '\n')

            for post in post_data:
                if post['post_author'] == request_user:
                    my_post.append(post)
                    print("\n" + f'Post id: {post["post_id"]}\nPost title: {post["post_title"]}\nPost description: {post["post_description"]}\nPost created date: {post["post_created_date"]}' + "\n")

            if len(my_post) == 0:
                print("\nYou don't have post.\nBut you can create a post!\n"
                      "1 - Continue\n"
                      "0 - Quit\n")
                choose = input('Enter your choice: ')
                if choose == '1':
                    return CreatePost()
                elif choose == '0':
                    return PostPage()
            try:
                choose = int(input('Select the post you want to delete by ID: \n'))
                for post in post_data:
                    for my_p in my_post:
                        if choose == post['post_id'] and choose == my_p['post_id']:
                            post_data.remove(post)
                            print(f'\nYou deleted post: {post["post_id"]}\n')
                            return PostPage()
                else:
                    print('\n'
                          'We have declared a mistake somewhere!\n'
                          'Check it out again, please!'
                          '\n')
                    return PostPage()
            except Exception as e:
                print(e)
                return PostPage()

        def DetailPost(post_id_detail):
            global choose, request_post
            request_post = post_id_detail
            for post in post_data:
                if post['post_id'] == request_post:
                    print(f'\n'
                          f'Post id: {post["post_id"]}\n'
                          f'Post author: {post["post_author"]}\n'
                          f'Post title: {post["post_title"]}\n'
                          f'Post description: {post["post_description"]}\n'
                          f'Post created data: {post["post_created_date"]}\n'
                          f'\n')
            print('**********\n'
                  '1 - Add like for this post\n'
                  '2 - Remove like at this post\n'
                  '3 - Add comment for this post\n'
                  '4 - Remove comment at this post\n'
                  ''
                  '**********\n')
            choose = input('Enter your choice: ')
            if choose == '1':
                for like in like_post:
                    if request_post == like['post_id'] and request_user == like['user_id']:
                        print('\n********** You can not add like for this post! **********\n')
                        return PostPage()
                like_post.append(
                    {
                        'user_id': request_user,
                        'post_id': request_post
                    }
                )
                print('\nYou successfully added like for this post!\n')
                return PostPage()
            elif choose == '2':
                print(like_post)
            return PostPage()

        return displayPostMenu()


if __name__ == '__main__':
    displayMenu()