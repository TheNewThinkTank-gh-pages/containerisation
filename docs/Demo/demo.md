# Demo

After starting the Docker Daemon,

``` bash
# start asciinema recording
asciinema rec ~/Desktop/containerization.cast -i 2
```

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

stop containers:

``` bash
docker stop $(docker ps -q)
```

## Scanning

``` bash
IMAGE_NAME="flask-single"
trivy image $IMAGE_NAME

# Scan with specific severity levels
trivy image --severity HIGH,CRITICAL $IMAGE_NAME

# Generate JSON report
trivy image --format json --output "scans/results-${IMAGE_NAME//[:\/]/-}-$(date +%Y-%m-%d).json" $IMAGE_NAME

# Custom script, to summarize HIGH/CRITICAL vulnerabilities, and to use in CI/CD later.
./trivy_vulnerability_counter.sh $IMAGE_NAME
```

## Docker-compose

``` bash
# Step 1: Build using bake (faster, parallel, better caching)
# using docker-bake.hcl
docker buildx bake --load

cat compose.yml

# resource limits
docker inspect <container_name>
docker stats --no-stream <container_name>

# Step 2: Run containers (no rebuild needed, images are already loaded)
docker compose up

# Or, just `docker compose up` directly.
# Or, to also re-build:
# docker compose up --build

# http://localhost:5001 → single-stage container
# http://localhost:5002 → multi-stage container

# Ctrl + c, stop containers.

docker compose down
```

## Cleanup

Optionally, show cleanup of stopped containers and images, from CLI, Docker Desktop or both.

``` bash
docker images
docker rmi -f <image-name> <another-image-name>
```

``` bash
# Finish asciinema
exit
enter
asciinema upload ~/Desktop/containerization.cast
```
