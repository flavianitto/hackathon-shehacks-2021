# Hackathon SheHacks 2021 - AlimentAí (Equipe Gaia)

## Contexto
Levando em consideração a questão de insegurança alimentar e miséria que assolam uma boa parcela da população brasileira, sendo que, por outro lado, temos a questão de desperdício de alimentos, foi idealizada uma plataforma capaz de solucionar ambos os problemas, o AlimentAí, um projeto criado durante o Hackathon SheHacks 2021 pela equipe Gaia.

## Objetivo
Unir dois cenários divergentes no Brasil: a fome e o desperdício de alimentos, transformando-os em solução um para o outro. Nossa ideia viabilizará que o pequeno produtor possa fornecer seu excedente de alimentos diário e, para as ONGs, será feito o repasse dos recursos recolhidos por essas.

## Protótipo
Inicialmente, foi criado um design para contemplar algumas telas principais que o aplicativo mobile forneceria, tais quais: tela inicial, tela de login, tela de cadastro inicial, homepage, tela de carregamento, informações de dados bancários e barra de navegação lateral. O fluxo simulado pela plataforma Figma por ser visualizado a seguir:

<p align="center"><img  width="698" alt="demonstração do aplicativo através do figma" src="https://user-images.githubusercontent.com/37030292/139593707-e6c7cd1f-6582-4bc8-bb2d-30a126b45d5d.PNG" /></p>

A arquitetura proposta para o MVP da plataforma seria utilizar Django REST Framework para o back-end e comunicação com o Banco de Dados Local, sendo que, para o front-end e Mobile, seria utilizado React Native com design responsivo, como ilustrado no fluxograma abaixo.

<p align="center"><img  width="500" alt="fluxograma do Django REST" src="https://miro.medium.com/max/614/1*9SmHhzWDXBCpRi3CpQKowg.png" /></p>

Trata-se de uma arquitetura bem simplória, mas que atenderia para fins demonstrativos no que tange a captação de parceiros e investidores/patrocinadores iniciais.

### Etapas
#### Back-end em Django REST Framework
Para consumir as requisições feitas para a plataforma, será utilizando o framework no intuito de se comunicar com o banco de dados e retornar as informações solicitadas como resposta. Executando a aplicação localmente, tem-se o painel de administrador a seguir para monitorar tais solicitações enviadas pelo usuário.

<p align="center"><img width="698" alt="backend Django REST" src="https://user-images.githubusercontent.com/37030292/139594127-140d9ae5-a4da-4a81-9273-40b74a46afcd.PNG"/></p>

#### Modelagem do Banco de Dados (`models.py`)
Através do levantamento de informações relevantes para o projeto, se é pretendido utiliza-las na composição do sistema de recomendação para clientes, como localidades carentes de auxílio próximas a eles.

##### User
```
class User(models.Model):

    """Model representing a user's info."""

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cpf_cnpj = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=15) 
    address = models.CharField(max_length = 254)
    number = models.CharField(max_length = 10)
    address_complement = models.CharField(max_length=30) 
    neighborhood = models.CharField(max_length = 30)
    city = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
```

##### UserType
```
class Bank(models.Model):

    """Model representing a Bank."""

    bank_id = models.AutoField(primary_key=True)
    code = models.IntegerField(max_length = 10)
    name = models.CharField(max_length=100)
```

##### Bank
```
USER_TYPE = (
        (0, "Receiver"),
        (1, "Donator")
    )

TRANSACTION_TYPE = (
        (0, "Money"),
        (1, "Food")
    )

class UserType(models.Model):

    """Model representing a user type."""

    user_type_id = models.AutoField(primary_key=True)
    user_type = models.IntegerField(choices=USER_TYPE, default=0)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, default=0)
```

##### Partner
```
class Partner(models.Model):

    """Model representing a parter's info."""

    partner_id = models.AutoField(primary_key=True)
    corporate_name = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=15) 
    address = models.CharField(max_length = 254)
    number = models.CharField(max_length = 10)
    address_complement = models.CharField(max_length=30) 
    neighborhood = models.CharField(max_length = 30)
    city = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
```

##### UserInstance
```
class UserInstance(models.Model):

    """Model representing a user instance's info."""

    record_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    user_type = models.ForeignKey(UserType, on_delete= models.CASCADE)
    account = models.ForeignKey(Bank, on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
```


#### Rotas principais de Request HTTP
- ```POST``` cadastro de usuário: inserir dados para fazer doação ou procurar pontos de compra.
- ```POST``` cadastro de parceiro: inserir dados para receber doação ou divulgar pontos de compra.
- ```GET``` filtro: permite que o usuário filtre as informações de interesse e receba uma interface renderizada baseada no sistema de recomendação.
- ```DELETE``` usuário: permite fazer com o que o usuário exclua sua conta.
- ```DELETE``` parceiro: permite fazer com o que o parceiro exclua sua conta.

#### Plataforma Desktop
Para fins de demonstração, é apresentado na imagem abaixo a homepage desktop inicial do template do bootstrap. 

## Projeto futuro
No futuro, pretende-se manter a implementação do back-end em Django REST Framework, e, além disso, serão desenvolvidos tantos front-end e mobile client em React Native. Na questão do armazenamento de dados, a proposta é utilizar o serviço Cloud (AWS Bucket S3) e estruturar um Data Lake para fluxo e tratamento de dados, utilizando o modelo de recomendação dentro do ambiente em nuvem para se comunicar com a API.

### Modelo de recomendação
Como método de filtragem de conteúdo, inicialmente, procura-se utilizar a filtragem baseada em contéudo, ou Content-Based, onde são geradas recomendações baseadas em contéudos já consumidos pelo usuário - criando um perfil desse. Tem como vantagem o feedback dispensável do usuário para que seja recomendado contéudo de qualidade. Futuramente, é possível a utilização de outra forma de filtragem de conteúdo, a colaborativa, ou Collaborative Filter. Tal abordagem assimila um padrão comum de contéudo entre usuários diferentes e passa a mesclar as características, gerando uma recomendação para ambos os usuários. Com relação à primeira filtragem, a coletiva permite que o usuário saia da bolha de conteúdo.
