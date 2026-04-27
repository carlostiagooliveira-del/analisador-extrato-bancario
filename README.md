# 📊 Analisador de Extrato Bancário

## O que é
Script Python que lê um extrato bancário em CSV, categoriza 
as transações e gera um resumo financeiro com saldo final.

## Por que fiz
Trabalhei 10 anos em controladoria fazendo esse tipo de análise 
manualmente. Esse projeto automatiza o processo usando Python.

## Tecnologias
- Python 3.x
- Módulos nativos: csv, collections

## Como rodar
```bash
python analisador.py
```

## Exemplo de saída
```
===================================
   ANALISE DO EXTRATO BANCARIO
===================================
- Alimentacao      R$    -470.00
- Moradia          R$  -1.380.00
+ Receita          R$   5.800.00
- Saude            R$     -89.00
- Transporte       R$     -45.00
-----------------------------------
Total Receitas:    R$   5.800,00
Total Despesas:    R$  -1.984,00
Saldo Final:       R$   3.816,00
===================================
```
