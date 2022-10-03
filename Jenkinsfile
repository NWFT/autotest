pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('pip') {
      steps {
        sh 'python3 -m pip install --upgrade pip'
      }
    }
    stage('hello') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
  }
}
