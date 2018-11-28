import datetime as dt
from statistics import median
from typing import Optional
import datetime

from api import get_friends
from api_models import User



def age_predict(user_id: int) -> Optional[float]:
    """ Наивный прогноз возраста по возрасту друзей

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: идентификатор пользователя
    :return: медианный возраст пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    
    friendsAges = []
    bdates = []

    data = get_friends(user_id, 'bdate')
    for i in data['response']['items']:
    	if i.get('bdate'):
    		bdates.append(i['bdate'])

    onlyYearBdates = []
    for i in bdates:
    	if len(i) in range(8,11):
    		onlyYearBdates.append(i)

    for elem in onlyYearBdates:
    	allo = list(map(int, elem.split('.')))
    	date = datetime.date(allo[2], allo[1], allo[0])
    	age = (datetime.date.today() - date) // 365
    	friendsAges.append(age.days)

    if friendsAges:
        friendsAges.sort()
        if len(friendsAges) % 2 == 1:
            return friendsAges[len(friendsAges) // 2]
        else:
            return int((friendsAges[len(friendsAges) // 2 - 1] + friendsAges[len(friendsAges) // 2]) / 2)
    else:
        return 0

