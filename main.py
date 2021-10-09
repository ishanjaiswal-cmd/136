from os import name
from flask import Flask, app,jsonify,request
from data import data

app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"success"
    }),200
@app.route("/planet")
def planet():
    name=request.args.get("name")
    planet_data=next(item for item in data if item["name"]==name)
    return jsonify({
        "data":planet_data,
        "message":"success"
    }),200
if __name__=="_main_":
    app.run()
