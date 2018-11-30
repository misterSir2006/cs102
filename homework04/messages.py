from collections import Counter
import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from typing import List, Tuple

from api import messages_get_history
from api_models import Message
import config


Dates = List[datetime.date]
Frequencies = List[int]
user_id = int(input('Введите id пользователя - '))

plotly.tools.set_credentials_file(
    username=config.PLOTLY_CONFIG['username'],
    api_key=config.PLOTLY_CONFIG['api_key']
)


def fromtimestamp(ts: int) -> datetime.date:
    return datetime.datetime.fromtimestamp(ts).date()


def count_dates_from_messages(messages: dict) -> list:
    """ Получить список дат и их частот

    :param messages: список сообщений
    """
    dates = []
    for message in messages:
        dates.append(message['date'])
    for i in range(len(dates)):
        dates[i] = datetime.datetime.fromtimestamp(dates[i]).strftime("%Y-%m-%d")
    if dates:
        return dates



def plotly_messages_freq(dates: list) -> None:
    """ Построение графика с помощью Plot.ly

    :param date: список дат
    :param freq: число сообщений в соответствующую дату
    """
    s = Counter(dates)
    xCoor = list(s.keys())
    yCoor = list(s.values())
    stats = [go.Scatter(x=xCoor, y=yCoor)]
    py.iplot(stats)

if __name__ == '__main__':
    s = count_dates_from_messages(messages_get_history(user_id))
    plotly_messages_freq(s)
