import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Story of a boy and his living toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                    "A marine on a mysterious planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
school_of_rock = media.Movie("School of Rock",
                             "A teacher uses rock music to teach his students",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
ratatouille = media.Movie("Ratatouille",
                             "A rat is a chef in Paris",
                             "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                             "https://www.youtube.com/watch?v=ALUmKa_mpik")
midnight_in_paris = media.Movie("Midnight in Paris",
                             "Going back in time to meet authors",
                             "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                             "https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games = media.Movie("Hunger Games",
                             "A really real reality show",
                             "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                             "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
# fresh_tomatoes.open_movies_page(movies)

# print (media.Movie.VALID_RATINGS)

print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)
