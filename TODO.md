# RenIA Roadmap

> Estado atual do projeto e próximos objetivos.

---

# ✅ Core v1.0

## Libraries
- [x] RoutineLibrary
- [x] ParameterLibrary

## Models
- [x] RoutineDefinition
- [x] Parameter

## Resolvers
- [x] DefinitionResolver
- [x] OptionResolver
- [x] ParameterResolver

## Validators
- [x] RoutineValidator
- [x] ParameterValidator
- [x] PermissionValidator
- [x] RequirementValidator
- [x] ValueValidator

## Validation Rules
- [x] Type
- [x] Minimum
- [x] Maximum
- [x] Allowed Values
- [x] Allowed Ranges

## Tests
- [x] Core validation tests

---

# 🚧 Engine v1.0

## Architecture
- [X] Definir arquitetura do Engine
- [X] Definir fluxo completo de execução
- [ ] Definir responsabilidades das classes

## Request
- [ ] Estrutura da requisição
- [ ] Normalização da entrada

## Intent
- [ ] Identificar intenção do usuário
- [ ] Classificar tipo de solicitação

## Routine Selection
- [ ] Selecionar rotina correta
- [ ] Resolver ambiguidades

## Parameter Extraction
- [ ] Extrair parâmetros da entrada
- [ ] Converter unidades
- [ ] Validar tipos básicos

## Integration
- [ ] Integrar com Validator
- [ ] Retornar erros estruturados

---

# 🔮 Futuro

## Generator
- [ ] Gerador de programas CNC

## AI
- [ ] Prompt Builder
- [ ] Context Builder
- [ ] Conversation Memory

## Error System
- [ ] ValidationError
- [ ] RuntimeError
- [ ] Error Messages

## Interfaces
- [ ] CLI
- [ ] API
- [ ] VS Code Extension
- [ ] GUI

---

# 📌 Regras do Projeto

- Pensar antes de implementar.
- Uma classe deve possuir uma única responsabilidade.
- Evitar duplicação.
- Evitar abstrações prematuras.
- Questionar a arquitetura antes do código.
- Toda implementação deve possuir testes.
- O código deve ser simples de ler.

# Decisões Arquiteturais

## Core

- Parameters contêm regras universais.
- Rotinas contêm exceções (overrides).
- ParameterResolver aplica overrides.
- Validator apenas orquestra.
- ValueValidator valida valores.

## Engine

Decisão #001 – O Engine é independente da IA.

O Engine recebe apenas requisições estruturadas e produz respostas estruturadas. Ele não conhece provedores de IA, não conversa com o usuário e não depende de um modelo específico. Toda interação em linguagem natural é responsabilidade da camada de integração com a IA.

Decisão #002

O Engine nunca solicita informações adicionais ao usuário.

Caso uma requisição esteja incompleta, ele retorna exatamente o que está faltando.

Cabe à IA decidir como obter essas informações do usuário.
