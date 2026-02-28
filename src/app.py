import streamlit as st
from services.credit_card_service import analyze_credit_card
from services.blob_service import upload_file_to_blob

def config_interface():
    st.title("Upload de Arquivo DIO - Desafio  Azure AI Document Intelligence")
    uploaded_file = st.file_uploader("Escolha um arquivo para upload", type=["pdf", "jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = upload_file_to_blob(uploaded_file, fileName)
        if blob_url:
             st.success("Arquivo enviado com sucesso!")
             credit_card_info = analyze_credit_card(blob_url)
             show_analysis_result(blob_url, credit_card_info)
        else:
            st.error("Falha ao enviar o arquivo para o Azure Blob Storage.")
  
def show_analysis_result(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada para análise", use_column_width=True)
    st.subheader("Resultados da Análise do Cartão de Crédito:")
    if credit_card_info:
        st.write("**Número do Cartão:**", credit_card_info.get("card_number", "Não identificado"))
        st.write("**Nome do Titular:**", credit_card_info.get("cardholder_name", "Não identificado"))
        st.write("**Data de Validade:**", credit_card_info.get("expiration_date", "Não identificado"))
        st.write("**Bandeira do Cartão:**", credit_card_info.get("card_brand", "Não identificado"))
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão de Crédito Inválido</h1>", unsafe_allow_html=True)
        st.warning("Este cartão de crédito não é válido.")

if __name__ == "__main__":
    config_interface()
