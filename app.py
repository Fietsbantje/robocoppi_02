from flask import Flask, render_template, request, jsonify
from flask_cors import CORS #delete this line if not using the standalone front end option
from chat import get_response

app = Flask(__name__)
CORS(app) # delete this line if not using the standalone front end option

# define two routes. One route to return the base html and one route to do the prediction.
# use this line when not using the standalone front end option: @app.get("/")
# use this line when not using the standalone front end option: def index_get():
# use this line when not using the standalone front end option: return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)