import requests
from bs4 import BeautifulSoup
import re
from slugify import slugify
from unidecode import unidecode 

def set_andresses(html, andresses):
  for andress in html.select('a.col-table') :
    lougadoro = andress.select_one('h3')
    [bairro, cidade, cep] = andress.select('p')
    lougadoro = lougadoro.text.strip()
    bairro = bairro.text.strip()
    cidade = cidade.text.strip()
    uf = cidade.split(' - ')[1]
    cidade = cidade.split(' - ')[0]
    cep = cep.text.strip()
    andresses.append({ 
      "lougadoro": lougadoro, 
      "bairro": bairro, 
      "cidade": cidade, 
      "uf": uf, 
      "cidade": cidade, 
      "cep": cep 
    })

def haveInList (list, key, value):
  for item in list :
    if item[key] == value:
      return True
  return False

def set_relatives(andresses, key, relatives, search):
  for andress in andresses :
    if re.search(unidecode(andress[key]), unidecode(search), re.IGNORECASE):
      if not haveInList(relatives, 'cep', andress['cep']):
        relatives.append(andress)

def search_andresses (search):
  slug = slugify(search)
  url = 'https://www.procep.com.br//localizar//'+slug
  reponse = requests.get(url)

  html = BeautifulSoup(reponse.text, 'html.parser')

  andresses = []
  set_andresses(html, andresses)

  relatives = []
  set_relatives(andresses, 'cep', relatives, search)
  set_relatives(andresses, 'lougadoro', relatives, search)
  set_relatives(andresses, 'bairro', relatives, search)
  set_relatives(andresses, 'cidade', relatives, search)
  set_relatives(andresses, 'uf', relatives, search)

  return relatives
