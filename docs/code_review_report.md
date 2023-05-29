###Contributors: Peter, Sabrina, Vasant, Aryaman, AB, Jose, Karry
## Design
We have designed our application using a Django framework, which has allowed us to take advantage of the built-in functions
offered by Django to enhance features such as connecting to our databases to display information and data to the front-end application.
During our development process, we have consistently refactored our code in order to make sure that the classes have
single or few responsibilities (Single Responsibility Principle) to remain highly cohesive. One issue that we encountered was high coupling
and dependencies between classes due to the need to import modules to make functions such as our algorithm run. We have attempted to mitigate these issues 
but concede that there may be more coupling than desired. We also followed the Dependency Inversion Principle to make sure that our
high-level classes do not have to change due to changes in lower-level classes or databases. We have made sure to take advantage of using generalized
models in Django and make the appropriate migrations to update the type of information we want to store inside the database.
Thus, we can alter the type of information we want to store about a particular user and make the appropriate updates to the database to 
reflect the input that we will be collecting. 

We created a Django application called scheduler within the eventPlanner folder. Within the scheduler application, we included 
a support folder that contains files such as algorithm and ticketmaster that are used to power the functionality of our app. We also included 
static and template folders that contain the files for our styling and front-end aesthetic. We plan on adding additional javascript files to add some dynamic elements to each of the HTML templates.

A problem we also ran into was with our deployment. We had trouble with permissions with the provided GitHub repository, which prompted us to create new repositories for our deployment. This helped with a myriad of deployment issues, but we ran into problems with the naming of these repositories. Something that we believe should be inspected for future reference is the permission status of assigned repositories. It could be an outlying case that we weren't able to directly deploy to Heroku from the repository the first time, but it could pose problems for groups in the future.

## Complexity
We believe that our code could be improved to be made simpler in our algorithm functions and use of API functions. We experienced
a sudden change in API keys due to changes from one of the providers we used, which is one reason that we were not able to simplify the
files that relied on these keys, as we needed. Additionally, the indexing of our algorithm could be improved since we shift the indices a considerable
amount of times, and we can better encapsulate this. If a developer were to review our code and use it in the future, I think they
would be able to understand how to use the code as long as the install all of the requirements from requirements.txt and follow 
the comments we provide about extended functionalities such as celery. 

## Tests
We do not have any tests right now in the application, but we can implement Django unit testing. We plan on adding extensive unit tests for each of the views soon.

## Naming    
We have appropriately named our classes to reflect their intentions and/or what they represent. We tried to remain 
consistent in naming for API keys that were needed to extract information. However, we could definitely improve on function naming and variable naming clarity, particularly in our algorithm.py file. This file, in particular, has relatively confusing naming due to having multiple versions of one function for debugging purposes and due to algorithm changes (each time we changed the algorithm, we would often create another function with a similar name to the previous version of the function). In additon, we did run into issues with the clarity of certain file names, such as the Events.py file containing an Eventfinder class. These issues are slightly mitigated in so far as the similarities between the real file name and the interior match up slightly, but the main issue is that the classes overall suffer from naming issues. Our variable naming in certain files such as the files that work directly with the API's contain good variable naming practices. We clearly have each attribute of an object named such that there is no confusion when working with these directly.

## Comments
The comments that are found throughout our code are useful when they exist and provide information about the certain dependencies. Right now, the most
useful comments are for our celery.py file which is a python extension that we are using to refresh our database on a timely basis, such as every 12
hours. However, many classes lack comments and a lot of our code is very hard to read; we need to add comments for functions regarding expected input and expected output (especially what we return in case of error). This issue is especially egregious since we are coding in python where the inputs and outputs could be of any type. This is something we definitely need to fix. In terms of commenting, algorithm.py requires a lot more commenting to explain code designs, input/output limitations, and generally provide clarity. views.py could also use more commenting since it is very difficult right now to figure out what each endpoint corresponds to based on naming alone; simple comments like "home page for website" or "redirects user to profile settings" could provide a lot of clarity and insight into the structure of our webpage.

## Style
Our code follows good programming practices for the most part since we have restructured numerous times to fulfill good Django practices. Django has a lot of built-in features like its usage of Models when dealing with databases which helped us in maintaining good object-oriented design principles. We attempted to adhere to appropriate design principles as much as possible such as the Open-Closed principle with the Yelp and Ticketmaster classes being integrated by a class eventfinder. We also organized files into folders based on their relevance to each other, such support and templates. However, we need to do a lot of refactoring especially in algorithm.py. Repeated changes in our databases/models classes led to our algorithm.py having to make a lot of adaptations and while we already completed one large refactor to minimize data clumps, the addition of new features (such as accounting for travel time and distances when recommending events) have led to more necessary parameters to functions causing new data clumps we have yet to address. We also have a good amount of duplicate code in algorithm.py due to bugs we ran into which should be addressed (also part of our we need to add more comments issue). views.py also has very long methods which we need to clean up. Part of this is due to the fact that we have not yet settled upon our overall website structure yet and are still making major revisions but with the deadline coming up, we definitely need to refactor this file. 

## Documentation
We provide documentation about how to install required dependencies (and how to run the server locally by setting a local postgresql database) in the README and all other required dependencies should be included in our Pipfile and Pipfile.lock. Downloading our code and initiating a pipenv shell should install all necessary dependencies (other than the manual steps required to a set up a local postgresql server; this is only an issue for running the code locally and not for deployment however). Admittedly, we should probably clean up our Readme in terms of unnecessary pip installs since our Pipfile should handle all of these at this point.

## Error Checking
In our views.py for example and across the codebase such in the models.py as well, we made sure to properly check for errors and throw/raise the appropriate exceptions and inform the users of their mistake. This enables both contributors and users to be aware of any arising problems and take action to either re-enter the input correctly or for the contributors to know the source of the problem and begin debugging properly. We also made sure, to print appropriate messages to the console and render the html on the page. 
