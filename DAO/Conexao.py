# -*- coding: UTF-8 -*-
import sys #Importa Sys
sys.path.insert(0, '..') #Importante para setar estrutura de arquivos para encontrar Modulos
from MySQLdb import connect


class Conexao:
    def __init__(self):
        self.Host = None
        self.DataBase = None
        self.DbConexao = None
        self.User = None
        self.Password = None
        self.IndicaString(host="localhost", user="root", password="ibc3car!", db="WebSpider",)

    def IndicaString(self, **kwargs):
        self.Host = kwargs["host"]
        self.DataBase = kwargs["db"]
        self.User = kwargs["user"]
        self.Password = kwargs["password"]


    def recebeConexao(self):
        self.DbConexao = connect(self.Host, self.User, self.Password, self.DataBase)
        return self.DbConexao


