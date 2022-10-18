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
        'subscriptions': [],
        'blocked_users': []
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
        'subscriptions': [],
        'blocked_users': []
    },
    {
        'email': 'zangar@stu.sdu.edu.kz',
        'password': 'Zangar2004',
        'name': 'Zangar',
        'surname': 'Zangar',
        'age': '18',
        'gender': 'Male',
        'phone_number': '87076098760',
        'user_created_data': datetime.datetime.now(),
        'subscriptions': [],
        'blocked_users': []
    }
]
post_data = []
post_id = 0
comment_id = 0
request_user = '200103257@stu.sdu.edu.kz'
request_post = ''
request_subscription = ''
request_blocked_user = ''
dif_posts_blocked_users = []
posts_blocked_users = []
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
          '5 - My blocking users\n'
          '6 - My Profile Page\n'
          '0 - Quit\n'
          '')

    choose = input('Choose menu: ')
    if choose == '1':
        return LoginPage()
    elif choose == '2':
        return PostPage()
    elif choose == '3':
        return mySubscriptionsPage()
    elif choose == '5':
        return displayMyBlockedUsers()
    elif choose == '6':
        return displayMyProfile()
    elif choose == '0':
        return
    else:
        return displayMenu()


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
                'subscriptions': [],
                'blocked_users': []
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
            return PostPage()

        def ViewListPost():
            global choose
            global post_data
            request_detail_post = 0
            test = False

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
                    for user in user_data:
                        if request_user == user['email'] and post['post_author'] not in user['blocked_users']:
                            print("\n" +
                                  f'Post id: {post["post_id"]}\n'
                                  f'Post title: {post["post_title"]}\n'
                                  f'Post description: {post["post_description"]}\n'
                                  f'Post created date: {post["post_created_date"]}\n'
                                  f'Post count of like: {len(post["like"])}\n'
                                  f'Post count of comments: {len(post["comment"])}'
                                  "\n")
                print('********** You can view post detail **********\n')
                print('1 - View Post Detail\n0 - Quit\n')
                choose = input('Enter your choice: ')
                if choose == '1':
                    choose = int(input('\nChoose which post you want to see in detail: '))
                    for post in post_data:
                        for user in user_data:
                            if request_user == user['email'] and post['post_author'] not in user['blocked_users'] and choose == post['post_id']:
                                request_detail_post = post['post_id']
                                test = True
                    if test:
                        return DetailPost(request_detail_post)
                    print('\n'
                          'We have declared a mistake somewhere!\n'
                          'Check it out again, please!'
                          '\n')
                    return PostPage()
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
                    post['like'].append(
                        {
                            'user_id': request_user
                        }
                    )
            print('\nYou have successfully added a like for this post!\n')
            return ViewListPost()

        def RemoveLikePost():
            for post in post_data:
                for like in post['like']:
                    if request_user in like['user_id'] and post['post_id'] == request_post:
                        post['like'].remove(like)
                        print('\nYou have successfully removed a like on this post!\n')
                        return DetailPost(request_post)
                    elif post['post_id'] == request_post:
                        print("\nYou haven't liked this post yet\n")
                        return DetailPost(request_post)
            print("\nYou haven't liked this post yet\n")
            return DetailPost(request_post)

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
                    if comm['user_id'] == request_user and len(comm) == 0:
                        print("\nYou don't have comment.\nBut you can create a new comment!\n"
                              "1 - Continue\n"
                              "0 - Quit\n")
                        choose = input('Enter your choice: ')
                        if choose == '1':
                            return AddCommentPost()
                        elif choose == '0':
                            return ViewListPost()
                    elif comm['user_id'] == request_user:
                        my_comment.append(comm)
                        if post['post_id'] == request_post and comm['comment_post_id'] == request_post:
                            print(
                                "\n" + f'Comment id: {comm["comment_id"]}\nComment title: {comm["comment_title"]}\nComment description: {comm["comment_description"]}\nComment created date: {comm["comment_created_date"]}' + "\n")
            try:
                choose = int(input('Select the comment you want to delete by ID: '))
                for post in post_data:
                    for comm in post['comment']:
                        if choose == comm['comment_id'] and comm['comment_post_id'] == request_post and comm['user_id'] == request_user:
                            post['comment'].remove(comm)
                            my_comment.remove(comm)
                            print(f'\nYou deleted comment: {comm["comment_id"]}\n')
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
                        if post['post_id'] == request_post and user['email'] == request_user:
                            if post['post_author'] in user['subscriptions']:
                                print('\n********** You are already following this person! **********\n')
                                return DetailPost(request_post)
                            elif request_user == post['post_author']:
                                print("\n********** You can't subscribe to yourself! **********\n")
                                return DetailPost(request_post)
                            else:
                                user['subscriptions'].append(post['post_author'])
                                print('\n********** You have successfully subscribed! **********\n')
                                return DetailPost(request_post)
            elif choose == '0':
                return DetailPost(request_post)

        return displayPostMenu()


