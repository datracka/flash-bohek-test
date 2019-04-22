import datetime
from wtforms import Form, TextField
from wtforms.fields.html5 import DateField


class Form(Form):
    keyword = TextField('Keyword', [], [], '', 'keyword', 'trump')
    num_tweets = TextField('Number of Tweets', [], [], '', 'num-tweets', '100')
    since = DateField('Since', format='%Y-%m-%d',
                      default=datetime.date.today() - datetime.timedelta(days=3))
    until = DateField('Until', format='%Y-%m-%d',
                      default=datetime.date.today())
