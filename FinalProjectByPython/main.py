import datetime

user_data = [
    {
        'email': '200103257@stu.sdu.edu.kz',
        'password': 'Anvarbek2003',
        'name': 'Anvarbek',
        'surname': 'Nurzhauganov',
        'age': '19',
        'gender': 'Male',
        'phone_number': '87076098760',
        'user_created_data': datetime.datetime.now(),
        'subscribers': []
    },
    {
        'email': '200103271@stu.sdu.edu.kz',
        'password': 'Aisana2003',
        'name': 'Aisana',
        'surname': 'Jumadilova',
        'age': '19',
        'gender': 'Female',
        'phone_number': '87076098760',
        'user_created_data': datetime.datetime.now(),
        'subscribers': []
    }
]
post_data = []
post_id = 0
comment_id = 0
request_user = ''
request_post = ''
request_subscriber = ''
global choose


def displayMenu():
    global post_id
    global choose
    print('\n********** Welcome to ErenArminMikasa *********\n')
    print(''
          '1 - Login page\n'
          '2 - Posts\n'
          '3 - My subscriptions\n'
          '4 - My subscribers\n'
          '0 - Quit'
          '\n')

    choose = input('Choose menu: ')
    if choose == '1':
        return LoginPage()
    elif choose == '2':
        return PostPage()
    elif choose == '3':
        return displayMySubscriptions()


