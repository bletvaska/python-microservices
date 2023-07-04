# URL Schema Aplikacie

navrh schemy REST API


* path
* query params
* url


![URL Format Explained](../images/url.format.explained.png)


## REST API

nase REST API bude pouzivat prefix `/api/v1/`


### Resource Files

| path                    | method   | meaning                               | status    |
|-------------------------|----------|---------------------------------------|-----------|
| `/api/pokemons/{slug}`  | `GET`    | get pokemon info as JSON document     | `200`     |
| `/api/pokemons/{slug}`  | `DELETE` | delete pokemon with given `slug`      | `200`, `204`  |
| `/api/pokemons/{slug}`  | `PUT`    | full update of pokemon with `slug`    | `200`     |
| `/api/pokemons/{slug}`  | `PATCH`  | partial update of pokemon with `slug` | `200`     |
| `/api/pokemons/`        | `POST`   | create new pokemon                    | `201`     |
| `/api/pokemons/`        | `GET`    | return list of pokemons               | `200`     |


### Resource Users

| path            | method   | meaning                        |
|-----------------|----------|--------------------------------|
| `/users/`       | `GET`    | retrieve list of users         |
| `/users/{slug}` | `GET`    | retrieve info about given user |
| `/users/`       | `POST`   | create new user                |
| `/users/{slug}` | `DELETE` | delete existing user           |
| `/users/me`     | `GET`    | shows my profile               |


### Others

| path            | method | meaning             |
|-----------------|--------|---------------------|
| `/`             | `GET`  | show homepage       |
| `/cron/`        | `GET`  | starts maintainance |
