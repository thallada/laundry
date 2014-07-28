##GMU Laundry##

A site that scrapes http://gmu.esuds.net and creates a pretty graph of the
current machine usage data for each hall.

This used to be part of my personalsite project (which is a django site), but I
decided to make this it's own website.

##Getting Started##

* Git clone the repo: `git clone https://github.com/thallada/laundry`
* Set-up a database. Create a `secrets.py` file in the `laundry/` folder
  with the following variables set:
  * SECRET_KEY
  * DATABASE_NAME
  * DATABASE_USER
  * DATABASE_PASSWORD
  * DATABASE_HOST
* Modify the `ADMINS` variable in `settings.py` so you get emails when the site
  errors (happens when eSuds changes something on their site).
* Create and activate a virtualenv: `virtualenv venv` and
  `source venv/bin/activate`
* Install the requirements: `pip install -r requirements.txt`
* Run syncdb: `python manage.py syncdb`
* Import the GMU Laundry Hall data: `python manage.py loaddata laundry.json`
* Run the server: `python manage.py runserver`
* Don't forget to set `DEBUG` to `False` when you are production ready.

##Errors##

Whoever is in the `ADMINS` variable in `settings.py` will get an e-mail whenever
an error on the site occurs. This most likely happens when eSuds changes
something on their site that breaks the webscraper (which is in `laundry.py`).

The most often change is that machines are added or removed from halls on the
eSuds website. To fix this issue you will need to manually modify the database
entry for the hall in the django shell. For example, adding a washer to
Whitetop Hall:

`python manage.py shell`

```python
>>> from laundry_app.models import Hall, LaundryMachine
>>> whitetop = Hall.objects.get(name="Whitetop")
>>> LaundryMachine.objects.create(number=10, type=LaundryMachine.WASHER, hall=whitetop)
```

The number is from the eSuds site in the chart for the hall (under the
"Washer #" column).

Sometimes errors happen when eSuds goes down too. Nothing we can really do about
that, but perhaps we can improve our downtime by caching previous results and
showing those in the intrim.

##Backups##

It would be a good idea to periodically dump the database because, right now,
there isn't an automated way of creating the Halls and LaundryMachines. To [save
the
database](https://docs.djangoproject.com/en/dev/ref/django-admin/#dumpdata-app-label-app-label-app-label-model)
run:

`python manage.py dumpdata laundry_app > laundry_backup.json`

You can load a backup with:

`python manage.py loaddata laundry_backup.json`

It would be nice of you to keep the `laundry.json` file in this repo up-to-date
as halls' laundry machine configurations change so that anyone setting up this
application will not have errors upon starting up.

##Todo##

Move away from Django to Javascript. There's no real reason to have a backend
for this site. It can just query esuds and make a chart in D3 or something.
Django is a lot of overhead for such a small site.

Add weekly usage stats. I was in the process of writing this but never finished.
It's a lot more complicated than the current usage stats because a record of
historical queries needs to be kept somehow.

Host this on a SRCT server. Right now it's somewhere that I probably only have
control over and with a database at MIT that I might loose access to eventually.

Make the site more reliable to eSuds changing, like machines getting added or
removed from halls.
