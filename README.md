# Containerisation

Theoretical background for containers.

## Demo

After starting the Docker Daemon,

1. Show the app

``` bash
cat app.py
```

2. Show the naive Dockerfile

``` bash
cat Dockerfile.single
```

3. Build & check size

``` bash
docker build -t flask-single -f Dockerfile.single .
docker images | grep flask
```

4. Inspect layers

``` bash
docker history flask-single
```

5. Show the multi-stage Dockerfile

``` bash
cat Dockerfile.multi
```

6. Build & compare

``` bash
docker build -t flask-multi -f Dockerfile.multi .
docker images | grep flask
```

7. Inspect layers again

``` bash
docker history flask-multi
```

8. Use dive

``` bash
dive flask-multi
```

9. Run both images

``` bash
docker run -d -p 5000:5000 flask-single
docker run -d -p 5001:5000 flask-multi
``

Visit:

http://localhost:5000 (single-stage)

http://localhost:5001 (multi-stage)

