# Create Azure Kubernetes Service (AKS)
Login to Azure portal, and create an AKS similar to the example bellow.

 - BASICS
    - Resource group: (new) blogea
    - Region: westus2
    - Kubernetes cluster name: blogea
    - DNS name prefix: blogea
    - Node count: 1
    - Node size: Standard_B2s
 - AUTHENTICATION
    - Enable RBAC: Yes
 - NETWORKING
    - Basic
 - MONITORING
    - Enable container monitoring: Yes

# Install and configure tools
```bash
brew install kubernetes-helm
brew install azure-cli
az login
az aks install-cli
```

## Configure kubectl to work with the new cluster
Get kubectl credentials for Azure
```bash
az aks get-credentials --resource-group blogea --name blogea
```
Tip: Make sure you are working with the right cluster with `kubectl config current-context`.

# Configure cluster
initialize Helm on both client and server:
```
helm init
```

## Install nginx controller
```bash
kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
```
Wait just a minute for Helm to finish initializing
```
helm install stable/nginx-ingress --version 1.17.1 --namespace kube-system --set controller.replicaCount=2 --set controller.service.externalTrafficPolicy="Local"
```
* If you get `Error: could not find a ready tiller pod` just wait a minute for Helm to finish initializing and try again

Get the external ip, assigned to the Load Balancer
```bash
kubectl get service -l app=nginx-ingress --namespace kube-system
```

## Register Azure domain name for the load balancer
Update dns.sh, copy external ip, set unique domain name for the load balancer.

Run the script:
```bash
sh dns.sh
```
Copy FQDN from the output (e.g. blogea.westus2.cloudapp.azure.com), this is the load balancer's domain name.
Tip: Set a custom domain (e.g blog.ea.com) to send traffic for the domain above.

# Application Deployment
```bash
kubectl apply -f env.yaml
kubectl apply -f blog-deployment.yaml
kubectl apply -f ingress.yaml
```

# Operations
## Auto deployments with Keel
Keel redeploys the app whenever the new version of the image is available.
It watches the registry by polling or using a webhook.
At this moment it's used only on Alpha cluster to redeploy the feature releases.
```bash
kubectl apply -f keel-rbac.yaml
```
