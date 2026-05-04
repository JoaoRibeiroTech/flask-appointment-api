from secrets import token_hex

#Criação de token para o 'SECRET_KEY' do __init__
app= token_hex(20)
print(app)