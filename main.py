from flask import Flask, render_template, request
from app.read_data import data_to_engine
# %% 

# entry point
app = Flask(__name__)

# %% 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/response", methods=["POST"])
def response():
    engine = data_to_engine()
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = engine.query(prompt)
        return render_template("response.html", prompt=prompt, response=response)

# %% 

if __name__ == "__main__":
    context = ('local.crt', 'local.key')
    app.run(debug=True)

