from skyprogramm import app


def test_api_posts_status_code():
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200


def test_api_posts_list():
    response = app.test_client().get('/api/posts/')
    assert type(response.json) == list


def test_api_posts_key():
    response = app.test_client().get('/api/posts/')
    assert list(response.json[0].keys()).sort() == ["poster_name", "poster_avatar", "pic", "content",
                                                    "views_count", "likes_count", "pk"].sort()


def test_api_posts_pk_dict():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict


def test_api_posts_pk_key():
    response = app.test_client().get('/api/posts/1')
    assert list(response.json.keys()).sort() == ["poster_name", "poster_avatar", "pic", "content",
                                                 "views_count", "likes_count", "pk"].sort()
