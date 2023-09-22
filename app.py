from flask import Flask, render_template


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello Machine Learners"



if __name__ == "__main__":
    app.run(debug=True)