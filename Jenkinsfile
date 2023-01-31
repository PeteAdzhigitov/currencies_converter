pipeline {

    agent any

    stages{

        stage("Installing all reqired dependicies"){

        steps{
            pip install -r requirements.txt
        }

        }

        stage("test"){

        steps{

            echo 'testing the application converter'

            pytest tests.py
            echo 'testing is completed see result'
            }
        }
    }
}