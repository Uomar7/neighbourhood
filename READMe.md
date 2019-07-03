# Awaaards Replica


professional web design and development competition site.

---

## Author

* **Uomar**
* **Email** : <uomarearlie7@gmail.com>

---

## BDD

|Input  | Behaviour | output |
|------|:-----:|-----|
|on landing in to the website.| | Get to see all the available projects.|
|On clicking on the view more.|See routed to the project| User will get to see the project details and also vote for it.|


---
## Features


As a user, You will:

1. View posted projects and their details.
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects 
5. View projects overall score
6. View my profile page.
---

## Github pages

Access the app files on my [github](https://github.com/Uomar7)

---

## Awaards Site

click to view site [here](https://oneawaard.herokuapp.com/)

---
### Installing

* View app repo @ [Awaards](https://github.com/Uomar7/awaards)

1. Clone this repo: git clone https://github.com/Uomar7/awaards.git .

2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)

3. To run the app, you'll have to run the following commands in your terminal
    
    
       `pip install -r requirements.txt`
4. On your terminal,Create database gallery using the command below.


       CREATE DATABASE award; 
       **if you opt to use your own database name, replace instaclone your preferred name, then also update settings.py variable DATABASES > NAME

5. Migrate the database using the command below


       `python3.6 manage.py migrate`
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       `python manage.py runserver`
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

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
