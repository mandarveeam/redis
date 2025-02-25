# Flask-Redis App

This project is a simple Flask web application that connects to a Redis database. The application increments and retrieves a counter from Redis every time the root URL is accessed.

## Features
- Built with Python 3.10 and Flask.
- Uses Redis as a backend data store.
- Packaged in a Docker container.
- Deployable on Kubernetes with a PersistentVolumeClaim (PVC) for Redis storage.
- Uses Azure Container Registry for storing container images.

## Prerequisites
- Docker
- Kubernetes (kubectl, minikube, or a cloud-based K8s cluster)
- Helm (if required for additional setups)
- Azure Container Registry (for pushing container images)

## Project Structure
```
app2/
│-- Dockerfile
│-- app.py
│-- requirements.txt
│-- manifest.yaml
```

## Setup and Usage

### 1. Build and Run Locally
#### Build Docker Image
```sh
docker build -t flask-redis-app .
```
#### Run Container
```sh
docker run -p 8000:8000 \
    -e REDIS_HOST=<your_redis_host> \
    -e REDIS_PORT=6379 \
    -e REDIS_PASSWORD=<your_redis_password> \
    flask-redis-app
```

### 2. Push to Azure Container Registry (ACR)
```sh
docker tag flask-redis-app mandar01.azurecr.io/flask-redis-app:latest
docker push mandar01.azurecr.io/flask-redis-app:latest
```

### 3. Deploy on Kubernetes
#### Apply Persistent Volume Claim
```sh
kubectl apply -f manifest.yaml
```
#### Deploy Application
```sh
kubectl apply -f manifest.yaml
```
#### Verify Deployment
```sh
kubectl get pods
kubectl get services
```

### 4. Access the Application
Find the external IP of the service:
```sh
kubectl get services flask-redis-app-service
```
Access the application in a browser:
```
http://<EXTERNAL-IP>
```

## Dockerfile Breakdown
- **Builder Stage:** Installs dependencies and copies application files.
- **Dev Environment:** Installs Git, Bash, and sets up a development user.
- **Multi-Stage Build:** Optimizes image size for production.

## Kubernetes Manifest Breakdown
- **PersistentVolumeClaim (PVC):** Provides persistent storage for Redis.
- **Deployment:** Defines Redis and Flask containers with appropriate environment variables.
- **Service:** Exposes the Flask application via a LoadBalancer.

## Notes
- Ensure Redis is accessible for the Flask app.
- If using an external Redis instance, update `REDIS_HOST` accordingly.
- Change the Service type to `NodePort` if LoadBalancer is not available.

## License
This project is licensed under the MIT License.

