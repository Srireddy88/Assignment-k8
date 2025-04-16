from flask import Flask, request, render_template_string
import os
import requests

app = Flask(__name__)

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000")

template = '''
<form method="POST">
  <input name="name" placeholder="Enter your name">
  <button type="submit">Submit</button>
</form>
{% if result %}
<p>{{ result }}</p>
{% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        name = request.form["name"]
        res = requests.post(f"{BACKEND_URL}/api", json={"name": name})
        result = res.json()["message"]
    return render_template_string(template, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
