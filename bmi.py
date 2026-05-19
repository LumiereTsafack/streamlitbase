import streamlit as st
st.title("Welcome to the BMI Calculator app")

weight = st.number_input("Enter your weight: ")
status = st.radio("select your height format",("cm","meters","feet"))

try: 
     if status == "cm":
         height = st.number_input("centimeters")
         bmi= weight / ((height/100)**2)
     elif status == "meters":
         height = st.number_input("meters")
         bmi= weight / ((height)**2)
     else:
          height = st.number_input("feet")
          bmi= weight / ((height/3.2808)**2)
     
except :
     print("Zero division error")

if (st.button("Calculate BMI")):
    st.write("Your BMI index is {}.".format(round(bmi, 2)))

    if bmi < 16:
         st.error('You are extremely underweight')
    elif (bmi >= 16) and (bmi < 18.5):
         st.warning('You are underweight')
    elif (bmi >= 18.5) and (bmi < 25):
         st.success('You are healthy')
    elif (bmi >= 25) and (bmi < 30):
            st.warning('You are overweight')
    elif (bmi >= 30) and (bmi < 35):
            st.error('You are moderately obese')
    st.balloons()
    
