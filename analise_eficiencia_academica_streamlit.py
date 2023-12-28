import streamlit as st
import pandas as pd
from datetime import datetime



# Configurar o tema da página
st.set_page_config(
    page_title="Projeto_Analise",
    page_icon="📊",  
    layout="wide",
    initial_sidebar_state="expanded"
)




with st.container():
    st.title("Eficiência Acadêmica - 2021")
    st.write("Informações sobre o desempenho dos alunos dos Institutos Federais")
    st.write("DataSet disponivel em: [dadosabertos.mec.gov.br](https://dadosabertos.mec.gov.br/pnp/item/180-2021-microdados-eficiencia-academica)")




@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("2021 - Eficiência Acadêmica.csv", delimiter=';')
    
    # Remover linhas em que todos os elementos são nulos
    tabela_sem_nulos = tabela.dropna(how='all')
    
    return tabela_sem_nulos

with st.container():
    st.write("---")

    dados = carregar_dados()

    # Remover linhas onde 'Idade' é nulo para a categoria 'Evadidos'
    dados_sem_nulos = dados.dropna(subset=['Idade'], inplace=False)

    st.subheader("Qual a média da idade dos alunos evadidos?")
    media_idade_evadidos = dados_sem_nulos.loc[dados_sem_nulos['Categoria da Situação'] == 'Evadidos', 'Idade'].mean()
    st.write("Média da idade dos alunos evadidos (sem nulos):", media_idade_evadidos)

    st.subheader("Qual o desvio padrão da idade dos alunos evadidos?")
    desvio_padrao_idade_evadidos = dados_sem_nulos.loc[dados_sem_nulos['Categoria da Situação'] == 'Evadidos', 'Idade'].std()
    st.write("Desvio padrão da idade dos alunos evadidos (sem nulos):", desvio_padrao_idade_evadidos)

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
    st.write("---")

    st.subheader("Evasão por estado")

    qnt_estados = st.selectbox("Selecione a Quantidade", ["5", "10", "15", "20"], key="chave_unica_para_o_selectbox")
    num_estados = int(qnt_estados)

    dados = carregar_dados()

    # Calculando a contagem de evasão por estado
    evasao_por_estado = dados[dados['Categoria da Situação'] == 'Evadidos']['UF'].value_counts()

    # Calculando a quantidade total de alunos por estado
    total_alunos_por_estado = dados['UF'].value_counts()

    # Calculando a taxa de evasão por estado
    taxa_evasao_por_estado = (evasao_por_estado / total_alunos_por_estado) * 100

    # Obtendo os estados com maior taxa de evasão
    top_estados_evasao = taxa_evasao_por_estado.sort_values(ascending=False).head(num_estados)

    if qnt_estados == "5":
         st.subheader("Top 5 estados com a maior quantidade de alunos evadidos:")
    elif qnt_estados == "10":
        st.subheader("Top 10 estados com a maior quantidade de alunos evadidos:")
    elif qnt_estados == "15":
        st.subheader("Top 15 estados com a maior quantidade de alunos evadidos:")
    elif qnt_estados == "20":
        st.subheader("Top 10 estados com a maior quantidade de alunos evadidos:")

    st.write(top_estados_evasao)
    st.bar_chart(top_estados_evasao)    

#--------------------------------------------------------------------------------------------
    # Obtendo os estados com maior taxa de evasão
    top_estados_evasao = taxa_evasao_por_estado.sort_values(ascending=True).head(num_estados)

    if qnt_estados == "5":
         st.subheader("Top 5 estados com a menor quantidade de alunos evadidos:")
    elif qnt_estados == "10":
        st.subheader("Top 10 estados com a menor quantidade de alunos evadidos:")
    elif qnt_estados == "15":
        st.subheader("Top 15 estados com a menor quantidade de alunos evadidos:")
    elif qnt_estados == "20":
        st.subheader("Top 10 estados com a menor quantidade de alunos evadidos:")

    st.write(top_estados_evasao)
    st.bar_chart(top_estados_evasao)    



with st.container():
    st.write("---")
    st.subheader("Quais são os eixos?")
    dados = carregar_dados()

    tipos_de_eixos = dados['Eixo Tecnológico'].unique()

    # Criar um DataFrame para os eixos
    df_eixos = pd.DataFrame({'Eixos Tecnológicos': tipos_de_eixos})


    # Exibir a tabela de eixos
    st.table(df_eixos)



