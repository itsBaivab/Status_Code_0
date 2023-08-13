# Status_Code_0
QwRAI:
 
# QR Art Generator using Stable Diffusion and Control Net

![Project Logo](link_to_your_logo_image.png)

## About
This project is developed by Team Cryptic Wizards with the goal of creating a Streamlit deployed application that generates QR Art using stable diffusion and control net techniques. The application allows users to generate custom QR codes that incorporate various information. 

## Why do we need QR.AI?

We've designed this keeping child safety in mind. The catch is- AI generates a QR. We scan it, which retrieves the information  in the QR, passes it through a PDF file, and then shows the downloadable link for the PDF file. 

How did we bring the user case of child safety into this? 
Every QR has an unique art, which blends into the QR. Hence, its favorable to kids and they'd like wearing it on a badge or on their bags. 
In our user case, we've defined form fields such as name, dob, etc. so if we need any information about any child, we can scan the QR code and find out their guardian's number and get them back to their destination safely. 

## PRIVACY CONCERNS:
One might consider this as a breach of personal information as the QR code would cause security issues as anyone could access it. This is why, we've incorporated AI art, so that its hard for people to tell its a QR code in the first place. People would rather wear them as a fashion statement, and rarely would someone figure out the QR unless it isn't looked at very closely.

## Features

- Generate unique QR Art using stable diffusion and control net.
- Fill out a user-friendly form to personalize QR codes.
- Support for information like Name, Date of Birth, Address, Parent's Names, Gender, Contact Details, School Info, and more.
- User-friendly interface powered by Streamlit.

  ## Technical Specifications:
  - We've used Huggingface API
  - Control Net and Stable Diffusion
  - Streamlit to build website interface
  - MongoDB for backend

 
