import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import glob
import os
import re
import inspect


st.title(":blue[New Employee Survey] :sunglasses:")
st.markdown("###### Please answer honestly and to the best of your ablilites")

educ = st.selectbox("Education Level", 
           options = ["--Make a selection--",
                      "High School Diploma",
                      "Some College",
                      "College Degree",
                         "Graduate Degree"])

if educ == "--Make a selection--":
    educ = ""
elif educ == "High School Diploma":
     educ = 1
elif educ == "Some College":
    educ = 2
elif educ == "College Degree":
    educ = 3
else:
    educ = 4


age = st.selectbox("Age Group", 
           options = ["--Make a selection--",
                      "18-30",
                      "31-45",
                      "46-65",
                         "66+",
                         "Prefer not to Answer"])

if age == "--Make a selection--":
    age = ""
elif age =="Young Adult":
     age = 1
elif age == "Adult":
    age = 2
elif age == "Senior":
    age = 3
elif age == "Prefer not to answer":
    age = 4
else:
    age= 0


income = st.selectbox("Household Income", 
           options = ["--Make a selection--",
                      "< $10,000",
                     "$10,000 to $30,000",
                     "$30,000 to $50,000", 
                    "$50,000 to $75,000",
                        "$100,000 to $150,000",
                        "$150,000 +"])


if income == "--Make a selection--": 
    income = ""
elif income == "Young Adult":
     income = 1
elif income == "Adult":
    income = 2
elif income == "Senior":
    income = 3
elif income == "Prefer not to answer":
    income = 4
else:
     income = 0

gender = st.selectbox("Gender Identity", 
           options = ["--Make a selection--",
                      "Male",
                     "Female",
                     "Other" ])

if gender == "--Make a selection--":
    gender = ""
elif gender == "Male":
     gender = 0
elif gender == "Female":
    gender = 1
else:
     gender = "Other"


married = st.radio(label="Are you married?", options=["Yes", "No"], horizontal=True)

parent = st.radio(label="Are you a parent?", options=["Yes", "No"], horizontal=True)


answer = st.selectbox(
    label="Do you have a LinkedIn account?",
    options=("Yes", "No", "I don't know what that is."),
)
if answer in ("No", "I don't know what that is."):
    st.write("Here are some resources for [LinkedIn](https://www.linkedin.com/)")

center = st.columns(1)
if center[0].button("Submit", use_container_width=True):
    st.warning('''Congratuations! You have completed the survey. :balloon:''')

if st.button("Reset", type="primary"):
    st.session_state.clear()



### For developer use only

#df = pd.DataFrame({
#     "office": ["MIA", "NY", "DC", "BOS"],
#     "sales": [100, 200, 350, 225]
# })

# st.write(df)

df = pd.read_csv("social_media_usage.csv")
s = pd.DataFrame(df)

def clean_sm(x):
    return np.where(x == 1, 1, 0)

s = pd.DataFrame(s[['income', 'educ2', 'par', 'marital', 'gender','age', 'web1a']])
s['sm_li'] = clean_sm(s['web1a'])

s['income'] = np.where(s['income'] > 9, np.nan, s['income'])
s['educ2'] = np.where(s['educ2'] > 8, np.nan, s['educ2'])
s['age'] = np.where(s['age'] > 98, np.nan, s['age'])
s['par'] = clean_sm(s['par'])
s['marital'] = clean_sm(s['marital'])
s['gender'] = np.where(s['gender'] > 2, np.nan, s['gender'])


st.write(s)
s = s.dropna()
print("'s'DataFrame :\n", s)

ss_model = pd.DataFrame({
    'income': [8, 8],
    'educ': [7, 7],
    'par': [0, 0],
    'marital': [1, 1],
    'gender': [0, 0],
    'age': [42, 82]
})

alt_plot = alt.Chart(s).mark_circle().encode(x="s['sm_li']",
    y="s[['income', 'educ2', 'par', 'marital', 'gender','age']]",
    tooltip=["LinkedIn User", "Characterisitcs "]).interactive()
alt_plot

st.dataframe(s.style.highlight_max(axis=0,color="yellow"))
