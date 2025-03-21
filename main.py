import streamlit as st

st.title('hello world')
st.write('welcome to streamlit app')

if st.button('say hello'):
    st.text('hello streamlit')

name=st.text_input('please enter your name: ')
if name:
    st.write(f'hello,{name}!')

if st.file_uploader("please upload aa file",type=["abc.txt","def.csv"]):
    st.write("thanks for uploading a file..")