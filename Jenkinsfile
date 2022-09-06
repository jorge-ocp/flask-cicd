pipeline {
    environment {
        imageName = "jocptwo/flask-demo-app:${env.BUILD_ID}"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred')
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

        stage('Build Image') {
            steps {
                script {
                   sh "sudo docker build -t jocptwo/flask-demo-app:${env.BUILD_ID} ."
                }
            }
        }

        stage('Push to Registry'){
            steps {
                script {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKER_CREDENTIALS_USR --password-stdin'
                    sh "sudo docker push jocptwo/flask-demo-app:${env.BUILD_ID}"
                    

                    

                }

                
            }
        }

    }
}