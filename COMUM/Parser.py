# -*- coding: UTF-8 -*-

import sys #Importa Sys
sys.path.insert(0, '..') #Importante para setar estrutura de arquivos para encontrar Modulos
import re
class ParseHtml(object):
    def __init__(self, html=None):
        self.html = self.PrepareHtml(html)

    def ExtractUrl(self):
        listUrls = []
        pattern = re.compile(r"<a href='(?P<url>[^']*?)'[^>]*?>")
        for match in pattern.finditer(self.html):
            if match:
                listUrls.append(match.groupdict())

        return listUrls

    def PrepareHtml(self, html):
        html = str(html).replace('"', "'") #Replacing double " to simple '
        return html

    def ExtractText(self):
        htmlText = re.sub(r"<script.*?>[^<]*?</script>", "",self.html)
        htmlText = re.sub(r"<style.*?>[^<]*?</style>", "", htmlText)
        htmlText = re.sub(r"<!--[^-]*?-->", "", htmlText)
        htmlText = re.sub(r"<[^>]*?>", "", htmlText)
        htmlText = re.sub(r"(?ms)^\s+", "", htmlText)
        return htmlText