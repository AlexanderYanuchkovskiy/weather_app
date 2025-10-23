pipeline {
    agent any
    
    triggers {
        pollSCM('H/10 * * * *')  // Проверять изменения каждые 10 минут
    }
    
    environment {
        DOCKER_HUB_REPO = 'keply186/weather-app'
        GIT_REPO = 'https://github.com/AlexanderYanuchkovskiy/weather_app'
        GIT_BRANCH = 'main'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: "${GIT_BRANCH}", 
                     url: "${GIT_REPO}"
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_HUB_REPO}:latest")
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("${DOCKER_HUB_REPO}:latest").push()
                    }
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
        }
    }
}