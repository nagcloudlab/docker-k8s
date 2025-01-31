Install Docker

```bash
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
docker --version
sudo usermod -aG docker $USER
newgrp docker

```

Install Kind

```bash

curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-$(uname)-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
kind --version

```

Install kubectl

````bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/$(uname | tr '[:upper:]' '[:lower:]')/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
kubectl version --client


Create a Kubernetes Cluster with Kind

```bash
kind help
kind create cluster --config kind-config.yaml --name k8s-cluster1
kind get clusters


````

4. Verify the Cluster

```bash
kubectl cluster-info --context kind-k8s-cluster1
kubectl get nodes
kubectl cluster-info
```

5. Delete the Cluster

```bash
kind delete cluster --name k8s-cluster1
kind get clusters
```

set alias for kubectl

```bash
echo "alias k=kubectl" >> ~/.bashrc
echo "complete -F __start_kubectl k" >> ~/.bashrc
source ~/.bashrc
```
