
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/jatinninety9/student-registration.git'
            }
        }

        stage('Test Registration Form') {
            steps {
                bat '"C:\\Users\\chauh\\AppData\\Local\\Python\\bin\\python.exe" test_form.py'
            }
        }
    }

    post {
        success {
            echo 'All tests passed successfully!'
        }

        failure {
            echo 'Pipeline failed! Check test results.'
        }
    }
}
