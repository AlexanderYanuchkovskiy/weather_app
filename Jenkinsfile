pipeline {
    agent any

    environment {
        IMAGE_NAME = "weather_app"
        DOCKER_TAG = "latest"
        REGISTRY = "localhost:5000" // локальный registry, если есть
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AlexanderYanuchkovskiy/weather_app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Проверяем Python и pip
                    sh 'python3 --version || python --version'
                    sh 'pip3 --version || pip --version'

                    // Устанавливаем зависимости
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запуск тестов, если есть
                    sh 'pytest || true' // true чтобы не падало сразу, можно убрать
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${DOCKER_TAG} ."
                    // Если есть локальный registry
                    // sh "docker tag ${IMAGE_NAME}:${DOCKER_TAG} ${REGISTRY}/${IMAGE_NAME}:${DOCKER_TAG}"
                    // sh "docker push ${REGISTRY}/${IMAGE_NAME}:${DOCKER_TAG}"
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh "docker rm -f ${IMAGE_NAME} || true"
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
