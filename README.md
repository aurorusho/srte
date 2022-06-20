# SRTE Project
### Note: This was one of my first projects, so the code may be difficult to read.
This is a website that can be used to study for written expression questions in the TOEFL exam.

You can clone this project in your local machine by:
```
$ mkdir srte-project
$ cd srte-project
$ python3 -m venv venv
$ . venv/bin/activate
$ git clone https://github.com/aurorusho/srte.git
$ cd srte
$ pip install -r requirements.txt
```
Now, create a file named scripts/wriexp.txt
### Note: I don't include this file in the repository because I am not the owner of any of the exercises I used when creating the website

This file needs to have a certain format: 

For example, this exercise 

![alt text](https://github.com/aurorusho/srte/blob/main/example.png?raw=true)

Would become
```
Without alphabetical order, _dictionaries_ would _be_ _impossibility_ _to#use_
C
```
The possible answers should start and end with an underscore.
The line next to the question should be only the letter of the answer (A, B, C or D)

As the regex used by the script uses the spaces to know which words are the possible answers,
if an answer has spaces between, they should be replaced by #

To add multiple questions, it is enough to make something like:
```
Without alphabetical order, _dictionaries_ would _be_ _impossibility_ _to#use_
C
The _research_ _for#the_ book Roots _taking_ Alex Haley _twelve#years_.
C
```


Now only run
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runscript insert_we.py
```
And start the server any time by running
```
$ python3 manage.py runserver
```

## If you want deploy this project, make sure you change the SECRET_KEY in settings.py
