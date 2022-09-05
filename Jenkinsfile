pipeline {
    environment {
        imageName = "jocptwo/flask-demo-app:${env.BUILD_ID}"
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
                        sh 'LASTIMAGEID=$(sudo docker images | awk '{print $3}' | awk 'NR==2')'
                        sh 'sudo docker rmi $LASTIMAGEID'
                    }
                }

                failure {
                    script {
                        sh 'sudo docker-compose down'
                        sh 'LASTIMAGEID=$(sudo docker images | awk '{print $3}' | awk 'NR==2')'
                        sh 'sudo docker rmi $LASTIMAGEID'
                    }
                }
            }
        }

        stage('Build Image') {
            steps {
                script {
                   MyImage = sh "sudo docker build -t jocptwo/flask-demo-app:${env.BUILD_ID} ."
                }
            }
        }

        stage('Push to Registry'){
            steps {
                script {
                    docker.withRegistry('https://docker.hub.com', 'dockerhub-cred') {
                        MyImage.push()

                    }

                }
            }
        }

    }
}