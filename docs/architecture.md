# Arquitetura do RenIA

## Objetivo

Este documento descreve a arquitetura do RenIA.

Seu objetivo é definir como o software será dividido em módulos, quais serão suas responsabilidades e como eles se comunicarão.

Este documento não descreve detalhes de implementação.

---

# Fluxo principal

Usuário

↓

Entrada

↓

Interpretação

↓

Motor de Programação

↓

Gerador de Programa

↓

Exportação

---

# Módulos

## Entrada

Responsável por receber as informações fornecidas pelo usuário.

Exemplos:

- Texto
- Formulário
- CAD (futuro)

---

## Interpretação

Transforma as informações recebidas em uma estrutura organizada.

Não gera programas.

Não conhece rotinas.

Sua única função é entender o pedido.

---

## Motor de Programação

É o núcleo do RenIA.

Responsável por:

- selecionar as rotinas
- montar a sequência lógica
- validar informações
- organizar o fluxo do programa

Este módulo não escreve G-code.

---

## Gerador

Recebe a sequência criada pelo Motor e gera o programa CNC.

É responsável apenas pela escrita do programa.

---

## Exportação

Permite ao usuário:

- visualizar
- copiar
- salvar
- exportar o programa gerado.