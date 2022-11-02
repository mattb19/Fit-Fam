CSC 450 - 2 Team Project
===
### Team Members:  
- Nick, Noah, Jacob, Michael, Matt
### Using:  
- Vue.js 2.7.10 and Python 3.10.7

## TABLE OF CONTENTS:  

### 1. First Time Installations:
- MAC
- WINDOWS
### 2. Running:
- MAC
- WINDOWS
### 3. Testing:
- Flask
        
## FIRST TIME INSTALLATION MAC:
1. Install Vue.js 2.7.10, Python 3.10.7 and Visual Studio Code
2. Clone the github repo into your desired directory then open the directory in vscode
3. Open terminal in vscode, navigate to the backend folder and
run the following:

        python3 -m pip install flask
        python3 -m pip install flask-cors
4. Run it
using:

        python3 -m flask run
6. While keeping the backend terminal instance running, open a NEW terminal instance
7. Navigate to the frontend folder and
run the following:

        npm i -g @vue/cli
        npm i --save-dev eslint eslint-plugin-vue
        npm i axios
7. Run it
using:

        npm run serve

---

## FIRST TIME INSTALLATION WINDOWS:
1. Install Vue.js 2.7.10, Python 3.10.7 and Visual Studio Code
2. Clone the github repo into your desired directory then open the directory in vscode
3. Open terminal in vscode, navigate to the backend folder and
run the following:

        python -m pip install flask
        python -m pip install flask-cors
4. Run it
using:

        python -m flask run
5. While keeping the backend terminal instance running, open a NEW terminal instance
6. Navigate to the frontend folder and
run the following:

        npm i -g @vue/cli
        npm i --save-dev eslint eslint-plugin-vue
        npm i axios
7. Clean up the incorrect End of Line characters
using:

        npm run lint -- --fix
8. Run it
using:

        npm run serve

---

## INSTALLING THE REMAINING PLUGINS:
1. Install sqlite3
2. After that, in a terminal navigate to the backend folder
3. Type these commands and hit enter after each one:

        pip install sqlalchemy
        pip install flask-sqlalchemy
        pip install flask-migrate
        pip install flask-login
        pip install werkzeug
        
---

## RUNNING ON MAC:
1. Open a new terminal instance
2. Navigate to the backend folder and
type:

        python3 -m flask run
3. Open a NEW terminal instance (without closing the backend one)
4. Navigate to the frontend folder and
type:

        npm run serve

## RUNNING ON WINDOWS:
1. Open a new terminal instance
2. Navigate to the backend folder and
type:

        python -m flask run
3. Open a NEW terminal instance (without closing the backend one)
4. Navigate to the frontend folder and
type: 

        npm run lint -- --fix
        npm run serve

---

## Extensions
- eslint
- Intellisense
- Intellisense (Pylance)
- Vue 3 Snippets
- Vue Language
- Python flask
- SQLAlchemy
- flask-sqlalchemy
- flask-migrate
- flask-login
- werkzeug

---

## TESTING:
- [Flask](https://flask.palletsprojects.com/en/2.2.x/testing/)



