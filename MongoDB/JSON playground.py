"""
To experiment with this code freely you will have to run this code locally.
Take a look at the main() function for an example of how to use the code. We
have provided example json output in the other code editor tabs for you to look
at, but you will not be able to run any queries through our UI.
"""
import json
import requests
import pprint

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

print (ARTIST_URL)

# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}
print (query_type["simple"])

def query_site(url, params, uid="", fmt="json"):
    """
    This is the main function for making queries to the musicbrainz API. The
    query should return a json document.
    """
    print (url)
    print (fmt)
    print (params)
    params["fmt"] = fmt
    print (params)
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    print (r.status_code)
    print (requests)
    print (r.json)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    """
    This adds an artist name to the query parameters before making an API call
    to the function above.
    """
    print (params)
    print (name)
    params["query"] = "artist:" + name
    print (url, params)
    pprint.pprint (query_type)
    return query_site(url, params)


def pretty_print(data, indent=4):
    """
    After we get our output, we can use this function to format it to be more
    readable.
    """
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    """
    Below is an example investigation to help you get started in your
    exploration. Modify the function calls and indexing below to answer the
    questions on the next quiz.

    HINT: Note how the output we get from the site is a multi-level JSON
    document, so try making print statements to step through the structure one
    level at a time or copy the output to a separate output file. Experimenting
    and iteration will be key to understand the structure of the data!
    """

    # Query for information in the database about bands named Nirvana
    results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    pretty_print(results)
    pprint.pprint (results["artists"])
    for artist in results["artists"]:
        if artist['country']:
            print artist['country']
        # print artist['name'], artist['score'], artist['country']
    # print (len(results))
    # pprint.pprint (query_type)

    # # Isolate information from the 4th band returned (index 3)
    # print "\nARTIST:"
    # pretty_print(results["artists"][3])
    #
    # # Query for releases from that band using the artist_id
    # artist_id = results["artists"][3]["id"]
    # print (artist_id)
    # print (ARTIST_URL, query_type)
    # artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    # pprint.pprint (artist_data)
    # releases = artist_data["releases"]
    #
    # # Print information about releases from the selected band
    # print "\nONE RELEASE:"
    # pretty_print(releases[0], indent=2)
    #
    # release_titles = [r["title"] for r in releases]
    # pprint.pprint (release_titles)
    # print "\nALL TITLES:"
    # for t in release_titles:
    #     print t

if __name__ == '__main__':
    main()
