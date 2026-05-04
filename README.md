# 📅 API de Agendamento

API REST para gerenciamento de usuários e agendamentos, desenvolvida com foco em organização, segurança e boas práticas de backend.

---

## 🚀 Sobre o projeto

Este projeto permite que usuários criem e gerenciem agendamentos de forma simples, garantindo que não existam conflitos de horário.

Ideal como base para sistemas como:

* Barbearias 💈
* Clínicas 🏥
* Serviços autônomos 💼

---

## ✨ Funcionalidades

✔ Cadastro de usuários
✔ Autenticação com JWT
✔ Criação de agendamentos
✔ Validação de conflito de horários
✔ Listagem por usuário
✔ Exclusão de agendamentos

---

## 🛠️ Tecnologias

* Python
* Flask
* SQLAlchemy
* JWT (autenticação)
* SQLite
* Bcrypt

---

## 📡 Principais rotas

| Método | Rota                       | Descrição           |
| ------ | -------------------------- | ------------------- |
| POST   | `/users`                   | Criar usuário       |
| POST   | `/login`                   | Autenticação        |
| POST   | `/appointments/create`     | Criar agendamento   |
| GET    | `/appointments`            | Listar agendamentos |
| DELETE | `/appointment/delete/<id>` | Deletar             |

---

## 📌 Regras do sistema

* Não permite agendamentos com horários sobrepostos
* O horário inicial deve ser menor que o final
* Cada usuário acessa apenas seus dados

---

## 💡 Melhorias futuras

* Atualização de agendamentos
* Paginação
* Integração com envio real de emails
* Deploy em nuvem
