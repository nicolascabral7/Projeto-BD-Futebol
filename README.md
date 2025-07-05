# Sistema de Torneios de eSports 🎮

## 📝 Análise de Requisitos Detalhada

---

### 1. 🎯 Objetivo do Sistema

Sistema para gerenciar torneios de eSports, permitindo o cadastro de jogadores, times, jogos, registro de partidas e armazenamento dos dados de forma organizada e segura.

---

### 2. 👥 Público-alvo e Usuários

- 🧑‍💼 Organizadores de torneios  
- 🎮 Jogadores e times  
- 👨‍💻 Administradores do sistema

---

### 3. ⚙️ Funcionalidades Principais

#### 📝 Cadastro de Jogadores

- Campos:  
  - Nome (texto)  
  - Idade (número inteiro)  
  - Nickname (texto único)  
- Regras:  
  - Nickname não pode repetir ❌  
  - Idade deve ser maior que zero 🔢  

#### 🏆 Criação de Times

- Campos:  
  - Nome do time (texto único)  
- Regras:  
  - Vínculo entre jogadores e times (muitos para muitos) 🔗  
  - Um jogador pode estar em vários times? (Definir) 🤔  

#### 🎲 Cadastro de Jogos

- Campos:  
  - Nome do jogo (texto)  
  - Categoria (ex: FPS, MOBA...)  
- Regras:  
  - Categoria pode ser lista fixa ou aberta (decidir) 📋  

#### 📅 Registro de Partidas

- Campos:  
  - Time 1 (time cadastrado)  
  - Time 2 (time cadastrado)  
  - Jogo (cadastrado)  
  - Data da partida (formato: AAAA-MM-DD) 📆  
  - Vencedor (um dos times que jogaram) 🥇  
- Regras:  
  - Não pode registrar partida com times inexistentes 🚫  
  - Data válida (não pode ser data futura, se preferir) ⏳  
  - Vencedor deve estar entre os times participantes ✅  

---

### 4. 📏 Regras de Negócio

- 🎮 Um jogador pode estar em quantos times?  
- 🕹️ Um time pode participar de vários torneios (se implementar torneios)?  
- 📅 Data das partidas deve ser válida e consistente.  
- 🚫 Evitar registros inválidos, como jogadores duplicados ou times inexistentes.  
- 🛡️ Garantir integridade dos dados (chaves estrangeiras funcionando).

---

### 5. 🧰 Tecnologias e Ferramentas

- Python 3.x 🐍  
- Banco de dados SQLite 🗄️  
- Ambiente virtual com `venv` ⚙️  
- Git e GitHub para controle de versão 🧑‍💻  
- Editor VSCode 💻  

---

### 6. 📋 Documentação Necessária

- README.md com:  
  - Descrição do projeto  
  - Como instalar e rodar  
  - Como usar (menu e funcionalidades)  
- Arquivos em `docs/`:  
  - Algoritmo (fluxo do sistema)  
  - Diagrama MER (`mer.png`)

---

### 7. ✅ Critérios de Aceitação

- O sistema deve permitir cadastrar jogadores, times, jogos e partidas com dados válidos.  
- Deve prevenir cadastro duplicado de nickname ou nome de time.  
- Deve armazenar dados corretamente no SQLite.  
- Deve permitir listar os dados cadastrados.  
- Deve tratar erros comuns (inserção duplicada, chave estrangeira inválida).

---
