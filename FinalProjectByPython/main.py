import datetime
from post_sorting import postBubbleSort, postMergeSort, postInsertionSort, postQuickSort

""" ========== Adding our basic data ========== """
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
        'subscriptions': ['200103271@stu.sdu.edu.kz', 'zangar@stu.sdu.edu.kz', '200103399@stu.sdu.edu.kz'],
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
        'subscriptions': ['200103257@stu.sdu.edu.kz', 'zangar@stu.sdu.edu.kz', '200103399@stu.sdu.edu.kz'],
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
        'subscriptions': ['200103271@stu.sdu.edu.kz', '200103257@stu.sdu.edu.kz', '200103399@stu.sdu.edu.kz'],
        'blocked_users': []
    },
    {
        'email': '200103399@stu.sdu.edu.kz',
        'password': 'Arshat2003',
        'name': 'Arshat',
        'surname': 'Kudabayev',
        'age': '19',
        'gender': 'Male',
        'phone_number': '87076098760',
        'user_created_data': datetime.datetime.now(),
        'subscriptions': ['200103271@stu.sdu.edu.kz', 'zangar@stu.sdu.edu.kz', '200103257@stu.sdu.edu.kz'],
        'blocked_users': []
    }
]

""" ========== All global variables that we need ========== """
post_data = [
    {
        'post_id': 1,
        'post_author': '200103399@stu.sdu.edu.kz',
        'post_title': 'Title 1',
        'post_description': 'Description 1',
        'post_created_date': datetime.datetime.now(),
        'like': ['max@example.com', 'no@example.com', 'qwerty@example.com'],
        'comment': []
    },
    {
        'post_id': 2,
        'post_author': '200103271@stu.sdu.edu.kz',
        'post_title': 'Title 2',
        'post_description': 'Description 2',
        'post_created_date': datetime.datetime.now(),
        'like': ['no@example.com', 'qwerty@example.com'],
        'comment': []
    },
    {
        'post_id': 3,
        'post_author': '200103257@stu.sdu.edu.kz',
        'post_title': 'Title 3',
        'post_description': 'Description 3',
        'post_created_date': datetime.datetime.now(),
        'like': ['200103257@stu.sdu.edu.kz', '200103271@stu.sdu.edu.kz', '200103399@stu.sdu.edu.kz', 'zangar@stu.sdu.edu.kz'],
        'comment': []
    },
    {
        'post_id': 4,
        'post_author': 'zangar@stu.sdu.edu.kz',
        'post_title': 'Title 4',
        'post_description': 'Description 4',
        'post_created_date': datetime.datetime.now(),
        'like': ['200103257@stu.sdu.edu.kz'],
        'comment': []
    }
]  # Global variable that contains the data of all posts
post_id = 0  # Global variable that defines the ID of the added posts
comment_id = 0  # Global variable that defines the ID of the comments added to the post.
request_user = '200103257@stu.sdu.edu.kz'  # Global variable that defines the User who entered the program
request_post = ''  # Global variable that determines which post we are currently working with
request_subscription = ''  # Global variable that defines which subscription we are currently working with
request_blocked_user = ''  # Global variable that determines which blocked user we are currently working with
dif_posts_blocked_users = []  # Global variable that defines a list of differences for blocked users' posts.
posts_blocked_users = []  # Global variable that defines the list of posts of blocked users
common_friends = []  # Global variable defining the list of mutual friends
global choose


def displayMenu():
    """ Display Main menu """
    global post_id, choose
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
    elif choose == '4':
        return
    elif choose == '5':
        return displayMyBlockedUsers()
    elif choose == '6':
        return displayMyProfile()
    return displayMenu()