with st.container():
    st.write("---")
    st.subheader("Quantidade de alunos por eixo")
    dados = carregar_dados()

    # Contando a quantidade de matrículas em cada eixo (Eixo Tecnológico)
    contagem_matriculas_por_eixo = dados['Eixo Tecnológico'].value_counts()


    st.write("Quantidade de matrículas em cada eixo:")
    st.write(contagem_matriculas_por_eixo)
    st.bar_chart(contagem_matriculas_por_eixo) 




with st.container():
    st.write("---")
    st.subheader("Quantidade de evasão por eixo")
    dados = carregar_dados()

    # Filtrando os dados para incluir apenas alunos evadidos
    evadidos = dados[dados['Categoria da Situação'] == 'Evadidos']

    # Contando a quantidade de evasões por curso (Eixo Tecnológico)
    evasao_por_curso = evadidos['Eixo Tecnológico'].value_counts()

    st.write("Evasão por curso:")
    st.write(evasao_por_curso)
    st.bar_chart(evasao_por_curso) 




with st.container():
    st.write("---")
    st.subheader("Quais os turnos?")
    dados = carregar_dados()

    turnos_tipos = dados['Turno'].unique()

    # Criar um DataFrame para os turnos
    df_turnos = pd.DataFrame({'Turnos': turnos_tipos})

    # Exibir a tabela de turnos
    st.table(df_turnos)


with st.container():
    st.write("---")
    st.subheader("Quantidade de alunos matriculados por turno")
    dados = carregar_dados()

    # Corrige os valores dos turnos
    dados['Turno'] = dados['Turno'].replace({'Norturno': 'Noturno'})

    # Filtra os dados excluindo o turno "Não se aplica"
    dados_filtrados = dados[dados['Turno'] != 'Não se aplica']

    # Calcula a contagem de registros por turno
    contagem_registros_por_turno = dados_filtrados.groupby('Turno').size()

    st.write("Quantidade de registros por turno:")
    st.write(contagem_registros_por_turno)
    st.bar_chart(contagem_registros_por_turno) 




with st.container():
    st.write("---")
    st.subheader("Quantidade de evasão por turno")
    dados = carregar_dados()

    # Corrige os valores dos turnos
    dados['Turno'] = dados['Turno'].replace({'Norturno': 'Noturno'})

    # Filtra os dados de evasão excluindo o turno "Não se aplica"
    evasao_filtrada = dados[(dados['Categoria da Situação'] == 'Evadidos') & (dados['Turno'] != 'Não se aplica')]

    # Agrupando por turno e contando a quantidade de evasões
    quantidade_evasao_por_turno = evasao_filtrada.groupby('Turno').size()

    st.write("Quantitativo geral de evasão por turno:")
    st.write(quantidade_evasao_por_turno)
    st.bar_chart(quantidade_evasao_por_turno) 








with st.container():
    st.write("---")
    st.subheader("Filtrar registros dos alunos por data de matrícula")

    dados = carregar_dados()

    # Convertendo a coluna 'Data de Ocorrência da Matrícula' para o tipo datetime
    dados['Data de Ocorrencia da Matricula'] = pd.to_datetime(dados['Data de Ocorrencia da Matricula'], format='%d/%m/%Y', errors='coerce')

    # Adicionando widgets para a entrada de datas no formato brasileiro
    data_inicio, data_fim = st.date_input("Selecione a data de início e término:", min_value=dados['Data de Ocorrencia da Matricula'].min().date(), max_value=dados['Data de Ocorrencia da Matricula'].max().date(), value=[dados['Data de Ocorrencia da Matricula'].min().date(), dados['Data de Ocorrencia da Matricula'].max().date()], format="DD/MM/YYYY")

    # Convertendo as datas de entrada para datetime64[ns]
    data_inicio = pd.to_datetime(data_inicio, format='%d/%m/%Y')
    data_fim = pd.to_datetime(data_fim, format='%d/%m/%Y')

    # Filtrando os dados com base nas datas fornecidas pelo usuário
    matriculas_filtradas = dados[(dados['Data de Ocorrencia da Matricula'] >= data_inicio) & (dados['Data de Ocorrencia da Matricula'] <= data_fim)]

    st.write(matriculas_filtradas.head(5))


