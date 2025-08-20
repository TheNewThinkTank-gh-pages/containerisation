# Scanning

Recommendation:

Start with Docker Scout since it's built-in, then consider Trivy for more detailed scanning.
Both are free and provide comprehensive vulnerability detection.

## Docker Scout (Built-in, Recommended)

Docker Scout is now integrated into Docker Desktop and is the easiest to get started with. Requires sign-in, however.

``` bash
# Scan an image
docker scout cves <image-name>

# Quick vulnerability summary
docker scout quickview <image-name>

# Compare with base image
docker scout compare --to <base-image> <your-image>
```

## Trivy (Popular Open Source)

Trivy is comprehensive and easy to use.

``` bash
# Install via Homebrew
# brew install trivy

IMAGE_NAME="flask-single"

# Scan an image
trivy image $IMAGE_NAME

# Scan with specific severity levels
trivy image --severity HIGH,CRITICAL $IMAGE_NAME

# Generate JSON report
trivy image --format json --output "scans/results-${IMAGE_NAME//[:\/]/-}-$(date +%Y-%m-%d).json" $IMAGE_NAME

# trivy image --format json --output scans/flask-single-trivy-results.json $IMAGE_NAME

# Custom script, to summarize HIGH/CRITICAL vulnerabilities, and to use in CI/CD later.
./trivy_vulnerability_counter.sh $IMAGE_NAME
```
