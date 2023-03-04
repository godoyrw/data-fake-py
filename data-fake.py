# Use Libs
import pandas as pd
from faker import Faker

# Instancia do Objeto
fk = Faker('pt_BR')

# Definindo o Total de Dados
total = 10

# Organizando os Dados
dados = {
    'Nome' : [
        fk.name() for i in range(total) 
        ],
    'E-Mail' : [
        fk.email() for i in range(total) 
    ],
    'Telefone' : [
        fk.cellphone_number() for i in range(total)
    ],
    'Data de Nascimento' : [
        fk.date() for i in range(total)
    ],
    'Endereço' : [
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


