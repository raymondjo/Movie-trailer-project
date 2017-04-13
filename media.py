import webbrowser


class Movie:
    """ This class provides a way to store movie related information

     Attributes:
            movie_title(str): This is the movie title.
            movie_storyline(str): This is the stroy line.
            poster_image(str): This is the movie image url.
            trailer_youtube_url(str): This is the movie trailer url.
    """
    # this is class variables is constant for all
    # objects from this class
    # NOTE : google style guide is capital letters
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube_url):
        """ Inits class variables ."""
        # all of them are instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Open trailer from youtube url for testing."""
        webbrowser.open(self.trailer_youtube_url)
