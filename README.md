# CustomImage-Kubernetes-Rancher

This project demonstrates containerizing a custom made Flask application and then deploying it on Kubernetes locally using Rancher.

**Prerequisites**

- Docker / Rancher Desktop

- Kubernetes Cluster

- kubectl Configured


**Steps(Terminal):**

mkdir git_custom_image

cd git_custom_image

git clone https://github.com/LokiSahetia/CustomImage-Kubernetes-Rancher.git

cd CustomImage-Kubernetes-Rancher

cd docker_custom_image

#you can edit the app.py accordingly and make sure you include the desired dependencies in requirements.txt.

docker build -t loki-flask-app . #you change loki-flask-app with your_image_name but make sure you change it in the deployment file as well.

docker images 

docker run -d -p 5000:5000 loki-flask-app #test your image 

docker ps

docker stop container_id #Gracefully stops the container (sends a SIGTERM signal)

cd ..

kubectl apply -f custom_image_deployment.yaml #this will launch your deployment and service in the default namespace 

Open your browser and go to localhost:30096

