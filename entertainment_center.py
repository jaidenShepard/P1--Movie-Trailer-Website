import media
import fresh_tomatoes

# Initialization of all the movies to be included on the site
matrix = media.Movie("The Matrix",
                     "http://moviefiles.alphacoders.com/288/poster-28.jpg",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                     "1999",
                     "The Wachowski Brothers",
                     "The Wachowski Brothers",
                     "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss")

kung_fury = media.Movie("Kung Fury",
                        "http://i0.wp.com/cypruscomiccon.org/wp-content/uploads/2015/08/Kung_Fury_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=72RqpItxd8M",
                        "2015",
                        "David Sandberg",
                        "David Sandberg",
                        "David Hasselhoff, David Sandberg, Jorma Taccone",)

star_wars_VII = media.Movie("Star Wars: The Force Awakens",
                            "http://vignette2.wikia.nocookie.net/starwars/images/f/fd/Star_Wars_Episode_VII_The_Force_A"  # NOQA
                            "wakens.jpg/revision/latest?cb=20151018162823",
                            "https://www.youtube.com/watch?v=sGbxmsDFVnE",
                            "2015",
                            "J.J. Abrams",
                            "Lawrence Kasdan, J.J. Abrams",
                            "Daisy Ridley, John Boyega, Oscar Isaac",)

terminator_2 = media.Movie("Terminator 2: Judgement Day",
                           "http://www.cinemasterpieces.com/t2nm.jpg",
                           "https://www.youtube.com/watch?v=eajuMYNYtuY",
                           "1991",
                           "James Cameron",
                           "James Cameron, WIlliam Wisher Jr.",
                           "Arnold Schwarzenegger, Linda Hamilton, Edward "
                           "Furlong",)

ex_machina = media.Movie("Ex Machina",
                         "http://resizing.flixster.com/JToNrl2pa0PTlZyqmjPN4vMta9U=/800x1185/dkpu1ddg7pbsk.cloudfront.n"  # NOQA
                         "et/movie/11/19/09/11190916_ori.jpg",
                         "https://www.youtube.com/watch?v=XYGzRB4Pnq8",
                         "2015",
                         "Alex Garland",
                         "alex Garland",
                         "Alicia Vikander, Domhnall Gleeson, Oscar Isaac",)

ant_man = media.Movie("Ant-Man",
                      "http://blogs-images.forbes.com/scottmendelson/files/2015/05/BF_Payoff_1-Sht_v8_Lg-1309x1940.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=pWdKf3MneyI",
                      "2015",
                      "Peyton Reed",
                      "Edgar Wright, Joe Cornish",
                      "Paul Rudd, Michael Douglas, Corey Stoll",)

# Movies are saved into an list, which is passed to the page generating script
movies = [matrix, kung_fury, star_wars_VII, terminator_2, ex_machina, ant_man]
fresh_tomatoes.open_movies_page(movies)
