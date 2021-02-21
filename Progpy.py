import pandas as pd
import openpyxl
import xlrd




def clear_df():
  obj = [[0]]
  col = [['CANTADOS']]
  df = pd.DataFrame(data=obj, columns=col,index=[0])
  df.to_csv('static/excel/BINGO.csv',index=False)

  return df


def list_bingo(num):

  df = pd.read_csv('static/excel/BINGO.csv')

  dados = [
            [num]
          ]
  col = ['CANTADOS']
  df2 = pd.DataFrame(data=dados, columns=col, index=[len(df)])

  new = df.append(pd.concat([df2]))
  new.to_csv('static/excel/BINGO.csv' ,index=False)

  return new['CANTADOS']


def singed():
  df = pd.read_csv('static/excel/BINGO.csv')

  return df







'''
def clear_df():

  obj = {'CANTADOS': [0]}
  df = pd.DataFrame(data=obj)
  #df = pd.DataFrame(columns=[obj])
  df.to_excel('static/excel/CANTADOS.xlsx')


def list_bingo(num):

  df = pd.read_excel('static/excel/CANTADOS.xlsx')
  print('>>>>>>>>--------:', num, 'len sem: ', len(df['CANTADOS']))

  df.loc[len(df['CANTADOS'])]=[num]
  df.to_excel('static/excel/CANTADOS.xlsx')

  #obj = {'CANTADOS': [num]}
  #df2 = pd.DataFrame(data=obj, index=[len(df)])

  #new = df.append(pd.concat([df2]))
  #new = new.drop_duplicates()
  #new= new.drop('Unnamed: 0', axis=1)
  #print('----: ', new)
  #new.to_excel('static/excel/CANTADOS.xlsx')

  return df['CANTADOS']


def singed():
  df = pd.read_excel('static/excel/CANTADOS.xlsx')

  return df

  '''
