# Backend

1. [Criando ambientes virtuais](#criando-ambientes-virtuais)  
2. [Instalando dependências](#instalando-dependencias)  
3. [Gerando tabelas no banco de dados](#gerando-tabelas-no-banco-de-dados)
4. [Criando um usuário administrador](#criando-um-usuario-administrador)
5. [Iniciando o servidor de desenvolvimento localmente](#iniciando-o-servidor-de-desenvolvimento-localmente)
6. [Acessando o django admin](#acessando-o-django-admin)
7. [Acessando a documentação das api's](#acessando-a-documentação-das-apis)

## Criando ambientes virtuais

O módulo venv fornece suporte para a criação de “ambientes virtuais” leves com seus próprios diretórios de site, opcionalmente isolados dos diretórios de site do sistema. Cada ambiente virtual possui seu próprio binário Python (que corresponde à versão do binário usado para criar esse ambiente) e pode ter seu próprio conjunto independente de pacotes Python instalados nos diretórios do site.

[Documentação oficial python](https://docs.python.org/pt-br/3/library/venv.html)

```python 
python3 -m venv .venv
```

Para ativar o ambiente execute o seguinte comando

```bash
. .venv/bin/activate
```

Para desativar o ambiente execute

```bash
deactivate
```


## Instalando dependências

Para instalar as dependências execute o seguinte na pasta raiz do projeto comando

```python
pip install -r requirements.txt
```

## Gerando tabelas no banco de dados

Para gerar as tabelas no banco é necessário executar o seguinte comando

```python
 python manage.py migrate
```

## Criando um usuário administrador

É necessário realizar a criação deste tipo de usuário para que se tenha acesso ao admin e a documentação das api's, para isso execute o seguinte comando

```python
python manage.py createsuperuser
```

## Iniciando o servidor de desenvolvimento localmente

Para iniciar o servidor de desenvolvimento execute o seguinte comando

```python
python manage.py runserver
```

Por padrão o servidor começa a funcionar na rota [http://127.0.0.1:8000/](http://127.0.0.1:8000/), caso necessário é possível definir a rota adicionando ao comando a rota desejada

## Acessando o django admin

O django admin é um painel de controle para visualização e manipulação das informações advindas do banco do banco de dados, para acessa-la levando em consideração que o servidor esteja rodando na 127.0.0.1:8000 é necessário apenas acessar a seguinte rota [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/), para entrar é necessário digitar o usuário e senha criado na seção [Criando um usuário administrador](#criando-um-usuario-administrador)


## Acessando a documentação das api's

O sistema conta com uma documentação explicativa sobre o uso das api's, para acessar basta ir até [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/), será solicitado as credenciais de um usuário de tipo administrador criado na seção [Criando um usuário administrador](#criando-um-usuario-administrador)