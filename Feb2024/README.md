# Class 2 Data Engineering -- Building our Pipeline

## Objectives for today
- Build!
    - We covered Docker and Docker Compose last month, we will rely on that

- Complex Data Types in Columns
    - Array/Structs as Column Types


## Tools we will need for this week:

- Docker (with Docker compose)
    - I use Docker Desktop to start up Docker on my computer and see what I have running, it's easy this way but the Docker CLI is very important to know how to use

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


### Now What?

- Finish the pipeline! And try to understand what's happening in Mage blocks, and add in complexities if you can. Understanding pipelines, DAGs, and orchestration is huge for a Data Engineer

### Next Time

- We will talk higher level about Data Modeling, it might be less hands on, but just as important.
- We will talk about Dim/Fact Data Modeling, and why it's important for Data Engineers to have familarity with both, and how they're different.
