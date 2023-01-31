pipeline {

    agent any

    stages{

        stage("test"){

        steps{

            echo 'testing the application converter'
            pip install -r requirements.txt
            pytest tests.py
            echo 'testing is completed see result'
            }
        }
    }
}