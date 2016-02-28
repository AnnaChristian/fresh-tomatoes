import json
import media
import fresh_tomatoes


def read_data_from_file(filepath):
    """
    Read jsondata from file at path provided
    Input: string filepath
    Returns: data read
    """
    if not len(filepath.strip()):
        print "No filepath"
        exit()

    try:
        filedata = open(filepath, 'r').read()
    except:
        print "failed to load from file: %s", filepath
        filedata = None

    return filedata


def get_jsondata(data):
    """
    Takes json and uses json.loads to convert it for python consumption
    Input: json data string
    Returns: coverted json data
    """

    if not len(str(data).strip()):
        print "Data is empty"
        exit()

    try:
        jsondata = json.loads(str(data))
    except:
        jsondata = None

    return jsondata


def create_movies_list_from_json(jsondata):
    """
    Take json data and convert it to a list of Movie objects
    """
    if not jsondata:
        print "No data. Will exit."
        exit()

#    if ('title' not in moviedata or
#       'story' not in moviedata or
#       'poster_url' not in moviedata or
#       'trailer_url' not in moviedata):
#        print "Malformed data"
#        exit()

    movies = []
    for item in jsondata:
        movie = media.Movie(
            item['title'],
            item['story'],
            item['poster_url'],
            item['trailer_url']
        )
        movies.append(movie)

    return movies

path = "data/movie_data.json"
filedata = read_data_from_file(path)

if not filedata:
    print "No file data"
    exit()
else:
    jsondata = get_jsondata(filedata)
    if not jsondata:
        print "No jsondata"
        exit()
    else:
        movies = create_movies_list_from_json(jsondata)
        fresh_tomatoes.open_movies_page(movies)

