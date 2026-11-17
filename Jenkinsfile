
pipeline {
    agent any

    environment {
        PYTHON = 'C:/Users/shahe/anaconda3/python.exe'
    }

    stages {

        stage('GitHub Checkout') {
            steps {
                echo 'GitHub checkout successful'
            }
        }

        stage('Check Python') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '"%PYTHON%" -m pytest -v tests/test_factorial.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t factorial-app:1.0 .'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '"%PYTHON%" -m pytest -v tests/test_selenium.py'
            }
        }
    }

    post {
        success {
            echo 'Factorial project completed successfully!'
        }

        failure {
            echo 'Factorial project failed!'
        }
    }
}
