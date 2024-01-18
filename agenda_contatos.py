def adicionar_contato(agenda, nome_contato, telefone_contato, email_contato):
    contato = {'nome': nome_contato, 'telefone': telefone_contato, 'email': email_contato, 'favorito': False}
    agenda.append(contato)
    print(f'\n{nome_contato} adicionado aos contatos.')
    return

def ver_contatos(agenda):
    print('\nContatos Salvos')
    for indice, contato in enumerate(agenda, start=1):
        favorito = " ★ " if contato['favorito'] == True else " "
        nome_contato = contato['nome']
        telefone_contato = contato['telefone']
        email_contato = contato['email']
        print(f'{indice}. [{favorito}] Nome:{nome_contato}  Telefone:{telefone_contato}  Email:{email_contato}')
    return

def atualizar_contato(agenda, posicao_contato, novo_nome, novo_numero, novo_email):
     posicao_ajustada = int(posicao_contato) - 1
     if posicao_ajustada >= 0 and posicao_ajustada <= len(agenda):
          if novo_nome != "":
              agenda[posicao_ajustada]['nome'] = novo_nome
          if novo_numero != "":
               agenda[posicao_ajustada]['telefone'] = novo_numero
          if novo_email != "":
               agenda[posicao_ajustada]['email'] = novo_email
          print('Contato atualizado com sucesso.')
     else:
          print('Indice de tarefa inválido.')
     return

def adicionar_favorito(agenda, posicao_contato):
     posicao_ajustada = int(posicao_contato) - 1
     if posicao_ajustada >= 0 and posicao_ajustada <= len(agenda):
          if agenda[posicao_ajustada]['favorito'] == False:
               agenda[posicao_ajustada]['favorito'] = True
          else:
               agenda[posicao_ajustada]['favorito'] = False
     print('Contato adicionado aos favoritos.')
     return

def ver_contatos_favoritos(agenda):
     print('\nContatos Favoritos')
     for indice, contato in enumerate(agenda, start=1):
        if contato['favorito'] == True: 
             favorito = " ★ " if contato['favorito'] == True else " "
             nome_contato = contato['nome']
             telefone_contato = contato['telefone']
             email_contato = contato['email']
             print(f'{indice}. [{favorito}] Nome:{nome_contato}  Telefone:{telefone_contato}  Email:{email_contato}')
     return

def apagar_contato(agenda, posicao_contato):
     posicao_ajustada = int(posicao_contato) - 1
     if posicao_ajustada >= 0 and posicao_ajustada <= len(agenda):
          nome = agenda[posicao_ajustada]['nome']
          validacao = input(f'Deseja apagar o contato de {nome}:  [S/N]').upper()
          if validacao[0] == 'S':
               del(agenda[posicao_ajustada])
               print('Contato removido com sucesso.')
          else:
            print('Operação cancelada.')
     else:
          print('Indice incorreto.')
     ...

agenda = []
while True:
    print('\nAgenda de Contatos.')
    print('1. Visualizar Lista de Contatos.')
    print('2. Adicionar Contato.')
    print('3. Editar Contato.')
    print('4. Adicionar/Remover aos Favoritos.')
    print('5. Visualizar Contato Favoritos.')
    print('6. Apagar Contato.')
    print('7. Sair.')

    escolha = input('\nQual ação deseja realizar: ')

    if escolha == '1':
            ver_contatos(agenda)
    elif escolha == '2':
        nome_contato = input('Nome do Contato: ')
        telefone_contato = input('Telefone do contato: ')
        email_contato = input('Email do Contato: ')
        adicionar_contato(agenda, nome_contato, telefone_contato, email_contato)
    elif escolha == '3':
         ver_contatos(agenda)
         posicao_contato = input('Qual contato deseja editar: ')
         novo_nome = input('Novo nome (Para manter o atual, tecle ENTER): ')
         novo_numero = input('Novo número (Para manter o atual, tecle ENTER): ')
         novo_email = input('Novo email (Para manter o atual tecle ENTER): ')
         atualizar_contato(agenda, posicao_contato, novo_nome, novo_numero, novo_email)
    elif escolha == '4':
         ver_contatos(agenda)
         posicao_contato = input('Qual contato deseja adicionar/remover dos favoritos: ')
         adicionar_favorito(agenda, posicao_contato)
    elif escolha == '5':
         ver_contatos_favoritos(agenda)
    elif escolha == '6':
         ver_contatos(agenda)
         posicao_contato = input('Qual contato deseja apagar: ')
         apagar_contato(agenda,posicao_contato)
    elif escolha == '7':
        break
