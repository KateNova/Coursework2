import pytest

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, get_posts_by_user, get_comments_all, \
                    search_for_posts


def test_get_post_all_list():
    assert type(get_posts_all()) == list


def test_get_comments_all_list():
    assert type(get_comments_all()) == list


def test_get_post_by_user_list():
    assert type(get_posts_by_user("leo")) == list


def test_get_post_by_user_value():
    with pytest.raises(ValueError):
        get_posts_by_user("kate")


def test_get_comments_by_post_id_list():
    assert type(get_comments_by_post_id(2)) == list


def test_get_comments_by_post_id_value():
    with pytest.raises(ValueError):
        get_comments_by_post_id(0)


def test_search_for_post():
    with pytest.raises(AttributeError):
        search_for_posts(5)


def test_get_post_by_pk():
    with pytest.raises(ValueError):
        get_post_by_pk(9)
