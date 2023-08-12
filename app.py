import streamlit as st
import QR_Gen
from PIL import Image
# Appname
st.set_page_config(page_title="AI QR Code Genarator")

st.title("AI QR Code Generator")
#Form UI
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
#image =Image.open('/tmp/gradio/175a626d1211ba6457ba3d3a4b5bd71b6938b029/tmpo9vdn2tg.png')




# Controlnet UI
with st.form(key= "form2"):
    st.text("QR Genaration")
    # QRCodeContent = st.text_input('')
    p_prompt = st.text_input('Positive Prompt')
    n_prompt = st.text_input('Negetive Prompt')
    conditioning_scale = st.slider('Controlnet Conditioning Scale', 0.0, 5.0)
    strength = st.slider('Strenght', 0.0, 1.0)
    guidance_scale = st.slider('Guidance Scale', 1.00, 50.00)
    sampler = str(st.selectbox('Sampler', ['DPM++ Karras SDE', 'DPM++ Karras', 'Heun', 'Euler', 'DDIM','DEIS']))
    seed = st.slider('Seed value', -1,  9999999999)
    genarate = st.form_submit_button(on_click=None)
positive_prompt = str(p_prompt)
negative_prompt = str(n_prompt)    
Sampler= str(sampler)
Conditioning_scale = float(conditioning_scale)
Strength = float(strength)
Guidance_scale = float(guidance_scale)
Seed = int(seed)

URL =""
if genarate:
    genimg = QR_Gen.generate_qr_code(URL,positive_prompt, negative_prompt,Sampler,Strength,Conditioning_scale,Guidance_scale,Seed)
    image = Image.open(genimg)
    st.image(image, caption='Genarated QR code')
    st.success("QR code genarated successfully")