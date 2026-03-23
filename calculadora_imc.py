#teste imc novamente do zero, programando sozinho com auxilio apenas a anotações

def calcular_imc(peso, altura):
        return peso/ (altura * altura)
def classificar_imc(resultado):
    if resultado < 18.5: return "Abaixo do peso ideal"
    elif resultado <= 24.9: return "Peso Normal (Saudável)"
    elif resultado <= 29.9: return "Sobrepeso (Atenção)"
    else: return "Obesidade (Cuidado)"
#Lista
historico = []
contador = 0
soma_imcs = 0

    #inicio do loop
while True:

    print("\n  PROGRAMA DE SAÚDE  ")

    nome= input("digeite seu nome ou ('sair'): ").strip() .title()

    if nome.lower() == 'sair':
         break
         
    
    try:

        peso_txt = input(f"peso de {nome} Kg: (Ex: 85,9) ") . replace(",",".")
        altura_txt = input(f"altura de {nome} M: ( Ex: 1,82)") . replace(",",".")

        altura=float (altura_txt)
        peso=float (peso_txt)
        
        resultado = calcular_imc(peso, altura)
        status = classificar_imc(resultado)
        
        contador += 1 
        soma_imcs += resultado


        print (f"\n RESULTADO PARA: {nome.upper()}: ")
        print (f"-> IMC: {resultado:.2f}")
        print(f"-> STATUS: {status}")

        # Criando historico
        registro = {
                "nome": nome,
                "imc": resultado,
                "clasificacao": status
                            }
        
        historico.append(registro)

    except ValueError:  
        print ("\n⚠️  ERRO: Digite apenas números válidos (ex: 75.5 ou 1.80). ")
       
       #Relatorio fnal quando sai do while
print("\n" + "="*30)
print(f"📊 FIM DA SESSÃO")
print(f"Total de pessoas atendidas: {contador}") # Mostra o número final
print("-" * 30)
if contador > 0:
     media = soma_imcs / contador
print(f"Média Geral de IMC: {media:.2f}")
if not historico:
        print("Nenhum Registro Encontrado.")
else:
   for pessoa in historico:
        # Usamos ['chave'] para buscar o valor específico
        print(f". {pessoa['nome']} | IMC: {pessoa['imc']:.2f} | Status: {pessoa['classificacao']}")