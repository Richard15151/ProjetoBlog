#teste
ambiente = 'producao' #teste ou produção

if ambiente == 'teste':
    # CONFIG BANCO DE DADOS
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'

if ambiente == 'producao':
    # CONFIG BANCO DE DADOS
    DB_HOST = 'Richard07.mysql.pythonanywhere-services.com'
    DB_USER = 'Richard07'
    DB_PASSWORD = 'pyRDsenai5'
    DB_NAME = 'Richard07$default'


# CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'blog'

# SENHA DO ADM
MASTER_PASSWORD = 'RRsenai5'

MASTER_EMAIL = 'richard.senai@gmail'