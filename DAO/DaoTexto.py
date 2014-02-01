# -*- coding: UTF-8 -*-
import sys #Importa Sys
sys.path.insert(0, '..') #Importante para setar estrutura de arquivos para encontrar Modulos
from MODEL.ModelTexto import ModelTexto
from DAO.Conexao import Conexao

class DaoTexto(object):
    def __init__(self):
        pass

    def insertTexto(self, objTexto):
        conn = Conexao()
        db = conn.recebeConexao()
        cursor = db.cursor()
        cursor.execute("INSERT INTO Texto VALUES (%s,%s,%s,%s)",
                       (objTexto.IdTexto, objTexto.Texto, objTexto.IdTipoTexto, objTexto.IdUrl))
        db.commit()
        db.close()