def LoginPage():
    """ Logging Page (operation #4) """
    def displayUserMenu():
        """ Display Main User Menu """
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

        """ Register New User """

        print('\n**************************\n'
              '******** REGISTER ********\n'
              '**************************')

        while True:
            new_email = input('\nEmail: ')
            for user in user_data:
                if new_email in user['email']:
                    print('\nEmail address already exists!\n')
                    return displayUserMenu()
            if new_email.__contains__('@'):
                break
            else:
                print('Enter a valid, existing mail!')

        while True:
            new_password = input('\nPassword (must have greater than 8!): ')
            if len(new_password) < 8:
                print('Uwyy! Password you entered is less than 8')
            else:
                break

        while True:
            new_name = input('\nName: ')
            if new_name.isalpha():
                break
            else:
                print('The Name must contain only letters!))')

        while True:
            new_surname = input('\nSurname: ')
            if new_surname.isalpha():
                break
            else:
                print('The Surname must contain only letters!')

        while True:
            new_age = input('\nAge: ')
            if new_age.isnumeric():
                break
            else:
                print('Age must contain only numbers!')

        while True:
            new_gender = input('\nGender (Male / Female): ')
            if new_gender == 'Male' or new_gender == 'Female' or new_gender == 'male' or new_gender == 'female':
                break
            else:
                print("Male or Female! There shouldn't be any other genders!!!")

        while True:
            new_phone_number = input('\nPhone number (+7 (XXX) XXX XX-XX): ')
            if len(new_phone_number) >= 10:
                break
            else:
                print("Enter your phone number instead of X!")
        user_created_data = datetime.datetime.now()
        print(
            '\n******************\nUser created: \n' + f'Email address: {new_email}' + "\n" + f'Password: {new_password}' + "\n" + f'Name: {new_name}' + "\n" + f'Surname: {new_surname}' + "\n" + f'Age: {new_age}' + "\n" + f'Gender: {new_gender}' + "\n" + f'Phone number: {new_phone_number}' + '\n\n' + f'User created data: {user_created_data}' + '\n' + '*******************')

        create_user = {
            'email': new_email,
            'password': new_password,
            'name': new_name,
            'surname': new_surname,
            'age': new_age,
            'gender': new_gender,
            'phone_number': new_phone_number,
            'user_created_data': user_created_data,
            'subscriptions': [],
            'friends': [],
            'blocked_users': []
        }
        user_data.append(create_user)
        return displayMenu()

    def oldUser():
        """ Login to account """
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
    """ Posting page (operations [#5, #7, #10, #11, #12]) """
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
            """ Display Main Post Menu """
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
            """ View All Posts / With the exclusion of posts of blocked users """
            global choose
            global post_data
            request_detail_post = 0
            test = False

            if len(post_data) == 0:
                print('\n********** Post data is empty! You can create a new post! **********\n')
                print('1 - Continue\n0 - Quit\n')
                choose = input('Enter your choice: ')
                if choose == '1':
                    return CreatePost()  # Returns a function that creates a new entry
                else:
                    return PostPage()  # Return a back page (Posting page)
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
                print('********** You can view post detail and view by sort **********\n')
                print('1 - View Post Detail\n2 - Post Sort List\n3 - View TOP posts\n0 - Quit\n')
                choose = input('Enter your choice: ')
                if choose == '1':
                    choose = int(input('\nChoose which post you want to see in detail: '))
                    for post in post_data:
                        for user in user_data:
                            if request_user == user['email'] and post['post_author'] not in user['blocked_users'] and choose == post['post_id']:
                                request_detail_post = post['post_id']
                                test = True
                    if test:
                        return DetailPost(request_detail_post)  # Returns a function that determines the details of the post
                    print('\n'
                          'We have declared a mistake somewhere!\n'
                          'Check it out again, please!'
                          '\n')
                    return PostPage()  # Return a back page (Posting page)
                elif choose == '2':
                    return PostListBySorting()  # Returns a function that defines posts with sorting
                elif choose == '3':
                    return ListTopPosts()  # Returns a list of TOP posts
                else:
                    return PostPage()  # Return a back page (Posting page)

        def ListTopPosts():
            global choose, post_data
            sorted_dict = {}

            try:
                choose = int(input("You can view top posts! TOP: "))
            except Exception as e:
                print(e)

            for post in post_data:
                sorted_dict[post['post_id']] = len(post['like'])

            sorted_dict = sorted(sorted_dict.items(), key=lambda x: x[1], reverse=True)
            sorted_dict = sorted_dict[:choose]

            for srtd_dict in sorted_dict:
                for post in post_data:
                    if srtd_dict[0] == post['post_id']:
                        print(f'\n'
                              f'Post id: {post["post_id"]}\n'
                              f'Post author: {post["post_author"]}\n'
                              f'Post title: {post["post_title"]}\n'
                              f'Post description: {post["post_description"]}\n'
                              f'Post created data: {post["post_created_date"]}\n'
                              f'Count of like: {len(post["like"])}\n'
                              f'Count of comment: {len(post["comment"])}'
                              f'\n')

            return displayPostMenu()

        def CreatePost():
            """ Create a new Post """
            global post_id
            global choose
            if request_user == '':  # If you entered the Create post page without logging into your account
                print('\nYou must sign in to account!\n'
                      '1 - Continue\n'
                      '0 - Quit\n')
                choose = input('Enter your choice: ')
                if choose == '1':
                    return LoginPage()  # Return a logging page
                elif choose == '0':
                    return PostPage()  # Return a back (Posting page)
            else:
                post_id += 1  # Each time we create a new post, +1 is added to the post ID
                post_title = input('Post title: \n')
                post_description = input('Post description: \n')
                post_created_data = datetime.datetime.now()
                post_author = request_user

                print('\nPost created:\nPost id: ' + str(
                    post_id) + '\nPost author: ' + post_author + '\nPost title: ' + post_title + '\nPost description: ' + post_description + '\nPost created date: ' + str(
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

                post_data.append(create_post)  # Added a new post to the list database

                return displayPostMenu()  # return a back (Display Main Post Menu)

        def DeletePost():
            """ Delete a post """
            global choose
            my_post = []  # Variable that has all my posts
            print('\n'
                  'You can only delete your posts.\n'
                  'Select the post you want to delete.'
                  '\n')

            for post in post_data:
                if post['post_author'] == request_user:
                    my_post.append(post)
                    print(
                        "\n" + f'Post id: {post["post_id"]}\n'
                               f'Post title: {post["post_title"]}\n'
                               f'Post description: {post["post_description"]}\n'
                               f'Post created date: {post["post_created_date"]}' + "\n"
                    )

            if len(my_post) == 0:  # If I haven't created any post yet
                print("\nYou don't have post.\nBut you can create a new post!\n"
                      "1 - Continue\n"
                      "0 - Quit\n")
                choose = input('Enter your choice: ')
                if choose == '1':
                    return CreatePost()  # Return Create a new post Page
                else:
                    return PostPage()  # Return a back (Posting page)
            try:
                choose = int(input('Select the post you want to delete by ID: \n'))  # Selects exactly by the ID of the post that the user wants to delete
                for post in post_data:
                    for my_p in my_post:
                        if choose == post['post_id'] and choose == my_p['post_id']:
                            post_data.remove(post)
                            print(f'\nYou deleted post: {post["post_id"]}\n')
                            return PostPage()  # Return a back (Posting page)
                else:
                    print('\n'
                          'We have declared a mistake somewhere!\n'
                          'Check it out again, please!'
                          '\n')
                    return PostPage()  # Return a back (Posting page)
            except Exception as e:
                print(e)
                return PostPage()  # Return a back (Posting page)

        def DetailPost(post_id_detail):
            """ Detail Post Page (Takes one parameter, which is then defined with (request post)) """
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
                  '1 - Add like for this post\n'  # To add a like
                  '2 - Remove like at this post\n'  # To remove a like
                  '3 - Add comment for this post\n'  # To add a comment to a post
                  '4 - Remove comment at this post\n'  # To delete a comment on a post
                  '5 - Subscribe the author of this post\n'  # To follow the author of this post
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
            """ Add like to post """
            for post in post_data:
                if [like for like in post['like'] if like['user_id'] == request_user] and post['post_id'] == request_post:
                    print('\n********** You can not add like for this post! **********\n')
                    return ViewListPost()  # If the user previously liked this post - Return a back (Posting page)
                elif post['post_id'] == request_post:
                    post['like'].append(
                        {
                            'user_id': request_user,
                            'post_id': request_post
                        }
                    )
            print('\nYou have successfully added a like for this post!\n')
            return ViewListPost()  # Return a back (View All Posts / With the exclusion of posts of blocked users)

        def RemoveLikePost():
            """ Remove like from post """
            for post in post_data:
                for like in post['like']:
                    if request_user == like['user_id'] and post['post_id'] == request_post:
                        post['like'].remove(like)
                        print('\nYou have successfully removed a like on this post!\n')
                        return DetailPost(request_post)  # After successfully deleting a like from a post Return a back (Detail Post Page)
                    elif post['post_id'] == request_post and request_user != like['user_id']:
                        print("\nYou haven't liked this post yet\n")
                        return DetailPost(request_post)  # After unsuccessfully deleting a like from a post Return a back (Detail Post Page)
                    else:
                        print("\nYou haven't liked this post yet\n")
            return DetailPost(request_post)  # Return a back (Detail Post Page)

        def AddCommentPost():
            """ Add Comment to the post """
            global comment_id
            comment_id += 1  # Each time we create a new comment on a post, +1 is added to the post ID.
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
            return ViewListPost()  # After successfully adding a comment to the post Return a back (View All Posts Page)

        def RemoveCommentPost():
            """ Delete a comment from post """
            global choose
            my_comment = []  # All my comments
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
                            return AddCommentPost()  # For create a first my comment to post
                        elif choose == '0':
                            return ViewListPost()  # Return a back (View All Posts Page)
                    elif comm['user_id'] == request_user:
                        my_comment.append(comm)
                        if post['post_id'] == request_post and comm['comment_post_id'] == request_post:
                            print(
                                "\n" + f'Comment id: {comm["comment_id"]}\n'
                                       f'Comment title: {comm["comment_title"]}\n'
                                       f'Comment description: {comm["comment_description"]}\n'
                                       f'Comment created date: {comm["comment_created_date"]}' + "\n")
            try:
                choose = int(input('Select the comment you want to delete by ID: '))
                for post in post_data:
                    for comm in post['comment']:
                        if choose == comm['comment_id'] and comm['comment_post_id'] == request_post and comm['user_id'] == request_user:
                            post['comment'].remove(comm)
                            my_comment.remove(comm)
                            print(f'\nYou deleted comment: {comm["comment_id"]}\n')
                            return ViewListPost()  # Return a back (View All Posts Page)
                print('\n'
                      'We have declared a mistake somewhere!\n'
                      'Check it out again, please!'
                      '\n')
                return DetailPost(request_post)  # Found an error somewhere Return a back (Detail Post Page)
            except Exception as e:
                print(e)
                return DetailPost(request_post)  # Found an error somewhere Return a back (Detail Post Page)

        def SubscribePostAuthor():
            """ Follow the author of the post """
            global choose
            for post in post_data:
                if post['post_id'] == request_post:
                    if post['post_author'] == request_user:  # If I am the author of the post, Return a back (Display Main Post Menu)
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
                                return DetailPost(request_post)  # If I have previously subscribed to this author, Return a back (Detail Post Page)
                            elif request_user == post['post_author']:
                                print("\n********** You can't subscribe to yourself! **********\n")
                                return DetailPost(request_post)  # If I am the author of the post, Return a back (Detail Post Page)
                            else:
                                user['subscriptions'].append(post['post_author'])
                                print('\n********** You have successfully subscribed! **********\n')
                                return DetailPost(request_post)  # If you successfully subscribed to the author of the post, Return a back(Detail Post Page)
            elif choose == '0':
                return DetailPost(request_post)  # Return a back (Detail Post Page)

    def PostListBySorting():
        """ View Posts with Sorted Post List """
        global choose, post_data, user_data
        postlist = []
        for post in post_data:
            for user in user_data:
                if user['email'] == request_user and post['post_author'] not in user['blocked_users']:
                    postlist.append(post)

        choose = input(
            '\n1 - With Bubble Sort\n'
            '2 - With Insertion Sort\n'
            '3 - With Quick Sort\n'
            '4 - With Merge Sort\n'
            '0 - Quit\n'
            '\nChoose: '
        )
        if choose == '1':
            postlist =  postBubbleSort(postlist)
        elif choose == '2':
            postlist = postInsertionSort(postlist)
        elif choose == '3':
            postlist = postQuickSort(postlist)
        elif choose == '4':
            postlist = postMergeSort(postlist)

        for post in postlist:
            print(f'\n'
                  f'Post id: {post["post_id"]}\n'
                  f'Post author: {post["post_author"]}\n'
                  f'Post title: {post["post_title"]}\n'
                  f'Post description: {post["post_description"]}\n'
                  f'Post created data: {post["post_created_date"]}\n'
                  f'Count of like: {len(post["like"])}\n'
                  f'Count of comment: {len(post["comment"])}'
                  f'\n')

    return displayPostMenu()  # Return a back (Display Main Post Menu)


def mySubscriptionsPage():
    """ My Subscriptions Page """
    def displayMySubscriptions():
        """ Display My Subscriptions Page """
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
                        print(f'User email: {subscription}')

        if test:
            print('\n********** Count of Common Friends **********\n')
            for user in user_data:
                for subscription in user['subscriptions']:
                    for common_friend in common_friends:
                        if request_user == user['email'] and common_friend['detail_user'] == subscription:
                            print(f'\nUser email: {subscription}\n'
                                  f'Count of common friends: {common_friend["count_of_friends"]}')

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
                            return DetailSubscription(subscription)  # Return a Detail Page more about subscription
                print('\n'
                      'We have declared a mistake somewhere!\n'
                      'Check it out again, please!'
                      '\n')
                return displayMySubscriptions()  # Return a back (Display Subscriptions Page)
            return displayMenu()  # Return a back (Display Main Menu)
        print("\n********** You haven't subscribed to anyone before! **********")
        return displayMenu()  # Return a back (Display Main Menu)

    def DetailSubscription(subscription_detail):
        """ Detail Subscription Page """
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
              "1 - Unsubscribe\n"  # To unsubscribe from a user
              "2 - Block user\n"  # To block a user
              "3 - View Post List\n"  # To View Post List
              "4 - View Common Friends\n"  # To View Common Friends
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
                return displayMenu()  # Return a back (Display Main Menu)
            elif choose == '3':
                return displayPostListUser(request_subscription)  # Return Display Post List Of This User Page
            elif choose == '4':
                return displayCommonFriends(request_subscription)  # Return Display Common Friends Of This User Page

        return displayMenu()  # Return a back (Display Main Menu)

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
        global request_subscription
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
        common_friends.append(
            {
                'detail_user': request_subscription,
                'count_of_friends': len(repeated)
            }
        )
        print(f'\nYou are subscribed to a user:')
        for repeat in repeated:
            print(f'\n{repeat}')

        return displayMenu()

    return displayMySubscriptions()


def displayMyBlockedUsers():
    """ Display My Blocked Users Page """
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
                        return DetailBlockedUser(blocked_user)  # Return a Detail a blocked user Page
            print('\n'
                  'We have declared a mistake somewhere!\n'
                  'Check it out again, please!'
                  '\n')
            return displayMyBlockedUsers()  # Return a back (Display My Blocked Users Page)
        return displayMenu()  # Return a back (Display Main Menu)
    print("\n********** You haven't blocked to anyone before! **********")
    return displayMenu()  # Return a back (Display Main Menu)


def DetailBlockedUser(blocked_user_detail):
    """ View Detail Blocked User """
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
    return displayMenu()  # Return a back (Display Main Menu)


def displayMyProfile():
    """ My Profile Page """
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
    return displayMenu()  # Return a back (Display Main Menu)


if __name__ == '__main__':
    displayMenu()
