pipeline {
    agent {
        kubernetes {
            label 'frontend-agent'
            idleMinutes 5
            yamlFile 'agent.yaml'
            defaultContainer 'ez-docker-helm-build'
        }
    }

    environment {
        DOCKER_CREDS = 'my_credential_dh'
        DOCKER_IMAGE_FRONT = 'guyk7/music-catalog-frontend'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE_FRONT}:latest", "--no-cache -f Dockerfile .")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDS) {
                        dockerImage.push("latest")
                    }
                }
            }
        }
    }
}
