alt = float(input('Qual a altura da parede (m): '))
lar = float(input('Qual a largura da parede (m): '))
area = alt * lar
balde = area/2
print('Com a sua parede tem {}m de altura e {}m de largura, a sua respectiva área é de {}m²'. format(alt,lar,area))
print('Como cada litro de tinta linta 2m², então vai precisar de {}L'.format(balde))