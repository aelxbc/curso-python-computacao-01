segundos_str= input("Por favor, entre com o número de segundos que deseja converter: ")
total_segundos = int(segundos_str)

dias = total_segundos // 86400 # 86400 segundos = 1 dia 
horas = total_segundos // 3600 # 3600 segundos = 1 hora
segundos_restantes = total_segundos % 3600
minutos = segundos_restantes // 60 # 60 segundos = 1 minuto
segundos_restantes_final = segundos_restantes % 60

print(dias, "dias", horas, "horas, ", minutos, "minutos e", segundos_restantes_final, "segundos.")

 
