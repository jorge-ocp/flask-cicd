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
                    sh 'sudo -A docker-compose rm -f; sudo -A docker-compose up -d images'
                }
            }
        }

        stage('Run Tests'){
            steps {
                script {
                    sh 'pip3 install -r requirements.txt; python3 -m pytest app/test.py'
                }
            }

            post {
                success {
                    script {
                        sh 'sudo docker-compose down'
                    }
                }

                failure {
                    script {
                        sh 'sudo docker-compose down'
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