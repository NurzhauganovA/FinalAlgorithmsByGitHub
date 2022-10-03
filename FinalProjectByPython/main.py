import sqlite3


def main(path):

    conn = ''

    try:
        conn = sqlite3.connect(path)
    except sqlite3.Error as error:
        print(error)

    cur = conn.cursor()
    post_data = cur.execute("SELECT * FROM post")
    post_data = post_data.fetchall()

    user_data = cur.execute("SELECT * FROM user")
    user_data = user_data.fetchall()

    category_data = cur.execute("SELECT * FROM category_post")
    category_data = category_data.fetchall()

    user_id, user_username = '', ''

    post_id, post_title, post_description, post_author, post_category = '', '', '', '', ''

    category_id, category_title = '', ''

    for data in post_data:
        for user in user_data:
            for category in category_data:
                post_id = data[0]
                post_title = data[2]
                post_description = data[3]
                post_author = data[5]
                post_category = data[6]

                user_id = user[0]
                user_username = user[4]

                category_id = category[0]
                category_title = category[2]

                if post_author == user_id and post_category == category_id:
                    print(f'\nPost id : {post_id}\nPost title : {post_title}\nPost description : {post_description}\nPost_author: {user_username}\nPost_category: {category_title}\n')


if __name__ == '__main__':
    main("C:\Python projects\FinalAlgorithm\FinalProjectAlgorithm\db.sqlite3")
