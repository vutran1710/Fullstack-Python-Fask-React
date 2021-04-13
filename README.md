# Demo flaskapp
## Running with Docker

```shell
$ docker build -t <image-tag> .
$ docker run -p 3000:3000 --name <container-name> <image-tag>:latest
```

## Run backend in development mode
- Install pipenv
- Install project dependencies

```shell
$ cd backend
$ pipenv install --dev --pre
$ pipenv run dev
```

- Run test with
```shell
$ pipenv run test
```
