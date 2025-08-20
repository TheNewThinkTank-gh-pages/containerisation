# Asciinema

``` bash
# start recording
asciinema rec

# stop recording
exit  # or, Ctrl + d

# save recording
<enter>  # uploads to asciinema.org
# or, Ctrl + c  # save locally

# play recording
asciinema play <recording-filepath>

# cut any idle time above 2 seconds
asciinema rec -i 2

# specify filename for recording. Will save locally as default.
asciinema rec containerization.cast
```
