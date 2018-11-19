# Run in kubernetes

## Use MS with Docker
[Install docker](https://docs.docker.com/install/)

Create and push the image
```
docker build -t data-domain -f Dockerfile .
```

Test the image:
```
docker run -d -p 5000:5000 data-domain
```

## Use MS with Kubernetes localy

Configure your service.yaml

Installing Kubernetes.
```
curl -Lo kubectl https://storage.googleapis.com/kubernetes-release/release/v1.9.0/bin/linux/amd64/kubectl && chmod +x kubectl && sudo mv kubectl /usr/local/bin/
```

Installing Minikube.
```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```    

Start minikube and set the environment of docker.
```
minikube start
eval $(minikube docker-env)
kubectl config use-context minikube
```
    
If a shell isn't your friend. You could use kubernetes web panel to see your pods.
```
minikube dashboard
```

Create your image.
```
docker build -t template:v1 .
```
    
Deploy your images localy.
```
kubectl apply -f service.yaml
minikube service template
```

Clean your environment.
```
kubectl delete template
kubectl delete template
docker rmi template:v1 -f
minikube stop
eval $(minikube docker-env -u)
minikube delete
```
