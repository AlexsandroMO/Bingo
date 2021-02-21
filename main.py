#Created by:  Alexsandro Monteiro
#Date:        26/07/2019
#Site for Tests Python / Flask
#Fipe Table Consult

#Python any Where
#https://www.pythonanywhere.com/user/AlexsandroMO/
#pip install flask

from flask import Flask, render_template, redirect, url_for, request,send_from_directory
import pandas as pd
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
    canto = random.randint(1,99)
    test = df_cantada[df_cantada['CANTADOS'] == canto ]
    
    if len(df_cantada['CANTADOS'] <= 99):
      if len(test['CANTADOS']) == 0:
        print('--------- Tudo certo', canto)
        return canto

      else:
        print('Ops')
        status = True
        while status is True:
          canto = random.randint(1,99)
          print('>>>> while >>>>>: ', test['CANTADOS'])
          
          if len(test['CANTADOS']) == 0:
            print('--------- Tudo certo', canto)
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

  falta = 0
  df_cantada = pd.read_csv('static/excel/BINGO.csv')
  
  num = rad(df_cantada)
  print('>>> num >>>>', num)

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


@app.route('/clear_all')
def clear_all():
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

