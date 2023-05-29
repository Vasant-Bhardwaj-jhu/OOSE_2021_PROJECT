# EventFul

## Deployment URL:
https://eventful-group-8.herokuapp.com/login

## Built With

Django


## To run server locally:

NOTE: YOU WILL REQUIRE PYTHON 3.10 IN ORDER TO MAKE PIPENV WORK CORRECTLY. You can download python 3.10 from https://www.python.org/downloads/

pip install pipenv

pipenv install

pipenv shell

brew services start postgresql

python manage.py makemigrations

python manage.py runserver

## How to create local postgres database

For Mac Users:

brew install postgresql

brew services start postgresql

psql postgres

Now within postgres terminal:

CREATE DATABASE eventplanner;


## Application Explanation

For this application, a user will be able to search for events based on their location and the amount of free time they have available. We are using the Yelp and Ticketmaster APIs to get a list of available events given the schedule of the user. As a user of this product, you will be able to have a list of recommended events to attend and be able to sort the events by category and other features. Our recommendation system will prioritize the events based on the user's preferences which type of event and distance between successive events. 

Currently, our Beta release has been significantly updated from our previous iterations to allow users to have a more aesthetic and user-friendly experience when using the app in order to see either a list of events or get an optimized schedule. We have successfully implemented the Ticketmaster and Yelp API in order to gather an extensive amount of events that a user can attend, and we are able to create an optimized scheudle based on preference and distance between events that makes sense for the user. 

## Getting started

Note: we changed our master branch recently (and renamed this new branch to master). Our previous commits/history is on the branch "old-master" while all our current and future work is on "master".

## If not every installed, install:

` pip install python-dateutil ` (note: you may need to specify which python version you want to install `python-dateutil` on. For example, in my case, I was running Python3.10. So I did `python3.10 -m pip install python-dateutil`)

To install the project dependencies, from the root directory, eventPlanner, run the following command (Note that you might need to create a new virtual environment and activate it before installing the packages. For more information, refer to https://docs.python.org/3/tutorial/venv.html):

`pip install -r requirements.txt`


## Running the Program

git clone https://github.com/jhu-oose/2021-fall-group-group8.git and wait for authorization if not granted already

First, you must navigate to settings.py and check for the TIME_ZONE parameter. In order to see the list of events with the proper time format,
you must change the variable to reflect the timezone you are currently in. A list of acceptable variations can be found
here: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568

You need api keys to access information used in our program and set these values as environmental variables

You can receive an API Key for Yelp and more information at https://www.yelp.com/developers/documentation/v3/authentication

You can receive an API Key for MapQuest and more information at https://developer.mapquest.com/plan_purchase/steps/business_edition/business_edition_free/register

You can receive an API Key for TicketMaster and more information at https://developer.ticketmaster.com/products-and-docs/apis/getting-started/

Put all 3 API keys into a file named `.env` (note the dot in the file name) inside the root folder of the project, eventPlanner, in the exact format shown below:

`YELP_API_KEY=your_yelp_api_key`

`MAPQUEST_API_KEY=your_mapquest_api_key`

`TICKETMASTER_API_KEY=your_ticketmaster_api_key`

If for some reason the process outlined above does not work, insert the API keys into the following files as hard code.

The YELP_API_KEY should be put into `eventPlanner/scheduler/support/yelp.py` at the key variable (this has a TODO on it)

The MAPQUEST_API_KEY should be put into `eventPLanner/scheduler/support/travel.py` (this has a TODO on it)

Use of the TICKETMASTER_API_KEY is not functional at this point so no action needs to be taken for this API key.

Finally, run the following commands from the eventPlanner directory:

`python manage.py makemigrations` (Commit the latest changes made to the databases)

`python manage.py migrate` (Push the latest changes to the databases)

`python manage.py runserver` (Start up the localhost server, click the provided link.)

When searching for events, our current constraint is that you can only search for events in the state of Marlyand. This is because we have not yet found a robust way to store events that are outside of the state of Maryland.

When searching, we have also implemented two options for users to get events. The schedule button allows for users to receive a schedule of events, while the events button lists out general events the user can attend to. 

Sentence case for the City parameter means that the city needs to begin with a capitalized letter and the rest lowercase. For example, "Baltimore" is considered sentence case. 

## Roadmap

* We have also improved our algorithm to get a better schedule for users that can be optimized by distances between next events

* We have updated our application to allow events to be filtered by category, and hope to expand this functionality

* We have successfully updated our user interface to be more aesthetic and take advantage of stylesheets to look more user-friendly

* We still want to expand our login features in the future by using Google authorization and/or letting users login with either a username or email

* We also hope to add more functionality a Google Places API in order to suggest more events to users in between events found by the Yelp and Ticketmaster API


## Contact
* If you have any questions or concerns, you can reach the project link at https://github.com/jhu-oose/2021-fall-group-group8.git.

* If you would like to speak to one of the team members, feel free to email at pnovell1@jhu.edu

## Acknowledgements
* We would like to acknowledge the contributions of each of the team members in coming up with the design of the project and sharing their ideas on how to constantly improve the application.

* We received assistance by watching publicly available videos of the course: CS50's Introduction to Web Programming with Python and Javascript offered by Harvard University
