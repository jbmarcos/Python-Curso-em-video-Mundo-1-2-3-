# mede área quadada e a quantidade detinta para cobrir essa área -=-

alt = float( input( 'Qual a altura da parede? '))
lar = float( input( 'Qual a larguta da parede? '))
area = alt * lar
tinta = area / 2
print('para uma parede de {:.2f} metros quadrados, serão necessários {:.2f} litros de tinta.'.format(area, tinta))