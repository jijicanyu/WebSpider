# -*- coding: UTF-8 -*-

import sys #Importa Sys
sys.path.insert(0, '..') #Importante para setar estrutura de arquivos para encontrar Modulos
from MODEL.ModelUrl import ModelUrl
from DAO.Conexao import Conexao
import time
from uuid import *

class DaoUrl(object):
    def __init__(self):
        pass

    def insertUrl(self, objectUrl):
        conn = Conexao()
        db = conn.recebeConexao()
        cursor = db.cursor()
        cursor.execute("INSERT INTO Url VALUES(%s, %s, %s, %s,%s,%s)",
                       (objectUrl.IdUrl, objectUrl.UrlCaminho, objectUrl.IdUrlPai,
                       objectUrl.NivelRecursividade, objectUrl.DataCadastro, objectUrl.SeBase))
        db.commit()
        db.close()


    def pesquisaUrlPeloIdPai(self, id):
        conn = Conexao()
        db = conn.recebeConexao()
        cursor = db.cursor()
        cursor.execute("SELECT * from Url WHERE IdUrlPai= %s", (id))
        retorno = cursor.fetchone()
        url = ModelUrl()
        url.IdUrl = retorno[0]
        url.UrlCaminho = retorno[1]
        url.IdUrlPai = retorno[2]
        url.NivelRecursividade = retorno[3]
        url.DataCadastro = retorno[4]
        if (str(retorno[5]) == "1"):
            url.SeBase = True
        else:
            url.SeBase = False
        db.close()
        return url

    def pesquisaUrlPelaUrl(self, url):
        conn = Conexao()
        db = conn.recebeConexao()
        cursor = db.cursor()
        cursor.execute("SELECT * from Url WHERE urlCaminho = %s", (url))
        retorno = cursor.fetchone()
        url = ModelUrl()
        if (retorno != None):
            url.IdUrl = retorno[0]
            url.UrlCaminho = retorno[1]
            if (str(retorno[2]) != None):
                url.IdUrlPai = retorno[2]
            else:
                url.IdUrlPai = None
            url.NivelRecursividade = retorno[3]
            url.DataCadastro = retorno[4]
            if (str(retorno[5]) == "1"):
                url.SeBase = True
            else:
                url.SeBase = False
        else:
            url = None

        db.close()
        return url

#def main():
#    d = DaoUrl()
#    m = ModelUrl()
#    m.DataCadastro = time.strftime("%Y-%m-%d")
#    m.IdUrl = str(uuid1())
#    m.UrlCaminho = "www.cogum.com.br"
#    m.IdUrlPai = None
#    m.SeBase = True
#    m.NivelRecursividade = 3
#    d.insertUrl(m)
#
#
#
#
#if __name__=="__main__":
#    main()
