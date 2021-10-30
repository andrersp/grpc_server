def TEAMS_URL = "https://inquestbr.webhook.office.com/webhookb2/da002111-b463-4dda-bda9-1a446d7e2c4f@7a2b646b-7d40-4b48-abb5-42661c89021c/JenkinsCI/b5834febac8c44af91ae2bc3b2a58d14/7fa94f26-79ba-4f54-89df-5d5dfef8baa4"


pipeline {
    
    agent {
            kubernetes {
                cloud 'kubernetes-dev'
                inheritFrom 'jenkins-slave'
                defaultContainer 'jenkins-slave'
                }
            }

    
    options {
        skipDefaultCheckout(false)
        // Keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
        }
    triggers {
        githubPush()
    }
    environment {
        PATH="/opt/conda/bin:$PATH" 
        }
    
    stages {
        stage('build and push web') {
            
            steps {
                script {
                    docker.withRegistry('https://registry.digitalocean.com', 'docker_credentials-do') {
                        def customImage = docker.build("staging-dh/app-dev:${BUILD_NUMBER}", "-f dockerfiles/Dockerfile .")

                        /* Push the container to the custom Registry */
                        customImage.push()
                    }
                }
            }
        }
        stage('build and push worker') {
            
            steps {
                script {
                    docker.withRegistry('https://registry.digitalocean.com', 'docker_credentials-do') {

                        def customImage = docker.build("staging-dh/app-dev-celery:${BUILD_NUMBER}", "-f dockerfiles/Dockerfile.celery .")

                        /* Push the container to the custom Registry */
                        customImage.push()
                    }
                }
            }
        }

        stage('deploy k8s') {
            steps {
                script {
                    kubernetesDeploy(configs: "manifest-dev.yaml", kubeconfigId: "kubeconfig-dev")
                }
            }
        }
    }

    post {
            // Always post result 
            always {  
                sh 'conda remove --yes -n ${BUILD_TAG} --all'                
                office365ConnectorSend message: "${JOB_NAME}", status:"Build ${currentBuild.currentResult}", webhookUrl: "${TEAMS_URL}"
            }        
        }
}
