atom_type_dict = {
 'HOC': '01',  'HOK': '02',  'HOP': '03', 'HOY': '04',
'OAP1': '11', 'OAP2': '12',  'OC1': '13', 'OC2': '14',  'OC3': '15',
 'OC4': '16',  'OC5': '17', 'OC23': '18','OC24': '19',  'OY1': '20',
 'OY2': '21',  'OY3': '22',  'OY4': '23', 'OY5': '24',  'OY6': '25',
 'OY7': '26',  'OY8': '27',  'OY9': '28', 
 'AC1': '41',  'AY1': '42',  'AY2': '43','AYT1': '44', 'AYT2': '45',
 'SC1': '51',  'SC4': '52',  'SY1': '53', 'SY2': '54',
 'PAP': '61',
 'NA+': 'NAp',  'K+': 'Kp', 'CA++': 'CApp', 'CA+A': 'CApA', 'CA+H': 'CApH',
  'AL': 'Al0',  'NI': 'Ni0',  'CU': 'Cu0', 'PD': 'Pd0', 'AG' : 'Ag0',
  'PT': 'Pt0',  'AU': 'Au0',  'PB': 'Pb0'
}

for i in atom_type_dict.keys():
    atom_type_dict[i.lower()] = atom_type_dict[i]

