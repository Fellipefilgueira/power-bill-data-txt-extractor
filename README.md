# Power bill data txt extractor (PBDTE)

The software allows to extract relevant data from a collection of electricity bills, generating as output a file compatible with spreadsheet softwares. Currently the program only receives .txt files as input and related to the COSERN energy concessionaire.


Current stable build: 1.0.0

### Data type fetched
    Conta contrato
    
    Classificação
    Data de leitura

    Valor da fatura (R$)
    Tributo (R$)

    Demanda ativa contratada (kW)
    Demanda ativa contratada FP (kW)
    Demanda ativa contratada NP (kW)
    
    Demanda ativa (kW)
    Demanda ativa FP (kW)
    Demanda ativa NP (kW)
    Despesa demanda ativa (R$)
    Despesa demanda ativa FP (R$)
    Despesa demanda ativa NP (R$)

    Demanda ultrapassagem (kW)
    Demanda ultrapassagem FP (kW)
    Demanda ultrapassagem NP (kW)
    Despesa demanda ultrapassagem (R$)
    Despesa demanda ultrapassagem FP (R$)
    Despesa demanda ultrapassagem NP (R$)

    Demanda medida FP (kW)
    Demanda medida NP (kW)
    Demanda máxima FP (kW)
    Demanda máxima NP (kW)
    Demanda máxima corrigida FP (kW)
    Demanda máxima corrigida NP (kW)

    Demanda reativa excedente (kvar)
    Demanda reativa excedente FP (kvar)
    Demanda reativa excedente NP (kvar)
    Despesa demanda reativa excedente (R$)
    Despesa demanda reativa excedente FP (R$)
    Despesa demanda reativa excedente NP (R$)

    Consumo ativo (kWh)
    Consumo ativo FP (kWh)
    Consumo ativo NP (kWh)
    Despesa consumo ativo (R$)
    Despesa consumo ativo FP (R$)
    Despesa consumo ativo NP (R$)

    VERDE Consumo ativo (kWh)
    VERDE Consumo ativo FP (kWh)
    VERDE Consumo ativo NP (kWh)
    VERDE Despesa consumo ativo (R$)
    VERDE Despesa consumo ativo FP (R$)
    VERDE Despesa consumo ativo NP (R$)

    AMARELA Consumo ativo (kWh)
    AMARELA Consumo ativo FP (kWh)
    AMARELA Consumo ativo NP (kWh)
    AMARELA Despesa consumo ativo (R$)
    AMARELA Despesa consumo ativo FP (R$)
    AMARELA Despesa consumo ativo NP (R$)

    VERMELHA Consumo ativo (kWh)
    VERMELHA Consumo ativo FP (kWh)
    VERMELHA Consumo ativo NP (kWh)
    VERMELHA Despesa consumo ativo (R$)
    VERMELHA Despesa consumo ativo FP (R$)
    VERMELHA Despesa consumo ativo NP (R$)

    Consumo reativo (kvarh)
    Consumo reativo FP (kvarh)
    Consumo reativo NP (kvarh)
    Consumo reativo excedente (kvarh)
    Consumo reativo excedente FP (kvarh)
    Consumo reativo excedente NP (kvarh)
    Despesa consumo reativo excedente (R$)
    Despesa consumo reativo excedente FP (R$)
    Despesa consumo reativo excedente NP (R$)

    Dias bandeira VERDE
    Dias bandeira AMARELA
    Dias bandeira VERMELHA

    Fator de carga FP
    Fator de carga NP           


### Required Python modules

XlsxWriter: required to write on .xlsx file

    >> pip install xlsxwriter
Datetime: required to make calculations with dates

    >> pip install datetime
Tkinter: required to fetch for .txt file gui 

    >> pip install tkinter
