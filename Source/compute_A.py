def compute_A(j, text, data):

    from datetime import datetime

    # set variables 

    ciclo = 0
    CANP = 0
    CAFP = 0
    XCANP = 0
    XCAFP = 0
    YCANP = 0
    YCAFP = 0
    DEMNP = 0
    DEMFP = 0
    
    for line in text[j]:
        if line.find('11') == 0:
            data['Conta contrato'] = line[26:36]
        if line.find('12') == 0 and line.find('A4') == 81:
            data['Classificação'] = line[81:83]
            data['Data de leitura'] = datetime.strptime(f'{line[102:110]}', '%d%m%Y').strftime('%d/%m/%Y')
            data['Valor da fatura (R$)'] = float(line[138:151])/100
            data['Demanda ativa contratada (kW)'] = float(line[187:216])/100
        if line.find('12') == 0 and line.find('A3') == 81:
            data['Classificação'] = line[81:83]
            data['Data de leitura'] = datetime.strptime(f'{line[102:110]}', '%d%m%Y').strftime('%d/%m/%Y')
            data['Valor da fatura (R$)'] = float(line[138:151])/100
            data['Demanda ativa contratada NP (kW)'] = float(line[187:216])/100
            data['Demanda ativa contratada FP (kW)'] = float(line[216:228])/100
        if line.find('13') == 0 and line.find('CANP') == 87:
            data['Consumo ativo NP (kWh)'] = float(line[151:166])/100
            d0 = datetime.strptime(f'{line[93:101]}', '%d%m%Y') 
            d1 = datetime.strptime(f'{line[101:109]}', '%d%m%Y')
            ciclo = int(abs((d1-d0).days))+1
        if line.find('13') == 0 and line.find('CAFP') == 87:
            data['Consumo ativo FP (kWh)'] = float(line[151:166])/100
        if line.find('13') == 0 and line.find('DEMNP') == 87:
            DEMNP = float(line[151:166])/100
            data['Demanda máxima NP (kW)'] = DEMNP
        if line.find('13') == 0 and line.find('DEMFP') == 87:
            DEMFP = float(line[151:166])/100
            data['Demanda máxima FP (kW)'] = DEMFP
        if line.find('13') == 0 and line.find('CRNP') == 87:
            data['Consumo reativo NP (kvarh)'] = float(line[151:166])/100
        if line.find('13') == 0 and line.find('CRFP') == 87:
            data['Consumo reativo FP (kvarh)'] = float(line[151:166])/100
        if line.find('13') == 0 and line.find('CRENP') == 87:
            data['Consumo reativo excedente NP (kvarh)'] = float(line[151:166])/100     
        if line.find('13') == 0 and line.find('CREFP') == 87:
            data['Consumo reativo excedente FP (kvarh)'] = float(line[151:166])/100  
        if line.find('13') == 0 and line.find('DMCRNP') == 87: 
            data['Demanda máxima corrigida NP (kW)'] = float(line[151:166])/100
        if line.find('13') == 0 and line.find('DMCRFP') == 87:
            data['Demanda máxima corrigida FP (kW)'] = float(line[151:166])/100              
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
            CANP = float(line[75:87])/100
            XCANP = float(line[100:113])/100   
        if line.find('14') == 0 and line.find('XCAFP') == 69:
            CAFP = float(line[75:87])/100
            XCAFP = float(line[100:113])/100        
        if line.find('14') == 0 and line.find('YCANP') == 69:
            YCANP = float(line[100:113])/100
        if line.find('14') == 0 and line.find('YCAFP') == 69:
            YCAFP = float(line[100:113])/100
            data['Despesa consumo ativo NP (R$)'] = XCANP + YCANP
            data['Despesa consumo ativo FP (R$)'] = XCAFP + YCAFP
            data['Fator de carga NP'] = round( CANP / ( DEMNP * ( ciclo - 8 )*3 ), 2)
            data['Fator de carga FP'] = round( CAFP / ( DEMFP * ( ( ciclo - 8 )*21 + 8*24 )), 2)
        if line.find('YCANPG') == 69: # check code with green flag in old files 
            data['VERDE Consumo ativo NP (kWh)'] = CANP
            data['VERDE Consumo ativo FP (kWh)'] = CAFP                   
            data['VERDE Despesa consumo ativo NP (R$)'] = XCANP + YCANP
            data['VERDE Despesa consumo ativo FP (R$)'] = XCAFP + YCAFP
            data['Dias bandeira VERDE'] = ciclo                       
        if line.find('YCANPA') == 69:
            data['AMARELA Consumo ativo NP (kWh)'] = CANP
            data['AMARELA Consumo ativo FP (kWh)'] = CAFP                   
            data['AMARELA Despesa consumo ativo NP (R$)'] = XCANP + YCANP
            data['AMARELA Despesa consumo ativo FP (R$)'] = XCAFP + YCAFP
            data['Dias bandeira AMARELA'] = ciclo
        if line.find('YCANPR') == 69: # check code with red flag in old files  
            data['VERMELHA Consumo ativo NP (kWh)'] = CANP
            data['VERMELHA Consumo ativo FP (kWh)'] = CAFP                   
            data['VERMELHA Despesa consumo ativo NP (R$)'] = XCANP + YCANP
            data['VERMELHA Despesa consumo ativo FP (R$)'] = XCAFP + YCAFP
            data['Dias bandeira VERMELHA'] = ciclo                    
        if line.find('14') == 0 and line.find('ZCRENP') == 69:
            data['Despesa consumo reativo excedente NP (R$)'] = float(line[100:113])/100
        if line.find('14') == 0 and line.find('ZCREFP') == 69:
            data['Despesa consumo reativo excedente FP (R$)'] = float(line[100:113])/100
        if line.find('14') == 0 and line.find('WHTAX ') == 69:
            data['Tributo (R$)'] = float(line[99:113])/100
            
    return(data)