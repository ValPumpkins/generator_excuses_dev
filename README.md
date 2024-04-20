<img src="https://i.imgur.com/fftqmuR.png" alt="repo title : Les excuses de dev" width=100%/>

## 📍 INTRODUCTION

**Les excuses de dev** is a project carried out as the entrance test for the **ForEach school**

It's a **random generator** of funny excuses for web developers

## 🔗 LINK
You can find the deployed project by clicking on the link below :

**[valentine.electrikbox.fr](http://valentine.electrikbox.fr/)**

You can also install it locally by following these steps

## 🏠 LOCAL INSTALLATION

This project consists of a :
- **BACKEND** developed on the micro framework **Flask** in <img src="https://i.imgur.com/dSF9etv.png" alt="python-logo" width="20" height="20" /> **Python**

<br>
<img src="https://i.imgur.com/V7x5vcJ.png" alt="flask-logo" width="100%" />
<br>
<br>

- **FRONTEND** developed with the library **React** in <img src="https://i.imgur.com/ZFMpiKH.png" alt="javascript-logo" width="20" height="20" /> Javascript

<br>
<img src="https://i.imgur.com/VL4KcRo.png" alt="react-logo" width="100%" />

### ⚙️ Backend

First, clone this repository :
```
git clone https://github.com/ValPumpkins/generator_excuses_dev.git
```
Then, go to the backend file :
```
cd backend
```
And create a new virtual environement :
```
python3 -m venv .venv
```
Activate it :
```
source .venv/bin/activate
```
and install the requirements :
```
pip install -r requirements.txt
```
**Note** : to close your virtual environement : `deactivate`

#### 🗂️ Database
The database used for this project has been createtd using <img src="https://i.imgur.com/EisNrxL.png" alt="sqlite logo" width="50" height="30" /> **SQLite** and can be found in the `db` directory

#### 🚀 **LAUNCH SERVER**

Finally, launch the **Flask server** with this command :
```
python3 app.py
```
### 🚕 API ROUTES
API routes are available on your http://localhost:5000/

For example : http://localhost:5000/api/excuses will show a list of all the excuses available in the database and http://localhost:5000/api/random will give you a random excuse each time you refresh the page.

If you want to test http://localhost:5000/api/create (route to create a new excuse), you can go to the `test.rest` file and click on *Send a request* on the second example (you can change the excuse if you want, the excuse will be saved in the db)

### 🪞 Frontend
Now, you can move to the frontend file :
```
cd frontend
```
(assuming you're back at the root of the "*Excuses-dev*" project)
and install all the dependecies :
```
npm install
```
#### Then 🚀 **LAUNCH** :
```
npm start
```
The project is now available on http://localhost:3000/

## 🎯 USAGE & PAGES

On the **Main page** :
- http://localhost:3000/ or
- http://valentine.electrikbox.fr/

you can perform two actions: click on the 🌺 **pink button** and randomly browse through new excuses, or click on the 🟢 **green button** and create a brand new excuse of your own (the newly created excuse is immediately available)

On the **Lost page** :
- http://localhost:3000/lost or
- http://valentine.electrikbox.fr/lost

enjoy a little gif before going back to the main page

On the **Http_code page** (you must put a 3-digit number after the url), ex :
- http://localhost:3000/738 or
- http://valentine.electrikbox.fr/738

you'll see the excuse(s) corresponding to the code in question

Finally, if no page matches, you'll get the famous **404 page**, ex :
- http://localhost:3000/help or
- http://valentine.electrikbox.fr/help

## 📬 CONTACT
- 🥦 Valentine Pumpkins -- [GITHUB](https://github.com/ValPumpkins) | [LINKEDIN](https://www.linkedin.com/in/valentine-quignon/)
