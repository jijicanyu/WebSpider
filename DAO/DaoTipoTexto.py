# -*- coding: UTF-8 -*-

import sys #Importa Sys
sys.path.insert(0, '..') #Importante para setar estrutura de arquivos para encontrar Modulos
from DAO.Conexao import Conexao
from MODEL.ModelTipoTexto import ModelTipoTexto

class DaoTipoTexto(object):
    def __init__(self):
        self.listaTipoTexto = []

    def PesquisaTodos(self):
        try:
            con = Conexao()
            db = con.recebeConexao()
            cursor = db.cursor()
            cursor.execute("Select * from tipoTexto")
            resultados = cursor.fetchall()
            if resultados:
                for row in resultados:
                    tipoTexto = ModelTipoTexto()
                    tipoTexto.IdTipoTexto = str(row[0])
                    tipoTexto.Descricao = str(row[1])
                    if (str(row[2]) == "1"):
                        tipoTexto.SeLingProgramacao = True
                    else:
                        tipoTexto.SeLingProgramacao = False
                    self.listaTipoTexto.append(tipoTexto)
            else:
                self.listaTipoTexto = None
            db.close()
            return self.listaTipoTexto
        except Exception, ex:
            db.close()
            self.listaTipoTexto = None
            print "ERRO: {0}".format(ex.message)
            return self.listaTipoTexto


#def main():
#    d = DaoTipoTexto()
#    d.PesquisaTodos()
#
#
#
#if __name__=="__main__":
#    main()
