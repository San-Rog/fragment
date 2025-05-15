import streamlit as st
import pyautogui 

if "clicks" not in st.session_state:
    st.session_state.clicks = 0
if "mult" not in st.session_state:
    st.session_state.mult = 0

@st.fragment
def count_to_five():
    if st.button("Botão do fragmento!"):
        st.session_state.clicks += 1
        if st.session_state.clicks % 5 == 0:
            st.session_state.mult += 1
            st.rerun()
    return

count_to_five()
st.header(f"Contagem de cliques de 5 em 5: {st.session_state.mult}", 
          help="Para cada cinco cliques, o contador é acionado.")

if st.button("Cheque o contador de cliques do fragmento", 
             help="Verifica quantos cliques foram dados no botão de fragmento."):
    st.toast(f"##### Total clicks: {st.session_state.clicks}")
if st.button("Fecha tela"):
    pyautogui.hotkey("ctrlleft", "F4")
