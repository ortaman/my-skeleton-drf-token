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
docker-compose exec web coverage run --source='.' my_app/manage.py test my_app
docker-compose exec web coverage run --source='./my_app/users' my_app/manage.py test users
docker-compose exec web coverage report

```

* Or in you python environment run the following from your project folder containing manage.py:
```sh
coverage run --source='.' manage.py test        # run the project tests
coverage run --source='./users' manage.py test  # run the users app tests
coverage report                                 # show a report in the terminal
```