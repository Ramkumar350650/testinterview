# testinterview
Welcome to blog application.

created environment variable name env

Activate ENV:

./env/scripts/activate

Start Projects: application 

python manage.py runserver 

home page:

login and logout buttons available.

user:ramkumar
password:Sriram@2024


home page:

http://127.0.0.1:8000/

login and logout url:

http://127.0.0.1:8000/accounts/login/

http://127.0.0.1:8000/accounts/logout/

Note:separate buttons available.

Swagger Access URl:

http://127.0.0.1:8000/generic/

create api and access token .

JWT Token Creation and Refresh :


http://127.0.0.1:8000/auth-jwt/

http://127.0.0.1:8000/auth-jwt/auth-jwt-verify/

auth-verification:

http://127.0.0.1:8000/auth-jwt-verify/


list of application URL and front end UI :


    http://127.0.0.1:8000/about/

    http://127.0.0.1:8000/post/(?P<pk>\d+)$'
    http://127.0.0.1:8000/post/new/$
    http://127.0.0.1:8000/post/(?P<pk>\d+)/edit/$
    http://127.0.0.1:8000/drafts/$
    http://127.0.0.1:8000/post/(?P<pk>\d+)/remove/$
    http://127.0.0.1:8000/post/(?P<pk>\d+)/publish/$
    http://127.0.0.1:8000/post/(?P<pk>\d+)/comment/$
    http://127.0.0.1:8000/comment/(?P<pk>\d+)/approve/$
    http://127.0.0.1:8000/comment/(?P<pk>\d+)/remove/$
    http://127.0.0.1:8000/auth-jwt/
    http://127.0.0.1:8000/auth-jwt-refresh/
    http://127.0.0.1:8000/auth-jwt-verify/
    http://127.0.0.1:8000/generic/$
    http://127.0.0.1:8000/detail_post/
    http://127.0.0.1:8000/detail_post/$


Admin interface :

    http://127.0.0.1:8000/admin/



user:ramkumar 

password:Sriram@2024

Database data added directly.already created superuser:


if need any column following steps:

added column name model.py and using python manage.py makemigrations and python manage.py migrate.


core header added base upon your host and port .you added host .allowed host name.if you required curd opertation enable to settings.py allowed api menrthods.


Everything tested and working fine.


activate env and finally deactivate.
