CSC 450 - 2 Team Project
========================
## Team Members:
Nick, Noah, Jacob, Michael, Matt
## Using
Vue.js 2.7.10 and Python 3.10.7

## TABLE OF CONTENTS:

### First Time Installations:
    - MAC
    - WINDOWS
### Running:
    - MAC
    - WINDOWS
        
## FIRST TIME INSTALLATION MAC:
1. Install Vue.js 2.7.10 and Python 3.10.7 and Visual Studio Code
2. Clone the github repo into your desired directory then open the directory in vscode
3. Open terminal in vscode, navigate to the backend folder and run the following:
    python3 -m pip install flask
    python3 -m pip install flask-cors
4. Run it with:
    python3 -m flask run
5. While keeping the backend terminal instance running, open a NEW terminal instance
6. Navigate to the frontend folder and run the following:
    npm i -g @vue/cli
    npm i --save-dev eslint eslint-plugin-vue
    npm i axios
7. Run it with:
    npm run serve

--------------------------------------------------------------------------------------------------

## FIRST TIME INSTALLATION WINDOWS:
1. Install Vue.js 2.7.10 and Python 3.10.7 and Visual Studio Code
2. Clone the github repo into your desired directory then open the directory in vscode
3. Open terminal in vscode, navigate to the backend folder and run the following:
    python -m pip install flask
    python -m pip install flask-cors
4. Run it with:
    python -m flask run
5. While keeping the backend terminal instance running, open a NEW terminal instance
6. Navigate to the frontend folder and run the following:
    npm i -g @vue/cli
    npm i --save-dev eslint eslint-plugin-vue
    npm i axios
7. Clean up the incorrect End of Line characters with:
    npm run lint -- --fix
8. Run it with:
    npm run serve

--------------------------------------------------------------------------------------------------

## RUNNING ON MAC:
1. Open a new terminal instance
2. Navigate to the backend folder and type:
    python3 -m flask run
3. Open a NEW terminal instance (without closing the backend one)
4. Navigate to the frontend folder and type:
    npm run serve

## RUNNING ON WINDOWS:
1. Open a new terminal instance
2. Navigate to the backend folder and type:
    python -m flask run
3. Open a NEW terminal instance (without closing the backend one)
4. Navigate to the frontend folder and type:
    npm run lint -- --fix
    npm run serve

--------------------------------------------------------------------------------------------------

## Extensions
    eslint
    Intellisense
    Intellisense (Pylance)
    Vue 3 Snippets
    Vue Language





