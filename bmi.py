import streamlit as st
    
w = st.number_(input('請輸入體重(KG)？'))
h = st.number_(input('請輸入身高(M)？'))
confirm_input = st.button('請輸入確認')

if confirm_input:
    bmi = w/(h*h)
    st.write('BMI為', bmi)
    if (bmi < 18):
      st.write('體重過輕')
    elif (bmi < 24):
      st.write('體重正常')
    elif (bmi < 27):
      st.write('體重過重')
    else:
      st.write('體重肥胖')
