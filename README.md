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

#### Rotas principais (HTTP REST API)

#### Plataforma Desktop
Para fins de demonstração, é apresentado na imagem abaixo a homepage desktop inicial do template do bootstrap. 

### Modelo de recomendação
Como método de filtragem de conteúdo, inicialmente procura-se utilizar a filtragem baseada em contéudo, ou Content-Based, onde são geradas recomendações baseadas em contéudos já consumidos pelo usuário - criando um perfil desse. Tem como vantagem o feedback dispensável do usuário para que seja recomendado contéudo de qualidade. Futuramente, é possível a utilização de outra forma de filtragem de conteúdo, a colaborativa, ou Collaborative Filter. Tal abordagem assimila um padrão comum de contéudo entre usuários diferentes e passa a mesclar as características, gerando uma recomendação para ambos os usuários. Com relação à primeira filtragem, a coletiva permite que o usuário saia da bolha de conteúdo.

## Projeto futuro
