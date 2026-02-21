def adicionar_tarefas(tarefas, nome_tarefa):
    tarefa = {'tarefa':nome_tarefa,
              'completa': False}
    tarefas.append(tarefa)
    print(f'A Tarefa: {nome_tarefa} foi adicionada com sucesso!')
    return

def ver_tarefas(tarefas):
    print('\nLISTA DE TAREFAS\n')
    for indice, tarefa in enumerate(tarefas, start=1):
        status = '✓' if tarefa['completa'] else " "
        nome_tarefa = tarefa['tarefa']
        print(f'{indice}. [{status}] {nome_tarefa}')
    return

def atualizar_nome_tarefas(tarefas, indice_tarefa, novo_nome_tarefa):
    indicie_tarefa_ajustado = indice_tarefa - 1
    if indicie_tarefa_ajustado >= 0 and indicie_tarefa_ajustado < len(tarefas):
        tarefas[indicie_tarefa_ajustado]['tarefa'] = novo_nome_tarefa
        print(f'Tarefa {indice_tarefa} atualizado para {novo_nome_tarefa}')
    else: 
        print('Indice de tarefas é invalido!')
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustado]['completa'] = True
    print(f'Tarefa {indice_tarefa} marcadada como completa')
    return

def deletar_tarefas_completas(tarefas):
   
    for tarefa in tarefas.copy(): # Segurança para não apagar os itens originais.
        if tarefa['completa']:
            tarefas.remove(tarefa)
            print("Tarefas completas foram deletadas.") 
    return

tarefas = []
while True:
    print('\n Menu do Gerenciador de Tarefas\n ')
    print('1. Adicionar Tarefa')
    print('2. Ver Tarefas')
    print('3. Atualizar Tarefas')
    print('4. Completar Tarefas')
    print('5. Deletar Tarefas Completas')
    print('6. Sair')

    escolha = int(input('Digite a sua escolha: '))

    if escolha == 1:
        nome_tarefa = input('Digite o nome da tarefa que deseja adcionar: ')
        adicionar_tarefas(tarefas, nome_tarefa)

    elif escolha == 2:
        ver_tarefas(tarefas)
    
    elif escolha == 3:
        ver_tarefas(tarefas)
        indice_tarefa = int(input('Digite o numero da tarefa que deseja atualizar: '))
        novo_nome = input('Digite o novo nome da tarefa: ')
        atualizar_nome_tarefas(tarefas, indice_tarefa, novo_nome)
    elif escolha == 4:
        ver_tarefas(tarefas)
        indice_tarefa = input('Digite o numero da tarefa que deseja completar: ')
        completar_tarefa(tarefas, indice_tarefa)
    
    elif escolha == 5:
        deletar_tarefas_completas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == 6:
        print('Programa Finalizado')
        break

