# Download and extract the latest release of eksctl $ setup on local machine
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version


# Download the latest release of Kubectl & setup on local machine 
curl -o kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.20.4/2021-04-12/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
kubectl version --client

# Install aws packages
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && sudo ./aws/install


# Install Helm3 and helm repo
curl -L https://git.io/get_helm.sh | bash -s -- --version v3.8.2
helm version --short


# Create IAM role with permissions defined at below link
# https://eksctl.io/usage/minimum-iam-policies/
# Attach that role with running EC2 & disable temporary credentials

# Create the cluster
eksctl create cluster -f cluster.yml