from app import app

@app.route("/index")
@app.route("/index")
def index():
    return "Hello Krystian Zdziebko"

@app.route("/name/", defaults={"name" :None})
@app.route("/name/<name>")
def name(name):
    return f"Hello {name}"