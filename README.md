# loan-prediction
This project is based on predicting if a customer will default on a requested loan. The prediction will be determined by data collected about the customer's personal and financial history.


### Command to run the deployed app in docker container

        docker build -t jenkins-ci-cd:latest .

        docker run -d -it --name web_app -p 8080:8080 jenkins-cicd:latest bash
        
        docker push sammiguy/my-jenkins-project:tagname

        docker push jenkins-ci-cd:latest

        docker exec web_app python predicting_loan_defaulters/training_pipeline.py

        docker exec web_app pytest -v --junitxml testResults.xml .

        docker cp web_app:/code/src/testResults.xml .

        docker exec -d -w /code web_app python main.py

To push the docker image to Docker hub, follow these steps:

        docker tag <username>/<repository_name> <username>/<new_repo_name>
        docker login -u <username> -p <password>
        docker push <username>/<new_repo_name>

Number 3 is currently not working. Still trying to figure out how to push docker build to docker hub



Example of JSON 
{
        "Age": 34,
        "Income": 80000,
        "LoanAmount": 700000,
        "CreditScore": 734,
        "MonthsEmployed": 24,
        "NumCreditLines": 1,
        "InterestRate": 7.5,
        "LoanTerm": 120,
        "DTIRatio": 0.5,
        "Education": "PhD",
        "EmploymentType": "Full-time",
        "MaritalStatus": "Single",
        "HasMortgage": "No",
        "HasDependents": "No",
        "LoanPurpose": "Home",
        "HasCoSigner": "No"
}