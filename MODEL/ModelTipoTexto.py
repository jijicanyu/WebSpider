# -*- coding: UTF-8 -*-

import sys #Importa Sys
sys.path.insert(0, '..') #Importante para setar estrutura de arquivos para encontrar Modulos

class ModelTipoTexto(object):
    def __init__(self, IdTipoTexto=None, Descricao=None, SeLingProgramacao=None):
        self.IdTipoTexto = IdTipoTexto
        self.Descricao = Descricao
        self.SeLingProgramacao = SeLingProgramacao