
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Factorial project checkout completed'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python -m pytest -v tests/test_factorial.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t factorial-app:1.0 .'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'python -m pytest -v tests/test_selenium.py'
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
