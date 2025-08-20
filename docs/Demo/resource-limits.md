# Verify container's resource configuration and monitor resource usage

## Docker Inspect

See the configuration/limits:

```bash
# Inspect a specific container
docker inspect <container_name>
```

## Docker Stats

Monitor actual resource usage in real-time:

```bash
# Show stats for all containers
# docker stats

# Show stats for specific container(s)
# docker stats <container_name> [<another_container_name>...]

# Show stats without streaming (just one snapshot)
docker stats --no-stream <container_name>

# Format the output to show specific columns
# docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}"
```

Example output of `docker stats`:

```
CONTAINER ID   NAME                CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O         PIDS
3b45678901ab   myapp              0.25%     84.5MiB / 512MiB     16.50%    656B / 656B      0B / 0B           1
```

Get container names when using docker-compose:

```bash
# List containers created by docker-compose
docker compose ps

# Then use the names with docker inspect or stats
docker stats <service_name>
```
