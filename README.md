# CarRecommendations

CS397A - Predictive Analytics in Python

Fall 2019

Purchasing a new car is one of the most impactful decisions an adult has to
make at any stage of their lives. It is costly, generally requiring you to take out a loan
either through a dealership or a bank, can potentially cost upwards of $30,000, and is
something that would more than likely be kept until it is broken down. These factors put
pressure on the buyer to get the right car, as they would not want to invest a large sum
of money in a product they would not be happy with, as it is used nearly everyday and
will likely last a long time. In deciding what car to purchase, it is apparent that there are
dozens upon dozens of options in between all the brands, and even within the same
brand, that offer different options, trim levels and styling that can often confuse the
buyer.

In addition, when talking to other people about car recommendations, it is very
apparent that people shop on cars based on marketing, brand loyalty, and word of
mouth almost solely. Obviously, the car has to have the features they desire, but people
seem to tend towards brands and models that are recommended through these options.
I wanted to create a tool that expanded a person’s shopping scope by suggesting cars
that are similar in traits to what the person is already considering.

I created a program that was able to recommend cars based on either a given
car model and a model year or given a year, horsepower, number of doors, and MSRP.
To do this, I used NearestNeighbors through sklearn. NearestNeighbors is essentially
the first half of k-Nearest Neighbors, which is one of the more popular predictive analytics methods.
In KNN, we have a training and testing dataset where we essentially
calculate the distance of any given data point to the predicted data point, and use the
k-nearest neighbor’s class value in a majority-vote style method in determining what the
predicted data point should be. When it comes to NearestNeighbors by itself, it is
different in the sense that it is unsupervised and is not trying to predict a specific class
attribute. Here, it is trying to find which K number of neighbors are closest to the
inputted values, and simply returning those values. I chose to use this method as I
determined of all the methods we learned in class, this seems to be the best way of
going about suggestions, as recommendations are generally best when they are close
to a desired product, but not exactly that product. If this program works perfectly, the
outputs would essentially be each brand’s competitors for a given model.

This project was designed as a proof of concept of the idea itself, which is why it lacks the level of polish a full-blown product would have. I plan on expanding on this project in the future by adding additional predictive analytics methods and combining them to get the most accurate suggestions. In addition, I would allow the user to select significantly more options and add different weights to each potential option as well.Lastly, I would want to add a proper UI/UX as opposed to just a script, and further clean up the dataset for the best results.
