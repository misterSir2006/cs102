import requests
import time

access_token = 'e25b4ead79df072bb7c0239adc60182d1a2c17c1a7848d7bdbace7d09584980ded089ca51bf6a3bd8c421'
user_id = '218902184'
url = 'https://api.vk.com/method'

def get(params={}, timeout=5, max_retries=5, backoff_factor=0.3) -> dict:
    """ Выполнить GET-запрос

    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    
    params = {
    'url': url,
    'access_token': access_token,
    'user_id': user_id,
    }

    query = "{url}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.87".format(**params)
    response = requests.get(query)
    return response

def get_friends(user_id: int, fields = '') -> dict:
    """ Вернуть данных о друзьях пользователя

    :param user_id: идентификатор пользователя, список друзей которого нужно получить
    :param fields: список полей, которые нужно получить для каждого пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"

    query_params = {
    'url': url,
    'access_token': access_token,
    'user_id': user_id,
    'fields': fields
    }

    query = "{url}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.87".format(**query_params)
    response = requests.get(query)
    return response.json()

def messages_get_history(user_id: int, offset=0, count=20) -> dict:
    """ Получить историю переписки с указанным пользователем

    :param user_id: идентификатор пользователя, с которым нужно получить историю переписки
    :param offset: смещение в истории переписки
    :param count: число сообщений, которое нужно получить
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "user_id must be positive integer"
    assert count >= 0, "user_id must be positive integer"
    max_count = 200

    query_params = {
    'url': url,
    'access_token': access_token,
    'v': '5.87',
    'user_id': user_id,
    'offset': offset,
    'count': min(count, max_count)
    }

    query = "{url}/messages.getHistory?access_token={access_token}&user_id={user_id}&offset={offset}&count={count}&v={v}".format(**query_params)
    response = requests.get(query)
    count = response.json()['response']['count']
    messages = []
    
    while count > 0:
        query2 = "{url}/messages.getHistory?access_token={access_token}&user_id={user_id}&offset={offset}&count={count}&v={v}".format(**query_params)
        response2 = requests.get(query2)
        data2 = response2.json()
        messages.extend(data2['response']['items'])
        count -= min(count, max_count)
        query_params['offset'] += 200
        query_params['count'] = min(count, max_count)

    return messages