from flask import Blueprint, render_template, request
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, \
                    get_posts_by_user

main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')


# добавление роута для вью главной страницы
@main_blueprint.route("/")
def page_index():
    """
    return: отрисованный шаблон index.html
    """
    return render_template("index.html", posts=get_posts_all())


# добавление роута для вью одного поста
@main_blueprint.route("/posts/<int:pk>")
def page_post(pk):
    """
    return: отрисованный шаблон post.html
    """
    comments = get_comments_by_post_id(post_id=pk)
    return render_template("post.html", post=get_post_by_pk(pk=pk),
                           comments_count=len(comments), comments=comments)


# добавление роута для поиска постов
@main_blueprint.route("/search/")
def page_search():
    """
    return: отрисованный шаблон search.html
    """
    if request.args.get("s", None):
        posts = search_for_posts(request.args["s"])
        return render_template("search.html", posts=posts, posts_count=len(posts))
    else:
        return render_template("search.html", posts=[], posts_count=0)


# добавление роута для показа ленты постов отдельного юзера
@main_blueprint.route("/users/<user_name>")
def user_posts(user_name):
    """
    return: отрисованный шаблон user-feed.html
    """
    user_feed = get_posts_by_user(user_name)
    return render_template("user-feed.html", posts=user_feed)
