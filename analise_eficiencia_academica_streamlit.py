import streamlit as st
import pandas as pd



st.set_page_config(page_title="Projeto_Analise")

with st.container():
    st.title("Eficiência Acadêmica - 2021")
    st.write("Informações sobre o desempenho dos alunos dos Institutos Federais")
    st.write("DataSet disponivel em: [dadosabertos.mec.gov.br](https://dadosabertos.mec.gov.br/pnp/item/180-2021-microdados-eficiencia-academica)")





@st.cache_data 
def carregar_dados():
    tabela = pd.read_csv("2021 - Eficiência Acadêmica.csv", delimiter=';')
    return tabela

with st.container():
    st.write("---")

    dados = carregar_dados()

    st.subheader("Qual a média da idade dos alunos evadidos?")
    media_idade_evadidos = dados.loc[dados['Categoria da Situação'] == 'Evadidos', 'Idade'].mean()
    st.write("Média da idade dos alunos evadidos:", media_idade_evadidos)

    st.subheader("Qual o desvio padrão da idade dos alunos evadidos?")
    desvio_padrao_idade_evadidos = dados.loc[dados['Categoria da Situação'] == 'Evadidos', 'Idade'].std()
    st.write("Desvio padrão da idade dos alunos evadidos:", desvio_padrao_idade_evadidos)

    # Gráfico de barras com média e desvio padrão
    st.bar_chart({"Média": [media_idade_evadidos], "Desvio Padrão": [desvio_padrao_idade_evadidos]})





with st.container():
    st.write("---")
    st.subheader("Evasão por Instituições")

    qnt_intituicoes = st.selectbox("Selecione a Quantidade", ["5", "10", "15", "20"])
    num_intituicoes = int(qnt_intituicoes)
    dados = carregar_dados()

    # Filtrando os dados para incluir apenas alunos evadidos
    alunos_evadidos = dados[dados['Categoria da Situação'] == 'Evadidos']

    top_instituicoes_evadidos = alunos_evadidos['Instituição'].value_counts().head(num_intituicoes)

    if qnt_intituicoes == "5":
         st.subheader("Top 5 instituições com a maior quantidade de alunos evadidos:")
    elif qnt_intituicoes == "10":
        st.subheader("Top 10 instituições com a maior quantidade de alunos evadidos:")
    elif qnt_intituicoes == "15":
        st.subheader("Top 15 instituições com a maior quantidade de alunos evadidos:")
    elif qnt_intituicoes == "20":
        st.subheader("Top 10 instituições com a maior quantidade de alunos evadidos:")

    st.write(top_instituicoes_evadidos)
    st.bar_chart(top_instituicoes_evadidos)




with st.container():
    st.write("---")
    st.subheader("Concluintes por Instituições")

    qnt_intituicoes_c = st.selectbox("Selecione a Quantidade", ["5", "10", "15", "20"], key="selectbox_concluintes")
    num_intituicoes_c = int(qnt_intituicoes_c)

    dados = carregar_dados()

    # Filtrando os dados para incluir apenas alunos concluintes
    alunos_concluintes = dados[dados['Categoria da Situação'] == 'Concluintes']

    # Obtendo as top 5 instituições com a maior quantidade de alunos concluintes
    top_instituicoes_concluintes = alunos_concluintes['Instituição'].value_counts().head(num_intituicoes_c)

    if qnt_intituicoes_c == "5":
         st.subheader("Top 5 instituições com a maior quantidade de alunos concluintes:")
    elif qnt_intituicoes_c == "10":
        st.subheader("Top 10 instituições com a maior quantidade de alunos concluintes:")
    elif qnt_intituicoes_c == "15":
        st.subheader("Top 15 instituições com a maior quantidade de alunos concluintes:")
    elif qnt_intituicoes_c == "20":
        st.subheader("Top 10 instituições com a maior quantidade de alunos concluintes:")


    st.write(top_instituicoes_concluintes)
    st.bar_chart(top_instituicoes_concluintes) 


