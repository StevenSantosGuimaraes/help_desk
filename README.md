# Help Desk

Sistema web de Help Desk desenvolvido em Django para gerenciamento de chamados, comunicação entre clientes e agentes, e base de conhecimento.

## Funcionalidades
- Autenticação de usuários (login/logout)
- Perfis: Cliente, Agente, Administrador
- Criação e acompanhamento de tickets (chamados)
- Comentários em tickets (com modal)
- Atribuição de tickets a agentes
- Filtros e busca de tickets
- Dashboard simples
- Base de conhecimento (artigos públicos)
- Alternância de tema (claro/escuro)
- Sidebar responsiva e footer fixo

## Como rodar o projeto
1. Clone o repositório e acesse a pasta do projeto
2. Crie e ative um ambiente virtual Python
3. Instale as dependências:
	```bash
	pip install -r requirements.txt
	```
4. Realize as migrações:
	```bash
	python manage.py migrate
	```
5. Crie um superusuário para acessar o admin:
	```bash
	python manage.py createsuperuser
	```
6. Inicie o servidor:
	```bash
	python manage.py runserver
	```
7. Acesse `http://127.0.0.1:8000/` no navegador.

## Como usar
- Cadastre grupos "Cliente" e "Agente" no admin e associe usuários.
- Clientes podem abrir e acompanhar tickets.
- Agentes podem visualizar e responder todos os tickets.
- Admin pode gerenciar usuários, grupos e artigos da base de conhecimento.

## Pontos de melhoria
- Permissões mais refinadas por grupo e ação
- Filtros avançados e busca por tickets/artigos
- Notificações por e-mail
- Dashboard com gráficos
- Upload de arquivos em tickets
- Interface mobile responsiva
- Testes automatizados
- Internacionalização completa

## Estrutura do projeto
- `helpdesk/` - App principal (tickets, comentários, artigos)
- `config/` - Configurações do projeto Django
- `templates/` - Templates HTML (modularizados)
- `static/` - Arquivos estáticos (CSS, JS)

---
Projeto para fins didáticos e evolução contínua.
