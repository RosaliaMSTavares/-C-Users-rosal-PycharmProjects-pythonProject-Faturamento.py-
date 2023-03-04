# Define o valor faturado em cada estado
faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 2716.48
faturamento_outros = 19849.53

# Calcula o valor total
valor_total = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

# Calcula o percentual de representação de cada estado
percentual_sp = (faturamento_sp / valor_total) * 100
percentual_rj = (faturamento_rj / valor_total) * 100
percentual_mg = (faturamento_mg / valor_total) * 100
percentual_es = (faturamento_es / valor_total) * 100
percentual_outros = (faturamento_outros / valor_total) * 100

# Imprime os resultados
print("Percentual de representação de cada estado no faturamento mensal da distribuidora:")
print("São Paulo: {:.2f}%".format(percentual_sp))
print("Rio de Janeiro: {:.2f}%".format(percentual_rj))
print("Minas Gerais: {:.2f}%".format(percentual_mg))
print("Espírito Santo: {:.2f}%".format(percentual_es))
print("Outros: {:.2f}%".format(percentual_outros))