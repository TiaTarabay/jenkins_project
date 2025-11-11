pipeline {
  agent any

  environment {
    VIRTUAL_ENV = 'venv'
    PIP_DISABLE_PIP_VERSION_CHECK = '1'
    PYTHONUTF8 = '1'
    PYTHONIOENCODING = 'utf-8'
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
            pip install flake8 pytest coverage bandit
          """
        }
      }
    }

    stage('Lint') {
      steps {
        bat """
          call ${VIRTUAL_ENV}\\Scripts\\activate
          flake8 app.py
        """
      }
    }

    stage('Security Scan') {
      steps {
        bat """
          chcp 65001 >NUL
          call ${VIRTUAL_ENV}\\Scripts\\activate
          bandit -r . --format json --output bandit.json --severity-level MEDIUM --confidence-level MEDIUM
        """
      }
    }

    stage('Test') {
      steps {
        bat """
          call ${VIRTUAL_ENV}\\Scripts\\activate
          pytest --junitxml=pytest.xml
        """
      }
    }

    stage('Coverage') {
      steps {
        bat """
          call ${VIRTUAL_ENV}\\Scripts\\activate
          coverage run -m pytest
          coverage xml -o coverage.xml
          coverage html
          coverage report -m
        """
      }
    }

    stage('Deploy') {
      steps {
        bat """
          call ${VIRTUAL_ENV}\\Scripts\\activate
          if not exist deployed_app mkdir deployed_app
          copy /Y app.py deployed_app\\
        """
        echo "Deployment complete (Windows local deploy)."
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'bandit.json, pytest.xml, coverage.xml, htmlcov/**, deployed_app/**', fingerprint: true
      catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
        junit 'pytest.xml'
      }
      cleanWs()
    }
  }
}
