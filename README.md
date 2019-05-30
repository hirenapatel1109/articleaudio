Run the server by cloning this repository and running server.py. On unix systems, one can do this in the terminal, from within this repository's directory, via:

    python server.py

Then, make a get request of the format

    localhost:8080?url=theurlyouwanttotest.com

This code will, in its current form, make a request to theurlyouwanttotest.com, try to get the HTML doc from there, and try to parse out a div with the class postArticle-content. On medium.com, this is the div that holds the article's contents. On other domains, this script probably won't do much.
