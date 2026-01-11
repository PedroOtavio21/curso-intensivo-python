# Capítulo 5 - Instruções If

Linguagens de programação no geral, permite trabalhar com condições específicas ao decorrer do desenvolvimento de um código. Não é diferente no Python.

## Testes Condicionais Básicos

O Python utiliza os operadores padrão de comparação para avaliar se uma expressão é True ou False.

- == : Igualdade (Diferente de JS, não existe ===).

* != : Diferença.

* > e < : Maior que e Menor que.

* >= e <= : Maior ou igual e Menor ou igual.

Nota: A comparação de strings diferencia maiúsculas de minúsculas ('Python' == 'python' é False). Use .lower() para comparações case-insensitive.

## Operadores Lógicos (and, or, in)

Em vez de && e || de outras linguagens, o Python usa palavras legíveis:

* and: Verdadeiro se ambas as condições forem verdadeiras.

* or: Verdadeiro se pelo menos uma condição for verdadeira.

* in: Verifica se um valor está dentro de uma lista (extremamente útil em dados).

* not in: Verifica se um valor não está na lista.

```py
# Exemplo de 'in'
usuarios_banidos = ['andre', 'felipe', 'maria']
usuario = 'thiago'

if usuario not in usuarios_banidos:
    print("Pode postar comentários.")
```

## A Estrutura if-elif-else

O Python usa elif em vez de else if.

```py

idade = 19

if idade < 4:
    preco = 0
elif idade < 18:
    preco = 25
else:
    preco = 40

print(f"Sua entrada custa R${preco}.")
```

## Verificação de Listas Vazias

Uma técnica muito comum em Python é verificar se uma lista possui itens antes de rodar um loop:

```py
pedidos = []

if pedidos:  # Se a lista tiver itens, retorna True
    for pedido in pedidos:
        print(f"Fazendo: {pedido}")
else:
    print("A lista de pedidos está vazia!")
```