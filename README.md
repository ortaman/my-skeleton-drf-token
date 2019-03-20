Test
===========

### Requirements
* [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [docker-compose](https://docs.docker.com/compose/install/)

### Set up development environment
* Open a console and run in the root directory:
```sh
docker-compose up
```
* The application is running on:
```sh
http://localhost:8000/
```

* The admin is running on:
```sh
http://localhost:8000/admin
```
* Login credentials:
```sh
user: admin
password: admin
```

### Tests

*  In the api directory run:
```sh
docker-compose exec web my_app/manage.py test
```
