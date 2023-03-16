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
docker-compose up -d
```

## Run Prod

```shell
docker-compose -f docker-compose-prod.yml up -d
```

### Restart Containers

#### Bring down

```shell
docker-compose down
```

#### Bring up

```shell
docker-compose up -d
```

## Configuration

To use this slack bot you need to create an app into https://api.slack.com.

First, you need to login into api.slack.com

### Create Slack App

Once logged in, go to "Your apps" option
![Your apps option](/img/your-apps-option.png)

Then, select From scratch option
![Create Slack App](/img/create-slack-app.png)

After that, set the app information
![Set app name](/img/set-app-name.png)

Finally, install the app in the workspace
![Install app](/img/install-app.png)

## Setup Slack App

Once the app is created you need to select "Bots" option in the next window.
![Slect bots option](/img/select-bot-option.png)

Then, in "Basic Information" get the "Signing Secret" value and paste it in the `.env` file
![Get signing secret](/img/get-signing-secret.png)

Now, set the app icon, preview color and description
![Set app info](/img/set-app-info.png)

After that, go to "OAuth & Permissions" to get "Bot User OAuth Token" and paste it in the `env` file
![Get bot auth token](/img/get-bot-auth-token.png)

Next, set the app scope
![Set app scope](/img/add-scope.png)

Following, go to "Event Subscriptions" option and set the URL and the bot events
![Set request url](/img/set-request-url.png)

Finally, go to "App Home" option and activate the following options
![Set home options](/img/set-home-options.png)

```

```
