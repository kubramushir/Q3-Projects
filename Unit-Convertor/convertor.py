#Project 01: Unit Convertor
#Build a Google Unit Convertor using Python and Streamlit:

import streamlit as st
st.markdown(
    """
   <style>
    body{
         background-color:black ; 
         color: white;
    }
    .stApp{
       background: linear-gradient(135deg, lightgray, paleblue);
       padding:30px;
       border-radius:15px;
       box-shadow:0px 10px 30px rgba(0,0,0,0.3);
    }
    h1{
       text-align:centre;
       font-size:36px;
       color:black;
    }
    .stButton>button{
       background:linear-gradient(45deg, lightblue,navyblue);
       color:white;
       font-size: 18px;
       padding: 10px 2opx;
       border-radius: 10px;
       transition:0.3s;
       box-shadow: 0px 5px 15px rgba(0,201,255,0.4);
    }
    .stButton>button: hower{
       transform: scale(1.05);
       background:linear-gradient(45deg, #navyblue, #skyblue);
       color:white;
    }
    .result-box{
        font-size:20px
        font-weight: bold;
        text-align: centre;
        background: grey ;
        padding: 25px;
        border-radius:10px;
        marging-top:20px;
        box-shadow:0px 5px 15px rgba(0,201,25,0.3);
    }
    .footer{
        text-align:centre;
        marging-top:50px;
        font-size: 14px;
        color:white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#title and description
st.markdown("<h1>🚀 Universal Unit Convertor</h1>", unsafe_allow_html=True)
st.write("Easily convert between units of length, weight, and temperature.")

#sidebar_type
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value= st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2= st.columns (2)

if conversion_type=="Length":
    with col1:
        from_unit= st.selectbox("From",["Meters","kilograms", "Centimeters","Milimeters", "Miles", "Yards", "Inches","Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feet"])
elif  conversion_type=="Weight":
    with col1:
        from_unit= st.selectbox("From",["Kilograms","Grams","Miligrams","Pounds","Ounces"])
    with col2:
        to_unit=st.selectbox("To",["Kilograms","Grams","Miligrams","Pounds","Ounces"]) 
elif conversion_type== "Temperature":
    with col1:
        from_unit= st.selectbox("From",["Celsius","Fahrenheit","Kelvin"])
    with col2:
        to_unit=st.selectbox("To",["Celsius","Fahrenheit","Kelvin"])

#converted function
def length_convertor(value,from_unit,to_unit):
    length_units={
        'Meters': 1,
        'Kilometers': 0.001,
        'Centimeters': 100,
        'Milimeters': 1000,
        'Miles': 0.000621371,
        'Yards': 1.09361,
        'Inches': 39.3701,
        'Feet': 3.28084
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value,from_unit,to_unit):
    weight_units={
        'Kilograms':1,
        'Grams':1000,
        'Miligrams':1000000,
        'Pounds':2.20462,
        'Ounces':35.274,
    }
    return value *weight_units[from_unit]/weight_units[to_unit]


def temperature_convertor(value,from_unit,to_unit):
    if from_unit=="Celsius":
        return (value *9/5+32) if to_unit=="Fahrenheit" else value+273.15 if to_unit=="Kelvin" else value
    elif from_unit=="Fahrenheit":
        return ((value-32)*5/9) if to_unit=="Celsius" else ((value-32)*5/9+273.15) if to_unit=="Kelvin" else value
    elif from_unit=="Kelvin":
        return (value-273.15) if to_unit=="Celsius" else ((value-273.15)*9/5+32) if to_unit=="Fahrenheit" else value
    return value


#button for conversion
if st.button("🤖Convert"):
    if conversion_type=="Length":
        result = length_convertor(value, from_unit, to_unit) 
    elif conversion_type=="Weight":
        result=weight_convertor(value,from_unit, to_unit)
    elif conversion_type=="Temperature":
        result=temperature_convertor(value,from_unit,to_unit)


    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

#footer
st.markdown("<div class='footer'>Developed by Kubra Muhir </div>", unsafe_allow_html=True)




