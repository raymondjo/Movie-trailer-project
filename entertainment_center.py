from media import Movie
import fresh_tomatoes

toy_story = Movie("Toy story", "toy",
                  "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",  # NOQA
                  "https://www.youtube.com/watch?v=TZeG23jEfHM")


avatar = Movie(
    "avatar movie",
    "avatar",
    "http://cdn.pcwallart.com/images/avatar-poster-wallpaper-3.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

divergent = Movie(
    "Divergent",
    "A thrilling action-adventure film set in a world where people are "
    "divided into distinct factions based on human virtues.",
    "https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg",
    "https://youtu.be/336qJITnDi0")

spider_Man = Movie("Spider-Man",
                    "Abandoned by his parents and raised by an aunt and uncle,"
                    " teenager Peter Parker (Andrew Garfield), AKA Spider-Man,"
                    " is trying to sort out who he is and exactly what his"
                    " feelings are for his first crush, Gwen Stacy "
                    " (Emma Stone). When Peter finds a mysterious "
                    " briefcase that was his father's,he pursues "
                    "a quest to solve his parents' disappearance.",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcQVzjsQN4VSZaWDXWYf1dCLQ6fU3ArTWTMh9fwmYcMke_RsOgP6",   # NOQA
                   "https://www.youtube.com/watch?v=xrzXIaTt99U")

Insurgent = Movie(
    "The Divergent Series: Insurgent",
    "Insurgent raises the stakes for Tris as she searches for allies "
    "and answers in the ruins of a futuristic Chicago.",
    "https://upload.wikimedia.org/wikipedia/en/a/af/Insurgent_poster.jpg",
    "https://youtu.be/sX9-l0iO5w4")

deadpool = Movie(
    "Deadpool",
    "Wade Wilson (Ryan Reynolds) is a former Special Forces operative "
    "who now works as a mercenary. His world comes crashing down "
    "when evil scientist Ajax (Ed Skrein) tortures, disfigures "
    "and transforms him into Deadpool.",
    "http://www.impawards.com/2016/posters/deadpool_ver9_xxlg.jpg",
    "https://www.youtube.com/watch?v=9vN6DHB6bJc")

star_trek = Movie(
    "Star Trek",
    "The greatest adventure of all time begins with Star Trek, "
    "the incredible story of a young crew's maiden voyage onboard"
    " the most advanced starship ever created: the U.S.S. Enterprise.",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
    "https://youtu.be/iGAHnZ555nI")

captain_america = Movie("Captain America",
                        "Political pressure mounts to install a system of"
                          " accountability when the actions of the "
                          " Avengers lead to collateral damage.The new status"
                          " quo deeply divides members of the team."
                          " Captain America (Chris Evans) believes superheroes"
                          " should remain free to defend humanity"
                          " without government interference.",
                           "http://t3.gstatic.com/images?q=tbn:ANd9GcTz1xU3qYlGXViIS51HIQh71D339ceW2nlWnb8zzSaJAL0newVj",   # NOQA
                          "https://www.youtube.com/watch?v=dKrVegVI0Us")


arrival = Movie("Arrival", "Linguistics professor Louise Banks (Amy Adams)"
                  " leads an elite team of investigators when gigantic "
                  "spaceships touch down in 12 locations around the world.",
                  "https://bia2movies3.org/wp-content/uploads/2017/01/xGgg2UI20qtEh7mura3RRwP8d3I.jpg",   # NOQA
                  "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

# this is the movies list which will be sent to open movies function
movies = [toy_story, avatar, divergent, deadpool,
          captain_america, star_trek, spider_Man, Insurgent, arrival]
          
fresh_tomatoes.open_movies_page(movies)
