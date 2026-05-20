import pandas as pd
import os
from time import sleep as mimir
import sys



PLANILHA_1 = r"C:\Users\SuportedeTI-AirMinas\AIR MINAS AR CONDICIONADO LTDA\TI - Documentos\CONTROLE DE ATIVOS\Inventario_TI_AirMinas.xlsx"#local da planilha
          

if sys.argv[1] == "--contar":#comando de contar
    os.system("taskkill /im excel.exe /f || cls")
    mimir(2)
    para = False
    for root,dirs,arquivos in os.walk("C:\\"):
        for i in arquivos:
            if  "pertence.xlsx" == i:#deleta outras versoes do pertence
                os.remove(f"{root}\\{i}")
                break
                para=True
        if para:
            break

    meu = pd.read_excel(PLANILHA_1, sheet_name="Inventário", header=1)#le a planilha, na parte de inventario neste caso, e a 1 linha conta como read
    oio = meu.columns#array contendo todos os nomes das colunas em meu
    numero = 0
    print("temos:\n")
    for i in oio:#printa a coluna
        numero = numero + 1
        print(f'[{numero}] coluna: ({i})')
    catigoria = input("diga a coluna que sera metrificada:  ")

    df = pd.DataFrame({#cria planilha
        "Nome": pd.Series(dtype="str"),
        "Dispositivos": pd.Series(dtype="int")
    })

    numero = 0
    
    # Agrupar e contar
    try:
        contador = meu[oio[int(catigoria)-1]].value_counts(dropna=False)#variavel contendo nomes na planilha e vezes que o nome repete, INCLUSIVE AS VAZIAS 
    except ValueError:
        contador = meu[catigoria].value_counts(dropna=False)#variavel contendo nomes na planilha e vezes que o nome repete, INCLUSIVE AS VAZIAS
    
    for usuario, qtd in contador.items():
        if usuario != "OBRIGATÓRIO":
            df.at[numero,"Nome"]= str(usuario)
            df.at[numero,"Dispositivos"]= qtd
            numero = numero+1

    df.to_excel("pertence.xlsx", index=False)

if sys.argv[1] == "--modificar":
    os.system("taskkill /im excel.exe /f || cls")
    mimir(2)

    for root,dirs,arquivos in os.walk("C:\\"):
        for i in arquivos:
            if  "pertence.xlsx" == i:#deleta outras versoes do pertence
                os.remove(f"{root}\\{i}")
                break

    meu = pd.read_excel(PLANILHA_1, sheet_name="Inventário", header=1)#le a planilha na parte de inventario, e a 1 linha conta como read

    meu = meu.drop_duplicates(subset=['Cód. Patrimônio'])#apaga as duplicatas em codigo de patrimonio

    meu.to_excel("pertence.xlsx", index=False)
