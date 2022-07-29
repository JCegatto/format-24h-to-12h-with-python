def convertHoras(horas):
    # Converte horas no formato 24h para o formato 12h
    if horas > 12:
        periodo = 'PM'
    else:
        periodo = 'AM'
    return periodo


while True:
    try:
        hora, minuto = input('Horario: ').split(':')
        hora, minuto = int(hora), int(minuto)
        if hora < 0 or hora >= 24:
            print('Horario invalido, tente novamente. ')
        elif minuto < 0 or minuto >= 60:
            print('Horario invalido, tente novamente.')
        else:
            break
    except:
        print('Formato de hora invalido, tente novamente. ')

periodo=convertHoras(hora)
if hora>12:
    hora=hora-12
print (f'{hora}:{minuto} {periodo}')'
