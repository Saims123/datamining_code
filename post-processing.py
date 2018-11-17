import pandas
import matplotlib.pyplot as plt
import pylab as pl

df = pandas.read_csv('./predictions_weka.csv')

free=[['Accordian'],212]
lip=[['Trombone',  'Trumpet', 'Trumpet', 'Tuba', 'FrenchHorn', 'EnglishHorn'], 3020]
single=[['Clarinet', 'Saxophone'], 1936]
double=[['Oboe', 'Bassoon'], 1208]
side=[['Flute', 'Piccolo'], 1379]
simple=[['Piano', 'SynthBass'],787]
composite=[['Viola', 'Cello', 'DoubleBass', 'AcousticBass', 'Violin'],2458]


replacements = {
    'TenorSaxophone' : 'Saxophone',
    'CTrumpet' : 'Trumpet',
    'B-flatclarinet' : 'Clarinet',
    'DTrumpet' : 'Trumpet',
    'ElectricGuitar' : 'Guitar',
    'TenorTrombone' : 'Trombone',
    'AltoSaxophone' : 'Saxophone',
    'SopranoSaxophone' : 'Saxophone',
    'BaritoneSaxophone' : 'Saxophone',
    'BassSaxophone' : 'Saxophone',
    'AcousticBass':  'DoubleBass',
    'B-flatTrumpet' : 'Trumpet',
    'B-FlatTrumpet' : 'Trumpet'
}
df['Instrument'].replace(replacements, inplace=True)

print(df.groupby(['Instrument']))
chart = df.groupby(['Instrument']).size().reset_index(name = 'count')
print('-+--+--+--+--+--+--+--+--+--+-Class2_count_calculation-+--+--+--+--+--+---+--+--+-+--+--+--+-')
print('Free : ' , chart.loc[chart['Instrument'].isin(free[0]), 'count'].sum(),  ' Diff : ', free[1] - chart.loc[chart['Instrument'].isin(free[0]), 'count'].sum() )
print('Lip_vibrate : ' ,chart.loc[chart['Instrument'].isin(lip[0]), 'count'].sum(), ' Diff : ', lip[1] - chart.loc[chart['Instrument'].isin(lip[0]), 'count'].sum() )
print('Single : ' ,chart.loc[chart['Instrument'].isin(single[0]), 'count'].sum(),  ' Diff : ', single[1] - chart.loc[chart['Instrument'].isin(single[0]), 'count'].sum() )
print('Double : ' ,chart.loc[chart['Instrument'].isin(double[0]), 'count'].sum() , ' Diff : ', double[1] - chart.loc[chart['Instrument'].isin(double[0]), 'count'].sum() )
print('Side : ' ,chart.loc[chart['Instrument'].isin(side[0]), 'count'].sum() , ' Diff : ', side[1] - chart.loc[chart['Instrument'].isin(side[0]), 'count'].sum() )
print('Simple : ' ,chart.loc[chart['Instrument'].isin(simple[0]), 'count'].sum(), ' Diff : ', simple[1] - chart.loc[chart['Instrument'].isin(simple[0]), 'count'].sum() )
print('Composite : ' ,chart.loc[chart['Instrument'].isin(composite[0]), 'count'].sum() , ' Diff : ', composite[1] - chart.loc[chart['Instrument'].isin(composite[0]), 'count'].sum())

print(chart)

p = chart.plot(grid=True,kind ='bar',x='Instrument', y='count', legend=False)
totals = []
for i in chart['count']:
   totals.append(i)

loop = 0

for i in p.patches:
    p.text(i.get_x()+ 0.05, i.get_height() + 3, str(totals[loop]) , fontsize=15, color='black')
    loop += 1
pl.show()

df.to_csv('./predictions_weka.csv', index=False)
