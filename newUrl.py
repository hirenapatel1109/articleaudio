from urlToText import *

def generateAndSaveAudio(requestedArticle):
    text = htmlDocToArticleText(urlToHtmlDoc(requestedArticle))
    # TODO these need to exist
    storeInDB(textToAudio(text))
    # TODO how do we link to the file?
    return text