with st.container():
    st.write("---")
    dados = carregar_dados()

    # Calculando a contagem de alunos por sexo
    contagem_alunos_por_sexo = dados['Sexo'].value_counts()

    # Filtrando alunos evadidos e concluintes
    alunos_evadidos = dados[dados['Categoria da Situação'] == 'Evadidos']
    alunos_concluintes = dados[dados['Categoria da Situação'] == 'Concluintes']

    # Calculando a contagem de evasão e concluintes por sexo
    evasao_por_sexo = alunos_evadidos['Sexo'].value_counts()
    concluintes_por_sexo = alunos_concluintes['Sexo'].value_counts()

    # Exibindo os resultados no Streamlit
    st.subheader("Contagem de alunos por sexo:")
    
    st.subheader("Masculino:")
    st.write("Matriculados:", contagem_alunos_por_sexo.get('Masculino', 0))
    st.write("Evasão:", evasao_por_sexo.get('Masculino', 0))
    st.write("Concluintes:", concluintes_por_sexo.get('Masculino', 0))

    st.write("\n")

    st.subheader("Feminino:")
    st.write("Matriculadas:", contagem_alunos_por_sexo.get('Feminino', 0))
    st.write("Evasão:", evasao_por_sexo.get('Feminino', 0))
    st.write("Concluintes:", concluintes_por_sexo.get('Feminino', 0))

     # Criando gráficos com o formato padrão do Streamlit
    st.subheader("Contagem Total de Alunos por Sexo:")
    st.line_chart(contagem_alunos_por_sexo)

    st.subheader("Contagem de Evasões por Sexo:")
    st.line_chart(evasao_por_sexo)

    st.subheader("Contagem de Concluintes por Sexo:")
    st.line_chart(concluintes_por_sexo)





with st.container():
    dados = carregar_dados()

    # Filtrando alunos evadidos
    alunos_evadidos = dados[dados['Categoria da Situação'] == 'Evadidos']

    # Calculando a contagem de alunos por modalidade
    contagem_alunos_modalidade = dados['Modalidade de Ensino'].value_counts()

    # Calculando a contagem de evasão por modalidade
    evasao_por_modalidade = alunos_evadidos['Modalidade de Ensino'].value_counts()

    st.subheader("Contagem de Alunos e Evasão por Modalidade:")
    

    st.write("Alunos do Ensino Presencial:", contagem_alunos_modalidade.get('Educação Presencial', 0))
    st.write("Evazão:", evasao_por_modalidade.get('Educação Presencial', 0))

    st.write("\n")

    st.write("Alunos da Ensino a Distância:", contagem_alunos_modalidade.get('Educação a Distância', 0))
    st.write("Evazão:", evasao_por_modalidade.get('Educação a Distância', 0))


            # Criando gráfico com st.area_chart
    st.subheader("Gráfico de Área: Contagem de Alunos e Evasão por Modalidade")
    chart_data = pd.DataFrame({
        'Total de Alunos': contagem_alunos_modalidade,
        'Evasão': evasao_por_modalidade
    })

    st.area_chart(chart_data, use_container_width=True)    




with st.container():
    dados = carregar_dados()

    # Calculando a contagem de evasão por estado
    evasao_por_estado = dados[dados['Categoria da Situação'] == 'Evadidos']['UF'].value_counts()

    # Calculando a quantidade total de alunos por estado
    total_alunos_por_estado = dados['UF'].value_counts()

    # Calculando a taxa de evasão por estado
    taxa_evasao_por_estado = (evasao_por_estado / total_alunos_por_estado) * 100

    # Obtendo os 5 estados com maior taxa de evasão
    top_5_estados_evasao = taxa_evasao_por_estado.sort_values(ascending=False).head(5)

    # Exibindo no Streamlit
    st.write("Top 5 estados com maior taxa de evasão:")
    st.write(top_5_estados_evasao)

    # Gráfico de barras
    st.bar_chart(top_5_estados_evasao)    