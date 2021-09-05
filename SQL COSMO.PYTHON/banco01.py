import sqlite3
from sqlite3 import Error 

###########Criar Conexão
def ConexaoBanco():
caminho="D:\\python\\exercicio\\banco\\agenda.db"
con=None
   try:
    con=sqlite3.connect(caminho)
   except Error as ex: return con
    print(ex)
   return con
vcon=ConexaoBanco()

vsql="""INSERT INTO tb_contatos
   (T_NOMECONTATO,T_PEDIDO,T_TAREFA)
VALUES('ANA_TELEFONE','ANA_PEDIDO',ANA_TAREFA')"""
def inserir(conexao,sql):
    try
      c=conexao.cursor()
      c.execute(sql)
      conexao.commit()
      print ("registro inserido")
    except Error as ex:
      print(ex)

inserir(vcon,vsql)
