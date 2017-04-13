# Movie-Trailer
In this project,we have a Movie Trailer Website where you can see your favorite movies and watch the trailers.
## Table of contents

- [Demo](#demo)
- [Quick start](#quick-start)
- [Documentation](#documentation)
- [Copyright and license](#copyright-and-license)

## Demo

For a demo, check out <>!

## Quick Start

After downloading the project files,
 a movie trailer page can be created by importing [media.py](https://github.com/raymondjo/Movie-trailer-project/blob/master/media.py)
  and **fresh_tomatoes.py** in **entertainment_center.py** file
Then create individual Movie objects by calling media.Movie()
and supplying it with four arguments 
-- title,  poster_url, and trailer_url. Lastly, 
 generate the movie trailers page by calling fresh_tomatoes.open_movies_page() 
and supply it with an array of the movie objects that's created. 





divergent = Movie(
    "Divergent",
    "A thrilling action-adventure film set in a world where people are "
    "divided into distinct factions based on human virtues.",
    "https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg",
    "https://youtu.be/336qJITnDi0")

```
import media
import fresh_tomatoes

#information for object arguments
title = "Divergent"
story_line = "A thrilling action-adventure film set in a world where people are divided into distinct factions based on human virtues."
poster_url = "https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg"
trailer = "https://youtu.be/336qJITnDi0"

# Create Movie object
divergent = media.Movie(title, story_line, poster_url, trailer_url)

# Create movie trailer page with array of one movie
fresh_tomatoes.open_movies_page([divergent])

```

### What's included

Within the download you'll find the following directories and files:

```
├── entertainment_center.py
├── fresh_tomatoes.html
├── fresh_tomatoes.py
├── media.py
└── README.md
```

## Documentation

### Movie object class

The Movie object class consists of four class variables, 
a simple constructor method, and a class method for playing a Movie object's movie trailer.
 The code is located in **media.py**. 

##### constructor method

The constructor method is called when a new Movie object is created 
and must include four arguments 
-- title, story_line, poster_url, and trailer_url.
 Each of these arguments is discussed further below.
ie(title, story_line, poster_url, trailer_url)


###### movie.title

movie.title is any string used to identify the movie object.

###### movie.poster_url

movie.poster_url is a string containing a URL linking to an image which will be used to represent the Movie object,
 such as a movie poster. 

###### movie.trailer_url

movie.trailer_url is a string containing a URL linking to the movie trailer on YouTube.com. 
The movie trailer page portion of the this project extracts the YouTube id from the URL.

##### show_trailer method

show_trailer can be called on any Movie class object to launch that object's movie trailer in a webpage.

### Movie Trailer Page Functions 

The functions used to create the final movie trailers page are located in **fresh_tomatoes.py**.

## Copyright and License

- Project starter code (supplied without rights information) contributed by [Udacity](http://www.udacity.com).




