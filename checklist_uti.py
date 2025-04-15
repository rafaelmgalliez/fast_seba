import streamlit as st
import pandas as pd

# Dicionário com as explicações para cada item do checklist
explicacoes = {
    "Terapia de fluidos e alimentação": "Avaliar o estado de hidratação do paciente e a necessidade de fluidos intravenosos. Questionar sobre a via de alimentação (oral, enteral, parenteral), a dieta prescrita, a tolerância à dieta e o balanço hídrico.",
    "Analgesia, Antieméticos e SAT*": "Verificar a presença de dor, sua intensidade (usar escalas como a EVA ou NRS) e a necessidade de analgesia. Questionar sobre a presença de náuseas e vômitos e a necessidade de antieméticos. SAT refere-se à profilaxia antitetânica; verificar o status da vacinação e a necessidade de reforço em caso de ferimentos.",
    "Sedação e teste de respiração espontânea": "Avaliar o nível de sedação do paciente (usar escalas como RASS ou SAS) e a necessidade de ajuste. Para pacientes ventilados mecanicamente, questionar sobre a possibilidade de realizar o teste de respiração espontânea (TRE) para avaliar a prontidão para extubação.",
    "Tromboprofilaxia, Profilaxia antitetânica": "Verificar a necessidade de profilaxia para tromboembolismo venoso (TEV), como o uso de heparina de baixo peso molecular ou dispositivos de compressão mecânica. Verificar novamente o status da vacinação antitetânica e a necessidade de profilaxia.",
    "Cabeceira elevada (30 graus) se intubado": "Confirmar se a cabeceira do leito está elevada em 30-45 graus em pacientes intubados para reduzir o risco de aspiração e pneumonia associada à ventilação mecânica (PAV).",
    "Profilaxia de úlcera": "Avaliar o risco de úlcera de estresse e a necessidade de profilaxia medicamentosa, como inibidores da bomba de prótons (IBP) ou antagonistas dos receptores H2.",
    "Controle glicêmico": "Verificar os níveis de glicemia do paciente e a necessidade de controle glicêmico, seguindo protocolos estabelecidos para manter a glicemia dentro da faixa alvo.",
    "Cuidados com a pele/olhos e aspiração": "Avaliar a integridade da pele, identificar áreas de risco para lesões por pressão e implementar medidas preventivas. Verificar a higiene ocular e a necessidade de lubrificação. Questionar sobre a necessidade de aspiração de vias aéreas (oral, traqueal) e sua frequência.",
    "Cateter vesical de demora": "Avaliar a necessidade de cateter vesical de demora (CVD) e considerar sua remoção o mais breve possível para reduzir o risco de infecção do trato urinário (ITU) associada ao cateter (CAUTI).",
    "Sonda nasogástrica": "Avaliar a necessidade de sonda nasogástrica (SNG), sua finalidade (alimentação, drenagem) e verificar seu posicionamento e permeabilidade.",
    "Cuidados intestinais": "Monitorar a função intestinal do paciente, incluindo frequência e consistência das evacuações. Questionar sobre a necessidade de laxativos ou outras intervenções para garantir a função intestinal adequada.",
    "Ambiente (ex: controle de temperatura, ambiente adequado em delirium)": "Avaliar o ambiente do paciente, incluindo controle de temperatura, ruído e iluminação. Para pacientes com delirium, garantir um ambiente calmo, seguro e com reorientação frequente.",
    "Descalonamento (ex: questões de fim de vida, tratamentos não mais necessários)": "Revisar o plano de tratamento do paciente e considerar o descalonamento de terapias que não são mais necessárias (antibióticos, ventilação mecânica, etc.). Discutir questões relacionadas ao fim da vida, se apropriado.",
    "Suporte psicossocial (para paciente, família e equipe)": "Avaliar as necessidades de suporte psicossocial do paciente, da família e da equipe. Considerar a necessidade de intervenção de psicólogos, assistentes sociais ou outros profissionais de apoio."
}

def main():
    st.title("Checklist de Round da UTI")
    st.subheader("FAST HUGS BID")

    num_pacientes = 10
    dados_pacientes = {}

    for i in range(1, num_pacientes + 1):
        st.header(f"Paciente {i}")
        dados_pacientes[f"Paciente {i}"] = {}
        for item in explicacoes:
            marcado = st.checkbox(item, key=f"paciente_{i}_{item}")
            if marcado:
                with st.expander("O que perguntar à equipe?", expanded=False):
                    st.write(explicacoes[item])
            dados_pacientes[f"Paciente {i}"][item] = marcado

    if st.button("Salvar Checklist"):
        df = pd.DataFrame.from_dict(dados_pacientes, orient='index')
        st.subheader("Dados do Checklist Salvos:")
        st.dataframe(df)
        st.success("Checklist salvo com sucesso!")

if __name__ == "__main__":
    main()
