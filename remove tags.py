# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags.
# You may assume the input does not include any unclosed tags, that is,
# there will be no '<' without a following '>'.

def find_tag(page):
    start_tag = page.find('<')
    end_tag = page.find('>', start_tag)
    tag = page[start_tag:end_tag + 1]
    return tag, end_tag

def get_all_tags(page):
    tags = []
    n = 0
    while n <= len(page):
        tag, end_tag = find_tag(page)
        if tag:
            tags.append(tag)
            page = page[end_tag:]
            n = n + 1
    return tags

def remove_tags(page):
    if '<' not in page:
        return page.split()
    new_page = ''
    for tag in get_all_tags(page):
        new_page = page.replace(tag, ' ', 1)
        page = new_page
    return new_page.split()

def remove_tags(string):
    start = string.find('<')
    while start != -1:
        end = string.find('>', start)
        string = string[:start] + " " + string[end + 1:]
        start = string.find('<')
    return string.split()

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
# #>>> ['Title','This','is','a','link','.']
#

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']