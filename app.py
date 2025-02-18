import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

 # Função para verificar o login
def check_password():
    """Verifica se o usuário digitou a senha correta."""
    def password_entered():
        """Verifica se a senha está correta."""
        if st.session_state["password"] == os.getenv("PASSWORD"): # Substitua "senha_correta" pela senha desejada
            st.session_state["authentication_status"] = True
        else:
            st.session_state["authentication_status"] = False
            st.error("Senha incorreta")
 

    if "authentication_status" not in st.session_state:
        st.session_state["authentication_status"] = False
 

    if not st.session_state["authentication_status"]:
        st.text_input("Senha", type="password", on_change=password_entered, key="password")
        return False
    elif st.session_state["authentication_status"]:
        return True
 

if check_password():
    # Cria um dataframe hipotético
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    df = pd.DataFrame(data)
 

    # Exibe o dataframe na página
    st.write("## Página protegida")
    st.dataframe(df)