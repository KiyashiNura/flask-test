from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route('/')
def about():
    return """
<html>
    <body>
        Это главная страница. 
        <br><a href="/me" title="Перейти">Мой любимый герой</a>
        <br><a href="/weather" title="Перейти">"Прогноз" погоды</a>
    </body>
</html>
"""


@app.route('/me')
def me():
    return render_template('hero.html')


weath = [
    {"description": "солнечно", "image": "http://www.asfera.info/files/conf_chief/86e225aae4319ecd2bd81360ead98c97.jpg" },
    {"description": "дождь","image": "https://images.unian.net/photos/2017_06/1498807243-9202.jpeg"},
    {"description": "сухо","image": "https://otvet.imgsmail.ru/download/973193fa7c49129fc054733325f772ba_h-43298.jpg"},
    {"description": "ветер","image": "https://avdet.org/wp-content/uploads/2017/07/veter.jpg"}
]


@app.route('/weather')
def weather():
    w = random.choice(weath)
    return render_template('weather.html', weather=w)


app.run(debug=True, port=8080)
