# 🎬 Movie Recommendation Engine — API Project

## 🎯 Goal

Build a Python movie recommendation engine that uses a **real movie API** instead of a static dataset.

The goal of this project is to practice the complete API workflow:

**Read documentation → authenticate → make a request → inspect JSON → extract data → process data → return useful results**

The application should allow a user to search for a movie and receive recommendations based on that movie.

You are **not** being given a dataset. Your program should retrieve the information it needs from the API.

---

# 🌐 API

### The Movie Database (TMDB) API

**Documentation:**
https://developer.themoviedb.org/

**Base URL:**

```text
https://api.themoviedb.org/3
```

TMDB provides access to movie information including titles, descriptions, release dates, ratings, genres, popularity, and other movie metadata.

You will need to create a TMDB account and obtain API credentials before making authenticated requests. TMDB supports authentication using an API key or a Bearer access token.

### Python tools

Use:

```python
import requests
```

You should **not** use a Python TMDB wrapper/library for this project.

The purpose is to practice making HTTP requests yourself.

---

# 🧠 Core Workflow

Your program should eventually be capable of doing something similar to:

```text
User enters a movie
        ↓
Python sends request to TMDB
        ↓
TMDB returns JSON
        ↓
Python extracts movie information
        ↓
Python identifies relevant movies
        ↓
Python ranks/filter recommendations
        ↓
User receives recommendations
```

---

# 📋 Requirements

## 1. API Authentication

Your program must authenticate with TMDB.

### Requirements

* Store your API credential securely.
* Do NOT hard-code your real API key directly into your Python source code.
* Research how environment variables work.
* Use the `requests` library to send authenticated requests.

### Research

Find out:

* How TMDB authentication works.
* What an API key/access token is.
* How to send authentication headers with `requests`.
* How to store your credential in an environment variable.

---

# 2. Search for a Movie

Ask the user for a movie title.

Example:

```text
Enter a movie: Inception
```

Your program should send a request to TMDB's movie search endpoint.

TMDB's movie search endpoint is:

```text
GET /search/movie
```

The endpoint accepts a `query` parameter for the movie title.

### Your program should:

1. Get the movie title from the user.
2. Send the API request.
3. Check the response.
4. Convert the response to JSON.
5. Inspect the JSON structure.
6. Extract the search results.
7. Display the matching movies.

Do **not** assume the first result is always correct.

---

# 3. Handle Multiple Search Results

The API may return multiple movies matching the user's search.

For example:

```text
Enter a movie: Batman

1. Batman
2. Batman Begins
3. The Batman
4. Batman Returns
...
```

Allow the user to select the movie they intended.

### Requirements

Your program should:

* Display multiple results.
* Give each result a number.
* Allow the user to select one.
* Store the selected movie's ID.

---

# 4. Retrieve Movie Details

Once the user selects a movie, use the movie's ID to request additional information.

Research the TMDB endpoint for retrieving details about a specific movie.

Your program should retrieve useful information such as:

* Title
* Overview
* Release date
* Rating
* Vote count
* Popularity
* Genres
* Runtime

Do not simply print the entire JSON response.

Practice extracting only the information your program actually needs.

---

# 5. Find Recommendations

Now build the actual recommendation component.

Research TMDB's recommendation/discovery endpoints.

TMDB provides functionality for finding movies using filters and for obtaining movie recommendations.

Your program should use the selected movie to find other movies that could be recommended to the user.

For example:

```text
Because you liked:

Inception

You might also like:

1. Interstellar
2. The Prestige
3. Shutter Island
4. Memento
5. Tenet
```

---

# 6. Process the Recommendations

Don't simply display whatever the API gives you.

Practice processing the API response.

For each recommended movie, consider:

* Title
* Rating
* Release date
* Popularity
* Genre
* Overview

You might decide to:

* Remove movies without release dates.
* Remove movies with very low ratings.
* Sort by rating.
* Sort by popularity.
* Limit results to the top 5 or 10 movies.

The recommendation logic is yours to design.

---

# 7. Build a Simple Recommendation Algorithm

Create your own basic recommendation logic.

For example, your program could score movies based on:

```text
Rating
Popularity
Genre similarity
Release year
```

You could create a simple score such as:

```text
recommendation_score =
    rating_weight +
    popularity_weight +
    genre_match_weight
```

The exact algorithm is up to you.

The important part is that **you understand why your program selected each movie.**

---

# 🧩 Suggested Functions

Your final program should be broken into functions rather than putting everything inside `main()`.

Possible functions:

```python
def search_movies(query):
    pass


def display_search_results(movies):
    pass


def select_movie(movies):
    pass


def get_movie_details(movie_id):
    pass


def get_recommendations(movie_id):
    pass


def filter_movies(movies):
    pass


def rank_movies(movies):
    pass


def display_recommendations(movies):
    pass


def main():
    pass
```

You do **not** have to use these exact functions.

Think about what each function should be responsible for.

---

# 🔎 API Questions to Research

Do not immediately ask for the implementation.

Use the TMDB documentation and Python documentation to answer these questions yourself.

## Authentication

