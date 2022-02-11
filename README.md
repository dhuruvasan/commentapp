# Comment App

      1. Sign-up where the user will be allowed to enter his emailID and password along
      with a secret code. This data will be validated and sent to the backend where the
      data will be stored in a Database.

      2. Sign-in where the user will be allowed to enter his emailID and password. This
      data will be sent to the backend where it will be  cross-checked with the data
      available in the database and a proper response  is returned to the frontend.

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

# Installation And Run

Developed in vscode using django,

To run clone this repo.

        git clone https://github.com/dhuruvasan/commentapp.git

Use virtual env (or) default python with django installed. use this commend to install it on Terminal.

        pip install django
        pip install django_mysql

next you want to migrate db and models so use this commend to migrate check you are in commentapp folder.

        python manage.py migrate

After migration just run in the manage.py in server to do that use this commend.

        python manage.py runserver

        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).
        February 09, 2022 - 12:41:49
        Django version 3.1.2, using settings 'commentapp.settings'
        Starting development server at
        http://127.0.0.1:8000/

go to the server link.

To chech database folow this link

        http://127.0.0.1:8000/admin

use username:

         dhuruvasan
password:

         dhuruvasan

# Working

sign up page to create a new account has expection handeling

![signup](https://raw.githubusercontent.com/dhuruvasan/commentapp/master/outputimg/Screenshot%20(89).png)

sign in page to sign in with authentication and expection handeling
![signin](https://raw.githubusercontent.com/dhuruvasan/commentapp/master/outputimg/Screenshot%20(86).png)

comment page for create and see a comments

![comment page](https://raw.githubusercontent.com/dhuruvasan/commentapp/master/outputimg/Screenshot%20(87).png)

only shows the users comments when click filter

![user comment page](https://raw.githubusercontent.com/dhuruvasan/commentapp/master/outputimg/Screenshot%20(88).png)

forgot pass word page to enter the email and password

![forgot pass word](https://raw.githubusercontent.com/dhuruvasan/commentapp/master/outputimg/Screenshot%20(90).png)

shows password page after verify your secrect code.

![show password](https://raw.githubusercontent.com/dhuruvasan/commentapp/master/outputimg/Screenshot%20(91).png)

For better UI. kindly use the application with online connections. because I used bootstrap css and js with online links

Is not work
![signup](https://raw.githubusercontent.com/dhuruvasan/commentapp/master/outputimg/Screenshot%20(97).png)
kindly change the settings.py Templates to dirs to the your path of templates (for my it is like('C:\vsc code\zoho projectes\commentapp\comment_app\templates'))

Thank You ZOHO!
