# exemple_31
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

# exemple_2
# $ python hello.py
#  * Running on http://127.0.0.1:5000/

# exemple_3
{% if user.is_authenticated %}
    Ви увійшли в систему як {{ user.username }}.
{% else %}
    Будь ласка, увійдіть в систему.
{% endif %}

# exemple_4
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>

# exemple_5
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Секретний ключ для захисту сесії

@app.route('/')
def index():
    session['username'] = 'John'
    return 'Сесія створена'

@app.route('/get')
def get():
    username = session.get('username')
    return 'Логін користувача: ' + username

if __name__ == '__main__':
    app.run()

# exemple_6
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Визначення класу форми
class MyForm(FlaskForm):
    name = StringField('Ім\'я')
    submit = SubmitField('Відправити')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        return f'Привіт, {name}!'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()

# exemple_7
from bottle import Bottle, run

app = Bottle()

@app.route('/')
def index():
    return "Привіт зі світу Bottle!"

if __name__ == '__main__':
    run(app, host='localhost', port=8080)
