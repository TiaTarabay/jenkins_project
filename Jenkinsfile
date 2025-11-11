pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
    }

    stages {

        stage('Setup') {
            steps {
                script {
                    if (!fileExists("${env.WORKSPACE}\\${VIRTUAL_ENV}")) {
                        bat "python -m venv ${VIRTUAL_ENV}"
                    }

                    bat """
                        call ${VIRTUAL_ENV}\\Scripts\\activate
                        pip install -r requirements.txt
                        pip install coverage bandit flake8 pytest
                    """
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    bat """
                        call ${VIRTUAL_ENV}\\Scripts\\activate
                        flake8 app.py
                    """
                }
            }
        }

        stage('Security Scan') {
            steps {
                script {
                    bat """
                        call ${VIRTUAL_ENV}\\Scripts\\activate
                        bandit -r .
                    """
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat """
                        call ${VIRTUAL_ENV}\\Scripts\\activate
                        pytest
                    """
                }
            }
        }

        stage('Coverage') {
            steps {
                script {
                    bat """
                        call ${VIRTUAL_ENV}\\Scripts\\activate
                        coverage run -m pytest
                        coverage report -m
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat """
                        call ${VIRTUAL_ENV}\\Scripts\\activate
                        if not exist deployed_app mkdir deployed_app
                        copy app.py deployed_app\\
                    """
                    echo "Deployment complete (Windows local deploy)"
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