def LoginPage():
    def displayUserMenu():
        status = input('\n'
                       '1 - Register\n'
                       '2 - Sign In\n'
                       '0 - Quit\n')
        if status == '1':
            return newUser()
        elif status == '2':
            return oldUser()
        elif status == '0':
            return displayMenu()

    def newUser():
        create_email = input('\nCreate user email address: \n')
        test = False

        for user in user_data:
            if create_email in user['email']:
                print('\n********** Email address already exists: ' + create_email + ' **********')
                return displayUserMenu()
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
                'user_created_data': user_created_data,
                'subscribers': []
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
    global comment_id
    global choose

    if request_user == '':
        print('\nYou must sign in to account!\n'
              '1 - Continue\n'
              '0 - Quit\n')
        choose = input('Enter your choice: ')
        if choose == '1':
            return LoginPage()
        elif choose == '0':
            return displayMenu()
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
            if len(post_data) == 0:
                print('\n********** Post data is empty! You can create a new post! **********\n')
                print('1 - Continue\n0 - Quit\n')
                choose = input('Enter your choice: ')
                if choose == '1':
                    return CreatePost()
                elif choose == '0':
                    return PostPage()
            else:
                for post in post_data:
                    try:
                        print("\n" +
                              f'Post id: {post["post_id"]}\n'
                              f'Post title: {post["post_title"]}\n'
                              f'Post description: {post["post_description"]}\n'
                              f'Post created date: {post["post_created_date"]}\n'
                              f'Post count of like: {len(post["like"])}\n'
                              f'Post count of comments: {len(post["comment"])}'
                              "\n")
                    except Exception as e:
                        print(e)
                print('********** You can view post detail **********\n')
                print('1 - Continue\n0 - Quit\n')
                choose = input('Enter your choice: ')
                if choose == '1':
                    for post in post_data:
                        print("\n" +
                              f'Post id: {post["post_id"]}\n'
                              f'Post title: {post["post_title"]}\n'
                              f'Post description: {post["post_description"]}\n'
                              f'Post created date: {post["post_created_date"]}\n'
                              f'Count of like: {len(post["like"])}\n'
                              f'Count of comments: {len(post["comment"])}' +
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

                print('\nPost created:\nPost id: ' + str(post_id) + '\nPost author: ' + post_author + '\nPost title: ' + post_title + '\nPost description: ' + post_description + '\nPost created date: ' + str(
                    post_created_data))

                create_post = {
                    'post_id': int(post_id),
                    'post_author': post_author,
                    'post_title': post_title,
                    'post_description': post_description,
                    'post_created_date': post_created_data,
                    'like': [],
                    'comment': []
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
                    print(
                        "\n" + f'Post id: {post["post_id"]}\nPost title: {post["post_title"]}\nPost description: {post["post_description"]}\nPost created date: {post["post_created_date"]}' + "\n")

            if len(my_post) == 0:
                print("\nYou don't have post.\nBut you can create a new post!\n"
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
                          f'Count of like: {len(post["like"])}\n'
                          f'Count of comment: {len(post["comment"])}'
                          f'\n')
            test = False
            for post in post_data:
                if len(post['comment']) > 0 and post['comment'][0] == request_post:
                    test = True
            if test:
                print('********** Comments **********')
            for post in post_data:
                for comment in post['comment']:
                    if post['post_id'] == request_post:
                        print(f'\n'
                              f'Comment author: {comment["user_id"]}\n'
                              f'Comment title: {comment["comment_title"]}\n'
                              f'Comment description: {comment["comment_description"]}\n'
                              f'Comment created: {comment["comment_created_date"]}\n'
                              f'\n******************************\n'
                              )
            print('**********\n'
                  '1 - Add like for this post\n'
                  '2 - Remove like at this post\n'
                  '3 - Add comment for this post\n'
                  '4 - Remove comment at this post\n'
                  '5 - Subscribe the author of this post\n'
                  '0 - Quit'
                  '\n**********\n')
            choose = input('Enter your choice: ')
            if choose == '1':
                return AddLikePost()
            elif choose == '2':
                return RemoveLikePost()
            elif choose == '3':
                return AddCommentPost()
            elif choose == '4':
                return RemoveCommentPost()
            elif choose == '5':
                return SubscribePostAuthor()
            return PostPage()

        def AddLikePost():
            for post in post_data:
                if request_user in post['like'] and post['post_id'] == request_post:
                    print('\n********** You can not add like for this post! **********\n')
                    return PostPage()
                elif post['post_id'] == request_post:
                    post['like'].append(request_user)
            print('\nYou have successfully added a like for this post!\n')
            return ViewListPost()

        def RemoveLikePost():
            for post in post_data:
                if request_user in post['like'] and post['post_id'] == request_post:
                    post['like'].remove(request_user)
                    print('\nYou have successfully removed a like on this post!\n')
                    return ViewListPost()
                elif post['post_id'] == request_post:
                    print("\nYou haven't liked this post yet\n")
                    return ViewListPost()

        def AddCommentPost():
            global comment_id
            comment_id += 1
            comment_title = input('Comment title: ')
            comment_description = input('Comment description: ')
            comment_created_date = datetime.datetime.now()

            create_comment = {
                'comment_id': int(comment_id),
                'user_id': request_user,
                'comment_post_id': request_post,
                'comment_title': comment_title,
                'comment_description': comment_description,
                'comment_created_date': comment_created_date
            }

            for post in post_data:
                if post['post_id'] == request_post:
                    post['comment'].append(create_comment)
            print(f'\n**********\nComment created:\n'
                  f'Comment id: {comment_id}\n'
                  f'Comment author: {request_user}\n'
                  f'Comment title: {comment_title}\n'
                  f'Comment description: {comment_description}\n'
                  f'\nComment created_date: {comment_created_date}'
                  f'\n**********\n')
            print('********** You have successfully created a new comment! **********\n')
            return ViewListPost()

        def RemoveCommentPost():
            global choose
            my_comment = []
            print('\n'
                  'You can only delete your comments.\n'
                  'Select the post you want to delete.'
                  '\n')

            for post in post_data:
                for comm in post['comment']:
                    if comm['user_id'] == request_user:
                        my_comment.append(comm)
                        if post['post_id'] == request_post:
                            print(
                                "\n" + f'Comment id: {comm["comment_id"]}\nComment title: {comm["comment_title"]}\nComment description: {comm["comment_description"]}\nComment created date: {comm["comment_created_date"]}' + "\n")

            if len(my_comment) == 0:
                print("\nYou don't have comment.\nBut you can create a new comment!\n"
                      "1 - Continue\n"
                      "0 - Quit\n")
                choose = input('Enter your choice: ')
                if choose == '1':
                    return AddCommentPost()
                elif choose == '0':
                    return ViewListPost()
            try:
                choose = int(input('Select the comment you want to delete by ID: '))
                for post in post_data:
                    for my_com in my_comment:
                        if choose == my_com['comment_id'] and my_com['comment_post_id'] == request_post:
                            post['comment'].remove(my_com)
                            my_comment.remove(my_com)
                            print(f'\nYou deleted comment: {my_com["comment_id"]}\n')
                            return ViewListPost()
                print('\n'
                      'We have declared a mistake somewhere!\n'
                      'Check it out again, please!'
                      '\n')
                return DetailPost(request_post)
            except Exception as e:
                print(e)
                return DetailPost(request_post)

        def SubscribePostAuthor():
            global choose
            for post in post_data:
                if post['post_id'] == request_post:
                    if post['post_author'] == request_user:
                        print(f'\n**********\nAuthor of this post: You)\n**********\n')
                    else:
                        print(f'\n**********\nAuthor of this post: {post["post_author"]}\n**********\n')
            print("\nAre you sure you want to follow this author?\n"
                  "1 - Continue\n"
                  "0 - Quit\n")
            choose = input('\nEnter your choice: ')
            if choose == '1':
                for post in post_data:
                    for user in user_data:
                        if post['post_id'] == request_post and user['email'] == post['post_author']:
                            if request_user in user['subscribers']:
                                print('\n********** You are already following this person! **********\n')
                                return DetailPost(request_post)
                            elif request_user == post['post_author']:
                                print("\n********** You can't subscribe to yourself! **********\n")
                                return DetailPost(request_post)
                            else:
                                user['subscribers'].append(request_user)
                                print('\n********** You have successfully subscribed! **********\n')
                                return DetailPost(request_post)
            elif choose == '0':
                return DetailPost(request_post)

        return displayPostMenu()


def displayMySubscriptions():
    global choose
    test = False
    for user in user_data:
        if request_user in user['subscribers']:
            test = True
    if test:
        print('\n********** My subscriptions **********\n')
    for user in user_data:
        if request_user in user['subscribers']:
            print(f'\nUser email: {user["email"]}\n')

    if test:
        print("\n********** You can view user detail **********\n"
              "1 - Continue\n"
              "0 - Quit\n")
        choose = input('\nEnter your choice: ')

        if choose == '1':

            choose = input('\nEnter email which user you want to see in detail: ')
            for user in user_data:
                if request_user in user['subscribers'] and choose == user['email']:
                    return DetailSubscriber(choose)
                print('\n'
                      'We have declared a mistake somewhere!\n'
                      'Check it out again, please!'
                      '\n')
                return displayMySubscriptions()
        return displayMenu()
    print("\n********** You haven't subscribed to anyone before! **********")

    return displayMenu()


def DetailSubscriber(subscriber_detail):
    global request_subscriber
    global choose
    request_subscriber = subscriber_detail

    for user in user_data:
        if request_subscriber == user['email']:
            print(f'\n'
                  f'User email: {user["email"]}\n'
                  f'User name: {user["name"]}\n'
                  f'User surname: {user["surname"]}\n'
                  f'User age: {user["age"]}\n'
                  f'User gender: {user["gender"]}'
                  f'\n')

    print("\n********** Do you want to unsubscribe? **********\n"
          "1 - Continue\n"
          "0 - Quit\n")
    choose = input('\nEnter your choice: ')

    if choose == '1':
        for user in user_data:
            if request_user in user['subscribers']:
                print(f'\nYou have successfully unsubscribed from the user: {user["email"]}\n')
                user['subscribers'].remove(request_user)
                return displayMenu()
    return displayMenu()


if __name__ == '__main__':
    displayMenu()
