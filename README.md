### Requirements
> [Docker Desktop](https://docs.docker.com/get-docker/)

### Set-up Instructions
This project is already fully configured to launch. You will only need to have docker installed on your system.

Clone this repository, navigate into the root directory, and boot up using `docker-compose up weather`. This command will pull the base python image, install requirements, migrate and launch the local server.

```
TODO:
To run the tests, open a second shell and use the `docker-compose exec weather bash` command to enter the running container. Then run the tests with `./manage.py test -v 2`.
```