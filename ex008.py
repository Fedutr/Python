medida = float(input('Digite uma medida em metro: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000

print('A sua medida em metros de {:.2f}m é convertida em km, hm, dam, dm, cm e mm é a seguinte'.format(medida))
print('{:.2f}km; \n{:.2f}hm; \n{:.2f}dam; \n{:.2f}m; \n{:.2f}dm; \n{:.2f}cm; \n{:.2f}mm.'.format(km, hm, dam, medida, dm, cm, mm))