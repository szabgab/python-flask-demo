from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')



@app.route("/", methods=['POST'])
def main_post():
    text = request.form['text']
    return render_template('main.html', msg = text)

