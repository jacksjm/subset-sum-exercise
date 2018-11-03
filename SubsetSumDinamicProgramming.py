# Chamada da Função recebe o Conjunto e o Valor de Soma
def subset_sum_dinamic_programming(aConjunto, nTestValue):

	aReturn = []

	# Cria uma matriz vazia para receber os valores
	# Alimenta a matriz de Retorno com a quantidade de itens do Conjunto mais uma posição,
	# Obs: a posição adicionada é apenas para não necessitar ficar tratando a cada loop dos for's
	for nCnt in range(len(aConjunto) + 1):
		aReturn.append([False] * (nTestValue + 1))

	# Define primeira posição como verdadeira
	aReturn[len( aConjunto )][0] = True

	for nCnt in range(len(aConjunto)-1,-1,-1):
		aReturn[nCnt][0] = True
		# Percorre as posições inicias definido já que não há como
		# avaliar posições anteriores ao seu próprio valor
		for nCnt2 in range(1,aConjunto[nCnt]-1):
			aReturn[nCnt][nCnt2] = aReturn[nCnt+1][nCnt2]

		# Percorre as demais posições para verificar se já está verdadeira ou
		# se alguma posição menos seu valor corresponde a uma verdade
		for nCnt2 in range(aConjunto[nCnt],nTestValue + 1):
			aReturn[nCnt][nCnt2] = aReturn[nCnt+1][nCnt2] or aReturn[nCnt+1][nCnt2 - aConjunto[nCnt]]
	return aReturn

# Define os valores
S = [2, 3, 5, 7, 8, 10, 15]
t = 23

aRet = subset_sum_dinamic_programming(S,t)

# Estrutura impressão customizada
cPrint = "|  |"
cSep = "----"
for nCnt in range(t+1):
	cPrint = cPrint + "|" + str(nCnt).zfill(2) + "|"
	cSep = cSep + "----"

print(cSep)
print(cPrint)
print(cSep)
for aLine in aRet:
	cLine = "|" + str(aRet.index(aLine) + 1).zfill(2) + "|"
	for lPos in aLine:
		if lPos:
			cLine = cLine + "|V |"
		else:
			cLine = cLine + "|F |"
	print(cLine)
	print(cSep)