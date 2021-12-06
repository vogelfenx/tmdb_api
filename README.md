# MOVIES WITH TMDB

## Overview
This package implements functions to search for movies in TMDB Database & get movie recommendations that match user interests.

The Movie Database (TMDB) is the popular database for movies. The service has an open [API](https://www.themoviedb.org/documentation/api) that allows you to collect movies, TV shows, actor images and/or data in an application.

## Overview of particular source files in this project
### Module make_own_db.py
This module is responsible for fetching movie data and saving them to a json file, when using the module as standalone script.  
By default 1000 movies would be collected.  
Using the module outside you can handle the fetched data in your way, e.g. saving them to your local database.
