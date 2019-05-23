import urllib2

def urlToHtmlDoc(url):
    response = urllib2.urlopen(url)
    return response.read()

def htmlDocToArticleText(rawHtml):
    print(rawHtml)
    return rawHtml
    # articleDiv = rawHtml[
    #    rawHtml.index("<div class=\"postArticle-content\""):
    #    rawHtml.index("</section>")
    #]
    #articleDiv = articleDiv[articleDiv.index("<section>") + len("section"):]
    # articleDiv is now the html between the section tags of the articles rawHtml
    #print(articleDiv)
