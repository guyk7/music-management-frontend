# Music Management Frontend 🎵

This is the frontend pipeline for the **Music Management App**. It builds and deploys the frontend application, connects to the backend APIs, and updates Helm charts for Kubernetes deployment.

---

## **Pipeline Overview**
The `Jenkinsfile` automates the CI/CD process for the frontend project, including:
- Checking out the code from GitLab.
- Building and pushing a Docker image to DockerHub.
- Updating Helm values and deploying the application.
- Committing updates to the `1-frontend_app` branch in GitLab.

The pipeline runs in a Kubernetes environment using the `agent.yaml` configuration to define required containers.

---

## **Requirements**
To run this project, ensure you have the following:
- Jenkins with Kubernetes integration.
- DockerHub credentials stored in Jenkins as `docker-creds`.
- GitLab credentials stored in Jenkins as `my_credentials_git`.
- Kubernetes cluster with Helm installed.
- Docker image `idoshoshani123/docker-dnd-aks:latest` available in your cluster.

---

## **Pipeline Steps**

### 1. Checkout Code
The pipeline checks out the `1-frontend_app` branch from GitLab:
```bash
git clone https://gitlab.com/sela-tracks/1109/students/guyk/final_project/application/main_app/frontend.git
```

### 2. Build Docker Image
The pipeline builds the Docker image using the `Dockerfile` located in the `app/` directory:
```bash
docker build -t <image-name>:<tag> --no-cache -f app/Dockerfile .
```

### 3. Push Docker Image
The pipeline tags and pushes the Docker image to DockerHub:
```bash
docker tag <image-name>:<tag> <repository>/<image-name>:<tag>
docker push <repository>/<image-name>:<tag>
```

### 4. Update Helm Values
The Helm `values.yaml` file is updated with the new Docker image tag:
```bash
sed -i "s|tag: .*|tag: <tag>|" ./helm/frontend/values.yaml
```

### 5. Deploy to Kubernetes
The updated application is deployed to the Kubernetes cluster using Helm:
```bash
helm upgrade --install frontend ./helm/frontend -f ./helm/frontend/values.yaml
```

### 6. Commit and Push Updates
After updating the Helm chart, the pipeline commits and pushes the changes back to GitLab:
```bash
git add ./helm/frontend/values.yaml
git commit -m "Updated Helm values with new image tag"
git push origin 1-frontend_app
```

---

## **How to Run Locally**
To test the frontend locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/guyk7/music-management-frontend.git
   cd music-management-frontend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the web interface:
   ```
   http://localhost:5001
   ```

---

## **Key Files**
- **`Jenkinsfile`**: CI/CD pipeline definition for Jenkins.
- **`agent.yaml`**: Kubernetes configuration for Jenkins agent.
- **`app/`**: Contains the Flask-based frontend application.
- **`templates/`**: Jinja2 HTML templates for rendering pages.
- **`static/`**: Contains CSS and other static assets.
- **`helm/`**: Helm chart for Kubernetes deployment.
- **`Dockerfile`**: Used for building the frontend Docker image.

---

## **Notes**
- Ensure that the backend API is running and accessible for full functionality.
- Verify that Jenkins credentials (`docker-creds` and `my_credentials_git`) are set up correctly.
- Update the Helm `values.yaml` file before deploying to Kubernetes.

