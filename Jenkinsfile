pipeline {
    agent any

    environment {
        IMAGE_NAME = "weather_app"
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AlexanderYanuchkovskiy/weather_app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Проверяем, что Docker доступен
                    sh 'docker --version'

                    // Собираем Docker образ
                    sh "docker build -t ${IMAGE_NAME}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Останавливаем контейнер, если уже существует
                    sh "docker rm -f ${IMAGE_NAME} || true"

                    // Запускаем контейнер
                    sh "docker run -d --name ${IMAGE_NAME} -p 5000:5000 ${IMAGE_NAME}:${DOCKER_TAG}"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline успешно завершён!'
        }
        failure {
            echo 'Pipeline завершился с ошибкой!'
        }
    }
}
