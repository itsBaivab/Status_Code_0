import streamlit as st
import QR_Gen
from PIL import Image
# Appname
st.set_page_config(page_title="AI QR Code Genarator")

st.title("AI QR Code Generator")

with st.form(key="form1"):
    st.text('Fill info')
    PF = st.file_uploader('Upload a jpg or jpeg')
    FirstName = st.text_input('Enter  First name')
    LastName = st.text_input('Enter  Last name')
    Address = st.text_input('Enter your address')
    Birthday = st.date_input('Your birthday')
    Gender = st.radio('Gender', ['Male', 'Female', 'Others'])
    Contact = st.number_input('Enter your contact number')
    anothercontact = st.number_input('Enter another contact number')
    Contact_Email = st.text_input('Enter Contact email address')
    FathersName = st.text_input("Enter  Father's name")
    MothersName = st.text_input('Enter  Mother"s name')
    SchoolName = st.text_input('Enter your school name')
    SchoolAddress = st.text_input('Enter your school address')
    city = st.text_input(' City')
    state = st.text_input(' State')
    ZipCode = st.number_input(' Zip code')
    Country = st.text_input(' Country')
    Addhar = st.number_input(' Last four digit of Addhar number')
    Blood_Group = st.selectbox('Blood Group', ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    Identification_mark = st.text_input('Identification mark')
    Allergenes = st.text_input('Allergenes')
    submit = st.form_submit_button(on_click=None)
Final = str(FirstName)+'#'+str(LastName)+'#'+str(FathersName)+'#'+str(MothersName)+'#'+str(Birthday)+'#'+str(Gender)
if submit:
    st.write(FirstName, LastName, Birthday, FathersName, MothersName, Gender)
    st.success("In the next step enter your prompt")
