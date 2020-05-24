from populartimes import get_id
from math import floor
from flask import Flask, render_template, jsonify, request
from datetime import datetime
from pytz import timezone
from calendar import weekday


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/postmethod', methods=['GET', 'POST'])
def post_javascript_data():
    if request.method != 'POST':
        print(f"request method is {request.method}")
        return jsonify({'prediction': 'not'})

    now = datetime.now(timezone('America/Chicago'))
    year = now.year
    month = now.month
    day_now = now.day
    now = now.hour

    today = weekday(year, month, day_now)
    days_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    today = days_map[today]

    place = request.form['place_data']
    resp = get_id('AIzaSyBxHF3IVYVssiQLUn_1VKCxritKrneCfj8', place)
    times = []
    if not 'populartimes' in resp:
        return jsonify({'prediction': 'probably not'})

    for day in resp['populartimes']:
        if day['name'] == today:
            times = day['data']
            break

    cur_people = times[now]
    times = [time for time in times if time > 0]

    max_people = max(times)
    min_people = min(times)
    high_threshold = floor(max_people * 0.7 + min_people * 0.3)
    low_threshold = floor(max_people * 0.3 + min_people * 0.7)

    prediction = "highly"

    if cur_people < low_threshold:
        prediction = "not"
    elif cur_people < high_threshold:
        prediction = "slightly"

    params = {'prediction': prediction}
    return jsonify(params)




