# colibri-proxy
A simple proxy server that adds JWT with certain claims

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


# Installation
### Docker installation
```sh
$ make build-docker && make run-docker
```
### Local installation

- Install [Redis](https://redis.io/download) on local machine
- Create or copy env file in /src folder

```sh
$ cp .myenv.example src/.myenv
```


- Provide your Redis host, claims and your upstream URL

`src/.myenv`
```txt
. . .
UPSTREAM_URL=<...>
REDIS_HOST=localhost
```

Install dependencies
```sh
$ make build
```

Then, start the server
```sh
$ make run
```
You can specify a port of your server as well (8080 by default)
```sh
$ make run HTTP_PORT=8000
```
