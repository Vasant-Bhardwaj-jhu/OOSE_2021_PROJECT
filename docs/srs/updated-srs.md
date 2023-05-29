# Software Requirement Specification

### Problem Statement:

There already exists quite a few websites/apps that recommend local events one can go to. However, I have not yet seen any of these websites/apps consider availability of transportation (there is an implicit assumption you can just drive there) or offer any kind of scheduling service (such as recommending a list of events that fit within a certain timeframe). Despite the number of sites like Eventbrite, there is still a lack of coverage for people who may not own a car (or have easy access to transportation) and for people who struggle to plan out a series of interesting activities.

### Potential Clients:
People who want to attend/find new local events but do not have (consistent) access to a car or would prefer to take public transportation.
People who find it hard to schedule out things to do within a period of time (accounting for things like transportation time, cost, etc.) → Example: Person A has 10 hours free today and is interested in going to X location but only plans on spending 2 hours at X location; Person A would like to spend all 10 hours of his/her time doing interesting things/visiting interesting places.


### Proposed Solution:
It would be interesting to design a piece of software that combines looking for local events to go to, recommending events based on how convenient (and how costly) it would be to get there (ex: it only recommends local concerts that you can easily reach by taking a local bus rather than concerts far away that would force you to Uber/drive, etc.), and offering a recommended itinerary for longer periods of time (Ex: offering you an itinerary for things to do on your day off).

### Must Have:
- As a someone trying to find new activities to do, I want to be able to view local events so that I can learn about things I am interested in attending.
- As a user of the app who enjoys Yelp, I want to be able to get all events in a certain time frame
- As a user of the app who enjoys TicketMaster, I want to be able to get all events in a certain time frame
- As a user of the app who also uses Yelp and just wants to browse, I want to be able to get all events at a certain location after a certain date
- As a user of the app who also uses TicketMaster and just wants to browse, I want to be able to get all events at a certain location after a certain date
- As a user of the app, I want to be able to sort events by date because then I can better schedule my time /ability to go to these events.
- As a user of the app, I want to be able to sort local events/happenings by category because this would allow me to narrow down things I am interested in.
- As a user of the app, I want recommendations for a set of events within a given time frame that I provide
- As a user who is limited in time, I want a set of recommendations which account for travel time and distance
- As a user with an account, I want some kind of encryption for the passwords I provide



### Nice to Have:
- As a user who frequents the site, I want some kind of cache so that searches I frequently make take less time to process
- As a user who cares about personalization, I want the recommendations to be personalized to me and I want control over how the recommendations are tailored
- As a user who struggles with planning out an itinerary, I want the app to give me a recommended itinerary based on things I’m interested in, transportation options, and time limitations (when things are opened/closed, how much time I have, etc.)
- As a user of the app, I want to be able to integrate my calendar so that only events that fit into my schedule will be recommended.
- As a user of the app, I want to be able to see local transportation options to and from these events because this would help me in being able to go to these events.
- As a budget-conscious user of this app, I want to be able to sort local transportation options by cost because this would allow me to evaluate the cost of my trip.
- As a user of the app, I want a sign/log in so that I can save events I like for easier time finding in the future
- As a practical user of the app, I want local weather to affect the recommendations I get from the app
- As a social user of the app, I want to be able to use this app with a group of friends and get recommendations for all of us


### Software Architecture:
It will most likely use a client server architecture. When a user enters their location, a request is sent to the server application to look for events that are marked as being in the same location (for example, if a user enters “Baltimore” then events tagged with the location “Baltimore” will be returned). This query will be executed and the matching results will be sent back to the user. Similar procedures will occur when users attempt to search for events on a certain day/time.
As for the transportation features, this may require the usage of something like Google Maps/Routes API. Given a user’s imputed location and the known location of the event, an HTTP request can be sent to get JSON/XML instructions in return which will then be formatted in a coherent manner before being returned to the app’s user.
