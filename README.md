# blog backend

This repository contains a backend API for a blog, which includes POST GET DELETE methods for managing blog postings and comments.

## Stack

This API was written in Python 3 by using Flask framework, and it is intended to run as a Docker container (Dockerfile included).

Dockerfile includes a multi-stage building process to guarantee the smallest and fastest container as possible. The most relevant step here is installing all requirements by using --user flag (`pip3 install --user -r requirements.txt`) to ensure all dependencies are included in `/root/.local` folder, so it can be copied from build stage to final image.

## CircleCI

CircleCI configuration file is included in `.circleci` folder. It sets up a build and test taks for the API, followed by a second one  that builds the Docker image and then push it into Docker Hub. Notice on `workflow` section that the second task only runs after approving all tests included in the first one.

The result of that successfull workflow is a new tagged image on registry: `hebertsonm/blogea:dev`.

## Manual Test

The following step are an example of how to run a local container and test the API manually.

First, pull the image and run the container.

`docker run -d --rm -p 5000:5000 --name blogea hebertsonm/blogea:dev`

Then, perform `curl` commands to invoke POST GET and DELETE methods:

```
 curl -d '{"title":"value2", "body":"value2", "author":"Jane"}' -H "Content-Type: application/json" -X POST http://localhost:5000/api/post
 curl -d '{"body":"value11", "author":"Jane"}' -H "Content-Type: application/json" -X POST http://localhost:5000/api/comment/0
 curl -X GET  http://localhost:5000/api/post/0
 curl -X GET  http://localhost:5000/api/comment/0
```

## Kubernetes

This solution is avaliable at the address `http://blogea.westus2.cloudapp.azure.com/api/post` which consists on a Azure Kubernetes Service deployment.

An `ingress` was set to route all incomming traffic from blogea.westus2.cloudapp.azure.com DNS to a `service` in charge to load balance the traffic to two `pod` replicas including this API.

Kubernetes inventory files are not provided in this repository at the moment.
