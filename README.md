## To run the projet use:
 - docker-compose up

## To make migrations use:
 - docker-compose run web python3 manage.py makemigrations

## To migrate:
 - docker-compose run web python3 manage.py migrate

## To create superuser:
 - docker-compose run web python3 manage.py createsuperuser

## To run pytest:
 - docker-compose run web pytest