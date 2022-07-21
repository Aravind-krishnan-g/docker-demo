# docker-demo

1. Clone the repo
2. Build the image
```
docker build -t myimage .
```
3. Run the container
```
docker run -d --name mycontainer -p 8000:8000 myimage
```
4. Visit [localhost](https://localhost:8000) to check our fastapi app
5. Stop the container
```
docker stop mycontainer
```
