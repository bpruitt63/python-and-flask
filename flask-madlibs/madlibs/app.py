from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    words = story.prompts
    return render_template('form.html', words = words)

@app.route('/story')
def show_story():
    stor = story.generate(request.args)
    return render_template('story.html', stor=stor)