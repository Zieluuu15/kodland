from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World</h1> <a href="/about">About Strona</a> <a href="/fakts">Fakty</a>'

@app.route("/szymon")
def szymon():
    return '<h1>hahahahahaha to ja</h1> <a href="/about">About Strona</a> <a href="/fakts">Fakty</a>'

@app.route("/about")
def about():
    return '<h1>About Page</h1> <a href="/">Home</a> <a href="/fakts">Fakty</a>'

@app.route('/fakts')
def fakty():
    liste = [
        "Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń."
        "Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów."
        "Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych."
    ]
    return f'<h1>{random.choice(liste)}</h1> <a href="/">Home</a> <a href="/about">About</a>'

app.run(debug=True)
