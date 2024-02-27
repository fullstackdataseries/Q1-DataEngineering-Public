# Data Engineering: Data Modeling

## January 30th, 2024

## Objectives for today
Learn! We will be talking about Fact/Dim Data Modeling.

## Tools we will need for this week:
- Python
- duckdb

## PPT for the Lab
[Canva PPT for Todays Session](https://www.canva.com/design/DAF6qdYt1uI/EDC80b79R8FiUZ7HNi6_ig/view?utm_content=DAF6qdYt1uI&utm_campaign=designshare&utm_medium=link&utm_source=editor).

## A little about the Lab
We are going to follow Kimball/STAR schema modeling to take raw data from a PoS Ecommerce System into a modeled (goal is 3NF) environment that covers the landing and staging layers of our environment.

We are also assuming ELT here, as storage is cheap but networking is expensive. So, we load the data into a landing zone and then stage it following our data model. We normally would design this data model before beginning to code, but here we do it while coding as we go discovering the data for agility sake (normally you would analyze the data, understand the business requirements, and design a data model to fit the two)




## Now What?
- Read "The Data Warehouse Toolkit: The Definitive Guide (3rd edition)" by Ralph Kimball
- Kimball Data Modeling is what it's referred to (this fact/dim type approach), you can continue diving in, as well as learning more about Inmon/OBT, and other types of non-relational modeling even like Graph Databases and NoSQL databases.