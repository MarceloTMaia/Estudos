# FAÇA UM SISTEMA PARA UM MERCADINHO.
# ESSE SISTEMA VAI PERMITIR QUE VOCÊ:
# CADASTRE UM PRODUTO
# VEJA OS PRODUTOS CADASTRADOS
# EDITE UM PRODUTO CADASTRADO
# EXCLUA UM PRODUTO CADASTRADO
# VAI PERMITIR TAMBÉM EFETUAR VENDAS, PARA FAZER UMA VENDA VOCÊ VAI PRECISAR:
# NOME DO CLIENTE
# ITENS COMPRADOS POR ELE
# TOTAL DA VENDA
# GUARDE AS VENDAS DIÁRIAS EM UMA LISTA
# NO FINAL DO EXPEDIENTE FAÇA UM SORTEIO ENTRE TODOS OS CLIENTES DO DIA, O SORTEADO GANHARÁ UM PRÊMIO X.
# MOSTRE TAMBÉM O TOTAL EM REAIS VENDIDO NO DIA, QUAL FOI A COMPRA MAIS CARA E QUAL FOI A COMPRA MAIS BARATA.

from datetime import datetime

agora = datetime.now()

motando = f"{agora.day}/{agora.month}/{agora.year} - {agora.hour}:{agora.minute}"




lista_produto = [
    {"id": 1, "nome": "Arroz", "quantidade": 2, "preco": 5.50},
    {"id": 2, "nome": "Feijão", "quantidade": 1, "preco": 7.00},
    {"id": 3, "nome": "Macarrão", "quantidade": 3, "preco": 3.20},
    {"id": 4, "nome": "Açúcar", "quantidade": 1, "preco": 4.00},
    {"id": 5, "nome": "Óleo", "quantidade": 1, "preco": 8.50},
    {"id": 6, "nome": "Leite", "quantidade": 6, "preco": 2.00},
    {"id": 7, "nome": "Uva", "quantidade": 5, "preco": 11.50},
]

contador = 8

lista_carrinho_compras = []
lista_compras_paga = []


contador_carrinho = 1
contador_compras = 1
valor_total_compras = 0





