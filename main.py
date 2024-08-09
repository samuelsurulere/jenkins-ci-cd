from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn, gunicorn
from predicting_loan_defaulters.predict import generate_predictions
import numpy as np
import pandas as pd


app = FastAPI(
    title='Predicting Loan Defaulters',
    description='Predicting Loan Defaulters API',
    version='1.0',
)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoanDefaulters(BaseModel):
    Age: int
    Income: int
    LoanAmount: int
    CreditScore: int
    MonthsEmployed: int
    NumCreditLines: int
    InterestRate: float
    LoanTerm: int
    DTIRatio: float
    Education: str
    EmploymentType: str
    MaritalStatus: str
    HasMortgage: str
    HasDependents: str
    LoanPurpose: str
    HasCoSigner: str


@app.get("/")
def index():
    return {"message": "Welcome to the Loan Defaulter Prediction API using FastAPI - CI CD Jenkins"}

@app.post("/prediction_api")
def predict_loan_defaulters(data: LoanDefaulters):
    data = data.model_dump()
    prediction = generate_predictions([data])["prediction"][0]
    if prediction == 'Defaulter':
        return {"prediction": "This borrower is likely to default payment"}
    else:
        return {"prediction": "This borrower is not likely to default payment"}


@app.post("/prediction_api_ui")
def predict_loan_defaulters_ui(
    Age: int,
    Income: int,
    LoanAmount: int,
    CreditScore: int,
    MonthsEmployed: int,
    NumCreditLines: int,
    InterestRate: float,
    LoanTerm: int,
    DTIRatio: float,
    Education: str,
    EmploymentType: str,
    MaritalStatus: str,
    HasMortgage: str,
    HasDependents: str,
    LoanPurpose: str,
    HasCoSigner: str
):
    input_data = [
        Age, Income, LoanAmount, CreditScore, MonthsEmployed, 
        NumCreditLines, InterestRate, LoanTerm, DTIRatio, 
        Education, EmploymentType, MaritalStatus, HasMortgage, 
        HasDependents, LoanPurpose, HasCoSigner
    ]
    cols = [
        'Age', 'Income', 'LoanAmount', 'CreditScore', 'MonthsEmployed', 
        'NumCreditLines', 'InterestRate', 'LoanTerm', 'DTIRatio', 
        'Education', 'EmploymentType', 'MaritalStatus', 'HasMortgage', 
        'HasDependents', 'LoanPurpose', 'HasCoSigner'
    ]
    data_dict = dict(zip(cols, input_data))
    prediction = generate_predictions([data_dict])["prediction"][0]
    if prediction == 'Defaulter':
        return {"prediction": "This borrower is likely to default payment"}
    else:
        return {"prediction": "This borrower is not likely to default payment"}



if __name__ == '__main__':
    uvicorn.run(app)