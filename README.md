# Checklist de Round da UTI - FAST HUGS BID

Este é um aplicativo Python construído com Streamlit para auxiliar na realização do checklist diário de pacientes na Unidade de Terapia Intensiva (UTI), seguindo o mnemônico FAST HUGS BID. A ferramenta permite marcar os itens verificados para até 10 pacientes e fornece uma breve explicação sobre o que perguntar à equipe para cada item.

## Funcionalidades

* **Interface intuitiva:** Desenvolvido com Streamlit para fácil utilização em navegadores web.
* **Checklist completo:** Inclui todos os itens do FAST HUGS BID:
    * Terapia de fluidos e alimentação
    * Analgesia, Antieméticos e SAT*
    * Sedação e teste de respiração espontânea
    * Tromboprofilaxia, Profilaxia antitetânica
    * Cabeceira elevada (30 graus) se intubado
    * Profilaxia de úlcera
    * Controle glicêmico
    * Cuidados com a pele/olhos e aspiração
    * Cateter vesical de demora
    * Sonda nasogástrica
    * Cuidados intestinais
    * Ambiente (ex: controle de temperatura, ambiente adequado em delirium)
    * Descalonamento (ex: questões de fim de vida, tratamentos não mais necessários)
    * Suporte psicossocial (para paciente, família e equipe)
* **Suporte para múltiplos pacientes:** Permite realizar o checklist para até 10 pacientes individualmente.
* **Explicações e sugestões de perguntas:** Para cada item do checklist, há uma breve explicação sobre sua importância e sugestões de perguntas a serem feitas à equipe durante o round.
* **Salvamento dos dados:** Permite salvar o checklist preenchido em formato de tabela (Pandas DataFrame) na tela.

## Como usar

1.  **Pré-requisitos:** Certifique-se de ter o Python instalado em sua máquina.
2.  **Instalação das Dependências:** Instale as bibliotecas necessárias usando o pip:
    ```bash
    pip install streamlit pandas
    ```
3.  **Execução do aplicativo:** Salve o código Python (disponível neste repositório como `checklist_uti.py`) e execute-o no terminal ou prompt de comando:
    ```bash
    streamlit run checklist_uti.py
    ```
4.  **Utilização:** O aplicativo será aberto automaticamente em seu navegador. Navegue pelas seções de cada paciente, marque os itens verificados e consulte as explicações. Clique em "Salvar Checklist" ao finalizar.

## Arquivos

* `checklist_uti.py`: O código fonte do aplicativo Streamlit em Python.
* `README.md`: Este arquivo com a descrição do projeto.
* `dependencias.txt`: (Conteúdo descrito abaixo)

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias ou novas funcionalidades.

## Licença

[Inserir aqui o tipo de licença, se aplicável]
