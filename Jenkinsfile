pipeline{
    agent any

    stages{
        stage("build"){
            steps{
                echo "Building the application..."
                sh 'python3 app.py'
                echo "Push Command Trigger From Github"
            }
        }
        stage("test"){
            steps{
                echo "Testing the application..."
            }
        }
        stage("deploy"){
            steps{
                echo "Depploying the application..."
            }
        }
    }
}
