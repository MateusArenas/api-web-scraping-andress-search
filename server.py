from flask import Flask, render_template

# base https://www.procep.com.br
# search https://www.procep.com.br//localizar//r-antonia-de-oliveira-n53-jardim-maria-eneida-maua-sp

from markupsafe import escape

from andress import search_andresses

app = Flask(__name__,  template_folder='pages')

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/<search>")
def search(search):
    return search_andresses(escape(search))
