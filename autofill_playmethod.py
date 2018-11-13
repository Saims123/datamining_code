import pandas
import csv
blow = ['TenorTrombone' , 'TenorSaxophone' ,'Trumpet' ,'DTrumpet','CTrumpet','SopranoSaxophone','AltoSaxophone', 'BassSaxophone' ,'BaritoneSaxophone' , 'Oboe', 'Clarinet', 'B-FlatTrumpet', 'B-flatclarinet' , 'Tuba']
hit = ['Piano','Accordian', 'Vibraphone', 'Marimba']
strings= ['Viola', 'Cello', 'ElectricGuitar' ,'Guitar', 'DoubleBass','Bass', 'AcousticBass', 'Violin']
playMethod= ['string','blown','struck_Hrm']

df = pandas.read_csv('./train_replace.csv')


df.loc[df['mix1_instrument'].isin(strings), 'playmethod'] = 'string'

df.loc[df['mix1_instrument'].isin(hit), 'playmethod'] = 'struck_Hmr'

df.loc[df['mix1_instrument'].isin(blow), 'playmethod'] = 'blown'



print(df['mix1_instrument'], df['playmethod'])

df.to_csv('./train_replace.csv', index=False)