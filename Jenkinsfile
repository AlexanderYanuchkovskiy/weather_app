pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AlexanderYanuchkovskiy/weather_app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('keply186/weather_app:latest')
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-login') {
                        docker.image('keply186/weather_app:latest').push()
                    }
                }
            }
        }
    }
}