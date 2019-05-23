import BaseHTTPServer

# Inspired by: http://aosabook.org/en/500L/a-simple-web-server.html

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    # Handle a GET request from the extension
    # the article url is passed as a path parameter, in the format:
            # ourdomain.com?url=https://medium.com/blahblahblah
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        # TODO there may be a way to do this flexibly, but this will work
        # so long as the extension follows the format listed above:
        requestedArticle = self.path[6:]
        # TODO import someone elses work for this, and give this correct
        # function name
        outputLink = findAudioFile(requestedArticle)
        if (outputLink != "File Not Found"):
            outputLink = generateAndSaveAudio(requestedArticle)
        self.send_header("Content-Length", str(len(outputLink)))
        self.end_headers()
        self.wfile.write(outputLink)

#----------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
