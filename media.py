import webbrowser

class Movie():
    """A movie object with attributes title, storyline, poster and trailer url"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """initializes the movie class with user inputted variables"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """plays the trailer by grabbing the url attribute and opening browser"""
        webbrowser.open(self.trailer_youtube_url)
