# Debugging

``` bash
# SSL cert issue, fix using macOS syntax:
# Export the certificate
security find-certificate -a -p -c "Zscaler Root CA" > ~/zscaler_root.pem
 
# Update both certificate locations
sudo cat ~/zscaler_root.pem >> /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/certifi/cacert.pem
sudo cat ~/zscaler_root.pem >> /Library/Frameworks/Python.framework/Versions/3.12/etc/openssl/cert.pem


# Make sure nothing else is running
docker stop $(docker ps -q)

docker exec -it <container_id> netstat -tlnp
```
