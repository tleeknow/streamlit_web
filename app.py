import streamlit as st

st.title("선후배 매칭 서비스")

st.write("환영합니다!")

name = st.text_input("이름")

if st.button("확인"):
    st.success(f"{name}님 환영합니다!")
