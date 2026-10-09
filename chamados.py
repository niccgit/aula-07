chamados = [
  { "id": 1, "titulo": "Erro no login", "prioridade": "Alta", "status": "Aberto", "usuario": "Ana Silva" },
  { "id": 2, "titulo": "Tela branca no app", "prioridade": "Crítica", "status": "Aberto", "usuario": "Bruno Costa" },
  { "id": 3, "titulo": "Atualizar cadastro", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Carlos Souza" },
  { "id": 4, "titulo": "Boleto não gerado", "prioridade": "Média", "status": "Aberto", "usuario": "Daniela Lima" },
  { "id": 5, "titulo": "Botão quebrado", "prioridade": "Baixa", "status": "Aberto", "usuario": "Eduardo Rocha" },
  { "id": 6, "titulo": "Lentidão na busca", "prioridade": "Média", "status": "Em progresso", "usuario": "Fernanda Alves" },
  { "id": 7, "titulo": "Recuperar senha", "prioridade": "Alta", "status": "Aberto", "usuario": "Gabriel Santos" },
  { "id": 8, "titulo": "Erro no Pix", "prioridade": "Crítica", "status": "Aberto", "usuario": "Amanda Melo" },
  { "id": 9, "titulo": "Mudar foto de perfil", "prioridade": "Baixa", "status": "Fechado", "usuario": "Igor Ribeiro" },
  { "id": 10, "titulo": "Exportar PDF falhou", "prioridade": "Média", "status": "Aberto", "usuario": "Juliana Vieira" },
  { "id": 11, "titulo": "Carrinho esvaziando", "prioridade": "Alta", "status": "Em progresso", "usuario": "Lucas Martins" },
  { "id": 12, "titulo": "Cupom inválido", "prioridade": "Média", "status": "Aberto", "usuario": "Mariana Dias" },
  { "id": 13, "titulo": "Página 404 no FAQ", "prioridade": "Baixa", "status": "Aberto", "usuario": "Nicolas Ferreira" },
  { "id": 14, "titulo": "Atraso na entrega", "prioridade": "Alta", "status": "Aberto", "usuario": "Patricia Gomes" },
  { "id": 15, "titulo": "Email de boas-vindas", "prioridade": "Baixa", "status": "Fechado", "usuario": "Rodrigo Ramos" },
  { "id": 16, "titulo": "Estorno pendente", "prioridade": "Alta", "status": "Em progresso", "usuario": "Sabrina Oliveira" },
  { "id": 17, "titulo": "Alerta de segurança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Thiago Barbosa" },
  { "id": 18, "titulo": "Link quebrado no menu", "prioridade": "Baixa", "status": "Aberto", "usuario": "Vanessa Cunha" },
  { "id": 19, "titulo": "Nota fiscal sumiu", "prioridade": "Média", "status": "Aberto", "usuario": "Willian Cardoso" },
  { "id": 20, "titulo": "Modo escuro travando", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Yasmim Lopes" },
  { "id": 21, "titulo": "Erro na API de CEP", "prioridade": "Alta", "status": "Aberto", "usuario": "Arthur Antunes" },
  { "id": 22, "titulo": "Notificação duplicada", "prioridade": "Baixa", "status": "Aberto", "usuario": "Beatriz Mendes" },
  { "id": 23, "titulo": "Sessão expirando rápido", "prioridade": "Média", "status": "Em progresso", "usuario": "Caio Nogueira" },
  { "id": 24, "titulo": "Erro no cartão de crédito", "prioridade": "Crítica", "status": "Aberto", "usuario": "Diana Prince" },
  { "id": 25, "titulo": "Traduzir termo em inglês", "prioridade": "Baixa", "status": "Fechado", "usuario": "Elton John" },
  { "id": 26, "titulo": "Chat de suporte offline", "prioridade": "Alta", "status": "Aberto", "usuario": "Fábio Assunção" },
  { "id": 27, "titulo": "Upload de comprovante", "prioridade": "Média", "status": "Aberto", "usuario": "Gisele Bündchen" },
  { "id": 28, "titulo": "Histórico sumiu", "prioridade": "Alta", "status": "Em progresso", "usuario": "Heitor Villa" },
  { "id": 29, "titulo": "Termos de uso desatualizados", "prioridade": "Baixa", "status": "Aberto", "usuario": "Isabela Garcia" },
  { "id": 30, "titulo": "Erro 500 no checkout", "prioridade": "Crítica", "status": "Aberto", "usuario": "Jorge Ben" },
  { "id": 31, "titulo": "Ajustar margem do header", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Karina Bacchi" },
  { "id": 32, "titulo": "Filtro por data quebrado", "prioridade": "Média", "status": "Aberto", "usuario": "Leonardo Dicaprio" },
  { "id": 33, "titulo": "Assinatura não renovada", "prioridade": "Alta", "status": "Aberto", "usuario": "Marta Vieira" },
  { "id": 34, "titulo": "Áudio do vídeo não funciona", "prioridade": "Média", "status": "Aberto", "usuario": "Neymar Junior" },
  { "id": 35, "titulo": "Atualizar política de privacidade", "prioridade": "Baixa", "status": "Fechado", "usuario": "Otávio Mesquita" },
  { "id": 36, "titulo": "Queda do servidor interno", "prioridade": "Crítica", "status": "Em progresso", "usuario": "Paula Toller" },
  { "id": 37, "titulo": "Convite por email falhou", "prioridade": "Baixa", "status": "Aberto", "usuario": "Quintino Aires" },
  { "id": 38, "titulo": "Extrato em branco", "prioridade": "Alta", "status": "Aberto", "usuario": "Renata Vasconcellos" },
  { "id": 39, "titulo": "ícone errado no painel", "prioridade": "Baixa", "status": "Aberto", "usuario": "Samuel Rosa" },
  { "id": 40, "titulo": "Duplicidade de cobrança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Tais Araújo" },
  { "id": 41, "titulo": "Validação de CNPJ", "prioridade": "Média", "status": "Em progresso", "usuario": "Umberto Eco" },
  { "id": 42, "titulo": "Mensagem de erro confusa", "prioridade": "Baixa", "status": "Aberto", "usuario": "Valéria Valenssa" },
  { "id": 43, "titulo": "Problema com fonte negrito", "prioridade": "Baixa", "status": "Aberto", "usuario": "Wagner Moura" },
  { "id": 44, "titulo": "Links de redes sociais fora do ar", "prioridade": "Média", "status": "Aberto", "usuario": "Xuxa Meneghel" },
  { "id": 45, "titulo": "Sem sinal de geolocalização", "prioridade": "Alta", "status": "Em progresso", "usuario": "Yuri Gagarin" },
  { "id": 46, "titulo": "Página recarregando sozinha", "prioridade": "Alta", "status": "Aberto", "usuario": "Zeca Pagodinho" },
  { "id": 47, "titulo": "Gráfico de vendas travado", "prioridade": "Média", "status": "Aberto", "usuario": "Alinne Moraes" },
  { "id": 48, "titulo": "Impossível remover endereço", "prioridade": "Média", "status": "Em progresso", "usuario": "Beto Jamaica" },
  { "id": 49, "titulo": "Vazamento de memória na aba", "prioridade": "Crítica", "status": "Aberto", "usuario": "Cláudia Raia" },
  { "id": 50, "titulo": "Ajustar alinhamento do rodapé", "prioridade": "Baixa", "status": "Fechado", "usuario": "Dado Dolabella" }
]


# pesquisa por usuário
# pesquisa por status
# pesquisa por prioridade
# chamados urgentes (criticos e abertos)
# abrir chamando (cadastrar novo chamado)
# resolver chamado (mudar status do chamado para progresso)
# fechar chamado (mudar status do chamado para fechado)


def filtrar_por_usuario():
   resposta_usuario1 = input("Digite o nome do usuário que você deseja visualizar o chamado: ")
   for cada_item in chamados:
      if cada_item['usuario'] == resposta_usuario1:
         print(f"Seu chamado é: ID: {cada_item['id']} | Título: {cada_item['titulo']} | Prioridade: {cada_item['prioridade']} | Status: {cada_item['status']} | Usuário: {cada_item['usuario']}")

def filtrar_por_status():
   resposta_usuario2 = input("Digite o status que você deseja para filtrar a lista de chamados: ")
   for cada_item in chamados:
      if cada_item['status'] == resposta_usuario2:
         print(f"Segue os chamados: ID: {cada_item['id']} | Título: {cada_item['titulo']} | Prioridade: {cada_item['prioridade']} | Status: {cada_item['status']} | Usuário: {cada_item['usuario']}")

def filtrar_por_prioridade():
   resposta_usuario3 = input("Digite a prioridade que você deseja para filtrar a lista de chamados: ")
   for cada_item in chamados:
      if cada_item['prioridade'] == resposta_usuario3:
         print(f"Segue os chamados: ID: {cada_item['id']} | Título: {cada_item['titulo']} | Prioridade: {cada_item['prioridade']} | Status: {cada_item['status']} | Usuário: {cada_item['usuario']}")

def filtrar_chamados_urgentes():
    for cada_item in chamados:
       if cada_item['prioridade'] == "Crítica" and cada_item['status'] == "Aberto":
          print(f"Segue os chamados: ID: {cada_item['id']} | Título: {cada_item['titulo']} | Prioridade: {cada_item['prioridade']} | Status: {cada_item['status']} | Usuário: {cada_item['usuario']}")

def cadastrar_chamado():
    
    opcoes = ["sim", "não", "nao"]

    resposta_adicao = input("Você gostaria de cadastrar um novo chamado à lista? (Sim/Não): ").lower()
    while resposta_adicao not in opcoes:
        resposta_adicao = input("Resposta inválida! Responda somente com 'Sim' ou 'Não': ").lower()
    
    while resposta_adicao == "sim":
        id_adicao = input("Qual o ID do novo chamado?")
        titulo_adicao = input("Qual o título do novo chamado? ")
        prioridade_adicao = input("Qual a prioridade do novo chamado? (Crítica/Alta/Média/Baixa) ")
        usuario_adicao = input("Qual o nome do usuário referente ao novo chamado?")
        
        novo_chamado = {
            'id': id_adicao,
            'titulo': titulo_adicao,
        	'prioridade': prioridade_adicao,
        	'status': "Aberto",
        	'usuario': usuario_adicao
        }
        chamados.append(novo_chamado)
        print(f"Chamado adicionado com sucesso! A lista de chamados atual está está assim: {chamados}")

        resposta_adicao = input("Deseja cadastrar outro chamado? (Sim/Não)").lower()
        while resposta_adicao not in opcoes:
            resposta_adicao = input("Resposta inválida! Responda somente com 'Sim' ou 'Não': ").lower()

def resolver_chamado():
    resposta = input("Digite o ID do chamado que você deseja alterar o status: ")
    for cada_item in chamados:
        if str(cada_item['id']) == resposta:
            cada_item['status'] = "Em progresso"
            print("Status de chamado atualizado para 'Em progresso' com sucesso!")
            break
            
def fechar_chamado():
    resposta = input("Digite o ID do chamado que você deseja alterar o status: ")
    for cada_item in chamados:
        if str(cada_item['id']) == resposta:
            cada_item['status'] = "Fechado"
            print("Status de chamado atualizado para 'Fechado' com sucesso!")
            break

while True:
    print("Histórico de Chamados")
    print("1 - Filtrar pesquisa de chamado por: Usuário")
    print("2 - Filtrar pesquisa de chamado por: Status")
    print("3 - Filtrar pesquisa de chamado por: Prioridade")
    print("4 - Filtrar pesquisa de chamado por: Prioridade = Crítica e Status = Aberto")
    print("5 - Cadastrar novo chamado")
    print("6 - Resolver chamado")
    print("7 - Fechar chamado")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        filtrar_por_usuario()
    elif opcao == "2":
        filtrar_por_status()
    elif opcao == "3":
        filtrar_por_prioridade()
    elif opcao == "4":
        filtrar_chamados_urgentes()
    elif opcao == "5":
        cadastrar_chamado()
    elif opcao == "6":
        resolver_chamado()
    elif opcao == "7":
        fechar_chamado()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente!")
