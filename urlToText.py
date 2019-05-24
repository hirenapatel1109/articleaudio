import urllib2

def urlToHtmlDoc(url):
    response = urllib2.urlopen(url)
    # TODO how do we handle a 403 response?
    return response.read()

def htmlDocToArticleText(rawHtml):
    articleDiv = rawHtml[
        rawHtml.index("<div class=\"postArticle-content\""):
        rawHtml.index("</section>")
    ]
    articleDiv = articleDiv[articleDiv.index("<section>") + len("section"):]
    # articleDiv is now the html between the section tags of the articles rawHtml
    # TODO parse articleDiv to get the actual text
    return articleDiv
