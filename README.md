# landerr

## What does this do?

It builds a very basic HTML landing page that contains links (passed in via an environment variable) and serves them.

Designed to fit elegantly into a `docker-compose.yml` file.

You can customize the template yourself

## Usage

Example `docker-compose.yml` file:

```
services:
  lander:
    image: landerr
    container_name: landerr
    restart: always
    ports:
      - 80:80
    volumes:
      - ./template:/usr/src/app/template
    environment:
      CONFIG: |
        site-name: Landing Page
        footer: A dockerized landing page with bootstrap framework
        links:
          - name: Service 1
            text: This is my first Service. 
            href: https://www.google.com/
          - name: Service 2
            text: My second Service. 
            href: https://reddit.com/
```

As you can see, just populate the `CONFIG` environment variable with a `YAML` string.

## Configuration

- `./template:/usr/src/app/template` mount the template folder as you like
- `site-name`: the `<title>` value of the HTML document.
- `footer`: the footer of the document.
- `links`: a `YAML` array of items each containing both a `name` (link value), `text` (as description) and `href` (link target).

## Customize template

Custom your `template.html` as you like inside your template folder.

To change template:
- Stop container
- Update your `template.html`
- Start container

## Docker Build

Build and run the docker image.
```
docker build -t landerr .
docker compose up
```

## Docker Hub image

You can find a prebuild docker image here: [docker/mrlittle113/landerr](https://hub.docker.com/repository/docker/mrlittle113/landerr)

Change the image in docker compose to:
```
image: mrlittle113/landerr
```

## Forked 
This repo is forked from https://github.com/chris2k20/simple-docker-lander 

Origin repo: https://github.com/benletchford/simple-docker-lander

Thank you for your work! :) 