# Função desenvolvida para realizar o calculo da sequência de fibonacci com um limite definido pelo valor desejado
# Desta forma não gerasse uma sequência infinita de números, apenas o que nos interessa
# Desenvolvida como parte do Exercicio Tecnico de número 1
def seq_fibonacci(valor):
    array_fibonacci = [0, 1]
    while array_fibonacci[-1] < valor:
        proximo = array_fibonacci[-1] + array_fibonacci[-2]
        array_fibonacci.append(proximo)

    return array_fibonacci

# Função desenvolvida para verificar se o valor informado pertence a sequência de Fibonacci
# Desenvolvida como parte do Exercicio Tecnico de número 1
def verifica_valor_fibonacci(valor):
    fibonacci = seq_fibonacci(valor)

    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

# Função desenvolvida para verificar se em uma frase existem letras Aa e contar o número de aparições na frase
# Desenvolvida como parte do Exercicio Tecnico de número 2
def verificar_e_contar_Aa(frase):
    frase = frase.upper()
    if "A" in frase:
        return f"A letra a está presente na frase e aparece {frase.count('A')} vezes."
    else:
        return f"A letra a não está presente na frase."




if __name__ == '__main__':
    # Execução de teste para o Exércicio tecnico de número 1
    numero = int(input("Informe um número: "))
    resultado = verifica_valor_fibonacci(numero)
    print(resultado)

    # Execução de teste para o Exércicio tecnico de número 2
    frase = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    res = verificar_e_contar_Aa(frase)
    print(res)
