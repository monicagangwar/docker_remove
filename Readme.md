#Docker Remove
Utility to easily remove Docker Container(s)/Image(s) through string matching  

##Usage
###Help
```
╰─$ docker_remove --help
usage: docker-remove [-h] [--container CONTAINER] [--image IMAGE]
                     [--name NAME] [-a] [-f]

Use this simple command to remove Docker container(s) or images(s) through
string matching.

optional arguments:
  -h, --help            show this help message and exit
  --container CONTAINER, -c CONTAINER
                        Flag to remove Docker container(s) only
  --image IMAGE, -i IMAGE
                        Flag to remove Docker image(s) only
  --name NAME, -n NAME  Flag to remove both Docker container(s) and image(s)
  -a                    Flag to remove hidden container(s)/image(s)
  -f                    Flag to forcefully remove container(s)/image(s)

```
