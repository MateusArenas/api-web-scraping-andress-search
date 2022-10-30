from flask import Flask

# base https://www.procep.com.br
# search https://www.procep.com.br//localizar//r-antonia-de-oliveira-n53-jardim-maria-eneida-maua-sp

from markupsafe import escape

from andress import search_andresses

app = Flask(__name__)

@app.route("/<search>")
def hello_world(search):
    return search_andresses(escape(search))