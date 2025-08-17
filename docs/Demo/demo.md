# Demo

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
docker run -d -p 5001:5000 flask-single
docker run -d -p 5002:5000 flask-multi
```

Visit:

http://localhost:5001 (single-stage)

http://localhost:5002 (multi-stage)

## Debugging

``` bash
# Make sure nothing else is running
docker stop $(docker ps -q)

docker exec -it <container_id> netstat -tlnp
```

## Docker-compose

``` bash
# Step 1: Build using bake (faster, parallel, better caching)
# using docker-bake.hcl
docker buildx bake --load

# Step 2: Run containers (no rebuild needed, images are already loaded)
docker compose up

# Or, docker compose up --build

# http://localhost:5001 → single-stage container
# http://localhost:5002 → multi-stage container

docker compose down
```
