import json

with open ('lista_produtos.json', 'r') as file:   # comando para ler lista
    lista_produtos = json.load(file)



contador_cdb = 1

print ('------Novo Mercado------')
while True:
    print (f'''
------Menu------

0 - Sair
1 - Sistema Mercado 
2 - Cadastro de Produtos Adc|Remov|Edit|List
''')
    
    menu_inicial = int(input('Digite uma opção acima---> '))
    match menu_inicial:

        case 0: # sair
            print ('Saindo')
            break

        case 1: # Sistema Mercado
            ...
        
        case 2: # Cadastro de Produtos Adc|Remov|Edit|List
            while True:
                print(f'''
------Cadastro de Produtos------

0 - Sair
1 - Adicionar.
2 - Remover.
3 - Editar.
''')
                menu_cadastro = int(input('Digite uma opção acima---> '))
                match menu_cadastro:

                    case 0: # sair
                        print ('Saindo')
                        break

                    case 1: # Adicionar
                        while True:
                            print('\n= Adicionar Produto =')
                            if not lista_produtos:
                                print ('Lista Vazia ')
                                break
                            print('\nDigite um item para adicionar ou digite "0" para sair')
                            
                            for item in lista_produtos:
                                if item['cdb'] >= contador_cdb:
                                    contador_cdb = item['cdb'] + 1

                            nome = input('Nome: ')
                            if nome == '0':
                                break
                            quantidade = int(input('Quantidade: '))
                            preco = float(input('Valor unitario: '))

                            produto = {
                                'cdb': contador_cdb,
                                'nome': nome,
                                'quantidade': quantidade,
                                'preco': preco
                            }

                            lista_produtos.append(produto)
                            

                            with open ('lista_produtos.json', 'w') as file:  # comando para inserir itens na lista
                                json.dump(lista_produtos,file,indent=4)
                            
                            print (f'''
--PRODUTO ADICIONADO--
Produto: {nome}
CDB: {contador_cdb}
''')
                    
                    case 2: # Remover
                        while True:    
                            print('\n= Remover Produto =')
                            if not lista_produtos:
                                print ('Lista Vazia ')
                                break
                            else:
                                for i in lista_produtos:
                                    print (f'Codigo: {i["cdb"]} - {i["nome"]}')

                            item_remover = int(input('Digite o codigo para remover ou "0" para sair---> '))
                            if item_remover == 0:
                                break
                            else:
                                for item in lista_produtos:
                                    if item['cdb'] == item_remover:
                                        lista_produtos.remove(item)
                                        with open('lista_produtos.json','w') as file:
                                            json.dump(lista_produtos,file,indent=4)
                                
                                print (f'''
--PRODUTO EXCLUIDO--
Produto: {item["nome"]}
CDB: {item["cdb"]}
''')
                    
                    case 3: # Editar
                        while True:
                            print('\n= Editar Produto =')
                            if not lista_produtos:
                                print ('Lista Vazia ')
                                break
                            print('''
------Editar------

0 - Sair.
1 - Nome.
2 - Quantidade.
3 - Preço.
''')
                            item_editar = int(input('Digite uma opção acima---> '))
                            match item_editar:
                                
                                case 0: # Sair
                                    print ('Saindo')
                                    break

                                case 1: # Nome
                                    print ('Editar nome')

                                    for i in lista_produtos:
                                        print (f'Codigo: {i["cdb"]} - {i["nome"]}')

                                    editar_nome = int(input('Digite o codigo "CDB" do produto: '))

                                    for item in lista_produtos:
                                        















                            








                        




                


        case _:
            ...


    




