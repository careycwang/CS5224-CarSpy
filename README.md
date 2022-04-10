# CS5224-CarSpy
CS5224 Final Report: CarSpy - An Intelligent Recommendation Platform to find your Dream Used Car in Singapore

You can click [CarSpy Link](https://cs5224-carspy.auth.us-east-1.amazoncognito.com/login?response_type=code&client_id=7i41mg13jhsou7lrkdusc2kp9o&redirect_uri=https://main.d2vgm0hwfxxab2.amplifyapp.com/) to login our website.


## Introduction
This GitHub is for automatic deployment on Amplify.

Our architecture diagram: 

![alt text](./img/Architecture_Diagram.jpg)


Our code files are:
```
CS5224-CarSpy/
|-- README.md

|-- assets/                 
|-- css/
|-- js/
|-- fonts/
|-- media/
|-- images/
|-- index.html
|-- listings.html
|-- listingDetail.html
|-- about.html              # frontend files

|-- lambda/                 # backend files
|-- img/                    # screenshots for our app
|-- data/                   # dataset files and recommendation
|-- cloudformation          # CloudFormation codes
```

## Dataset
We obtain used cars data from Kaggle's [100,000 Singapore Used Car Data set](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes). It contains the scraped data of 100,000 used cars listings, which have been separated into files corresponding to each car manufacturer.

### Steps to Use Our Saas
We already deployed our SaaS application on AWS cloud. You can follow these steps to view our app:
1. Go to https://cs5224-carspy.auth.us-east-1.amazoncognito.com/login?response_type=code&client_id=7i41mg13jhsou7lrkdusc2kp9o&redirect_uri=https://main.d2vgm0hwfxxab2.amplifyapp.com/
2. 

## Contributor
- [Wang Changqin](https://github.com/archiewang0716)
- [Zhang Haolin](https://github.com/A0236053M)
- [Zhang Lei](https://github.com/AronnZzz)
- [Liu Haoyang](https://github.com/Ethan601)
