# flask-cicd

This is a simple flask app CI/CD 

1. Jenkins build the image from a python image using the Dockerfile
2. Start the container to execute a simple test
3. Take down the container
4. Recreate the image once it is tested.
5. If success push the image to docker hub.

