def collect_until_error(values: list[int]) -> list[int]:
    chisla_cel = [] # задали пустой список

    for i in values:
        if i < 0:
            break

        chisla_cel.append(i) # добавить значение в список
    
    return chisla_cel

print(collect_until_error([10, 20, -5, 30, 40]))