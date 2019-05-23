from urlToText import *

def generateAndSaveAudio(requestedArticle):
    return htmlDocToArticleText(urlToHtmlDoc(requestedArticle))
