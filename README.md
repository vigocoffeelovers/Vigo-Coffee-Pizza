# Vigo-Coffee & Pizza
Resolviendo el reto mensual número 11 de mouredev 

https://retosdeprogramacion.com/mensuales2022 

https://go.rviewer.io/dev-buon-appetito-es/?utm_source=mouredev&amp;utm_medium=github_repo&amp;utm_campaign=buon_appetito_mouredev


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the required libraries.

```bash
pip install -r requirements.txt
```

## Usage

First migrate the imported django applications.

```bash
python manage.py migrate
```

Load the static files in the STATIC_ROOT folder.

```bash
python manage.py collectstatic
```

Then create a superuser.

```bash
python manage.py createsuperuser
```

Lastly launch the server with:

```bash
python manage.py runserver #8000 as the default port (any other port will work fine)
```

The admin view will be available at: [localhost:8000/admin/](http://127.0.0.1:8000/admin/)

Remember that this execution is for local testing. For dev you must edit the settings.py, use a web interface and a webserver to retrieve the files.
Learn more about Django deploy [here](https://docs.djangoproject.com/en/4.1/howto/deployment/)


