pipeline {
    environment {
        imageName = "jocptwo/flask-demo-app:{env.BUILD_ID}"
        customImage = ''
    }

    agent any
    stages {

        stage('Start Container for Testing') {
            steps {
                script {
                    sh 'docker --version'
                    sh 'sudo docker-compose rm -f; sudo docker-compose up -d images'
                }
            }
        }

        stage('Run Tests'){
            steps {
                script {
                    sh 'pip3 install -r requirements.txt; python3 -m pytest /app/test.py'
                }
            }

            post {
                success {
                    script {
                        sh 'docker-compose down'
                    }
                }

                failure {
                    script {
                        sh 'docker-compose down'
                    }
                }
            }
        }

        stage('Buld Image') {
            steps {
                script {
                    customImage = docker.build(imageName)
                }
            }
        }

    }
}