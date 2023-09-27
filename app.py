from flask import Flask, render_template
from housing.logger import logging as log
from housing.exception import HousingException
import sys

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        log.info("We are testing logger package")
        raise Exception("We are testing custom exception")
    except Exception as e:
        log.info("Error has occured at the index function of app.py")
        housing = HousingException(e, sys)
        log.info(housing.error_message)



if __name__ == "__main__":
    app.run(debug=True)