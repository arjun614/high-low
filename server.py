from flask import Flask, render_template_string
import random

app = Flask(__name__)


random_number = random.randint(0, 9)
print(f"Random number to guess: {random_number}")


home_html = """
    <h1 style="text-align: center">Guess a number between 0 and 9</h1>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style="display: block; margin: auto;"/>
"""

@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple; text-align: center'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' style='display: block; margin: auto;'/>"
    elif guess < random_number:
        return "<h1 style='color: red; text-align: center'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' style='display: block; margin: auto;'/>"
    else:
        return "<h1 style='color: green; text-align: center'>Congratulations! You guessed correctly!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' style='display: block; margin: auto;'/>"

if __name__ == "__main__":
    app.run(debug=True)
