import pandas
import csv

free=['Accordian']
lip=['TenorTrombone',  'Trumpet', 'DTrumpet','CTrumpet', 'Tuba', 'FrenchHorn', 'EnglishHorn']
single=['Clarinet', 'B-FlatTrumpet', 'B-flatclarinet', 'TenorSaxophone','SopranoSaxophone','AltoSaxophone', 'BassSaxophone' ,'BaritoneSaxophone' ]
double=['Oboe', 'Bassoon']
side=['Flute', 'Piccolo']
simple=['Piano', 'SynthBass']
composite=['Viola', 'Cello' , 'ElectricGuitar' ,'Guitar', 'DoubleBass','Bass', 'AcousticBass', 'Violin']


aero = ['aero_free-reed','aero_lip-vibrated','aero_single-reed','aero_double-reed','aero_side']
chrd = ['chrd_simple', 'chrd_composite']

df = pandas.read_csv('./train_replace.csv')


df.loc[df['mix1_instrument'].isin(free), 'class2'] = aero[0]
df.loc[df['mix1_instrument'].isin(lip), 'class2'] = aero[1]
df.loc[df['mix1_instrument'].isin(single), 'class2'] = aero[2]
df.loc[df['mix1_instrument'].isin(double), 'class2'] = aero[3]
df.loc[df['mix1_instrument'].isin(side), 'class2'] = aero[4]
df.loc[df['mix1_instrument'].isin(simple), 'class2'] = chrd[0]
df.loc[df['mix1_instrument'].isin(composite), 'class2'] = chrd[1]

df.loc[df['mix1_instrument'].isin((free + lip+single+double)), 'class1'] = 'aerophone'
df.loc[df['mix1_instrument'].isin((simple + composite)), 'class1'] = 'chordophone'



print(df['mix1_instrument'], df['class2'], df['class1'])

df.to_csv('./train_replace.csv', index=False)