

print('\n=== converta ===\n')
dias = 1
horas = 3
min = 46
seg = 40


print('=== dias em segundos ===')


diasSeg = dias * 24 * 60 * 60
horasSeg = horas * 60 * 60
minSeg = min * 60
print(diasSeg)
print(horasSeg)
print(minSeg)


print('segundos totais =', diasSeg + horasSeg + minSeg + seg)


print('\n=== segundos em dias ===')
segundos = 100000


segMinutos = segundos // 60
segFinais = segundos % 60  # segundos ja esta certo


segHoras = segMinutos // 60
minutosFinais = segMinutos % 60  # minuto ja esta certo


segDia = segHoras // 24  # dia ja esta certo
horasFinais = horas % 24


print(segundos)
print('dia', segDia)
print('horas', horasFinais)
print('minutos', minutosFinais)
print('segundos', segFinais)
