def writeMS(objeto, filePath):
    fp = open(filePath, "w")
    
    for item in objeto:
        last = len(item[LISTA]) - 1 # pegando no tamanho da lista subtrais 1 para obter o ultimo elemento
        print(item[LISTA][FIRST], item[LISTA][last])
        
        linha = "# " + item[LISTA][FIRST].getName() + " - " + item[LISTA][last].getName() + "\n"
        fp.write(linha)
        linha = str(item[TEMPO]) + ", "
        count = 1
        for elem in item[0]:
            if count == last:
                linha += elem.getName() + "\n"
                
            else:
                
                linha += elem.getName() + ", "
            count += 1
        fp.write(linha)
            

objeto = firstTest()
filePath = "l:/Aulas/Ano1/2Sem/ProgII/Projeto2/teste.txt"
writeMS(objeto, filePath)