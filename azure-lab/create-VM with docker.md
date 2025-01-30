create a resource group

```bash
az group create --name myResourceGroup --location centralindia
```

delete a resource group

```bash
az group delete --name myResourceGroup
```

create a ubuntu virtual machine in the resource group

```bash
az vm create \
  --resource-group myResourceGroup \
  --name myVM \
  --image Ubuntu2404 \
  --admin-username azureuser \
  --ssh-key-values ~/.ssh/id_rsa.pub \
  --public-ip-sku Standard
```

delete the virtual machine

```bash
az vm delete --resource-group myResourceGroup --name myVM2
```

open port 80 to allow web traffic to host

```bash
az vm open-port --port 22 --resource-group myResourceGroup --name myVM --priority 1001
```

get the public IP address of the VM

```bash
az vm list-ip-addresses --resource-group myResourceGroup --name myVM --output table
```

ssh into the VM

```bash
chmod 600 ~/.ssh/id_rsa
ssh azureuser@20.204.130.52
```

---

```bash
cat /etc/os-release
```

install docker

```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl status docker

sudo usermod -aG docker ${USER}
```
