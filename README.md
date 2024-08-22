# mdn-django-diyblog
DIY mini blog website written in Django - [MDN Django Assessment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog#steps_to_complete)

To get this project up and running locally on your computer: \
Set up the Python development environment, then run the following commands:

```console
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py test # Run the standard tests. These should all pass.
python3 manage.py createsuperuser # Create a superuser
python3 manage.py runserver
```
Open a browser to http://127.0.0.1:8000/admin/ to open the admin site \
Create a few test objects of each type. \
Open tab to http://127.0.0.1:8000 to see the main site, with your new objects.
