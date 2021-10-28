## Get started

### How to run this project



#### Configure environment variables
Create a **settings.toml** file on the root project and put this variables:
```
[default]
SQLALCHEMY_TRACK_MODIFICATIONS=false


FLASK_ENV="development"


EXTENSIONS = [
    "grpc_server.blueprints.v1",
    "grpc_server.ext.database",
    "grpc_server.ext.commands"
    
]

[development]
SQLALCHEMY_DATABASE_URI= SQL DATABASE URI

```
You can change variables per environment. See more about [Dynaconf](https://www.dynaconf.com/).

Create a file **.env** to store secrets.

```
FLASK_ENV=development
FLASK_APP=grpc_server/app.py
TZ=America/Sao_Paulo

```

#### Run Project

```
docker-compose up --build
```



