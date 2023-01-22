from application import app

@app.route("/")
def index():
    return "What is your problem dude?"