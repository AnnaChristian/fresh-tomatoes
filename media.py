class Movie():
    """ Class defining a movie.

    Attributes:
        title (str): movie title
        storyline (str): brief description of the movie's story line
        poster_image_url (str): URL of movie's box art
        trailer_youtube_url (str): URL of movie's trailer on YouTube

    Methods:
        show_trailer()
    """

    def __init__(self, title, storyline, poster_img_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_img_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """
        opens trailer_youtube_url in default web browser
        """

        import webbrowser
        webbrowser.open(self.trailer_youtube_url)

