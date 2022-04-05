# Mini quiz demo

Created as project for Code Bootcamp Häme 2022 course.

# Description:

Simple quiz application made using Python Flask and Jinja2. 

App includes:

- Login page (password = "bootcamp")
- Quiz page
- Results page, with user's name and results being uploaded to remote database and leaderboard displayed on browser.  

# How To Run application:

1. Install virtualenv:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ source /env/Scripts/activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default.

