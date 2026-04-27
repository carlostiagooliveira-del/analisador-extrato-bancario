import csv
from collections import defaultdict

def analisar_extrato(arquivo):
    categorias = defaultdict(float)
    total_receitas = 0
    total_despesas = 0

    with open(arquivo, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            categoria = linha['categoria']
            valor = float(linha['valor'])
            categorias[categoria] += valor
            if valor > 0:
                total_receitas += valor
            else:
                total_despesas += valor

    print("=" * 35)
    print("   ANALISE DO EXTRATO BANCARIO")
    print("=" * 35)
    for cat, total in sorted(categorias.items()):
        emoji = "+" if total > 0 else "-"
        print(f"{emoji} {cat:<15} R$ {total:>10.2f}")
    print("-" * 35)
    print(f"Total Receitas:   R$ {total_receitas:>10.2f}")
    print(f"Total Despesas:   R$ {total_despesas:>10.2f}")
    print(f"Saldo Final:      R$ {(total_receitas + total_despesas):>10.2f}")
    print("=" * 35)

analisar_extrato('extrato.csv')