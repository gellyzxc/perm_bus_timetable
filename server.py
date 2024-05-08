import json
from flask import Flask
from main import getInfo

app = Flask(__name__)


@app.route('/timetable/<stop_id>/')
def generate_password(stop_id):
    data = getInfo(stop_id=stop_id)
    
    response = app.response_class(
        response=json.dumps({
            "version": '1.0 public beta',
            "dev": "gellyzxc https://gekksume.t.me/",
            "data": data
        }),
        status=200,
        mimetype='application/json'

    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)