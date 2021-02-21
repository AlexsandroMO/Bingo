
#Created by:  Alexsandro Monteiro
#Date:        21/02/2021
#Site for Tests Python / Flask
#Canto Bingo
#Python any Where
#https://repl.it/@AlexsandroMO/BingoSing#main.py
#SITE: https://bingosing.alexsandromo.repl.co/

from flask import Flask, render_template, redirect, url_for, request,send_from_directory
import pandas as pd
import numpy as np
import random
import Progpy as prog
import openpyxl
import xlrd

#==================================
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_us():
  return render_template('home.html')


@app.route('/index')
def index():

  def rad(df_cantada):
    status = False
    #canto = random.randint(1,99)
    lista = []
    Lista = pd.read_csv('static/excel/Lista.csv')

    for i in Lista['LIS']:
      lista.append(i)

    if len(df_cantada['CANTADOS'] <= 99):
      canto = random.choice(lista)
      test = df_cantada[df_cantada['CANTADOS'] == canto ]
      if len(test['CANTADOS']) == 0:
        prog.actualy_list(canto)
        return canto

      else:
        status = True
        while status is True:
          #canto = random.randint(1,99)
          canto = random.choice(lista)
          
          if len(test['CANTADOS']) == 0:
            status = False
            prog.actualy_list(canto)
            return canto

          else:
            status = True
          
          status = False

    else:
      return '-'

  #-----------------------------------
  df_cantada = pd.read_csv('static/excel/BINGO.csv')
  num = rad(df_cantada)

  if num != None:
    falta = 0

    if num == '-':
      falta = 'Acabou!'
      var_list = prog.singed()
      var_list = var_list['CANTADOS']
      return render_template('index.html',var_list=var_list, num=num, falta=falta)

    else:
      falta = 99 - len(df_cantada['CANTADOS'])
      var_list = prog.list_bingo(num)
      var_list = sorted(var_list)

      if len(df_cantada['CANTADOS']) == 100:
        falta = 'Acabou!'
        return render_template('index.html',var_list=var_list, num=num, falta=falta)
      else:
       return render_template('index.html',var_list=var_list, num=num, falta=falta)

  else:
    falta = 99 - len(df_cantada['CANTADOS'])
    var_list = sorted(df_cantada['CANTADOS'])

    if len(df_cantada['CANTADOS']) == 100:
      falta = 'Acabou!'
      return render_template('index.html',var_list=var_list, num=num, falta=falta)
    else:
      return render_template('index.html',var_list=var_list, num=num, falta=falta)


'''  def rad(df_cantada):

    status = False
    lista = []
    #canto = random.randint(1,99)
    for i in df_cantada['CANTADOS']:
      lista.append(i)

    canto = random.choice(lista)

    test = df_cantada[df_cantada['CANTADOS'] == canto ]
    
    if len(df_cantada['CANTADOS'] <= 99):
      if len(test['CANTADOS']) == 0:
        return canto

      else:
        status = True
        while status is True:
          canto = random.randint(1,99)
          
          if len(test['CANTADOS']) == 0:
            status = False
            return canto

          else:
            status = True
          
          status = False

    else:
      return '-'

#-----------------------------------

      #return canto
    #else:
      #canto = '-'
      #return canto
  df_cantada = pd.read_csv('static/excel/BINGO.csv')
  num = rad(df_cantada)
  
  if num != None:

    falta = 0

    if num == '-':
      falta = 'Acabou!'
      var_list = prog.singed()
      var_list = var_list['CANTADOS']

    else:
      falta = 99 - len(df_cantada['CANTADOS'])
      var_list = prog.list_bingo(num)
      var_list = sorted(var_list)
      print('>>> else >>>>', num)

    return render_template('index.html',var_list=var_list, num=num, falta=falta)
  
  else:
    
    falta = 99 - len(df_cantada['CANTADOS'])
    var_list = sorted(df_cantada['CANTADOS'])
    print('>>> else >>>>', num)

    return render_template('index.html',var_list=var_list, num=num, falta=falta)
'''

@app.route('/clear_all')
def clear_all():
  prog.clear_List()
  prog.clear_df()
  return redirect("/")
  

@app.route('/singed')
def singed():
  df_cantada = prog.singed()
  
  var_list = df_cantada['CANTADOS']
  var_list = sorted(var_list)
  
  total = len(var_list)

  return render_template('tabela-cantada.html', var_list=var_list, total=total)


if __name__ == '__main__':
  #app.run(host='0.0.0.0', port=8080, debug=True)
  app.run(host='127.0.0.1', port=5000, debug=True)

