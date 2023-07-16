# My Blog

This project is my first using Python and Django.

This project is a Medium Copycat which allows me to create a post and list them like popular blog sites like Medium and Tumbler.

## Features

- Display a list of posts.
- See the details of a post on a separate page.
- Create a post draft, and publish a post.
- Add a comment to a post.
- As an authorised user, the ability to approve or reject comments attached to a post.

## Technologies

- **Python**
- **Django**
- **Bootstrap**

## Getting Started
After cloning the repository
```
cd my_blog
python manage.py runserver
```
The app should be available on the browser at `http://localhost:8000`

## Project Structure
- `my_blog_project/` - Contains the URL maps and settings for this project.
- `blog/urls.py`:  Contains url mapping for the blog app.
- `blog/views.py`:  Contains view functions for the blog app.
- `blog/models.py`:  Contains models used for the blog app.
