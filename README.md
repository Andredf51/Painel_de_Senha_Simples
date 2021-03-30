# Painel_de_Senha_Simples
Painel de senha simples em Django, avaliação 01 de PPI2 (2021)

Comando para usar o Painel de senha

Projeto de um painel de senha simples usando Django e banco SQLite.

Dados inseridos pelo Shell.

Aplicação cadastra novas senhas e categorias no banco de dados.


Rodar o projeto - python manage.py runserver

Endereço para acessar - http://localhost:8000/


Propagar as mudanças em nosso modelo no esquema do banco de dados – Makemigrations
Na aplicação usar o comando - python manage.py makemigrations
Para efetivar as alterações usar o migrate.
Na aplicação – python manage.py migrate
(Modulo 06)

Alimentar as colunas do banco de dados
python manage.py shell
from perfis_senhas.models import Status_senha
perfis_senhas – Nome utilizado na models.py, é uma casse e uma coluna.
status = Status_senha.objects.create(id_status='01', nome_status='Em Andamento')
status.save()
exit()

Repedir para: Categoria_senha, Tipo_senha, Tipo_senha (diferente o modo de salvar)


Para visualizar os dados
from perfis_senhas.models import Status_senha
status = Status_senha.objects.get(id=1)
status.nome_status
