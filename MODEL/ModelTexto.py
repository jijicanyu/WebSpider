# -*- coding: UTF-8 -*-

import sys #Importa Sys
sys.path.insert(0, '..') #Importante para setar estrutura de arquivos para encontrar Modulos

class ModelTexto(object):
    def __init__(self, IdTexto=None, Texto=None, IdTipoTexto=None, IdUrl=None):
        self.IdTexto = IdTexto
        self.Texto = Texto
        self.IdTipoTexto = IdTipoTexto
        self.IdUrl = IdUrl


