# Assignment-k8

# 🚀 Kubernetes Deployment Commands for Flask + Express App

## ✅ Step-by-Step Commands to Deploy on Minikube

### 🔁 Start Minikube
```bash
minikube start
docker build -t srilakshmiyannam/express-backend .
docker build -t srilakshmiyannam/flask-app .
kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f frontend-service.yaml
kubectl get pods
kubectl get svc
minikube service frontend


