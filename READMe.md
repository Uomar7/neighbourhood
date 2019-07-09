# NEIGHBOURHOOD

Professional web app for a user to see all the available neighbourhoods and even join one. User can add business or even create new neighbourhood.

---

## Author

* **Uomar**
* **Email** : <uomarearlie7@gmail.com>

---

## BDD

|Input  | Behaviour | output |
|------|:-----:|-----|
|on landing in the website| | Login or register in the app.|
|Then create or join in an already existing neighbourhood.| Routed in the neighbour page.| See all the posts and businesses in that particular neighbourhood.|
|Go to profile and view user profile|Routed to the profile page| View the user profile and all the user posts or businesses.|
|Click on Add Post to your neighbourhood.|Routed back to the neighbourhood| Get to see all the posts on that neighbourhood|
|Click on a particular post| Routed to the post.| User can see the post, all the details and even comment on a post. |

---

## Features

As a user, You will:

1. View posts in a particular neighbourhood.
2. Post anything in a particular neighbourhood.
3. Write a comment on a post.
4. Search for projects.
5. Join an already there neighbourhood or create a new neighbourhood.
6. View my profile page.
7. Create a new business.

---

## Github pages

Access the app files on my [github](https://github.com/Uomar7)

---

## Awaards Site

click to view site [here](https://neighbpur.herokuapp.com)

---

### Installing

* View app repo @ [Neighbourhood](https://github.com/Uomar7/neighbourhood)

1. Clone this repo: git clone <https://github.com/Uomar7/neighbourhood.git> .

2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)

4. To run the app, you'll have to run the following commands in your terminal

       `pip install -r requirements.txt`

5. On your terminal,Create database gallery using the command below.

       CREATE DATABASE neigh; 
       **if you opt to use your own database name, replace instaclone your preferred name, then also update settings.py variable DATABASES > NAME

6. Migrate the database using the command below

       `python3.6 manage.py migrate`
7. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

       `python manage.py runserver`
8. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

---

## Built With

* [Django](https://www.djangoproject.com/) - web framework used
* Javascript - For DOM(Document Object Manipulation) scripts
* HTML - For building Mark Up pages/User Interface
* CSS
* Bootstrap 4

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

---

## Acknowledgments

* MC17 TMs
