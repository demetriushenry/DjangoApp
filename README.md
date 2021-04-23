# DjangoApp

## Python Django Rest Framework Test

### Environment vars

1. Create the .env file in the root folder with the followings:
    ```
    DEBUG=0
    SECRET_KEY=<generated-django-secret-key>
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=djangoapp
    SQL_USER=djangoapp
    SQL_PASSWORD=<database-password>
    SQL_HOST=db
    SQL_PORT=5432
    DATABASE=postgres
    ```
    Change all the variables with "<>"
1. Create the .env.db file in the root folder with the followings:
    ```
    POSTGRES_USER=djangoapp
    POSTGRES_PASSWORD=<database-password>
    POSTGRES_DB=djangoapp
    ```

### Using Docker to run the application

Build the imagens and up the containers

    ```
    $ docker-compose up -d --build
    ```

Check whether the application is running or not with:

    ```
    $ docker ps
    ```

3 containers must appear in the list

Now it is necessary to run the script for creating the migrations in the django container, generate your static files and, finally, generate a super user to serve as an administrator:

    ```
    $ docker-compose exec api ./init-prepare.sh
    ```

### Testing
    
Test it at [http://localhost:1337/admin/](http://localhost:1337/admin/). The application uses **Nginx** to serve the static files and **Gunicorn** to run the Django app.

## Unit Tests

If you want to run the unit tests, run the following command:

    ```
    $ docker-compose exec api python manage.py test
    ```