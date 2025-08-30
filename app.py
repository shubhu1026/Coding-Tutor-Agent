import streamlit as st
from tutor.tutor_client import TutorClient

st.set_page_config(page_title="AI Coding Tutor", layout="wide")

st.title("AI Coding Tutor")
st.write("Paste your code or error below, and I will explain it, provide fixes, and suggest improvements.")

tutor = TutorClient()

# Callback to clear text area
def clear_text():
    st.session_state["code_input"] = ""
    st.session_state["result"] = None  

# Initialize session state
if "code_input" not in st.session_state:
    st.session_state["code_input"] = ""
if "result" not in st.session_state:
    st.session_state["result"] = None

# Text area linked to session state
code_input = st.text_area(
    "Enter your code or error here:",
    height=200,
    key="code_input"
)

col1, col2 = st.columns(2)
with col1:
    if st.button("Ask Tutor"):
        if not st.session_state["code_input"].strip():
            st.warning("Please paste some code or error first.")
        else:
            with st.spinner("Thinking..."):
                st.session_state["result"] = tutor.ask_tutor(st.session_state["code_input"])

with col2:
    st.button("Clear", on_click=clear_text)

# Display results if available
result = st.session_state.get("result")
if result:
    st.subheader("Explanation")
    st.write(result.get("explanation", ""))

    if result.get("fix", "No fix needed.") != "No fix needed.":
        st.subheader("Fix")
        st.write(result["fix"])
        if result.get("fixed_code"):
            st.subheader("Fixed Code")
            st.code(result["fixed_code"])

    if result.get("improvement", "No improvement needed.") != "No improvement needed.":
        st.subheader("Improvement")
        st.write(result["improvement"])
        if result.get("improved_code"):
            st.subheader("✨ Improved Code")
            st.code(result["improved_code"])
