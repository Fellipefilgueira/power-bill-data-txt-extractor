def compute_B(j, text, data):    
    
    from datetime import datetime

    # set lists 

    ZDIFB_lst = []

    # set variables 

    ciclo = 0
    CAT = 0
    XCAT = 0
    YCAT = 0
    ZCAT = 0
    ZDIFB = 0

    for line in text[j]:

        # code for bills in 2019 or before 
        
        if line.find("14") == 0 and line.find("ZCAT") == 69:
            CAT = float(line[75:87])/100
            data['Consumo ativo (kWh)'] = CAT
            ZCAT = float(line[100:113])/100

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
            data['Despesa consumo ativo (R$)'] = (XCAT + YCAT)
        if line.find("14") == 0 and line.find("ZCRE") == 69:
            data['Consumo reativo excedente (kvarh)'] = float(line[75:87])/100
            data['Despesa consumo reativo excedente (R$)'] = float(line[100:113])/100
        if line.find("ZDIFBA") == 69:
            data['AMARELA Consumo ativo (kWh)'] = CAT
            data['AMARELA Despesa consumo ativo (R$)'] = XCAT + YCAT + ZCAT
            data['Dias bandeira AMARELA'] = ciclo
        if line.find("ZDIFBM") == 69:
            data['VERMELHA Consumo ativo (kWh)'] = CAT 
            data['VERMELHA Despesa consumo ativo (R$)'] =  XCAT + YCAT + ZCAT
            data['Dias bandeira VERMELHA'] = ciclo
        if line.find("ZDIFB") == 69:
            ZDIFB_lst.append(1)
            ZDIFB = sum(ZDIFB_lst)
            if ZDIFB == 0:
                data['VERDE Consumo ativo (kWh)'] = CAT 
                data['VERDE Despesa consumo ativo (R$)'] = XCAT + YCAT + ZCAT
                data['Dias bandeira VERDE'] = ciclo
        else: 
            ZDIFB_lst.append(0)
            ZDIFB = sum(ZDIFB_lst)
            if ZDIFB == 0:
                data['VERDE Consumo ativo (kWh)'] = CAT 
                data['VERDE Despesa consumo ativo (R$)'] = XCAT + YCAT + ZCAT
                data['Dias bandeira VERDE'] = ciclo
        if line.find('14') == 0 and line.find('WHTAX') == 69:
            data['Tributo (R$)'] = float(line[99:113])/100

        # ZDIFB_lst.append(line.find("ZDIFB"))
        # ZDIFB_avg = sum(ZDIFB_lst)/len(ZDIFB_lst)
        # if not 69 in ZDIFB_lst:
        #     data['VERDE Consumo ativo (kWh)'] = CAT 
        #     data['VERDE Despesa consumo ativo (R$)'] = XCAT + YCAT + ZCAT
        #     data['Dias bandeira VERDE'] = ciclo

        # # code for bills in 2019 or before 
        
        # if line.find("14") == 0 and line.find("ZCAT") == 69:
        #     CAT = float(line[75:87])/100
        #     data['Consumo ativo (kWh)'] = CAT
        #     ZCAT = float(line[100:113])/100
        # if line.find("ZDIFB") == 69:
        #     ZDIFB_count = ZDIFB_count + 1
        # if ZDIFB_count == 0:
        #     data['VERDE Consumo ativo (kWh)'] = CAT 
        #     data['VERDE Despesa consumo ativo (R$)'] = ZCAT
        #     data['Dias bandeira VERDE'] = ciclo
        # if line.find('ZDIFBA') == 69:
        #     data['AMARELA Consumo ativo (kWh)'] = CAT
        #     data['AMARELA Despesa consumo ativo (R$)'] = ZCAT
        #     data['Dias bandeira AMARELA'] = ciclo
        # if line.find('ZDIFBM') == 69:
        #     data['VERMELHA Consumo ativo (kWh)'] = CAT 
        #     data['VERMELHA Despesa consumo ativo (R$)'] =  ZCAT
        #     data['Dias bandeira VERMELHA'] = ciclo
        

    return(data)