def mySubscriptionsPage():

    def displayMySubscriptions():
        global choose
        test = False
        for user in user_data:
            if request_user == user['email'] and len(user['subscriptions']) != 0:
                test = True
        if test:
            print('\n********** My subscriptions **********\n')
        for user in user_data:
            for subscription in user['subscriptions']:
                if request_user == user['email']:
                    print(f'\nUser email: {subscription}')

        if test:
            print("\n********** You can view user detail **********\n"
                  "1 - Continue\n"
                  "0 - Quit\n")
            choose = input('\nEnter your choice: ')

            if choose == '1':
                choose = input('\nEnter email which user you want to see in detail: ')
                for user in user_data:
                    for subscription in user['subscriptions']:
                        if subscription == choose:
                            return DetailSubscription(subscription)
                print('\n'
                      'We have declared a mistake somewhere!\n'
                      'Check it out again, please!'
                      '\n')
                return displayMySubscriptions()
            return displayMenu()
        print("\n********** You haven't subscribed to anyone before! **********")
        return displayMenu()

    def DetailSubscription(subscription_detail):
        global request_subscription
        global choose
        request_subscription = subscription_detail

        for user in user_data:
            if request_subscription == user['email']:
                print(f'\n'
                      f'User email: {user["email"]}\n'
                      f'User name: {user["name"]}\n'
                      f'User surname: {user["surname"]}\n'
                      f'User age: {user["age"]}\n'
                      f'User gender: {user["gender"]}'
                      f'\n')

        print("\n********** Do you want to unsubscribe/block/view post list? **********\n"
              "1 - Unsubscribe\n"
              "2 - Block user\n"
              "3 - View Post List\n"
              "4 - View Common Friends\n"
              "0 - Quit\n")
        choose = input('\nEnter your choice: ')

        for user in user_data:
            if choose == '2':
                if request_user == user['email']:
                    print(f'\n********** You have blocked {request_subscription} user **********')
                    user['blocked_users'].append(request_subscription)
                if request_user == user['email'] and request_subscription in user['subscriptions']:
                    print(
                        f'\n********** Blocked user: {request_subscription} removed from your list of subscriptions **********')
                    user['subscriptions'].remove(request_subscription)
            elif choose == '1' and request_user == user['email'] and request_subscription in user['subscriptions']:
                print(f'\nYou have successfully unsubscribed from the user: {user["email"]}\n')
                user['subscriptions'].remove(request_subscription)
                return displayMenu()
            elif choose == '3':
                return displayPostListUser(request_subscription)
            elif choose == '4':
                return displayCommonFriends(request_subscription)

        return displayMenu()

    def displayPostListUser(subscription_user_detail_id):
        global request_subscription, choose
        request_subscription = subscription_user_detail_id

        print(f'\nView detail user {request_user}\n')
        print('\n********** POST LIST **********\n')

        for post in post_data:
            if post['post_author'] == request_subscription and len(post_data) == 0:
                print('\n********** User does not have post! **********\n')
                return displayMenu()
            elif post['post_author'] == request_subscription:
                print(f'\n'
                      f'Post title: {post["post_title"]}\n'
                      f'Post description: {post["post_description"]}\n'
                      f'Post created data: {post["post_created_date"]}\n'
                      f'Count of like: {len(post["like"])}\n'
                      f'Count of comment: {len(post["comment"])}'
                      f'\n')
                for comment in post['comment']:
                    print(f'\n'
                          f'********** COMMENTS **********\n'
                          f'Comment Author: {comment["user_id"]}\n'
                          f'Comment Title: {comment["comment_title"]}\n'
                          f'Comment Description: {comment["comment_description"]}\n'
                          f'Comment Created Date: {comment["comment_created_date"]}\n'
                          f'\n')
        return displayMySubscriptions()

    def displayCommonFriends(user_common_friends):
        global choose, request_subscription, request_user
        request_subscription = user_common_friends
        my_subscriptions = []
        user_subscriptions = []
        for user in user_data:
            if request_user == user['email']:
                for subscription in user['subscriptions']:
                    my_subscriptions.append(subscription)
            if request_subscription == user['email']:
                for subscription in user['subscriptions']:
                    user_subscriptions.append(subscription)
        result = my_subscriptions + user_subscriptions
        _size = len(result)
        repeated = []
        for i in range(_size):
            k = i + 1
            for j in range(k, _size):
                if result[i] == result[j] and result[i] not in repeated:
                    repeated.append(result[i])
        print(f'\nYou are subscribed to a user:')
        for repeat in repeated:
            print(f'\n{repeat}')

        print("\n********** You can view user detail **********\n"
              "1 - Continue\n"
              "0 - Quit\n")
        choose = input('\nEnter your choice: ')

        if choose == '1':
            choose = input('\nEnter email which user you want to see in detail: ')
            for user in user_data:
                for common in repeated:
                    if request_user == user['email'] and common not in user['blocked_users'] and common == choose:
                        return DetailSubscription(common)
            print('\n'
                  'We have declared a mistake somewhere!\n'
                  'Check it out again, please!'
                  '\n')
            return displayMySubscriptions()

        return displayMenu()

    return displayMySubscriptions()


