# 💱 Conversor de Moedas em Python

Um programa de conversão de moedas desenvolvido em Python para praticar lógica de programação, estruturas condicionais, validação de entradas e cálculos financeiros.

## 📌 Sobre o projeto

O Conversor de Moedas permite informar um valor em reais, selecionar a finalidade da operação e escolher entre dólar americano (USD) e euro (EUR).

A partir das opções escolhidas, o programa calcula o IOF conforme as regras definidas no exercício, aplica um spread sobre a cotação comercial e apresenta o valor líquido e o valor convertido.

## ✨ Funcionalidades

- Entrada de valores monetários com vírgula ou ponto decimal.
- Formatação de valores no padrão brasileiro.
- Seleção da finalidade: conta própria ou investimento.
- Validação das opções informadas pelo usuário.
- Cálculo de IOF conforme a finalidade selecionada.
- Conversão entre real brasileiro (BRL), dólar americano (USD) e euro (EUR).
- Aplicação de spread conforme a faixa do valor bruto.
- Exibição organizada do resultado no terminal.

## 🛠️ Tecnologias utilizadas

- **Python 3**
- Funções de entrada e saída (`input()` e `print()`)
- Estruturas condicionais (`if`, `elif` e `else`)
- Laços de repetição (`while`)
- Manipulação de strings (`replace()` e `lower()`)
- Conversão de tipos (`float()`)
- Formatação de strings com f-strings

## 🧠 Conceitos praticados

Durante o desenvolvimento, pratiquei:

- Validação de dados fornecidos pelo usuário.
- Controle de fluxo e tomada de decisões.
- Operações matemáticas e cálculo de percentuais.
- Aplicação de regras de negócio.
- Formatação e apresentação de valores monetários.
- Organização da lógica de um programa do início ao fim.

## 🚀 Como executar

**Pré-requisito:** ter o Python 3 instalado.

1. Clone este repositório:

   ```bash
   git clone URL_DO_SEU_REPOSITORIO
   ```

2. Entre na pasta do projeto.
3. Execute o arquivo Python pelo terminal:

   ```bash
   python conversor.py
   ```

   Caso necessário, utilize `python3 conversor.py`.

4. Informe o valor bruto, a finalidade da operação e a moeda desejada.

> Se o arquivo Python tiver outro nome, substitua `conversor.py` pelo nome correto.

## 📊 Regras de cálculo

O programa utiliza valores de cotação e percentuais definidos diretamente no código para fins didáticos.

- **Conta própria:** IOF de 3,5%.
- **Investimento:** IOF de 1,1%.
- **USD:** cotação comercial definida como R$ 5,18.
- **EUR:** cotação comercial definida como R$ 5,88.
- **Spread:** 4%, 3% ou 2%, conforme a faixa do valor bruto.

Esses valores são parâmetros do exercício e não representam necessariamente cotações ou alíquotas vigentes para operações reais.

## 📚 Aprendizados

Este projeto foi uma oportunidade de transformar conceitos de lógica de programação em uma aplicação funcional, trabalhando com entradas, validações, cálculos e apresentação dos resultados.

O desenvolvimento também contribuiu para fortalecer minha compreensão de estruturas condicionais, laços de repetição e manipulação de dados em Python.

## 👩‍💻 Desenvolvido por

**Clara Lima**

Estudante de Análise e Desenvolvimento de Sistemas, construindo projetos práticos
