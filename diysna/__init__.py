import os
from flask import Flask, render_template, flash, request
from wtforms import Form
from bokeh.embed import components

# https://stackoverflow.com/questions/24302754/python-submodule-imports-using-init-py
from diysna import renders_bokeh
from diysna import renders_dash
from diysna.tweet import Tweet
from diysna.form import Form


app = Flask(__name__)

# env config
# FLASK_ENV default is 'production'
if os.getenv('FLASK_ENV') == 'development':
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.ProductionConfig')


# nodes = []
# edges = [(887504298493562881, 454071012), (312264011, 1080427519126528005), (2956611591, 999453985)]


@app.route('/', methods=['GET', 'POST'])
def index():
    protocol = os.getenv('PROTOCOL')
    form = Form(request.form)
    script = ""
    div = ""
    if request.method == 'POST':
        keyword = request.form['keyword']
        num_tweets = request.form['num_tweets']
        since = request.form['since']
        until = request.form['until']

        tweet = Tweet(app)
        list_of_tweets = tweet.get_list_of_tweets(
            keyword, since, until, num_tweets)
        nodes = tweet.get_nodes(list_of_tweets)
        edges = tweet.get_edges(list_of_tweets)

        # plot = renders_bokeh.render_custom_graph(nodes, edges)
        plot = renders_bokeh.render_from_fb_combined()
        script, div = components(plot)

    return render_template("index.html", form=form, script=script, div=div, protocol=protocol)


if __name__ == '__main__':
    app.run()
