pipeline {
  agent any
  
  parameters {
    string(name: 'DEV_ENVIRONMENT', defaultValue: 'development', description: 'development environment')
    string(name: 'STAGING_ENVIRONMENT', defaultValue: 'staging', description: 'staging environment')
    string(name: 'PROD_ENVIRONMENT', defaultValue: 'production', description: 'production environment')
  }

  stages {

    stage('Install App Dependencies') {
        steps {
          sh 'cd cidr_convert_api/python && pip install virtualenv && virtualenv samuel && source samuel/bin/activate  && pip install -r requirements.txt' 
        }
      }

    stage('Build Image') {
      steps {
        sh 'echo "docker build phase"'
        sh 'docker build -f cidr_convert_api/python/Dockerfile -t name/samuel:${BUILD_NUMBER} .'
      }
    }

    stage('Push Image') {
      steps{
        sh 'echo "Pushing Image to Docker Hub"'
        sh 'docker push name/samuel:${BUILD_NUMBER}'
      }
    }   
    stage('Deploy to Dev') {
      when {branch 'dev'}
      environment {
          KUBECONFIG = credentials('kubeconfig')
      }
      
      steps {
        sh 'kubectl --kubeconfig=${KUBECONFIG} --namespace=${DEV_ENVIRONMENT} --record deployment/api set image deployment/api api=name/samuel:${BUILD_NUMBER}' 
      }
    }

    stage('Deploy to Staging') {
      when {branch 'dev'}
      input{message "Deploy staging deployment?"}
      environment {
          KUBECONFIG = credentials('kubeconfig')
      }
      steps {
        sh 'kubectl --kubeconfig=${KUBECONFIG} --namespace=${STAGING_ENVIRONMENT} --record deployment/api set image deployment/api api=name/samuel:${BUILD_NUMBER}' 
      }
    }

    
    stage('Deploy to Production') {
      when {branch 'master'}
      input{message "Deploy production deployment?"}
      environment {
          KUBECONFIG = credentials('kubeconfig')
      }
      steps {
        sh 'kubectl --kubeconfig=${KUBECONFIG} --namespace=${PROD_ENVIRONMENT} --record deployment/api set image deployment/api api=name/samuel:${BUILD_NUMBER}' 
      }
    }
  }
}
