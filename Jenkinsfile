pipeline {

    agent any

    stages{

        stage("test PythonEnv") {

            withPythonEnv('python3') {
                sh 'pip install pytest'
                sh 'pytest tests.py'
                }
            }

        stage("test"){

        steps{

            echo 'testing the application converter'

            echo 'testing is completed see result'
            }
        }
    }
}
