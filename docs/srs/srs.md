# Software Requirement Specification

### Problem Statement

A common problem when searching for a product on the internet is the oversaturation of the same product on multiple websites. This makes it difficult to find a trustworthy source to buy a product from. In addition, the reviews on a certain product can be dispersed across many different sites, meaning users may be unable to understand the full usefulness of a product. In order to do this currently, users have to do a lot of digging and can get drained very easily. Thus, users who browse for products online need a software application that provides them with a consolidated set of listings and reviews for their chosen product across multiple purchasing websites so that they can make the best decision as to where to buy from and at what price.

### Potential Clients

Online shoppers who are looking to improve their e-commerce experience by saving time and resources looking at duplicate or untrustworthy products.

### Proposed Solution

The creation of an application/website that consolidates the reviews and listings of items across multiple websites and online applications. This site could perform an image scrape of a sample provided by the user (most likely provided by an image on a store), and present to them all the product listings, associated price and customer reviews from multiple large e-seller companies like Amazon, AliExpress, eBay, etc.

### Functional Requirements

#### Must Have

As a user who primarily shops on Amazon, I would like to upload a picture of the product I want so that I can get a list of similar products and reviews from Amazon.

As a user who primarily shops on AliExpress, I would like to upload a picture of the product I want so that I can get a list of similar products and reviews from AliExpress.

As a user who primarily shops on eBay, I would like to upload a picture of the product I want so that I can get a list of similar products and reviews from eBay.

As a user of this website, I would like to view a comprehensive rating for each listing so that I can make the best decision when choosing my product.

As a review-focused user of this site, I would like to see images/videos of the product from users who actually own it.

As a user of this application, I would like to see product recommendations for items from either eBay, Amazon, or AliExpress since these are the most used marketplaces.

#### Nice to Have

As a user who might not be tech-savvy, I would like to be able to see if the product I’m buying is a knock-off of another product.

As a user of this website, it would be nice to be able to view the return policies of each of the retailers selling the product of interest.

As a user who needs assistance deciding which product is the best, I would like to see the ranking of different retailers.

As a user who utilizes multiple different marketplaces, it would be nice to have the website pull similar/same products from various marketplaces.

As a user who isn’t too picky, I would like to see different images that are similar to the sample we are given.

As a user who cares about the workers creating the products, I would like to know which retailers are eco-friendly and promote fair-work policies.

As a user who may be on a timeline, I want to be able to sort by the shipping speed of the product.

As a user who cares about where my product is manufactured, I want to be able to determine the country of origin of a product’s manufacturer.

As a user who cares about how long it takes the website to load, I want commonly searched items/categories to be cached for faster access.

As a user who wants recommendations to be tailored to me, I want to be able to provide feedback in terms of good/bad recommendations which will tune newer recommendations for me.

### Software Architecture:

We plan on implementing a server using either the Flask or Django package in Python. We also plan on using React.js (JavaScript) for the frontend webpage and MongoDB to implement the databases we will need for the images and corresponding posts/reviews. There will be significant client-server interaction involved. The user feeds in an image of the product they are looking for, which is then looked up in the backend database. If the image is found, the corresponding posts are retrieved from the database and presented to the user on the front end in the order of their ranks which are calculated based on product price, the manufacturer, the e-seller company selling the product, etc. If however, the image is not in the database, it is processed and then searched on multiple large sellers’ websites. If the image is a match, a rank is calculated for it and added to a list which stores the corresponding posts for an image. This list is added to the database and then presented to the user on the front end.