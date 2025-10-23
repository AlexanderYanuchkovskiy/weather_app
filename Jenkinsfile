pipeline {
    agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    
    triggers {
        pollSCM('H/10 * * * *')
    }
    
    environment {
        DOCKER_HUB_REPO = 'keply186/weather-app'
        GIT_REPO = 'https://github.com/AlexanderYanuchkovskiy/weather_app'
        GIT_BRANCH = 'main'
        // Замените на ваши реальные данные
        DOCKER_USERNAME = 'keply186'
        DOCKER_PASSWORD = 'your-dockerhub-password-or-token'
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
                    sh "docker build -t ${DOCKER_HUB_REPO}:latest ."
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                    sh "docker push ${DOCKER_HUB_REPO}:latest"
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
            sh 'docker logout || true'
        }
    }
}