from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return 'ok'

@app.route("/routes")
def routes():
    route_path = './data/rk_berlin_routes/'
    routes = [json.load(open(os.path.join(route_path, filename))) for filename in os.listdir(route_path)]
    routes = [dict(id=i+1,
                   points=map(lambda x: dict(lat=x['latitude'], lon=x['longitude']), route)) 
              for i, route in enumerate(routes)]
    return jsonify(results=routes)

if __name__ == '__main__':
    app.run(debug=True)