# Use Libs
import pandas as pd
from faker import Faker

# Instancia do Objeto
fk = Faker(locale='pt_BR')

# Gerando os Dados
fk.name(), fk.sentence(), fk.address(), fk.email(), fk.date(), fk.country(), fk.phone_number(), fk.random_number(digits=6)

# Definindo o Total de Dados
total = 10000

# Organizando os Dados
dados = {
    'Nome' : [
        fk.name() for i in range(total) 
        ],
    'E-Mail' : [
        fk.email() for i in range(total) 
    ],
    'Data de Nascimento' : [
        fk.address().replace('\n', ' ') for i in range(total)
    ],
    'Texto' : [
        fk.sentence() for i in range(total)
    ]
}

# Montando o DataFrame
df = pd.DataFrame(dados)

# Gerando o CSV
df.to_csv('assets/data-fake-py.csv', index=False)


