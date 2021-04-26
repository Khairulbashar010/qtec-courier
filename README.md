# Project Setup

I hope you have virtualenv and MySQL installed in your machine. Activate a virtual environment or create a new to run this project.<br/>
After starting your virtual environment clone the repo to your desired location.<br/>
cd to qtec-courier and run `pip3 install -r requirements.txt` in linux or `pip install -r requirements.txt` in windows.<br/>

# Database Setup
Look for `DATABASES` in the `settings.py` file and create a database acordingly.<br/>
If you want to use postgreSQL the set the firstline of `DATABASES` to `'ENGINE': 'django.db.backends.postgresql',` and the last to `'PORT': '5432',` ( Change port to your machine's port)<br/>
Run the following commands to migrate (For Linux): 
`python3 manage.py makemigrations`<br/>
`python3 manage.py migrate`<br/>

Run the following commands to migrate (For Windows): 
`python manage.py makemigrations`<br/>
`python manage.py migrate`<br/>

# Superuser Setup
Now that our database is ready, we can add our superuser to the app.<br/>
Run `python3 manage.py createsuperuser` in linux or `python manage.py createsuperuser` in windows and fillup the credentials.<br/>

# Run Project
Run `python3 manage.py startserver` in linux or `python manage.py startserver` in windows to start the dev server.<br/>

# Note
If you still get errors then you probably missed a point. Check everything again and run.



