pipeline {

    agent any

    stages{

        stage("test"){

            steps{

                echo 'testing the application converter'
                pytest tests.py
                echo 'testing is completed see result'
            }
        }
    }
}