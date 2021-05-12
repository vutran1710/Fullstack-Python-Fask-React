# A simple fullstack app built with Python-Flask & React

## Challenge

Build a simple server-side app with **Flask** that generate random values of `String, Integer, Float and Alphanumeric` and save it to a file with maxium size of 2MB. Allow to download such file from a web client written in **React**. Calculate how many values of each type generated from such file.

## Screenshot

<p align="center">
  <img src="docs/ss.png" height="500">
</p>

## Running

The most simple way is to run with docker, which has everything bundled and ready to use

```shell
$ docker build -t <image-tag> .
$ docker run -p 3000:3000 --name <container-name> <image-tag>:latest
```

After the application has started, open your web-browser and go to http://localhost:3000

## Development
### Overall
<p align="center">
  <img src="docs/architech.png" width="100%">
</p>

### Backend
- *Pipenv*, *Python3.8* are required

- Install dependencies and run it
```shell
$ cd backend
$ pipenv install --dev --pre
$ pipenv run dev
```

- Run test with
```shell
$ pipenv run test
```
### Frontend
- Node 14 is required
- Prepare a `.env` file

```
# Not neccessary when running with flask-backend in development mode
REACT_APP_SERVER_URL=http://localhost:3000
# Enable the following env-var when running with flask-backend in development mode
# REACT_APP_API_URL=http://localhost:5000
```

- Run or build with npm
```shell
$ npm start
$ npm run build
```
