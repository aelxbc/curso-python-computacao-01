segundosTotal = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundosTotal // 86400
segundosRestantes = segundosTotal % 86400
horas = segundosRestantes // 3600
segundosRestantes = segundosRestantes % 3600
minutos = segundosRestantes // 60
segundos = segundosRestantes % 60

print (dias, "dias,", horas,"horas,", minutos, "minutos e", segundos, "segundos.")

