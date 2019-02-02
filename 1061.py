dia_ini = input().split(' ')[1]
hora_ini, min_ini, seg_ini = input().split(' : ')
dia_fim = input().split(' ')[1]
hora_fim, min_fim, seg_fim = input().split(' : ')

segx, minx, horax = 0, 0, 0
hora_ini, min_ini, seg_ini = int(hora_ini), int(min_ini), int(seg_ini)
hora_fim, min_fim, seg_fim = int(hora_fim), int(min_fim), int(seg_fim)
dia_fim, dia_ini = int(dia_fim), int(dia_ini)

if seg_fim >= seg_ini:
    segx = seg_fim - seg_ini
else:
    segx = seg_fim - seg_ini + 60
    min_fim -= 1

if min_fim >= min_ini:
    minx = min_fim - min_ini
else:
    minx = min_fim - min_ini +60
    hora_fim -= 1

if hora_fim >= hora_ini:
    horax = hora_fim - hora_ini
else:
    horax = hora_fim - hora_ini + 24
    dia_fim -= 1

diax = dia_fim - dia_ini

print('{} dia(s)' .format(diax))
print('{} hora(s)' .format(horax))
print('{} minuto(s)' .format(minx))
print('{} segundo(s)' .format(segx))