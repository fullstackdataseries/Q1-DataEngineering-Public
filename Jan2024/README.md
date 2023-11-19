# Class 1 Data Engineering -- Getting Started

## Tuesday, January 30th, 2024

## Objectives for today
- Cover basics of Docker
- Learn about Docker Compose
- Start our Docker Compose services
    - Really grasp what's going on inside of these

## Tools we will need for this week:
- Docker (with Docker compose)
    - I use Docker Desktop to manage most things

## Docker Compose

### Docker Compose Components
- Inside of Docker-Compose:
    - [Postgres + Mage Docker Compose](https://docs.mage.ai/guides/docker/connecting-a-database)
    - Mage
        - Pipeline Development
        - Competitors: Airflow, Prefect
    - PostGres
        - Database for stateful operations
        - Competitors: literally any relational DB


### Starting Docker Compose

- cd into root dir
- make sure docker is running on your machine
- `docker-compose up -d`

You'll then see that your service has started for Mage.
I'm sticking to the Mage UI for this but all of what we're doing is possible via VSCode, also. It just doesn't feel as intuitive as the UI does.


### Now what?

- Try logging into Mage and building an example pipeline.
    - Next month we are going to focus on building the pipeline with things like:
        - Conditional blocks, Dynamic blocks, and Reducing Output to overwrite Postgres Database

    - Data Engineering Concept:
        - Struct/Array Types in Colums

- If you don't want to use the API we are using (MLB Stats API) in class, make sure you pick an API by next time and start trying to learn about it before then
    - Make sure it has at least 1 complex data type in the response when you convert it to a DataFrame if you want to fully follow along next month
    - If not, that's okay, you can observe that part in the lab next time


### Mage Resources

- [Slack Channel](https://www.mage.ai/chat)
- [Matt Palmer, Documentation Creator](https://www.linkedin.com/in/matt-palmer/)
- [Mage Docs](https://docs.mage.ai/)