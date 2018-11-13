import pandas
import matplotlib.pyplot as plt
import pylab as pl

df = pandas.read_csv('./predictions_weka.csv')



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
print(chart['count'])

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
