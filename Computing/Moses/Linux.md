### Install docker

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo apt install docker-compose
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```
At this point, you should log out and log back in to apply the changes. You can check if the installation was successful by running `docker --version` and `docker-compose --version`.

### Running the container
```bash
git clone https://github.com/cadia-lvl/SMT.git
cd SMT
docker-compose up -d
```
Now, you can translate:
```bash
echo "Hæ, ég er Moses." | docker run -i haukurp/moses-lvl:3.2.0 ./main.py preprocess - - "is" | docker run -i haukurp/moses-smt:is-en /opt/moses/bin/moses -f /work/moses.ini | docker run -i haukurp/moses-lvl:3.2.0 ./main.py postprocess - - "en"
```

And this should all be working now.
