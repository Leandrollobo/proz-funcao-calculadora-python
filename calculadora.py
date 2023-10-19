
def calcular():
    calculado = False
    while (calculado == False):
        try:
            resultado = 0
            numero1 = int(input("Digite o primeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            operacao = (input("Selecione a operação: +, -, /, *: "))

            if operacao == '+':
                resultado = numero1 + numero2
                print("Resultado: ", numero1, operacao,
                      numero2, "= ", resultado)
            elif operacao == '-':
                resultado = numero1 - numero2
                print("Resultado: ", numero1, operacao,
                      numero2, "= ", resultado)
            elif operacao == '*':
                resultado = numero1 * numero2
                print("Resultado: ", numero1, operacao,
                      numero2, "= ", resultado)
            elif operacao == '/':
                resultado = numero1 / numero2
                print("Resultado: ", numero1, operacao,
                      numero2, "= ", resultado)
            else:
                print("Digite uma operação válida (+,-,*,/)")
                novoCalculo = (
                    input("Deseja realizar outra operação?, digite S para sim ou N para não"))
                if novoCalculo == 's':
                    print("Vamos realizar um novo calculo")
                    calcular()
                elif novoCalculo == 'n':
                    print("Programa encerrado")
                    break
                else:
                    print("Opção invalida, vamos inciar os cálculos novamente")
        except:
            print("Erro, nenhum numero digitado vamos iniciar os cálculos novamente")


calcular()
