# Reflection: Tiny RESTful API with Dynamic Formatting

I followed the tutorial and video by creating a project folder and virtual environment, installing Flask, adding a hard-coded list of books, building the four CRUD endpoints, testing them, and adding an HTML view with conditional styling. My changes were adding a new book to the data and renaming every /books route to /goodbooks.

What surprised me most was that the data resets whenever the server restarts because it lives only in memory. I also hit a snag on my Mac, where I had to use python3 instead of python before the virtual environment would activate. Troubleshooting that taught me how much each individual step in the setup matters.

My code evolved from plain JSON endpoints to consistent status codes (200, 201, 204, 404), and then to an HTML page that loads data from the API, shows a loading message, handles errors, and highlights top-rated rows.

I now understand routing, HTTP verbs, and status codes much better after this assignment. I'd like to learn more about using a database for persistent storage and about validating the data users send to the API.
