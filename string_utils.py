def inverter_string(s):
    """Inverte a string fornecida."""
    return s[::-1]

def contar_vogais(s):
    """Conta o número de vogais na string fornecida."""
    vogais = 'aeiouAEIOU'
    return sum(1 for char in s if char in vogais)