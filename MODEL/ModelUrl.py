# -*- coding: UTF-8 -*-

import sys #Importa Sys
sys.path.insert(0, '..') #Importante para setar estrutura de arquivos para encontrar Modulos

class ModelUrl(object):
    def __init__(self, IdUrl=None, UrlCaminho=None, IdUrlPai=None, NivelRecursividade=None,
                 DataCadastro=None, SeBase=None):
        self.IdUrl = IdUrl
        self.UrlCaminho = UrlCaminho
        self.IdUrlPai = IdUrlPai
        self.NivelRecursividade = NivelRecursividade
        self.DataCadastro = DataCadastro
        self.SeBase = SeBase