while True:
  print (f'''\n------------------------------Mercadinho Infinity------------------------------''')
  print (motando)

  print (f'''
MENU -------------------         
1 - Cadastrar produto (Adc|Edit|Remov|list).
2 - Sistema de Vendas.
3 - Controle financeiro
0 - Sair.''')
  
  menu = input('Digite uma opção: ').strip()

  match menu:

    case '1':#--------------------------------------------------------------------------------------------------------------------------------------------CASE 1 CADASTRAR
      while True:
        print('\nCADASTRAR ---------')
        print (f'''
1 - Adicionar.
2 - Editar.
3 - Remover.
4 - Listar.
0 - Sair.         
''')
        cadastrar = input('Digite uma opção: ').strip()
        match cadastrar:

          case '1': #----------------------------------------------------------- CASE 1 ADICIONAR OK

            print ('\nADICIONAR----------')
            produto = input('Nome do produto: ').strip() #----ENTRADA PRODUTO
            if produto == '0':
              print ('Voltar')
              continue
            
            quantidade = input('Quantidade:').strip() #----ENTRADA QUANTIDADE
            if not quantidade.isdigit():
              print ('Digite uma quantidade valida.')
              continue
            quantidade = int(quantidade)

            preco = input('Preço: ').strip() #----ENTRADA PRECO

            try:
              preco = float(preco)
            
            except ValueError:
              print ('Digite um valor valido.')
              continue
            

            #DICIONARIO DA LISTA PRODUTO  
            novo_produto = {
              "id": contador,
              'nome': produto,
              'quantidade': quantidade,
              'preco': preco
            }
            contador += 1

            lista_produto.append(novo_produto)

            print (f'----Produto "{produto}" adicionado.---- ')
          
          case '2': #----------------------------------------------------------- CASE 2 EDITAR OK
            print ('\nEDITAR----------')
            
            print (f'''
1 - Editar Nome.
2 - Editar Quantidade.
3 - Editar Preço. 
0 - Sair.                                      
''')
            editar_opcao = input('Digite uma opções: ').strip()

            match editar_opcao:

              case '1': #--------------------------- CASE 1 EDITAR NOME OK
                print ('\nEDITAR NOME----------') # Exibe o cabeçalho para a edição de nome
                print ('\nLISTA DE PRODUTOS') # Informa que a lista de produtos será exibida
                
                for produto in lista_produto: # Itera sobre a lista de produtos
                  print (f'- {produto["nome"]} | id - {produto["id"]}') # Exibe o nome e ID de cada produto

                id_encontrada = False
                id_edit_nome = input('\nDigite a ID do produto: ').strip() #----ENTRADA EDITAR NOME: solicita ID do produto
                
                if not id_edit_nome.isdigit(): # Verifica se a ID inserida é um número
                  print ('Digite uma ID valida.') # Mensagem de erro se a ID não for válida
                  continue
                
                id_edit_nome = int(id_edit_nome) # Converte a ID para um número inteiro
                
                for produto_da_vez in lista_produto: # Itera sobre a lista de produtos para encontrar o correto
                  if produto_da_vez["id"] == id_edit_nome: # Verifica se o ID do produto corresponde ao ID inserido
                    id_encontrada = True
                    print (f'Produto - {produto_da_vez["nome"]}') # Exibe o nome do produto encontrado
                    
                    novo_nome = input('Digite o novo nome: ').strip() # ----ENTRADA NOVO NOME: solicita o novo nome
                    
                    produto_da_vez["nome"] = novo_nome # Atualiza o nome do produto
                    print (f'Nome do produto atualizado - {novo_nome}') # Mensagem de confirmação da atualização
                
                if not id_encontrada:
                  print ('ID nao encontrada.')

              case '2': #--------------------------- CASE 2 EDITAR QUANTIDADE OK
                print ('EDITAR QUANTIDADE----------') # Exibe o cabeçalho para a edição de quantidade  
                print ('\nLISTA DE PRODUTOS') # Informa que a lista de produtos será exibida
                
                for produto in lista_produto: # Itera sobre a lista de produtos
                  print (f'- {produto["nome"]} | id - {produto["id"]} | Qnt - {produto["quantidade"]}') # Exibe nome, ID e quantidade de cada produto

                id_encontrada = False
                id_edit_quantidade = input('\nDigite a ID do produto: ').strip() # ----ENTRADA EDITAR QUANTIDADE: solicita ID do produto
                
                if not id_edit_quantidade.isdigit(): # Verifica se a ID inserida é um número
                  print ('Digite uma ID valida.') # Mensagem de erro se a ID não for válida
                  continue

                id_edit_quantidade = int(id_edit_quantidade) # Converte a ID para um número inteiro

                for produto_da_vez in lista_produto: # Itera sobre a lista de produtos para encontrar o correto
                  if produto_da_vez["id"] == id_edit_quantidade: # Verifica se o ID do produto corresponde ao ID inserido
                    id_encontrada = True
                    print (f'Produto - {produto_da_vez["nome"]} | {produto_da_vez["quantidade"]}') # Exibe o nome e a quantidade do produto encontrado
                    
                    nova_quantidade = input('Digite a nova quantidade: ').strip() # ----ENTRADA NOVA QUANTIDADE: solicita a nova quantidade
                    
                    if not nova_quantidade.isdigit(): # Verifica se a nova quantidade inserida é um número
                      print ('Digite uma quantidade valida') # Mensagem de erro se a quantidade não for válida
                      continue
                    
                    nova_quantidade = int(nova_quantidade) # Converte a nova quantidade para um número inteiro
                    
                    produto_da_vez["quantidade"] = nova_quantidade # Atualiza a quantidade do produto
                    print (f'quantidade do produto atualizada - {nova_quantidade}')
                
                if not id_encontrada:
                  print ('ID nao encontrada.')

              case '3': #--------------------------- CASE 3 EDITAR PREÇO OK
                print ('EDITAR PREÇO----------') # Exibe o cabeçalho para a edição de preço
                print ('\nLISTA DE PRODUTOS') # Informa que a lista de produtos será exibida
                for produto in lista_produto: # Itera sobre a lista de produtos
                  print (f'- {produto["nome"]} | id - {produto["id"]} | Preço - R$ {produto["preco"]}') # Exibe nome, ID e preço de cada produto

                id_edit_preco = input('\nDigite a ID do produto: ').strip() #----ENTRADA EDITAR PRECO: solicita ID do produto
                if not id_edit_preco.isdigit():
                  print ('Digite uma ID valida.')
                  continue

                id_encontrada = False
                id_edit_preco = int(id_edit_preco) # Converte a ID para um número inteiro
                
                for produto_da_vez in lista_produto: # Itera sobre a lista de produtos para encontrar o correto
                  if produto_da_vez["id"] == id_edit_preco: # Verifica se o ID do produto corresponde ao ID inserido
                    id_encontrada = True
                    print (f'Produto - {produto_da_vez["nome"]} | R$ {produto_da_vez["preco"]}')
                    
                    novo_preco = input('Digite o novo preço: ').strip() #----ENTRADA NOVO PRECO: solicita o novo preço 
                    
                    try:
                        novo_preco = float(novo_preco)  # TENTA CONVERTER PARA FLOAT, para garantir que o preço seja um valor numérico 
                        produto_da_vez["preco"] = novo_preco  # Atualiza o preço
                        print(f'Preço atualizado para R$ {produto_da_vez["preco"]:.2f} com sucesso!') # Mensagem de confirmação da atualização
                    
                    except ValueError: # Captura o erro se a conversão falhar
                        print('Digite um preço válido.') # Mensagem de erro se o preço não for um número
                
                if not id_encontrada:
                  print ('ID nao encontrada.')
              
              case '0': #--------------------------- CASE 4 SAIR OK
                print ('\nSAIR----------')
                break
                
              case _: #--------------------------- ELSE OK
                      print ('---OPÇÃO INVALIDA---')
                      continue
                      
          case '3': #----------------------------------------------------------- CASE 3 REMOVER OK 
            print ('\nREMOVER----------') # Exibe o cabeçalho para a operação de remoção
            print('LISTA') # Informa que a lista de produtos será exibida
            
            for produto_da_vez in lista_produto: # Itera sobre a lista de produtos
              print(f'''ID: {produto_da_vez["id"]} - {produto_da_vez["nome"]}''')

            id_encontrada = False
            encontrar_produto_apagar = input("Digite a ID do produto para remover: ").strip() # Solicita ao usuário a ID do produto a ser removido
            
            if not encontrar_produto_apagar.isdigit(): #Verifica se o que esta sendo digitado é digito
              print ('Digite uma ID valida.')#Se nao for ele printa digite uma id valida
              continue

            encontrar_produto_apagar = int(encontrar_produto_apagar) #Se for um deigito ele converte para um numero inteiro

            for produto_apagar in lista_produto: # Itera sobre a lista de produtos para encontrar o produto a ser removido
              if produto_apagar['id'] == encontrar_produto_apagar: # Verifica se a ID do produto corresponde à ID inserida
                id_encontrada = True
                print(f'Produto - {produto_apagar["nome"]}') # Pergunta ao usuário se deseja remover o produto
                
                perguntar_remover_produto = input('Deseja remover o produto S|N? ')
                if perguntar_remover_produto.lower() not in ['s','n']:
                  print ('Digite S ou N.')
                  continue

                elif perguntar_remover_produto == "s":

                  lista_produto.remove(produto_apagar)
                  print ('Produto removido.')
                  break

                else:
                  print('Saindo')
                  continue
          

            if not id_encontrada:
              print ('ID nao encontrada')
                      
          case '4': #----------------------------------------------------------- CASE 4 LISTAR OK
            print ('\nLISTAR----------')
            print('ESTOQUE DE PRODUTOS')
            
            for produto_da_vez in lista_produto:
              print(f'''
ID: {produto_da_vez["id"]} | Qnt: {produto_da_vez["quantidade"]}
{produto_da_vez["nome"]} | Preço: {produto_da_vez["preco"]}''')
          
          case '0': #----------------------------------------------------------- CASE 5 SAIR OK
            print ('\nSAIR----------')
            break
          
          case _: #------------------------------------------------------------- ELSE OK
            print ('---OPÇÃO INVALIDA---')
            continue

    case '2':#--------------------------------------------------------------------------------------------------------------------------------------------CASE 2 VENDER
      print ('\nSISTEMA DE VENDAS----------')
      while True:
        print (f'''
MENU DE COMPRAS
1 - Carrinho de compras.
2 - Remover compras.
3 - Pagar compras.
4 - Limpar carrinho.
0 - Sair.
''')
        menu_de_compras = input('Digite uma opção: ')

        match menu_de_compras:
          case '1': # ---------------------------------------------------------- CASE 1 ADICIONAR COMPRAS
            
            print('CARRINHO DE COMPRAS----------')
            for item in lista_carrinho_compras:        
                print(f'''{item["item"]} | {item["nome"]} - CDB: {item["id"]} ------------------- R$ {item["preco"]}''')
                
            print(f'------------------------------------------Valor total: R$ {valor_total_compras:.2f}')

            while True:  # Loop para adicionar produtos ao carrinho
                id_encontrada = False  # Flag para verificar se o ID foi encontrado

                entrada_produto = input(f'Digite ID ou digite 0 para voltar: ').strip()  # Solicita o ID do produto

                # Verifica se a entrada é um número
                if not entrada_produto.isdigit():
                    print('---> ID incorreta.')
                    continue
                else:
                    entrada_produto = int(entrada_produto)  # Converte a entrada para inteiro

                # Se o usuário digitar 0, sai do loop
                if entrada_produto == 0:
                    print('Voltando')
                    break

                # Itera sobre a lista de produtos para encontrar o produto correspondente ao ID
                for produto_da_vez in lista_produto:
                    if produto_da_vez['id'] == entrada_produto:  # Se o ID for encontrado
                        id_encontrada = True  # Marca que o ID foi encontrado
                        
                        

                        compras = {
                          'item': contador_carrinho,
                          'nome': produto_da_vez['nome'],
                          'id': produto_da_vez['id'],
                          'preco': produto_da_vez['preco']                          
                        }

                        

                        lista_carrinho_compras.append(compras)
                        valor_total_compras += produto_da_vez['preco']
                        

                        contador_carrinho += 1  # Incrementa o contador para o próximo item

                        # Atualiza o valor total das compras
                          # Adiciona o preço do produto ao total
                        

                # Exibe o carrinho atualizado fora do loop `for` para não repetir a exibição
                for item in lista_carrinho_compras:        
                    print(f'''{item["item"]} | {item["nome"]} - CDB: {item["id"]} ------------------- R$ {item["preco"]}''')
                # Mostra o valor total das compras
                print(f'------------------------------------------Valor total: R$ {valor_total_compras:.2f}')
                
                

                # Se o ID não foi encontrado, informa o usuário
                if not id_encontrada:
                    print('---> ID não cadastrada')

          case '2': #----------------------------------------------------------- CASE 2 REMOVER COMPRAS
            print ('REMOVER COMPRAS DO CARRINHO----------')
            for item in lista_carrinho_compras:
              print(f'''{item["item"]} | {item["nome"]} - CDB: {item["id"]} ------------------- R$ {item["preco"]}''')

            entrada = input('Digite o numero do item para remover ou 0 para sair: ')

            if not entrada.isdigit():
              print ('Digite um numero valido')
              continue
            
            else:
              entrada = int(entrada)

              if entrada == 0:
                print ('Voltando')
                continue

              for item in lista_carrinho_compras:
                
                if item['item'] == entrada:
                  
                  apagar_item = input('Deseja apagar o item S|N?')
                  if apagar_item.lower() not in ['s','n']:
                    print ('Digite S|N')
                  
                  elif apagar_item.lower() == 's':
                    lista_carrinho_compras.remove(item)
                    valor_total_compras = valor_total_compras - item['preco']
                          
                    print (f'''ITEM {item["item"]} {item["nome"]} - {item["id"]} -- R$ {item["preco"]} ------- REMOVIDO''')

                    for index, item in enumerate(lista_carrinho_compras, start=1): # enumera os itens do carrinho depois de retirar produtos ex: item 1,2,3,4 apaga o 2 fica 1,3,4 renumera 1,2,3
                      item['item'] = index

                      maior_numero = 0  # faz com que o numero item no carrinho continue do ultimo numero renumerado pelo contador depois de diminuir a quantidade de produto no carrinho 
                      #porque senao ele continuara a partir do numero de itens que haviam e nao de itens que ha porque voce esta retirando itens antes ex: tinha 4 produtos apagou um ficou 3
                      #em vez dele continuar a partir do 4 ele continua a partir do maior_numero que ser o 3 senao ficara assim: 1,2,3,5,
                      for item in lista_carrinho_compras:
                        if item['item'] > maior_numero:
                          maior_numero = item['item']
                                                    
                          contador_carrinho = maior_numero+1
                        

                  else:
                      break
          
          case '3': #----------------------------------------------------------- CASE 3 PAGAR
            print ('PAGAMENTO----------')
            if not lista_carrinho_compras:
              print ('Carrinho vazio')
              break
            
            for item in lista_carrinho_compras:
              print(f'''{item["item"]} | {item["nome"]} - CDB: {item["id"]} ------------------- R$ {item["preco"]}''')
            print (f'------------------------------------------valor total {valor_total_compras:.2f}')
            print (f'Time: {motando}')

            forma_de_pagamento = input('Deseja finalizar compra s/n? ').strip()
            if forma_de_pagamento not in ['s','n']:
              print ('Escolha s/n')
              continue
            elif forma_de_pagamento.lower() == 's':
              print (f'''
Forma de pagamento
1 - Dinheiro.
2 - Cartão.  
3 - Pix.
0 - Sair.                                                                               
''')
              escolha_forma_pagamento = input('Digite a forma de pagamento: ').strip() #PAREI AQUI E REVISAR AQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUI

              match escolha_forma_pagamento:
                case '1': #--------- CASE 1 PAGAMENTO EM DINHEIRO
                  print ('\nPAGAMENTO EM DINHEIRO')

                  for item in lista_carrinho_compras:
                    print(f'''{item["item"]} | {item["nome"]} - CDB: {item["id"]} ------------------- R$ {item["preco"]}''')

                  print (f'Valor total a pagar -----------------------------------R$ {valor_total_compras:.2f}')
                  
                  valor_cliente = input('Digite o valor recebido: ').strip()

                  try:
                    valor_cliente = float(valor_cliente)

                  except ValueError:
                    print ('Digite um valor valido')
                    continue
                  
                  troco = valor_cliente - valor_total_compras

                                    
                  print ('\n---COMPRA FINALIZADA---')
                  print (f'Valor da compra: R$ {valor_total_compras:.2f}')
                  print (f'Valor dado pelo cliente: R$ {valor_cliente:.2f}')
                  print (f'Troco do cliente: R$ {troco:.2f}')
                  print (f'''
                  ------------------------------       
                  ----Imprimindo Nota Fiscal----
                  ------------------------------''')
                  
                  compras_pagas = {
                    'valor_total': valor_total_compras,
                    'time': motando,
                    'contador': contador_compras,
                    'todos_itens': lista_carrinho_compras.copy()
                  }
                  
                  lista_compras_paga.append(compras_pagas)
                  # for item in lista_compras_paga:
                  #   print (f'''
                  #   {item["contador"]}
                  #   {item["todos_itens"]}
                  #   ''')

                  contador_compras+=1
                  lista_carrinho_compras.clear()
                  valor_total_compras = 0
                  contador_carrinho = 1


                  break

                # case '2': #--------- CASE 2 PAGAMENTO EM CARTÃO 
                #   print ('PAGAMENTO EM CARTÃO')
                #   for item in lista_carrinho_compras:
                #     print (f'''{item["item"]} - {item['nome']} ------------------- R$ {item['preco']}''')
                #   print (f'Valor total a pagar -----------------------------------R$ {valor_total_compras:.2f}')
                #   print ('Insira seu cartão. ')


                #   print ('\n---COMPRA FINALIZADA---')
                #   print (f'Valor da compra: R$ {valor_total_compras:.2f}')
                #   print (f'Valor cliente: R$ {valor_cliente:.2f}')
                #   print (f'''
                #   ------------------------------       
                #   ----Imprimindo Nota Fiscal----
                #   ------------------------------''')
                  
                #   lista_compras_paga.extend(lista_carrinho_compras)
                #   lista_carrinho_compras.clear()
                #   valor_total_compras = 0 #valor total reiniciada
                #   contador_carrinho = 1 #carrinho de compras reinicializado

                #   break

                # case '3': #--------- CASE 3 PAGAMENTO EM PIX
                #   print ('PAGAMENTO EM PIX')
                #   for item in lista_carrinho_compras:
                #     print (f'''{item["identificacao"]} - {item['nome']} ------------------- R$ {item['preco']}''')
                #   print (f'Valor total a pagar -----------------------------------R$ {valor_total_compras:.2f}')
                #   print ('Aguarde o QR code. ')

                #   print ('\n---COMPRA FINALIZADA---')
                #   print (f'Valor da compra: R$ {valor_total_compras:.2f}')
                #   print (f'Valor cliente: R$ {valor_cliente:.2f}')
                #   print (f'''
                #   ------------------------------       
                #   ----Imprimindo Nota Fiscal----
                #   ------------------------------''')
                  
                #   lista_compras_paga.extend(lista_carrinho_compras)
                #   lista_carrinho_compras.clear()
                #   valor_total_compras = 0 #valor total reiniciada
                #   contador_carrinho = 1 #carrinho de compras reinicializado

                #   break
  
                case '0': #--------- CASE 4 SAIR
                  print ('\nSAIR----------')
                  break
                
                case _: #--------- ELSE
                  print ('Digite uma das opções:')

            else:
              continue
          
          case '4': #----------------------------------------------------------- CASE 4 LIMPAR CARRINHO
            print ('\nLIMPAR CARRINHO----------')
            
            lista_carrinho_compras.clear() #apagar itens carrinho
            print ('Carrinho vazio')
            valor_total_compras = 0 #apos limpar carrinho o valor total das compras tem que atualizar e zerar novamento

            contador_carrinho = 1 #o contador do carrinho precisa ser zerado tambem
            continue

          case '0': #----------------------------------------------------------- CASE 0 SAIR
            print ('\nSAIR----------')
            break
          
          case _: #----------------------------------------------------------- ELSE
            print ('---OPÇÃO INVALIDA---')

    case '3':#--------------------------------------------------------------------------------------------------------------------------------------------CASE 3 CONTROLE FINANCEIRO 
      print ('CONTROLE FINANCEIRO----------') 

      while True:
        print (f'''
MENU -------------------
1 - Extrato de vendas
2 - Listagem de Vendas
0 - Sair
''')
        controle_financeiro = input('Digite uma das opções: ')
        match controle_financeiro:
          
          case '1': #----------------------------------------------------------- CASE 1 EXTRATO
            print ('\nEXTRATO DE VENDAS----------')

            for compra in lista_compras_paga:
              print (f'Compra {compra["contador"]} Valor da compra: {compra["valor_total"]} - {compra["time"]}')
              for item in compra["todos_itens"]:
                print (f'{item["item"]} | Nome: {item["nome"]} - Id: {item["id"]} ---- Preço: {item["preco"]}')
            continue
          
          case '2': #----------------------------------------------------------- CASE 2 VENDAS
            print ('\nLISTAGEM DE VENDAS----------')
            ...
          case '0': #----------------------------------------------------------- CASE 0 SAIR
            print ('\nSAIR----------')
            break
            
          case _: #----------------------------------------------------------- ELSE
            print ('---OPÇÃO INVALIDA---')
            continue
    
    case '0':#--------------------------------------------------------------------------------------------------------------------------------------------CASE 0 SAIR
      print ('\nSAIR----------')
      break
    
    case _:#----------------------------------------------------------------------------------------------------------------------------------------------ELSE
      print ('---OPÇÃO INVALIDA---')
      continue

  

