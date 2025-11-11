pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
    }

    stages {

        stage('Setup') {
            steps {
                script {
                    if (!fileExists("${env.WORKSPACE}/${VIRTUAL_ENV}")) {
                        sh "python -m venv ${VIRTUAL_ENV}"
                    }

                    sh """
                        source ${VIRTUAL_ENV}/bin/activate
                        pip install -r requirements.txt
                        pip install coverage bandit
                    """
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    sh """
                        source ${VIRTUAL_ENV}/bin/activate
                        flake8 app.py
                    """
                }
            }
        }

        stage('Security Scan') {
            steps {
                script {
                    sh """
                        source ${VIRTUAL_ENV}/bin/activate
                        bandit -r .
                    """
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh """
                        source ${VIRTUAL_ENV}/bin/activate
                        pytest
                    """
                }
            }
        }

        stage('Coverage') {
            steps {
                script {
                    sh """
                        source ${VIRTUAL_ENV}/bin/activate
                        coverage run -m pytest
                        coverage report -m
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "Starting deployment..."

                    sh """
                        source ${VIRTUAL_ENV}/bin/activate
                        mkdir -p deployed_app
                        cp -r app.py deployed_app/
                    """

                    echo " Deployment complete "
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
