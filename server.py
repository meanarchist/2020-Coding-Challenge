from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

scoreboard = [
    {
    "id": 1,
    "name": "Boston Bruins",
    "score": 7
    },

    {
    "id": 2,
    "name": "Tampa Bay Lightning", 
    "score": 5
    },

    {
    "id": 3,
    "name": "Toronto Maple Leafs", 
    "score": 2
    },

    {
    "id": 4,
    "name": "Florida Panthers", 
    "score": 1
    },

    {
    "id": 5,
    "name": "Buffalo Sabres", 
    "score": 1
    },
]


def sort_scoreboard():
    global scoreboard
    scoreboard.sort(key=lambda x: x["score"], reverse=True)

@app.route('/')
def show_scoreboard():
    return render_template('scoreboard.html', scoreboard=scoreboard)


@app.route('/increase_score', methods=['POST'])
def increase_score():
    global scoreboard

    data = request.get_json()
    team_id = data["id"]

    for team in scoreboard:
        if team["id"] == team_id:
            team["score"] += 1

    # Sort the scoreboard based on scores in non-increasing order
    sorted_scoreboard = sorted(scoreboard, key=lambda x: x["score"], reverse=True)
    
    sort_scoreboard()
    return jsonify(sorted_scoreboard)


if __name__ == '__main__':
    app.run(debug=True)