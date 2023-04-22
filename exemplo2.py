anos  = int(input("Insira sua idade expressa em anos:"))
meses = int(input("Insira a quantidade de meses desde seu último aniversário:"))
dias  = int(input("Insira a quantidade de dias "))

qtdDiasAno   = anos * 365
qtdDiasMeses = meses * 30 

qtdDiasDeNascimento = qtdDiasAno + qtdDiasMeses + dias

print("A quantidade de dias de nascimento é ", qtdDiasDeNascimento)