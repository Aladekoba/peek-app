# peek-app
Avoid crowded places by checking (taking a "peek") before heading out. I built both web/front end, chat bot, and API interfaces for Peek.

## How It Works
- I built peek on populartimes, Google Maps, and Google Places APIs.
- When a user logs on to the app, they are prompted for their destination. 
- A prediction of how crowded the location is expected to be at the time the prompt was entered is then displayed.
- The prediction is computed relative to the expected minimum and maximum number of people (This information is obtained using the populartimes API).

## Tools Used
- Populartimes API
- Flask, Flask-Restful
- Google Places API, Google Maps API
- Google Cloud App Engine
- Javascript/HTML/CSS
- jQuery

## What I learned
- Building an API with Flask and Flask-Restful
- Using jQuery for making HTTP requests.

## Try It Out
### Frontend
- Try it out here: http://safe-peek.ue.r.appspot.com/

### API
- http://safe-peek.ue.r.appspot.com/api

### Chat Bot
- http://m.me/104662897961170
