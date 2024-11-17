pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'ajinkya924'
        KUBECONFIG_PATH = '/path/to/your/kubeconfig' // Replace with the actual path to your kubeconfig file
    }

    stages {
        stage('Build Docker Images') {
            steps {
                script {
                    // Build Docker images for user-service and matchmaking-service
                    sh 'docker build -t ${DOCKER_HUB_REPO}/user-service:latest ./user-service'
                    sh 'docker build -t ${DOCKER_HUB_REPO}/matchmaking-service:latest ./matchmaking-service'
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    // Login to Docker Hub
                    sh 'echo "your_docker_hub_password" | docker login -u "ajinkya924" --password-stdin'

                    // Push Docker images to Docker Hub
                    sh 'docker push ${DOCKER_HUB_REPO}/user-service:latest'
                    sh 'docker push ${DOCKER_HUB_REPO}/matchmaking-service:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Apply Kubernetes deployments
                    sh 'kubectl --kubeconfig=${KUBECONFIG_PATH} apply -f kubernetes/mongodb-deployment.yaml'
                    sh 'kubectl --kubeconfig=${KUBECONFIG_PATH} apply -f kubernetes/mongodb-match-deployment.yaml'
                    sh 'kubectl --kubeconfig=${KUBECONFIG_PATH} apply -f kubernetes/user-service-deployment.yaml'
                    sh 'kubectl --kubeconfig=${KUBECONFIG_PATH} apply -f kubernetes/matchmaking-service-deployment.yaml'
                }
            }
        }

        stage('Check Pod Status') {
            steps {
                script {
                    // Check the status of the pods
                    sh 'kubectl --kubeconfig=${KUBECONFIG_PATH} get pods'
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images
            sh 'docker rmi ${DOCKER_HUB_REPO}/user-service:latest'
            sh 'docker rmi ${DOCKER_HUB_REPO}/matchmaking-service:latest'
        }
    }
}