def displayMyBlockedUsers():
    global choose
    test = False

    for user in user_data:
        if request_user == user['email'] and len(user['blocked_users']) != 0:
            test = True

    if test:
        print('\nMy blocked users:\n')

    for user in user_data:
        for blocked_user in user['blocked_users']:
            if request_user == user['email']:
                print(f'\nUser email: {blocked_user}')

    if test:
        print("\n********** You can view blocked user detail **********\n"
              "1 - Continue\n"
              "0 - Quit\n")
        choose = input('\nEnter your choice: ')

        if choose == '1':
            choose = input('\nEnter email which user you want to see in detail: ')
            for user in user_data:
                for blocked_user in user['blocked_users']:
                    if blocked_user == choose:
                        return DetailBlockedUser(blocked_user)
            print('\n'
                  'We have declared a mistake somewhere!\n'
                  'Check it out again, please!'
                  '\n')
            return displayMyBlockedUsers()
        return displayMenu()
    print("\n********** You haven't blocked to anyone before! **********")
    return displayMenu()


def DetailBlockedUser(blocked_user_detail):
    global request_blocked_user
    global choose
    request_blocked_user = blocked_user_detail

    for user in user_data:
        if request_blocked_user == user['email']:
            print(f'\n'
                  f'User email: {user["email"]}\n'
                  f'User name: {user["name"]}\n'
                  f'User surname: {user["surname"]}\n'
                  f'User age: {user["age"]}\n'
                  f'User gender: {user["gender"]}'
                  f'\n')

    print("\n********** Do you want to unblock? **********\n"
          "1 - Continue\n"
          "0 - Quit\n")
    choose = input('\nEnter your choice: ')

    for user in user_data:
        if choose == '1' and request_user == user['email'] and request_blocked_user in user['blocked_users']:
            print(f'\nYou have successfully unblocked: {request_blocked_user}\n')
            user['blocked_users'].remove(request_subscription)
    return displayMenu()


def displayMyProfile():
    global choose
    global request_user
    print('\n********** My Post List **********\n')
    for post in post_data:
        if post['post_author'] == request_user:
            print(f'\n'
                  f'Post title: {post["post_title"]}\n'
                  f'Post description: {post["post_description"]}\n'
                  f'Post created data: {post["post_created_date"]}\n'
                  f'Count of like: {len(post["like"])}\n'
                  f'Count of comment: {len(post["comment"])}'
                  f'\n')
    print('\n********** My Comment List **********\n')
    for post in post_data:
        for comment in post['comment']:
            if comment['user_id'] == request_user and post['post_id'] == comment['comment_post_id']:
                print(f'\n'
                      f'Post Title: {post["post_title"]}\n'
                      f'Comment Title: {comment["comment_title"]}\n'
                      f'Comment Description: {comment["comment_description"]}\n'
                      f'Comment Created Date: {comment["comment_created_date"]}\n'
                      f'\n')
    return displayMenu()


if __name__ == '__main__':
    displayMenu()