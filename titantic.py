

import pandas as pd 

df=pd.read_csv('titanic.csv')
#print(df)

## Jag vill att den ska titta på titanic datan, se hur stor den är i shape, 
## Genom det får den aldrig vara färre columns än det som inputades
## Om vi har många som droppas så ska det synas på något sätt.... fan.
## Vi kommer förstås att förändra antalet kols och rader.


## vi vill kontrollera för vilket datatypes det är som kommer in och ut
## Är det ens värt att kontrollera att funktionerna gör vad de ska göra? Låter 
## som att det kommer att ta mycket tid?

## Jag vill använda pydantic för att kontrollera input från en API, 
## Om den stämmer, vilket jag kommer att testa, då ska den merga, annars skippar den


## Vi kan köra så att vi frågar många GPT modeller om vad som stämmer, 
## så ska vi korsverifiera vad det är som är överens i alla modeller för ett bolag
## Det är troligen något som vi kan lita på...


def expecation(df):
    return [df.shape[0],df.shape[1]]
    

print(expecation(df))

def set_dtypes(df):
    df = df.convert_dtypes()
    return df

df = df.pipe(set_dtypes).head()

