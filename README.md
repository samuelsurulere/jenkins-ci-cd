# loan-prediction
This project is based on predicting if a customer will default on a requested loan. The prediction will be determined by data collected about the customer's personal and financial history.


### Command to run the deployed app in docker container

        docker build -t jenkins-ci-cd:latest .

        docker run -p 8501:8501 --name streamlit_app loan-defaulter:1.0

        docker push jenkins-ci-cd:latest

        docker exec web_app python predicting_loan_defaulters/training_pipeline.py

        docker exec web_app pytest -v --junitxml testResults.xml .

        docker cp web_app:/code/src/testResults.xml .

        docker exec -d -w /code web_app python main.py

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