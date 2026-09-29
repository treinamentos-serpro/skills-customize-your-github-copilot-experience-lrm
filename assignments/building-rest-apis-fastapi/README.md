# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST em Python usando o framework FastAPI, definindo endpoints, validando dados com modelos Pydantic e tratando recursos inexistentes.

## 📝 Tasks

### 🛠️ Criar endpoints para listar e cadastrar itens

#### Descrição

Complete o starter code para criar uma API de itens. A API deve permitir consultar todos os itens e cadastrar um novo item usando requisições HTTP.

#### Requisitos

O programa concluído deve:

- Criar uma instância do FastAPI.
- Implementar `GET /items` para retornar todos os itens cadastrados.
- Implementar `POST /items` para receber um item no corpo da requisição e adicioná-lo à coleção.
- Definir um modelo Pydantic com os campos `name` e `description`.
- Retornar o item criado com um identificador único.

### 🛠️ Adicionar consulta, atualização e exclusão de itens

#### Descrição

Expanda a API para permitir o gerenciamento completo dos itens cadastrados a partir do identificador de cada recurso.

#### Requisitos

O programa concluído deve:

- Implementar `GET /items/{item_id}` para retornar um item específico.
- Implementar `PUT /items/{item_id}` para atualizar os dados de um item existente.
- Implementar `DELETE /items/{item_id}` para remover um item.
- Retornar o status HTTP `404` quando o identificador não existir.
- Usar parâmetros de rota e modelos de requisição com tipos explícitos.

### 🛠️ Documentar e validar a API

#### Descrição

Melhore a API para que ela forneça validações úteis e possa ser explorada pela documentação interativa do FastAPI.

#### Requisitos

O programa concluído deve:

- Validar que `name` não esteja vazio e tenha no máximo 100 caracteres.
- Validar que `description` tenha no máximo 500 caracteres.
- Retornar mensagens de erro claras para dados inválidos.
- Definir códigos de status apropriados para criação, sucesso, ausência de recurso e exclusão.
- Permitir que os endpoints sejam testados pela documentação disponível em `/docs`.
