class Movie():
    """ Doctring """

    def __init__(self, title, storyline, poster_img_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
#        self.year = year
#        self.cast = cast
#        self.director = director
        self.poster_image_url = poster_img_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        import webbrowser
        webbrowser.open(self.trailer_youtube_url)

