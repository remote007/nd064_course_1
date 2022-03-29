from urllib import response
from flask import Flask
import json
import logging

app = Flask(__name__)

@app.route("/status")
def healthcheck():
    response = app.response_class(
        response = json.dumps({"result":"OK-Healthy"}),
        status = 200,
        mimetype = 'application/json'
    )
    app.logger.info("status checked successfully")
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response = json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status = 200,
        mimetype = 'application/json'
    )
    app.logger.info("metric request succesful")
    return response

@app.route("/")
def hello():
    return "Hello World!"
    app.logger.info("main request successful")

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
