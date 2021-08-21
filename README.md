# prometheus-monitoring
This tool collects the status from internet http urls https://httpstat.us/503 https://httpstat.us/200 and exports the metrics for up status and response time in the /metrics API using prometheus python client.

## Prerequisities
- Docker engine installed in your machine
- Kubernetes cluster setup done or minikube running in your local  [ if you are running the tool in kubernetes ]

## Build
### Build docker image
    ./docker_build.sh
This script builds the image in the http_monitor.

## Run tool using docker
### Run docker image
    ./docker_run.sh
This command runs the http_monitor image in the host and exposes and binds the port 8080

## Run tool in kubernetes
## Create the deployment in k8 cluster
    kubectl create -f k8s-deploy/deployment.yaml

This command assumes the docker image created is available to the kubernetes cluster. If you are using minikube then you can refer https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube to make the image available for the minikube.
Otherwise, you need to push the image to the registry and pull the image from that registry to your cluster.

## Create the service in k8 cluster
    kubectl create -f k8s-deploy/service.yaml

This service uses NodePort type so we can reach the service using
http://<k8 node>:<node port>/metrics
Use th below command to find the node port
   
    kubectl describe service/http-monitor-service

## Usage
Once the container is up and running, the /metrics endpoint will be available in the API http://localhost:8080/metrics

This API can be configured in prometheus configurations to scrape the metrics at a periodic interval.