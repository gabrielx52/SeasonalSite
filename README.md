# SeasonalSite
Django web app used to track seasonal produce based on location

# Getting started:
1. Install necessary packages using:
    pip install requirements.txt
    
2. Create the database structure:
    ./manage.py migrate
    
3. Migrate from any previous database structure versions (if necessary):
    ./manage.py makemigrations
    
4. For testing, load the test database fixture so there is data to test with:
    ./manage.py loaddata test_produce

5. To start the server:
    ./manage.py runserver

6. The site will run locally @ http://localhost:8000/
