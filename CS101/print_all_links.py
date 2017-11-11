# Define a procedure, print_all_links, that prints
# all the links in a page

def get_next_target (page):
    start_link = page.find('<a href=')
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def print_all_links (page):
    while True:
        url, endpos = get_next_target (page)
        if url:
            print url
            page = page[endpos:]
        else:
            break