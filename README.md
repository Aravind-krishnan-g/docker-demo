# Demo for Docker 
<br>

## Useful resources
1. [Concept of containerization](https://www.docker.com/resources/what-container/)
2. [Docker overview](https://docs.docker.com/get-started/overview/)
3. [Docker compose overview](https://docs.docker.com/compose/)
<br>

## Step by step instructions
1. Clone the repo
2. Build an image of our fastapi app with name *myimage*
  ```
  docker build -t myimage .
  ```
3. Check for the created image 
  ```
  docker images
  ```
4. Run the container with name *mycontainer*
  ```
  docker run -d --name mycontainer -p 8000:8000 myimage
  ```
5. Check the running containers
  ```
  docker ps
  ```
4. Visit [localhost](http://localhost:8000) to check our fastapi app
5. Stop the container
  ```
  docker stop mycontainer
  ```
6. Check the status of containers
  ```
  docker ps -a
  ```
7. Remove the container
  ```
  docker rm mycontainer
  ```
8. Remove image
  ```
  docker rmi myimage
  ```
