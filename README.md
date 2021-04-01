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
status = Status_senha.objects.create(id_categoria='01', nome_status='Em Andamento')
status.save()
exit()

catagoria= Categoria_senha.objects.create(id_categoria='01', nome_categoria='Matrícula')

tipo= Tipo_senha.objects.create(id_tipo='01', nome_tipo='Não preferencial')

Repedir para: Categoria_senha, Tipo_senha, Tipo_senha (diferente o modo de salvar)

Adicionar os usuário com senha
from perfis_senhas.models import Senha, Status_senha, Categoria_senha, Tipo_senha
status = Status_senha.objects.get(id=1)
status.nome_status
categoria = Categoria_senha.objects.get(id=1)
categoria.nome_categoria
tipo = Tipo_senha.objects.get(id=1)
tipo.nome_tipo
perfil = Senha(senha=2, Status=status, Tipo=tipo, Categoria=categoria)
perfil.save()

Para visualizar os dados
from perfis_senhas.models import Status_senha
status = Status_senha.objects.get(id=1)
status.nome_status



Colunas do Banco de dados
Status:
1 – Em Andamento
2 - Na fila
3 - Ausente
4 – Atendida

Categoria
1 – Matrícula
2 – Rematrícula
3 – Diploma
4 - Trancamento

Tipo
1 - Não preferencial
2 – Preferencial

