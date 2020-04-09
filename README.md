# Podcasts with Django

This is a Heroku-ready website for Developing your own podcasts.

## Default Heroku URL

HEROKU_PROJECT_NAME.herokuapp.com

## Development

    python manage.py collectstatic
    python manage.py makemigrations
    python manage.py migrate

## Prod

    heroku run -a HEROKU_PROJECT_NAME python manage.py compilemessages -l en
    heroku run -a HEROKU_PROJECT_NAME python manage.py collectstatic
    heroku run -a HEROKU_PROJECT_NAME python manage.py makemigrations
    heroku run -a HEROKU_PROJECT_NAME python manage.py migrate
    heroku run -a HEROKU_PROJECT_NAME python manage.py createsuperuser

## Logs

    heroku logs --tail -a HEROKU_PROJECT_NAME

## DB

    heroku pg:copy HEROKU_PROJECT_NAME::DATABASE_URL HEROKU_POSTGRESQL_GOLD_URL -a HEROKU_PROJECT_NAME
    heroku pg:info -a HEROKU_PROJECT_NAME


## Config vars

View current config var values

> heroku config
> GITHUB_USERNAME: joesmith
> OTHER_VAR: production

> heroku config:get GITHUB_USERNAME
> joesmith

Set a config var

> heroku config:set GITHUB_USERNAME=joesmith
> Adding config vars and restarting myapp... done, v12
> GITHUB_USERNAME: joesmith

Remove a config var

> heroku config:unset GITHUB_USERNAME
> Unsetting GITHUB_USERNAME and restarting myapp... done, v13

## Translations


Before making translation
heroku buildpacks:set https://github.com/grauwoelfchen/heroku-buildpack-gettext.git -a HEROKU_PROJECT_NAME

How to make and update new translations

    python manage.py makemessages -l ru

    python manage.py compilemessages -l ru


## To deploy on Heroku just copy static to staticfiles if there is any problem
