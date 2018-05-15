node{

   stage('############### Checking out repo ##################') {
    checkout scm
    }

    stage('############### Building project ##################') {      
      sh  "docker build --rm -t testing:latest ."

    }

    stage('############### Running Tests ##################') {

      sh '''docker run testing:latest ./test
 
      if [ $? -ne 0 ]; then
              echo "Tests did not pass! Fix it please."
              exit 1
      fi
       
          '''
    }

    stage('############### Stopping services ##################') {      
      sh  "/usr/local/bin/docker-compose down"
    }
    

    stage('############### Starting Services ##################') {      
      sh  "/usr/local/bin/docker-compose up -d"
    }

    stage('############### Printing logs ##################') {      
      sh  '''/usr/local/bin/docker-compose logs --tail="all" '''

    }

  }
