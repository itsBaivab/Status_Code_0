
import streamlit as st
import QR_Gen
import pdf_create as pdf
from PIL import Image
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))

def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))

def layout(*args):
    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="white",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def footer():
    myargs = [
        "Made in ",
        image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4', width=px(25), height=px(25)),
        " with ❤️ by Cryptic Wizards",
        link("https://twitter.com/ChristianKlose3", "@ChristianKlose3"),
        br(),
        link("https://buymeacoffee.com/chrischross", image('https://i.imgur.com/thJhzOO.png')),
    ]
    layout(*myargs)

# Appname
st.set_page_config(page_title="AI QR Code Generator",layout="wide")

st.title("AI QR Code Generator")

# Split the page into two columns
col1, col2 = st.columns(2,gap='medium')









# Form UI in the first column
with col1:
    st.text('Fill info')
    with st.form(key="form1"):
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        Name = st.text_input('Enter First name')
        Address = st.text_input('Enter your address')
        Birthday = st.date_input('Your birthday')
        Gender = st.radio('Gender', ['Male', 'Female', 'Others'])
        Contact = st.number_input('Enter your contact number')
        anothercontact = st.number_input('Enter another contact number')
        Contact_Email = st.text_input('Enter Contact email address')
        FathersName = st.text_input("Enter Father's name")
        MothersName = st.text_input('Enter Mother"s name')
        SchoolName = st.text_input('Enter your school name')
        SchoolAddress = st.text_input('Enter your school address')
        city = st.text_input('City')
        state = st.text_input('State')
        ZipCode = st.number_input('Zip code')
        Country = st.text_input('Country')
        Addhar = st.number_input('Last four digit of Addhar number')
        Blood_Group = st.selectbox('Blood Group', ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
        Identification_mark = st.text_input('Identification mark')
        Allergenes = st.text_input('Allergenes')
        submit = st.form_submit_button(label="Submit")

# Controlnet UI in the second column
with col2:
    st.text("QR Generation")
    with st.form(key="form2"):
        p_prompt = st.text_input('Positive Prompt')
        n_prompt = st.text_input('Negative Prompt')
        conditioning_scale = st.slider('Controlnet Conditioning Scale', 0.0, 5.0)
        strength = st.slider('Strength', 0.0, 1.0)
        guidance_scale = st.slider('Guidance Scale', 1.00, 50.00)
        sampler = st.selectbox('Sampler', ['DPM++ Karras SDE', 'DPM++ Karras', 'Heun', 'Euler', 'DDIM', 'DEIS'])
        seed = st.slider('Seed value', -1, 9999999999)
        genarate = st.form_submit_button(label="Generate")

# Process form submissions and getting the link of the generated pdf
if submit:
    st.write(Name,  Birthday, FathersName, MothersName, Gender)
    if uploaded_file is not None:
        st.subheader("Uploaded Image")
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
        save_path = "uploaded_image.png"
        pil_image = Image.open(uploaded_file)
        pil_image.save(save_path)
        st.success(f"Image saved as {save_path}")
    else:
        st.info("Please upload an image.")
        
        
       
    fileURL = pdf.create_qr_code_pdf(save_path,Name,Birthday,FathersName,MothersName,Address,Gender,Contact,anothercontact,Contact_Email,SchoolName,SchoolAddress,city,state,ZipCode,Country,Blood_Group,Identification_mark,Allergenes)
    st.success("In the next step enter your prompt")
    st.write(fileURL)
#QR code generation
if genarate:
    positive_prompt = str(p_prompt)
    negative_prompt = str(n_prompt)
    Sampler = str(sampler)
    Conditioning_scale = float(conditioning_scale)
    Strength = float(strength)
    Guidance_scale = float(guidance_scale)
    Seed = int(seed)
    URL = "this is a qr code ai art generator"
    
    genimg = QR_Gen.generate_qr_code(fileURL, positive_prompt, negative_prompt, Sampler, Strength, Conditioning_scale, Guidance_scale, Seed)
    image = Image.open(genimg)
    st.image(image, caption='Generated QR code')
    st.success("QR code generated successfully")

# Footer
if __name__ == "__main__":
    footer()
