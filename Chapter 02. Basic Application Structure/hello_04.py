from flask import request, Flask
app = Flask(__name__)

@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    return """
        <p>Your browser is {}</p>
    """.format(user_agent)