# -*- coding: UTF-8 -*-
import sys #Importa Sys
sys.path.insert(0, '..') #Importante para setar estrutura de arquivos para encontrar Modulos

from COMUM.DownloadPage import DownloadPage
from COMUM.Parser import ParseHtml
from DAO.DaoUrl import DaoUrl
from threading import Thread
from MODEL.ModelUrl import ModelUrl
from MODEL.ModelTexto import ModelTexto
from DAO.DaoTexto import DaoTexto
from uuid import *
from BeautifulSoup import *
import time

def main():
    global NivelRecursividade # Seta NivelRecursividade do inicio
    NivelRecursividade = 0
    f = open("../ARQUIVOS/UrlBases", "r") #Abre arquivo de url bases
    for urlArq in f.readlines(): #Percorre arquivo
      if urlArq:
        #ExecuteUrlSpider(str(urlArq).strip("\n"))
        th = Thread(target=ExecuteUrlSpider, args=(str(urlArq).strip("\n"), None)) #Lança thread com url sem pai
        th.start() #Inicia thread


def ExecuteUrlSpider(url, urlFather=None):
    dwPage = DownloadPage(url) #Cria objeto DownloadPage
    page = dwPage.DownloadHtml() #Faz download do html
    InsertUrl(url, urlFather) # Insere Url no db
    parser = ParseHtml(page) # Cria objeto parser
    htmlText = parser.ExtractText()
    SaveText(htmlText, url)
    listDictUrl = parser.ExtractUrl() #Chama metódo para extrair Url
    global NivelRecursividade
    NivelRecursividade += 1#Adiciona nivel de recursividade
    for urlSon in listDictUrl: #Percorre lista de url filhas extraidas
        if (ValidateUrl(str(urlSon['url']),url)):
            print str(urlSon['url'])
            try:
                th = Thread(target=ExecuteUrlSpider, args=(str(urlSon['url']).strip("\n"), url)) #Lança thread com url sem pai
                th.start() #Inicia thread
                #ExecuteUrlSpider(str(urlSon['url']), url) # Chama metódo recursivamente passando urlPai
            except Exception, ex:
                print ("Erro ao executar URL ~> {0}".format(str(urlSon['url'])))

def VerficaUrlExistente(url):
    dUrl = DaoUrl()
    urlSearch = dUrl.pesquisaUrlPelaUrl(url)
    if (urlSearch == None):
        return False
    else:
        return True



def InsertUrl(urlSon, urlFather):
    dUrl = DaoUrl()
    m = ModelUrl()
    if (urlFather == None):
        m.IdUrlPai = None
        m.SeBase = True
    else:
        mUrlFather = dUrl.pesquisaUrlPelaUrl(urlFather)
        m.IdUrlPai = mUrlFather.IdUrl
        m.SeBase = False
    m.IdUrl = str(uuid1())
    m.DataCadastro = time.strftime("%Y-%m-%d")
    global NivelRecursividade
    m.NivelRecursividade = NivelRecursividade
    m.UrlCaminho = urlSon
    dUrl.insertUrl(m)

def SaveText(htmlText, url):
    dUrl = DaoUrl()
    dTexto = DaoTexto()
    m = ModelTexto()
    m.IdTexto = str(uuid1())
    m.IdTipoTexto = 'a02e67b8-016a-423b-b6a4-f0500f880d6f'
    m.Texto = BeautifulStoneSoup(htmlText,
                                 convertEntities=BeautifulStoneSoup.HTML_ENTITIES) # Formata encode Resposta
    urlObject = dUrl.pesquisaUrlPelaUrl(url)
    if (urlObject):
        m.IdUrl = urlObject.IdUrl
    else:
        m.IdUrl = None
    dTexto.insertTexto(m)


def ValidateUrl(url, urlFather):
    if (url != urlFather and url.find("http://") == 0):
        if (not VerficaUrlExistente(url)):
            if (url.find("facebook") != 0):
                return True

    return False

if __name__ == "__main__":
    main()
