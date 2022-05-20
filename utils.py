import json


def get_posts_all():
    """
    функция прочтения файла 'data.json'
    return: список постов
    """
    with open("data/data.json", "r", encoding="utf-8") as f:
        posts_list = json.load(f)
    return posts_list


def get_comments_all():
    """
    функция прочтения файла 'comments.json'
    return: список комментариев
    """
    with open("data/comments.json", "r", encoding="utf-8") as f:
        comments_list = json.load(f)
    return comments_list


def get_posts_by_user(user_name):
    """
    функция получения всех постов определенного пользователя
    return: список постов пользователя
    """
    user_name_posts = []
    for post in get_posts_all():
        if user_name == post["poster_name"]:
            user_name_posts.append(post)
    # вызов ошибки в случае отсутствия пользователя
    if not user_name_posts:
        print("Пользователь не найден")
        raise ValueError()
    return user_name_posts


def get_comments_by_post_id(post_id):
    """
    функция получения комментариев к определенному посту
    return: список комментариев к посту
    """
    post_comments = []
    for comment in get_comments_all():
        if post_id == comment["post_id"]:
            post_comments.append(comment)
    return post_comments


def search_for_posts(query):
    """
    функция получения списка постов по вхождению ключевого слова в текст поста
    return: список постов по ключевому слову
    """
    posts_list_by_query = []
    for post in get_posts_all():
        if query.lower() in post["content"].lower():
            posts_list_by_query.append(post)
    return posts_list_by_query[:10]


def get_post_by_pk(pk):
    """
    функция возврата поста по идентификатору
    return: пост
    """
    for post in get_posts_all():
        if pk == post["pk"]:
            return post
    raise ValueError()
