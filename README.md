# Bravo Group's Social Network Analysis

based on

- [python3](https://www.python.org/) & [Flask Framework](http://flask.pocoo.org/docs/1.0/)
- [GraphQL](https://graphql.org/) as public API language. 
- market prooft [React](https://reactjs.org/) ecosystem ([babel](https://babeljs.io/), [webpack](https://webpack.js.org/))
- deployable in [Heroku](http://heroku.com) out of the box
- Client network graph lib (WIP!)

dependencies:

- [python3](https://www.python.org/) - currently v3.7.2
- [pipenv](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv)
- [yarn](https://yarnpkg.com)
- [nodejs](https://nodejs.org) - currently v11.6.0
  
run locally:

- Be sure you installed all deps and clone app
- Add a `settings.cfg` file for env variables under `diysna` folder.
- activate pip virualenv  `"$ pipenv shell"`
- install dependencies `"$ pipenv install && yarn"`
- run `"$ yarn serve"` to run server locally under `http://localhost:5000`
  - (*) if you use Visual Code there is a default FLASK configuration to run it in debug mode just have to set `FLASK_ENV` to `development` in `env` key

>> for watching assset changes run `"$ yarn watch"` in another window

deploy app in Heroku

- run `"$ yarn build"`
- commit all to github repo
- run deploy from heroku from selected branch (usually master)

## .env example should contains these keys

- TWITTER_CONSUMER_KEY='twitter-consumer-key'
- TWITTER_CONSUMER_SECRET='twitter-consumer-key-secret'
- TWITTER_ACCESS_TOKEN_KEY='twitter-access-token-key'
- TWITTER_ACCESS_TOKEN_SECRET='twitter-access-token-key'
- SECRET_KEY='auto-gerenrated-secret-key-whatever-you-like'
