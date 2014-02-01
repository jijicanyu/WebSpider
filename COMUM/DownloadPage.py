# -*- coding: UTF-8 -*-

import sys #Importa Sys
sys.path.insert(0, '..') #Importante para setar estrutura de arquivos para encontrar Modulos
import urllib2
from BeautifulSoup import BeautifulStoneSoup

class DownloadPage(object):
    def __init__(self, url):
        self.url = url


    def DownloadHtml(self):
        try:
            pass
            userAgent = r"Googlebot/2.1 (+http://www.googlebot.com/bot.html)"
            req = urllib2.Request(self.url)
            req.add_header("User-Agent", userAgent)
            response = urllib2.urlopen(req)
            html = response.read()
            return html
        except Exception, ex:
            print ("ERRO: Foi gerada uma exceção do tipo {0} ao conectar na url:{1}".format(str(ex.message)
                                                                                                ,self.url))
            return None


#def main():
#    d = DownloadPage("http://www.blogvinhotinto.com.br/harmonizacoes/harmonizacao-ceia-natal-ano/")
#    page = d.DownloadHtml()
#    print page
#
#
#if __name__ == "__main__":
#    main()
#


