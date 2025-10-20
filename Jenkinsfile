pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'weather_app'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AlexanderYanuchkovskiy/weather_app.git'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Тестирование приложения (если тесты появятся позже)'
                // sh 'pytest'  # можно добавить позже
            }
        }

        stage('Run container (optional)') {
            steps {
                echo 'Запуск контейнера для проверки (опционально)'
                // sh 'docker run -d -p 5000:5000 --name weather_app $DOCKER_IMAGE:$DOCKER_TAG'
            }
        }
    }

    post {
        success {
            echo '✅ CI успешно завершён — Docker-образ собран!'
        }
        failure {
            echo '❌ Ошибка при сборке Docker-образа!'
        }
    }
}
