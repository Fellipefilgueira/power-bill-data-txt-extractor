def compute_A(j, text, data):

    from datetime import datetime

    # set lists 

    DEMNP_lst = []
    DEMFP_lst = []
    CRNP_lst = []
    CRFP_lst = []
    CRENP_lst = []
    CREFP_lst =[]
    DMCRNP_lst = []
    DMCRFP_lst = []

    # set variables

    ciclo = 0
    ciclo_bd1 = 0
    ciclo_bd2 = 0
    CANP = 0
    CANPD = 0
    CANPA = 0
    CANPM = 0
    CAFP = 0
    CAFPD = 0
    CAFPA = 0
    CAFPM = 0
    XCANP = 0
    XCAFP = 0
    YCANP = 0
    YCAFP = 0
    DEMNP = 0
    DEMFP = 0
    
    for line in text[j]: 

        # code for bills in 2020 or after

        if line.find('11') == 0:
            data['Conta contrato'] = line[26:36]
        if line.find('12') == 0 and line.find('A4') == 81:
            data['Classificação'] = line[81:83]
            data['Data de leitura'] = datetime.strptime(f'{line[102:110]}', '%d%m%Y').strftime('%d/%m/%Y')
            data['Valor da fatura (R$)'] = float(line[138:151])/100
            data['Demanda ativa contratada (kW)'] = float(line[187:216])/100
            d0 = datetime.strptime(f'{line[118:126]}', '%d%m%Y') 
            d1 = datetime.strptime(f'{line[126:134]}', '%d%m%Y')
            ciclo = int(abs((d1-d0).days))+1
        if line.find('12') == 0 and line.find('A3') == 81:
            data['Classificação'] = line[81:83]
            data['Data de leitura'] = datetime.strptime(f'{line[102:110]}', '%d%m%Y').strftime('%d/%m/%Y')
            data['Valor da fatura (R$)'] = float(line[138:151])/100
            data['Demanda ativa contratada NP (kW)'] = float(line[187:216])/100
            data['Demanda ativa contratada FP (kW)'] = float(line[216:228])/100
            data['Demanda ativa contratada (kW)'] = float(line[187:216])/100
            d0 = datetime.strptime(f'{line[118:126]}', '%d%m%Y') 
            d1 = datetime.strptime(f'{line[126:134]}', '%d%m%Y')
        if line.find('13') == 0 and line.find('DEMNP') == 87:
            DEMNP_lst.append(float(line[151:166])/100)
            DEMNP = sum(DEMNP_lst)
            data['Demanda máxima NP (kW)'] = DEMNP
        if line.find('13') == 0 and line.find('DEMFP') == 87:
            DEMFP_lst.append(float(line[151:166])/100)
            DEMFP = sum(DEMFP_lst)
            data['Demanda máxima FP (kW)'] = DEMFP
        if line.find('13') == 0 and line.find('CRNP') == 87:
            CRNP_lst.append(float(line[151:166])/100)
            data['Consumo reativo NP (kvarh)'] = sum(CRNP_lst)
        if line.find('13') == 0 and line.find('CRFP') == 87:
            CRFP_lst.append(float(line[151:166])/100)
            data['Consumo reativo FP (kvarh)'] = sum(CRFP_lst)
        if line.find('13') == 0 and line.find('CRENP') == 87:
            CRENP_lst.append(float(line[151:166])/100)
            data['Consumo reativo excedente NP (kvarh)'] = sum(CRENP_lst)
        if line.find('13') == 0 and line.find('CREFP') == 87:
            CREFP_lst.append(float(line[151:166])/100)
            data['Consumo reativo excedente FP (kvarh)'] = sum(CREFP_lst)
        if line.find('13') == 0 and line.find('DMCRNP') == 87:
            DMCRNP_lst.append(float(line[151:166])/100)
            data['Demanda máxima corrigida NP (kW)'] = sum(DMCRNP_lst)
        if line.find('13') == 0 and line.find('DMCRFP') == 87:
            DMCRFP_lst.append(float(line[151:166])/100)
            data['Demanda máxima corrigida FP (kW)'] = sum(DMCRFP_lst)
        if line.find('14') == 0 and line.find('ZDEM') == 69:
            data['Demanda ativa (kW)'] = float(line[75:87])/100
            data['Despesa demanda ativa (R$)'] = float(line[100:113])/100
        if line.find('14') == 0 and line.find('ZDNP') == 69:
            data['Demanda ativa NP (kW)'] = float(line[75:87])/100
            data['Despesa demanda ativa NP (R$)'] = float(line[100:113])/100
        if line.find('14') == 0 and line.find('ZDFP') == 69:
            data['Demanda ativa FP (kW)'] = float(line[75:87])/100
            data['Despesa demanda ativa FP (R$)'] = float(line[100:113])/100
        if line.find('14') == 0 and line.find('ZDULT') == 69:
            data['Demanda ultrapassagem (kW)'] = float(line[75:87])/100
            data['Despesa demanda ultrapassagem (R$)'] = float(line[100:113])/100
        if line.find('14') == 0 and line.find('ZDRE ') == 69:
            data['Demanda reativa excedente (kvar)'] = float(line[75:87])/100
            data['Despesa demanda reativa excedente (R$)'] = float(line[100:113])/100
        if line.find('14') == 0 and line.find('ZDRENP') == 69:
            data['Demanda reativa excedente NP (kvar)'] = float(line[75:87])/100
            data['Despesa demanda reativa excedente NP (R$)'] = float(line[100:113])/100
        if line.find('14') == 0 and line.find('ZDREFP') == 69:
            data['Demanda reativa excedente FP (kvar)'] = float(line[75:87])/100
            data['Despesa demanda reativa excedente FP (R$)'] = float(line[100:113])/100            
        if line.find('14') == 0 and line.find('XCANP') == 69:
            data['Consumo ativo NP (kWh)'] = float(line[75:87])/100
            CANP = float(line[75:87])/100
            XCANP = float(line[100:113])/100   
        if line.find('14') == 0 and line.find('XCAFP') == 69:
            data['Consumo ativo FP (kWh)'] = float(line[75:87])/100
            CAFP = float(line[75:87])/100
            XCAFP = float(line[100:113])/100        
        if line.find('14') == 0 and line.find('YCANP') == 69:
            YCANP = float(line[100:113])/100
        if line.find('14') == 0 and line.find('YCAFP') == 69:
            YCAFP = float(line[100:113])/100
            data['Despesa consumo ativo NP (R$)'] = XCANP
            data['Despesa consumo ativo FP (R$)'] = XCAFP 
            data['Fator de carga NP'] = round( CANP / ( DEMNP * ( ciclo - 8 )*3 ), 2)
            data['Fator de carga FP'] = round( CAFP / ( DEMFP * ( ( ciclo - 8 )*21 + 8*24 )), 2)
        if line.find('YCAFPD') == 69: # check code with green flag in old files 
            data['VERDE Consumo ativo NP (kWh)'] = CANP
            data['VERDE Consumo ativo FP (kWh)'] = CAFP                   
            data['VERDE Despesa consumo ativo NP (R$)'] = YCANP
            data['VERDE Despesa consumo ativo FP (R$)'] = YCAFP
            data['Dias bandeira VERDE'] = ciclo                       
        if line.find('YCAFPA') == 69:
            data['AMARELA Consumo ativo NP (kWh)'] = CANP
            data['AMARELA Consumo ativo FP (kWh)'] = CAFP                   
            data['AMARELA Despesa consumo ativo NP (R$)'] = YCANP
            data['AMARELA Despesa consumo ativo FP (R$)'] = YCAFP
            data['Dias bandeira AMARELA'] = ciclo
        if line.find('YCAFPM') == 69: # check code with red flag in old files  
            data['VERMELHA Consumo ativo NP (kWh)'] = CANP
            data['VERMELHA Consumo ativo FP (kWh)'] = CAFP                   
            data['VERMELHA Despesa consumo ativo NP (R$)'] = YCANP
            data['VERMELHA Despesa consumo ativo FP (R$)'] = YCAFP
            data['Dias bandeira VERMELHA'] = ciclo                    
        if line.find('14') == 0 and line.find('ZCRENP') == 69:
            data['Despesa consumo reativo excedente NP (R$)'] = float(line[100:113])/100
        if line.find('14') == 0 and line.find('ZCREFP') == 69:
            data['Despesa consumo reativo excedente FP (R$)'] = float(line[100:113])/100
        if line.find('14') == 0 and line.find('WHTAX ') == 69:
            data['Tributo (R$)'] = float(line[99:113])/100

        #
        # code for bills in 2019 or before 
        #
        #
        #

        if line.find('14') == 0 and line.find('ZCANP') == 69:
            ZCANP = float(line[100:113])/100 
        if line.find('14') == 0 and line.find('ZCAFP') == 69:
            ZCAFP = float(line[100:113])/100 
        if line.find('ZCANPD') == 69: # check code with green flag in old files 
            CANPD = float(line[75:87])/100
            data['VERDE Consumo ativo NP (kWh)'] = CANPD
            data['VERDE Despesa consumo ativo NP (R$)'] = ZCANP
        if line.find('ZCANPA') == 69:
            CANPA = float(line[75:87])/100
            data['AMARELA Consumo ativo NP (kWh)'] = CANPA
            data['AMARELA Despesa consumo ativo NP (R$)'] = ZCANP
        if line.find('ZCANPM') == 69: # check code with red flag in old files 
            CANPM = float(line[75:87])/100
            data['VERMELHA Consumo ativo NP (kWh)'] = CANPM
            data['VERMELHA Despesa consumo ativo NP (R$)'] = ZCANP
        if line.find('ZCAFPD') == 69: # check code with green flag in old files 
            CAFPD = float(line[75:87])/100
            data['VERDE Consumo ativo FP (kWh)'] = CAFPD                   
            data['VERDE Despesa consumo ativo FP (R$)'] = ZCAFP
            data['Dias bandeira VERDE'] = ciclo                       
        if line.find('ZCAFPA') == 69:
            CAFPA = float(line[75:87])/100
            data['AMARELA Consumo ativo FP (kWh)'] = CAFPA                  
            data['AMARELA Despesa consumo ativo FP (R$)'] = ZCAFP
            data['Dias bandeira AMARELA'] = ciclo
        if line.find('ZCAFPM') == 69: # check code with red flag in old files  
            CAFPM = float(line[75:87])/100
            data['VERMELHA Consumo ativo FP (kWh)'] = CAFPM                  
            data['VERMELHA Despesa consumo ativo FP (R$)'] = ZCAFP
            data['Dias bandeira VERMELHA'] = ciclo 
        if line.find('14') == 0 and line.find('ZCANP') == 69:
            CANP = CANPD + CANPA + CANPM
            data['Consumo ativo NP (kWh)'] = CANP
            data['Fator de carga NP'] = round( CANP / ( DEMNP * ( ciclo - 8 )*3 ), 2)
        if line.find('14') == 0 and line.find('ZCAFP') == 69:
            CAFP = CAFPD + CAFPA + CAFPM
            data['Consumo ativo FP (kWh)'] = CAFP
            data['Fator de carga FP'] = round( CAFP / ( DEMFP * ( ( ciclo - 8 )*21 + 8*24 )), 2)

    return(data)