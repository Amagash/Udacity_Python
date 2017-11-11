import urllib

def check_profanity(text_to_check):
    connection = urllib.urlopen(
        "http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
def read_text():
    quotes = open("/home/tiffany/lab/Udacity_Python/movie_quote")
    content = quotes.read()
    print (content)
    quotes.close()
    check_profanity(content)

read_text()