1. How does TMDB authenticate API requests?
2. What is a Bearer token?
3. How do you send an `Authorization` header using `requests`?
4. How should you keep your API credential out of your source code?

---

## Requests

5. How does `requests.get()` work?
6. What does the `params` argument do?
7. What does `response.json()` return?
8. What is the difference between a URL parameter and a request header?

---

## JSON

9. What type of Python object do you get from `response.json()`?
10. How do you access a value inside a dictionary?
11. How do you access a list inside a dictionary?
12. How do you loop through a list of dictionaries?
13. What happens if a JSON field doesn't exist?

---

## Error Handling

14. What HTTP status codes should you be concerned about?
15. How can you determine whether a request was successful?
16. What happens if the user's movie search returns zero results?
17. What happens if the API request fails?
18. How should your program handle an invalid movie selection?

Research:

```python
response.raise_for_status()
```

---

## TMDB Data

19. What information does the movie search endpoint return?
20. What is the movie's `id`?
21. What is `vote_average`?
22. What is `vote_count`?
23. What is `popularity`?
24. What is `genre_ids`?
25. How can you convert genre IDs into readable genre names?

---

# 🛠️ Suggested Development Order

Don't try to build the entire application at once.

Build it in stages.

### Stage 1 — Make one API request

Hard-code a movie temporarily.

Your only goal:

```text
Python → TMDB → JSON response
```

---

### Stage 2 — Search

Allow the user to enter a movie.

```text
User → Movie title → API → Search results
```

---

### Stage 3 — Selection

Allow the user to choose one movie from the results.

```text
Search results → User selection → Movie ID
```

---

### Stage 4 — Details

Use the movie ID to retrieve additional information.

```text
Movie ID → API → Movie details
```

---

### Stage 5 — Recommendations

Use the selected movie to retrieve potential recommendations.

```text
Selected movie → API → Recommended movies
```

---

### Stage 6 — Processing

Filter and sort the recommendations.

```text
API results
     ↓
Filter
     ↓
Sort
     ↓
Top recommendations
```

---

### Stage 7 — Polish

Add:

* Input validation
* Exception handling
* Clean output
* Functions
* Environment variables
* API error handling

---

# 🚀 Minimum Viable Version

Your first completed version should allow the user to:

```text
Enter a movie
      ↓
Search TMDB
      ↓
Select a movie
      ↓
Retrieve recommendations
      ↓
Display 5 recommended movies
```

Don't overcomplicate the first version.

Get this working first.

---

# ⭐ Stretch Goals

Once the basic application works, add additional features.

## ⭐ 1. Genre Filtering

Allow the user to specify a genre.

```text
Genre: Science Fiction
```

Then use the API to filter the results.

---

## ⭐ 2. Minimum Rating

Ask:

```text
Minimum rating: 7.5
```

Only recommend movies meeting that rating.

---

## ⭐ 3. Release Year

Allow the user to specify a year range.

```text
From: 2015
To: 2025
```

---

## ⭐ 4. Multiple Recommendation Criteria

Allow the user to choose:

```text
1. Similar movies
2. Highest rated
3. Most popular
4. Recently released
5. Same genre
```

---

## ⭐ 5. Recommendation Scoring

Create your own scoring algorithm.

For example:

```text
Movie A
Rating: 8.4
Popularity: 92
Genre match: 100%

Movie B
Rating: 8.7
Popularity: 65
Genre match: 50%
```

Your program decides which movie gets the higher recommendation score.

---

## ⭐ 6. Movie Posters

Research TMDB's image configuration.

Display movie posters alongside recommendations.

---

## ⭐ 7. Caching

Research why repeatedly requesting the same API data can be inefficient.

Implement a simple cache so that your program doesn't repeatedly request information it already retrieved.

---

## ⭐ 8. Pagination

TMDB's search results are paginated.

Research:

```text
page
total_pages
total_results
```

Allow the user to move through multiple pages of search results.

---

## ⭐ 9. Multiple Movies

Instead of recommending movies based on one movie, allow the user to enter several movies they like:

```text
Movie 1: Inception
Movie 2: Interstellar
Movie 3: The Matrix
```

Then create recommendations based on their combined preferences.

---

## ⭐ 10. Build a User Profile

Allow the user to build a simple movie preference profile.

For example:

```text
Favorite genres:
- Science Fiction
- Thriller
- Drama

Minimum rating:
8.0

Preferred release period:
2010–2026
```

Use those preferences to generate recommendations.

---

# 🧠 What You Are Practicing

This project is specifically designed to practice:

* Python functions
* Variables
* Lists
* Dictionaries
* Loops
* Conditionals
* Exception handling
* JSON
* HTTP requests
* REST APIs
* API authentication
* Query parameters
* HTTP status codes
* Data extraction
* Data filtering
* Data sorting
* Basic algorithms
* Program decomposition

Most importantly, you're practicing this mental model:

```text
I need some data
       ↓
Where does the data live?
       ↓
Find the API documentation
       ↓
Find the correct endpoint
       ↓
Understand authentication
       ↓
Make the request
       ↓
Inspect the response
       ↓
Find the data I need
       ↓
Process it
       ↓
Use it in my program
```

That workflow is the **real skill** this project is designed to teach.
