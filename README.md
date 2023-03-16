# IBL Mentor Slack Bot

Slack bot developed with slack bolt

## Dependency

- Docker and Docker compose installed

## Define environment variables

Copy from sample variable file and update to suite your environment

```shell
cp sample.env .env
```

## Run Dev

```shell
docker-compose -f docker-compose.yml up -d
```

## Run Prod

```shell
docker-compose up -d
```

````

### Restart Containers

#### Bring down

```shell
docker-compose down
````

#### Bring up

```shell
docker-compose up -d
```

## Configuration

To use this slack bot you need to create an app into https://api.slack.com.

First, you need to login into api.slack.com

### Create Slack App
