import pandas

df = pandas.read_csv('./probe.csv')


df.loc[df['Id'].between(1,5499), 'Instrument'] = 'EnglishHorn'
df.loc[df['Id'].between(5500,11000), 'Instrument'] = 'FrenchHorn'

print(df)

df.to_csv('./probe.csv', index=False)