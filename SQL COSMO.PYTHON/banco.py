import sqlite3
from sqlite3 import Error 

def ConexaoBanco():
caminho="D:\\python\\exercicio\\banco\\agenda.db"
con=None
try:
con=sqlite3.connect(caminho)
except Error as ex: return con
print(ex)
return con


vcon=ConexaoBanco()

########## Criar tabela
vsql="""CREATE TABLE tb_contatos(
N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENTE,
T_NOMECONTATO VARCHAR (30)
T_PEDIDO VARCHAR (14)
T_ TAREFA VARCHAR (14)
T_LISTATELEFONICA (30)
);'''
def criarTabela():
try:
c=conexao.cursor()
c.execute(sql)
print(ex)

criarTabela(vcon,vsql)

vcon.close()






















