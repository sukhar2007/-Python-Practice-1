income = int(input("Введите общий доход компании: "))
expense_p = int(input("\nВведите сумму производственных расходов: "))
expense_a = int(input("\nВведите сумму административных расходов: "))
expense_m = int(input("\nВведите сумму маркетинговых расходов: "))

if income < 0 or expense_p < 0 or expense_a < 0 or expense_m < 0:
    print("\nНеверные введённые данные")
else:
    expense_total = expense_p + expense_a + expense_m
    tax_benefits_p = expense_p * 0.2
    tax_benefits_a = expense_a * 0.1
    tax_benefits_m = expense_m * 0.05
    tax_benefits_total = tax_benefits_p + tax_benefits_a + tax_benefits_m  # 11500 5250
    profit = income - expense_total + tax_benefits_total
    if profit <= 0:
        tax = 0
    elif profit <= 10000:
        tax = profit * 0.1
    elif profit <= 50000:
        tax = profit * 0.2
    else:
        tax = profit * 0.3
    if profit > 0:
        print(f"\nЧистая прибыль: {profit}\n\nИтоговый налог: {tax}")
    else:
        print(f"\nУбыток: {-profit}\n\nИтоговый налог: {tax}")
