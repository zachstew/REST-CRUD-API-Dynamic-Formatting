# Reflection: Tiny RESTful API with Dynamic Formatting

I followed the tutorial and video in broad steps: create a project folder and virtual environment, install Flask, add a hard-coded list of books, build the four CRUD endpoints, test them, then add an HTML view with conditional styling. My changes were adding a new book to the data and renaming every /books route to /goodbooks.

What surprised me most was that the data resets whenever the server restarts, because it lives only in memory. I also hit a snag on my Mac, where I had to use python3 instead of python before the virtual environment would activate. Troubleshooting that taught me how much the setup matters.

My code evolved from plain JSON endpoints to consistent status codes (200, 201, 204, 404), and then to an HTML page that loads data from the API, shows a loading message, handles errors, and highlights top-rated rows.

I now understand routing, HTTP verbs, and status codes much better. I'd like to learn more about databases for persistent storage.