import streamlit as st
from streamlit.proto.NumberInput_pb2 import NumberInput
import model
import joblib
import os
import numpy as np

st.set_page_config(page_title="CredScore Calculator",
                   page_icon="📵", layout="wide")

curr_path = os.path.dirname(os.path.realpath(__file__))

feature_cols = joblib.load(curr_path + "/features.joblib")

def format_fun(option):
    return choice[option]

def formtchk(option):
    return chk_acc_choice[option]

def formtsav(option):
    return sav_choice[option]

def formtpurp(option):
    return pur_choice[option]

def formtemp(option):
    return emp_choice[option]

def formthis(option):
    return cre_his_choice[option]

def formdg(option):
    return D_G_choice[option]

def formsex(option):
    return sex_choice[option]

def formhouse(option):
    return Hous_choice[option]

def formjob(option):
    return job_choice[option]

def formforeign(option):
    return for_choice[option]

def formprop(option):
    return prop_choice[option]

with st.form("prediction_form"):
    st.header("Enter the Details to calulate credit Risk")
    st.write("click [here](https://credit-vis.herokuapp.com/) to see visualization")
    Credit_Amount = st.number_input("Enter Credit Amount: ",value=0, format="%d")
    Age = st.number_input("Age: ", value=0, format="%d")
    Duration = st.number_input("Duration(in Months): ", value=0, format="%d")
    Installment_rate = st.number_input("Enter the installment rate: ")

    choice={0:"bank",1:"none",2:"store"}
    Install_plans=st.selectbox("select the installment plan:",options=list(choice.keys()),format_func=format_fun)


    chk_acc_choice={0:"No account",1:"Little Amount",2:"Moderate amount",3:"Rich"}
    Checking_Account=st.selectbox("Select the Checking account type:",options=list(chk_acc_choice.keys()),format_func=formtchk)

    sav_choice={0:"No account",1:"Little Amount",2:"Moderate amount",3:"Quite Rich",4:"Rich"}
    Savings_Account =st.selectbox("Select the savings account type:",options=list(sav_choice.keys()),format_func=formtsav)

    pur_choice={0:"Others",1:"business",2:"car (new)",3:"car (used)",4:"domestic appliances",5:"education",6:"furniture/equipment",7:"radio/television",8:"repairs",9:"retraining"}
    Purpose=st.selectbox("Select the purpose for Loan:",options=list(pur_choice.keys()),format_func=formtpurp)

    No_of_credits=st.number_input("Enter No of existing credit at the bank(1-4):", value=0, format="%d")


    emp_choice={0:"No Employement",1:"Amateur Employee",2:"Professional Employee",3:"Expert Employee",4:"Master"}
    Employement = st.selectbox("Select the employement skills",options=list(emp_choice.keys()),format_func=formtemp)

    cre_his_choice={0:"All credits at this bank paid back duly",1:"Critical Account",2:"Delay in paying off in the past",3:"Existing credits paid back duly till now",4:"No credits taken/ all credits paid back duly"}
    Credit_History=st.selectbox("Select the Credit History Type:",options=list(cre_his_choice.keys()),format_func=formthis)


    D_G_choice={0:"Co-applicant",1:"Guarantor",2:"None"}
    Deb_gran=st.selectbox("Select Debtor/Guarantors:",options=list(D_G_choice.keys()),format_func=formdg)

    sex_choice={0:"Female",1:"Male"}
    sex=st.selectbox("Select Gender:", options=list(sex_choice.keys()),format_func=formsex)

    Hous_choice = {0: "For Free", 1: "Own House", 2: "For Rent"}
    Housing = st.selectbox("Select Housing type:", options=list(Hous_choice.keys()), format_func=formhouse)

    job_choice={0:"Unemployed/ unskilled - non-resident",1:"Unskilled - resident",2:"Skilled employee / official",3:"Highly qualified employee/ officer"}
    Job_type =st.selectbox("Select the type of Job:", options=list(job_choice.keys()),format_func=formjob)

    for_choice={0:"No",1:"Yes"}
    Foreigner = st.selectbox("Are you a Foreigner?",options=list(for_choice.keys()),format_func=formforeign)

    prop_choice={0:"Unknown / no property",1:"Building society savings agreement/ life insurance",2:"Car or other",3:"Real Estate"}
    Property = st.selectbox("Select the property Type:",options=list(prop_choice.keys()),format_func=formprop)

    submit_val = st.form_submit_button("Predict Credit Risk")

if submit_val:
    attributes = np.array([Checking_Account,Duration,Purpose,Credit_Amount,No_of_credits,Employement,Savings_Account,
                           Deb_gran,Credit_History,Installment_rate,Install_plans,sex,Age,Housing,Job_type,Property,Foreigner])
    print("attributes value")
    status = model.predict(attributes.reshape(1, -1))
    if status:
        st.error("Bad Credit Rating")
    else:
        st.success("Good Credit Rating")
        st.balloons()