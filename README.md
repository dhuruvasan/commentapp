# Comment App

      1. Sign-up where the user will be allowed to enter his emailID and password along
      with a secret code. This data will be validated and sent to the backend where the
      data will be stored in a Database.

      2. Sign-in where the user will be allowed to enter his emailID and password. This
        data will be sent to the backend where it will be cross-checked with the data
        available in the database and a proper response is returned to the frontend.
      3. Forget-password where the user will be allowed to enter the email id and
      secret code. This data will be sent to the  backend and If the data matches with
      any record already in the database then the  password should be shown to the
      user In frontend.

      4. After sign-in the user will be presented with  a text area where he will be able to
      type any comments. After submitting, the comment  will be taken to the backend
      and saved in database.

      5. Below the text area, the user will also see  other users' comments along with
      the respective email ids next to them.

      6. There will be a filter button on click it, the  comment area will show only the
      comments of the logged in user

# Installation

Developed in vscode using django,

To run clone this repo.


        git clone https://github.com/dhuruvasan/commentapp.git

Use virtual env (or) default python with django installed. is not use this commend to install it on Terminal.

        pip install django

next you want to migrate db and models so use this commend to migrate check you are in comment_app folder.

        python manage.py migrate

After migration just run in the manage.py in server to do that use this commend.

        python manage.py runserver

