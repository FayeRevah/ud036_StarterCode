import media
import fresh_tomatoes

# Toy story movie: movie title, storyline, poster image and movie trailer url
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that can come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# Avatar movie: movie title, storyline, poster image and movie trailer url
avatar = media.Movie("Avatar",
                     "A marine on an alient planet",
                     "https://www.movieposter.com/posters/archive/main/"
                     "101/MPW-50968",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

# Titanic movie: movie title, storyline, poster image and movie trailer url
titanic = media.Movie("Titanic",
                      "The night the Titanic sunk",
                      "https://images-na.ssl-images-amazon.com/images/I/"
                      "51n%2BW2kt8DL._SY450_.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

# Jurassic Park movie: movie title, storyline, poster image and movie trailer
# url
jurassic = media.Movie("Jurassic Park",
                       "An island theme park populated by dinosaurs",
                       "https://images-na.ssl-images-amazon.com/images/I"
                       "/61RLRZnbc%2BL._SY550_.jpg",
                       "https://www.youtube.com/watch?v=lc0UehYemQA")

# Jaws movie: movie title, storyline, poster image and movie trailer url
jaws = media.Movie("Jaws",
                   "A great shark terrorizes Amity Island",
                   "https://i0.wp.com/media2.slashfilm.com/slashfilm/"
                   "wp/wp-content/images/jaws.jpeg",
                   "https://www.youtube.com/watch?v=U1fu_sA7XhE")

# Pirates of the Caribbean movie: movie title, storyline, poster image
# and movie trailer url
pirates = media.Movie("Pirates of the Caribbean",
                      "Pirate tries to save girl from his former allies",
                      "http://www.joblo.com/newsimages1/pirates-of-the-"
                      "caribbean-dead-men-tell-no-tales-poster-3-small.jpg",
                      "https://www.youtube.com/watch?v=naQr0uTrH_s")

# an array of movies that will be passed to the html page and displayed
movies = [toy_story, avatar, titanic, jurassic, jaws, pirates]

# calls the method from fresh_tomatoes file to open the HTML display and pass
# in the movie array
fresh_tomatoes.open_movies_page(movies)
