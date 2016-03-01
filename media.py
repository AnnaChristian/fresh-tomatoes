class Movie():
    """ 
    Class devining a movie.
    Instance variables: 
    title, storyline, poster_image_url, trailer_youtube_url
    Methods:
    show_trailer()
    """

    def __init__(self, title, storyline, poster_img_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
#        self.year = year
#        self.cast = cast
#        self.director = director
        self.poster_image_url = poster_img_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
    	"""
    	opens trailer_youtube_url in default web browser
    	"""
    	
        import webbrowser
        webbrowser.open(self.trailer_youtube_url)

