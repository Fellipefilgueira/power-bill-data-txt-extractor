def compute_B(j, text, data):    
    
    from datetime import datetime

    # set variables 

    ciclo = 0

    for line in text[j]:
        if line.find("11") == 0:
            data['Conta contrato'] = line[26:36]
        if line.find("12") == 0:
            data['Classificação'] = line[81:83]
            data['Data de leitura'] = datetime.strptime(f'{line[102:110]}', '%d%m%Y').strftime('%d/%m/%Y')  
            data['Valor da fatura (R$)'] = float(line[138:151])/100
        if line.find("13") == 0 and line.find("CAT") == 87:
            d0 = datetime.strptime(f'{line[93:101]}', '%d%m%Y') 
            d1 = datetime.strptime(f'{line[101:109]}', '%d%m%Y')
            ciclo = int(abs((d1-d0).days))+1
        if line.find("13") == 0 and line.find("CRT") == 87:
            data['Consumo reativo (kvarh)'] = float(line[136:166])/100
        if line.find("14") == 0 and line.find("XCAT") == 69:
            CAT = float(line[75:87])/100
            data['Consumo ativo (kWh)'] = CAT
            XCAT = float(line[100:113])/100
        if line.find("14") == 0 and line.find("YCAT") == 69:
            YCAT = float(line[100:113])/100
            data['Despesa consumo ativo (R$)'] = XCAT + YCAT
        if line.find("14") == 0 and line.find("ZCRE") == 69:
            data['Consumo reativo excedente (kvarh)'] = float(line[75:87])/100
            data['Despesa consumo reativo excedente (R$)'] = float(line[100:113])/100 
        if line.find("14") == 0 and line.find("ZDIFB") == 69: # vai apresentar problema quando um mês possuir duas bandeiras
            bandeira = line[ 133 : line.find('\n') ]
            if bandeira == 'VERDE':
                data['VERDE Consumo ativo (kWh)'] = CAT 
                data['VERDE Despesa consumo ativo (R$)'] = XCAT + YCAT
                data['Dias bandeira VERDE'] = ciclo
            if bandeira == 'AMARELA':
                data['AMARELA Consumo ativo (kWh)'] = CAT
                data['AMARELA Despesa consumo ativo (R$)'] = XCAT + YCAT
                data['Dias bandeira AMARELA'] = ciclo
            if bandeira == 'VERMELHA':
                data['VERMELHA Consumo ativo (kWh)'] = CAT 
                data['VERMELHA Despesa consumo ativo (R$)'] =  XCAT + YCAT
                data['Dias bandeira VERMELHA'] = ciclo
        if line.find('14') == 0 and line.find('WHTAX') == 69:
            data['Tributo (R$)'] = float(line[99:113])/100
                
    return(data)