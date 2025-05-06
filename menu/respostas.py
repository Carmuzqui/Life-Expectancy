import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer

def render():
    st.markdown("## 💡 Respostas/Insights")
    st.markdown("Selecione uma pergunta abaixo para visualizar a resposta com análise estatística:")

    perguntas = {
        "Pergunta 1: Os vários fatores preditivos inicialmente escolhidos realmente afetam a expectativa de vida?": 1,
        "Pergunta 2: Quais são as variáveis preditivas que realmente afetam a expectativa de vida?": 2,
        "Pergunta 3: Um país com expectativa de vida < 65 anos deve aumentar os gastos com saúde para melhorar?": 3,
        "Pergunta 4: Como as taxas de mortalidade infantil e adulta afetam a expectativa de vida?": 4,
        "Pergunta 5: Qual é o impacto da escolaridade na expectativa de vida dos seres humanos?": 5,
        "Pergunta 6: A expectativa de vida tem relação positiva ou negativa com o consumo de álcool?": 6,
        "Pergunta 7: Países densamente povoados tendem a ter menor expectativa de vida?": 7,
        "Pergunta 8: Qual é o impacto da cobertura vacinal na expectativa de vida?": 8,
        "📊 Resumo geral": 9
    }

    selected_question = st.selectbox("🔽 Selecione a pergunta:", list(perguntas.keys()))

    # Carregamento local e limpeza dos dados
    df = pd.read_csv("dados/Life Expectancy Data.csv")
    df.columns = df.columns.str.strip()

    imputer = KNNImputer()
    for col in df.select_dtypes(include="number").columns:
        df[col] = imputer.fit_transform(df[[col]])

    
    def wisker_bounds(col):
        q1, q3 = np.percentile(col, [25, 75])
        iqr = q3 - q1
        return q1 - 1.5 * iqr, q3 + 1.5 * iqr

    numerical_cols = df.select_dtypes(include="number").columns
    outlier_percent = {
        col: round(100 * ((df[col] < wisker_bounds(df[col])[0]) | (df[col] > wisker_bounds(df[col])[1])).sum() / len(df), 2)
        for col in numerical_cols
    }

    treated_cols = [
        'Year', 'Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure',
        'Hepatitis B', 'Measles', 'BMI', 'under-five deaths', 'Polio', 'Total expenditure',
        'Diphtheria', 'HIV/AIDS', 'GDP', 'Population', 'thinness  1-19 years',
        'thinness 5-9 years', 'Income composition of resources', 'Schooling'
    ]
    for col in treated_cols:
        lw, uw = wisker_bounds(df[col])
        df[col] = np.clip(df[col], lw, uw)






    # Cálculo da matriz de correlação
    correlation = df.corr(numeric_only=True)
    life_corr = correlation["Life expectancy"].sort_values(ascending=False)

     # Criar mapa de calor com destaque nas correlações negativas
    plt.figure(figsize=(12, 12))
    sns.heatmap(
        correlation,
        cmap=sns.diverging_palette(240, 0, as_cmap=True),  # 240=azul → 0=vermelho
        center=0,             # centraliza no 0
        annot=True,           # exibe os valores
        fmt=".2f",
        cbar=True,
        cbar_kws={"shrink": 0.75},
        square=True,
        linewidths=0.5
    )

    if perguntas[selected_question] == 1:

        st.markdown("## ✅ Resposta com base nas correlações")

        st.markdown("""
        Sim, diversos fatores preditivos escolhidos inicialmente **têm forte relação com a expectativa de vida**, conforme evidenciado pela análise de correlação abaixo. As variáveis mais relevantes incluem:
        """)

        st.markdown("---")
        st.markdown("### 🔼 Fatores positivamente correlacionados (aumentam com a expectativa de vida)")
        st.markdown("""
        - **Escolaridade** (`correlação = 0.738`)  
        Quanto maior o nível de escolaridade, maior tende a ser a expectativa de vida.

        - **Composição de renda** (`0.729`)  
        Reflete o acesso a recursos econômicos, saúde e bem-estar.

        - **Cobertura vacinal**  
        - Difteria: `0.573`  
        - Poliomielite: `0.567`  
        Alta cobertura vacinal está associada à redução de mortalidade infantil e doenças evitáveis.

        - **Índice de Massa Corporal (BMI)** (`0.559`)  
        Reflete nutrição adequada, com implicações na saúde geral.

        - **PIB per capita (GDP)** (`0.498`)  
        Economias mais fortes tendem a ter sistemas de saúde mais eficazes.
        """)

        st.markdown("---")
        st.markdown("### 🔽 Fatores negativamente correlacionados (diminuem a expectativa de vida)")
        st.markdown("""
        - **HIV/AIDS** (`-0.796`)  
        Altamente letal e com forte impacto em regiões com baixa cobertura de tratamento.

        - **Mortalidade adulta** (`-0.691`)  
        Reflete maior prevalência de doenças e condições fatais.

        - **Mortalidade infantil** (`-0.566`) e **Mortes de menores de cinco anos** (`-0.603`)  
        Indicadores críticos da saúde pública e da qualidade do sistema de saúde.

        - **Desnutrição infantil**  
        - Thinness 1-19: `-0.512`  
        - Thinness 5-9: `-0.509`  
        Condições frequentemente associadas à pobreza, insegurança alimentar e serviços de saúde deficientes.

        - **Sarampo (Measles)** (`-0.336`)  
        A falta de imunização está relacionada com surtos da doença e maior mortalidade.
        """)

        st.markdown("---")
        st.markdown("## 📌 Conclusão")
        st.markdown("""
        A análise estatística mostra que **há uma forte relação entre expectativa de vida e vários fatores socioeconômicos, nutricionais, epidemiológicos e de infraestrutura de saúde**. Portanto, os fatores preditivos escolhidos têm, sim, **efeito significativo** sobre a expectativa de vida.
        """)
        st.markdown("---")


        plt.title("Matriz de correlação")
        st.pyplot(plt)

    elif perguntas[selected_question] == 2:

        st.markdown("## ✅ Resposta")

        st.markdown("""
        Com base nas **correlações** entre as variáveis preditivas e a expectativa de vida, podemos identificar quais fatores têm uma **relação significativa** com a expectativa de vida. As variáveis mais relevantes, com suas respectivas correlações, são:
        """)

        st.markdown("---")
        st.markdown("### 🔼 Fatores positivamente correlacionados com a expectativa de vida:")
        st.markdown("""
        - **Escolaridade**  
        Correlation: `0.738`  
        Aumento da escolaridade está fortemente associado a uma maior expectativa de vida, indicando que o acesso à educação tem um impacto significativo na saúde e bem-estar de uma população.

        - **Composição de renda**  
        Correlation: `0.729`  
        A maior capacidade econômica (representada pela composição de renda) é um dos fatores mais fortes que influenciam a expectativa de vida, pois está relacionado ao acesso a melhores serviços de saúde e nutrição.

        - **Cobertura vacinal**  
        - **Difteria**: `0.573`  
        - **Poliomielite**: `0.567`  
        A cobertura vacinal está fortemente correlacionada com a expectativa de vida, refletindo a importância da imunização na redução de doenças fatais.

        - **Índice de Massa Corporal (BMI)**  
        Correlation: `0.559`  
        A nutrição e a saúde geral, refletidas pelo índice de massa corporal, têm uma correlação positiva com a longevidade.

        - **PIB per capita (GDP)**  
        Correlation: `0.498`  
        O crescimento econômico (medido pelo PIB per capita) está relacionado com um sistema de saúde mais robusto, resultando em uma maior expectativa de vida.
        """)

        st.markdown("---")
        st.markdown("### 🔽 Fatores negativamente correlacionados com a expectativa de vida:")
        st.markdown("""
        - **HIV/AIDS**  
        Correlation: `-0.796`  
        A pandemia de HIV/AIDS tem um forte impacto negativo na expectativa de vida, especialmente em países com baixos índices de tratamento e prevenção.

        - **Mortalidade adulta**  
        Correlation: `-0.691`  
        A mortalidade adulta, geralmente associada a doenças crônicas e estilo de vida, tem um impacto negativo direto na expectativa de vida.

        - **Mortalidade infantil**  
        Correlation: `-0.566`  
        A mortalidade infantil é um forte indicativo de deficiências nos serviços de saúde e na qualidade de vida, afetando diretamente a expectativa de vida.

        - **Mortalidade de menores de cinco anos**  
        Correlation: `-0.603`  
        Semelhante à mortalidade infantil, é um indicativo de problemas no acesso à saúde para crianças pequenas.

        - **Desnutrição infantil**  
        - **Thinness 1-19 anos**: `-0.512`  
        - **Thinness 5-9 anos**: `-0.509`  
        A desnutrição infantil é um fator crucial que reduz a expectativa de vida, associada à falta de alimentação adequada e cuidados de saúde para as crianças.

        - **Sarampo (Measles)**  
        Correlation: `-0.336`  
        A falta de imunização contra doenças como o sarampo impacta negativamente a saúde pública e reduz a longevidade.
        """)

        st.markdown("---")
        st.markdown("### 📌 Conclusão")
        st.markdown("""
        As variáveis que mais afetam a **expectativa de vida** são as relacionadas à **educação, saúde, nutrição e economia**. Fatores como escolaridade, cobertura vacinal, PIB per capita e mortalidade infantil estão entre os mais significativos. Além disso, problemas de saúde pública, como HIV/AIDS e desnutrição, têm uma correlação negativa substancial com a expectativa de vida.

        Esses resultados destacam a importância de **investir em educação, saúde pública e infraestrutura econômica** para aumentar a longevidade das populações.
        """)
        st.markdown("---")


        plt.title("Matriz de correlação")
        st.pyplot(plt)

    elif perguntas[selected_question] == 3:
        
        st.markdown("## ✅ Resposta")

        st.markdown("""
        A **correlação** entre os **gastos totais com saúde (Total expenditure)** e a **expectativa de vida (Life expectancy)** para os países com uma expectativa de vida inferior a 65 anos é de **-0.1477**. Essa correlação negativa, embora baixa, sugere que **não há uma relação forte** entre o aumento dos gastos com saúde e a melhoria da expectativa de vida nesses países.
        """)

        st.markdown("---")
        st.markdown("### 🔍 Interpretação")
        st.markdown("""
        - **Correlação negativa fraca (-0.1477)**: Significa que, em geral, quando os gastos com saúde aumentam, a expectativa de vida tende a diminuir levemente, mas a relação é fraca, o que sugere que o aumento dos gastos não tem um impacto direto significativo sobre a expectativa de vida.

        - **Fatores adicionais**: Outros fatores além dos gastos com saúde, como **condições econômicas, políticas de saúde pública, educação, infraestrutura e fatores sociais**, provavelmente têm um impacto maior na expectativa de vida.
        """)

        st.markdown("---")
        st.markdown("### 📌 Conclusão")
        st.markdown("""
        Apesar de ser importante aumentar os investimentos em saúde para melhorar a qualidade de vida e o bem-estar da população, a **correlação fraca negativa** sugere que **outros fatores** estão desempenhando um papel mais importante na determinação da expectativa de vida nesses países. O aumento dos gastos com saúde, isoladamente, pode não ser suficiente para promover uma melhoria substancial na expectativa de vida de países com expectativa de vida inferior a 65 anos.

        **Portanto, aumentar os gastos com saúde pode não ser a solução única ou mais eficaz para melhorar a expectativa de vida média nesses países.** A análise de outros determinantes sociais e estruturais também é essencial para alcançar melhorias significativas na saúde da população.
        """)
        st.markdown("---")


        filtered = df[df['Life expectancy'] < 65]
        correlation = filtered[['Total expenditure', 'Life expectancy']].corr().iloc[0, 1]
        st.markdown(f"**Correlação Total expenditure vs Life expectancy:** `{correlation:.4f}`")

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=filtered, x="Total expenditure", y="Life expectancy", hue="Status", alpha=0.7, ax=ax)
        ax.set_title("Gastos com Saúde x Expectativa de Vida (Expectativa < 65 anos)")
        ax.set_xlabel("Total expenditure")
        ax.set_ylabel("Life expectancy")
        st.pyplot(fig)

    elif perguntas[selected_question] == 4:

        st.markdown("## ✅ Resposta")

        st.markdown("""
        A **mortalidade infantil** e a **mortalidade adulta** são fatores importantes que afetam diretamente a **expectativa de vida** de um país. A análise das correlações entre essas variáveis e a expectativa de vida pode ajudar a entender melhor como esses indicadores estão relacionados.
        """)

        st.markdown("---")
        st.markdown("### 🔍 Análise das Correlações")
        st.markdown("""
        1. **Mortalidade infantil (_infant deaths_)**:  
        A **correlação** entre a **mortalidade infantil** e a **expectativa de vida** é **-0.5656**, o que indica uma **relação negativa moderada**. Isso significa que, em países com maior mortalidade infantil, a expectativa de vida tende a ser mais baixa. Essa relação reflete o impacto da saúde materno-infantil e das condições de vida no início da vida de um indivíduo, afetando diretamente a longevidade.

        2. **Mortalidade adulta (_Adult Mortality_)**:  
        A **correlação** entre a **mortalidade adulta** e a **expectativa de vida** é **-0.6912**, sugerindo uma **relação negativa forte**. Ou seja, países com altas taxas de mortalidade adulta tendem a ter uma expectativa de vida mais baixa. Esse fator reflete a saúde geral da população adulta e os riscos de doenças crônicas e acidentes que afetam a longevidade.
        """)

        st.markdown("---")
        st.markdown("### 📊 Interpretação")
        st.markdown("""
        - **Mortalidade infantil**: O aumento da mortalidade infantil indica deficiências nos cuidados de saúde infantil e nas condições de vida das crianças, o que pode reduzir a expectativa de vida média de um país. Melhorias na saúde infantil, como vacinação, nutrição e acesso a cuidados médicos, podem aumentar a expectativa de vida.

        - **Mortalidade adulta**: A mortalidade adulta, que está frequentemente associada a doenças não transmissíveis (como doenças cardíacas, câncer, diabetes, etc.), também impacta negativamente a expectativa de vida. Países com alta mortalidade adulta geralmente enfrentam desafios em termos de acesso a cuidados médicos, controle de doenças e prevenção de riscos de saúde.
        """)

        st.markdown("---")
        st.markdown("### 📌 Conclusão")
        st.markdown("""
        As taxas de **mortalidade infantil** e **mortalidade adulta** têm um impacto significativo e negativo na **expectativa de vida**. A **mortalidade infantil** afeta a longevidade devido a condições de saúde precárias e a falta de acesso a cuidados adequados para crianças. A **mortalidade adulta**, por sua vez, está relacionada a doenças crônicas e fatores de risco presentes na população adulta.

        Portanto, **reduzir as taxas de mortalidade infantil e adulta** deve ser uma prioridade para melhorar a **expectativa de vida média** de um país. Isso pode ser alcançado por meio de políticas públicas eficazes de saúde, educação e infraestrutura, focando no acesso a cuidados de saúde adequados, prevenção de doenças e promoção de estilos de vida saudáveis.
        """)
        st.markdown("---")


        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        sns.scatterplot(data=df, x="infant deaths", y="Life expectancy", hue="Status", ax=axes[0], alpha=0.7)
        axes[0].set_title("Mortalidade Infantil vs Expectativa de Vida")

        sns.scatterplot(data=df, x="Adult Mortality", y="Life expectancy", hue="Status", ax=axes[1], alpha=0.7)
        axes[1].set_title("Mortalidade Adulta vs Expectativa de Vida")

        plt.tight_layout()
        st.pyplot(fig)

        corr_infant = df["infant deaths"].corr(df["Life expectancy"])
        corr_adult = df["Adult Mortality"].corr(df["Life expectancy"])
        st.markdown(f"**Correlação Infant Mortality vs Life expectancy**: `{corr_infant:.4f}`")
        st.markdown(f"**Correlação Adult Mortality vs Life expectancy**: `{corr_adult:.4f}`")

    elif perguntas[selected_question] == 5:

        st.markdown("## ✅ Resposta")

        st.markdown("""
        A análise dos dados mostra que a **escolaridade (_Schooling_)** possui uma **correlação positiva forte** com a **expectativa de vida (_Life expectancy_)**.
        """)

        st.markdown("---")
        st.markdown("### 📈 Resultado da Correlação")
        correlation_schooling = df[['Schooling', 'Life expectancy']].corr()
        valor_corr = correlation_schooling.loc['Schooling', 'Life expectancy']
        st.write(f"Correlação entre Escolaridade e Expectativa de Vida: **{valor_corr:.3f}**")

        st.markdown("---")
        st.markdown("### 🔍 Interpretação")
        st.markdown("""
        - Pessoas com maior escolaridade tendem a ter:
        - **Maior acesso a informações de saúde**;
        - **Hábitos de vida mais saudáveis**;
        - **Melhor acesso ao sistema de saúde**;
        - E **melhores condições socioeconômicas**.
        - Isso sugere que **educação é um dos fatores preditivos mais relevantes** para a longevidade humana.
        """)

        st.markdown("---")
        st.markdown("### 📊 Visualização")

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(data=df, x='Schooling', y='Life expectancy', hue='Status', alpha=0.7, ax=ax)
        ax.set_title("Relação entre Escolaridade e Expectativa de Vida", fontsize=14)
        ax.set_xlabel("Escolaridade (anos esperados de estudo)")
        ax.set_ylabel("Expectativa de Vida (anos)")
        ax.legend(title="Status")
        st.pyplot(fig)

        st.markdown("---")
        st.markdown("### 📌 Conclusão")
        st.markdown("""
        A escolaridade tem um impacto **positivo e significativo** na expectativa de vida. Políticas públicas que **ampliem o acesso à educação de qualidade** podem contribuir diretamente para o **aumento da longevidade** e melhoria da qualidade de vida da população.
        """)

    elif perguntas[selected_question] == 6:

        st.markdown("## ✅ Resposta")
        st.markdown("""
        A análise da **correlação entre o consumo de álcool** e a **expectativa de vida** indica uma **relação positiva moderada**, com coeficiente de correlação de aproximadamente **+0.39**.
        """)

        st.markdown("---")
        st.markdown("### 🔍 Interpretação")
        st.markdown("""
        - **Correlação positiva moderada (+0.39)**: Isso sugere que, de maneira geral, **maiores níveis de consumo de álcool estão associados a uma maior expectativa de vida**.
        - Essa relação **não significa causalidade**. Países com maior expectativa de vida costumam ter **níveis de desenvolvimento mais altos**, o que pode coincidir com **um consumo controlado e social de álcool**, além de melhor acesso a cuidados de saúde e estilo de vida mais saudável no geral.
        - Em países com expectativa de vida menor, o consumo de álcool pode estar mais associado a padrões prejudiciais e à falta de infraestrutura de saúde adequada.
        """)

        st.markdown("---")
        st.markdown("### 📈 Correlação")
        correlation_alcohol = df['Alcohol'].corr(df['Life expectancy'])
        st.write(f"Correlação entre consumo de álcool e expectativa de vida: **{correlation_alcohol:.3f}**")

        st.markdown("### 📊 Visualização")

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(data=df, x='Alcohol', y='Life expectancy', hue='Status', alpha=0.7, ax=ax)
        ax.set_title("Consumo de Álcool vs Expectativa de Vida", fontsize=14)
        ax.set_xlabel("Consumo de Álcool (litros per capita)")
        ax.set_ylabel("Expectativa de Vida (anos)")
        ax.legend(title="Status do País")
        st.pyplot(fig)

        st.markdown("---")
        st.markdown("### 📌 Conclusão")
        st.markdown("""
        Embora o resultado possa parecer contraintuitivo, a **correlação positiva entre o consumo de álcool e a expectativa de vida** não implica que beber mais leva a viver mais. Essa relação é provavelmente **mediada por outros fatores**, como **nível socioeconômico**, **educação**, e **qualidade do sistema de saúde**.

        **Portanto, a expectativa de vida mostra uma relação positiva com o consumo de álcool, mas esse resultado deve ser interpretado com cautela e dentro de um contexto mais amplo de desenvolvimento humano.**
        """)


    elif perguntas[selected_question] == 7:

        st.markdown("## ✅ Resposta")
        st.markdown("""
        Com base na correlação fornecida, a relação entre a **população** (Population) e a **expectativa de vida** (Life expectancy) é muito fraca, com um valor de correlação de **0.0102**, praticamente próximo de zero. Isso indica que **não há uma correlação significativa entre a densidade populacional e a expectativa de vida**.
        """)

        st.markdown("---")
        st.markdown("### 🔍 Interpretação")
        st.markdown("""
        - **Correlação muito baixa (0.0102)**: A correlação extremamente baixa sugere que a densidade populacional **não tem um impacto significativo** na expectativa de vida. Ou seja, um país com uma alta densidade populacional não tende, necessariamente, a ter uma expectativa de vida menor.
        - **Fatores mais importantes**: Outros fatores, como **acesso a cuidados de saúde, qualidade de vida, educação, economia e políticas públicas**, provavelmente têm um efeito mais substancial na expectativa de vida.
        """)

        st.markdown("### 📈 Correlação")
        correlation_population = df['Population'].corr(df['Life expectancy'])
        st.write(f"Correlação entre População e Expectativa de Vida: **{correlation_population:.4f}**")

        st.markdown("### 📊 Visualização")

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(data=df, x='Population', y='Life expectancy', hue='Status', alpha=0.7, ax=ax)
        ax.set_title("População vs Expectativa de Vida", fontsize=14)
        ax.set_xlabel("População")
        ax.set_ylabel("Expectativa de Vida (anos)")
        ax.legend(title="Status do País")
        st.pyplot(fig)

        st.markdown("---")
        st.markdown("### 📌 Conclusão")
        st.markdown("""
        **A densidade populacional** por si só **não é um fator determinante** na expectativa de vida dos países. A análise de outras variáveis, como os cuidados com a saúde, educação, e condições econômicas, é fundamental para entender as variações na expectativa de vida.
        """)


    elif perguntas[selected_question] == 8:

        st.markdown("## ✅ Resposta")
        st.markdown("""
        A **cobertura vacinal** tem um impacto **positivo** na **expectativa de vida**, especialmente para doenças como **Difteria**, **Polio** e **Hepatite B**.
        """)

        st.markdown("### 📊 Correlações observadas:")
        st.markdown("""
        - **Difteria**: Correlação de **0.5732**, indicando uma relação **positiva moderada**.
        - **Poliomielite**: Correlação de **0.5672**, também **positiva moderada**.
        - **Hepatite B**: Correlação de **0.2972**, relação **positiva mais fraca**.
        """)

        st.markdown("### 🔍 Interpretação")
        st.markdown("""
        - **Difteria**: Menos mortes pela doença devido à vacinação impactam diretamente na expectativa de vida.
        - **Polio**: Cobertura vacinal mais alta tende a eliminar doenças evitáveis, promovendo maior longevidade.
        - **Hepatite B**: Apesar da correlação mais baixa, a prevenção de doenças hepáticas ainda contribui para a saúde da população.
        """)

        # Cálculo das correlações
        corr_diphtheria = df['Diphtheria'].corr(df['Life expectancy'])
        corr_polio = df['Polio'].corr(df['Life expectancy'])
        corr_hepatitis_b = df['Hepatitis B'].corr(df['Life expectancy'])

        st.write(f"**Correlação Difteria**: {corr_diphtheria:.4f}")
        st.write(f"**Correlação Polio**: {corr_polio:.4f}")
        st.write(f"**Correlação Hepatite B**: {corr_hepatitis_b:.4f}")

        st.markdown("### 📈 Visualização")

        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        variables = ['Diphtheria', 'Polio', 'Hepatitis B']
        titles = ['Difteria', 'Poliomielite', 'Hepatite B']

        for i, var in enumerate(variables):
            sns.scatterplot(data=df, x=var, y='Life expectancy', hue='Status', alpha=0.7, ax=axes[i])
            axes[i].set_title(f'{titles[i]} vs Expectativa de Vida')
            axes[i].set_xlabel(f'{titles[i]} (%)')
            axes[i].set_ylabel('Expectativa de Vida')

        plt.tight_layout()
        st.pyplot(fig)

        st.markdown("### 📌 Conclusão")
        st.markdown("""
        A análise das correlações sugere que a **melhoria na cobertura vacinal** contra doenças como **Difteria**, **Polio** e **Hepatite B** tem um **impacto positivo** na **expectativa de vida**. A vacinação reduz a mortalidade e contribui para a melhoria da saúde pública e da longevidade.

        **Portanto, aumentar a cobertura vacinal contra essas doenças é uma estratégia eficaz para elevar a expectativa de vida média nos países.**
        """)



    elif perguntas[selected_question] == 9:

        # Dicionário com fatores e correlações discutidas
        correlacoes_resumo = {
            "Escolaridade": 0.738,
            "Composição de renda": 0.729,
            "Vacinação (Difteria)": 0.573,
            "Vacinação (Polio)": 0.567,
            "BMI": 0.559,
            "PIB per capita": 0.498,
            "Hepatite B": 0.297,
            "Álcool": 0.390,

            "HIV/AIDS": -0.796,
            "Mortalidade adulta": -0.691,
            "Menores de 5 anos": -0.603,
            "Mortalidade infantil": -0.566,
            "Desnutrição (1-19)": -0.512,
            "Desnutrição (5-9)": -0.509,
            "Sarampo": -0.336,
            "População": 0.010
        }

        # Criar DataFrame para visualização
        df_corr_resumo = pd.DataFrame.from_dict(correlacoes_resumo, orient='index', columns=["Correlação"])
        df_corr_resumo = df_corr_resumo.sort_values("Correlação")

        # Plot
        plt.figure(figsize=(10, 8))
        sns.barplot(x="Correlação", y=df_corr_resumo.index, data=df_corr_resumo, palette="vlag")
        plt.title("Resumo das correlações com a Expectativa de Vida", fontsize=14)
        plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
        plt.ylabel("Variáveis analisadas")
        plt.tight_layout()
        st.pyplot(plt)


    
