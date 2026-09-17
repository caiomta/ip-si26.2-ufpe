SELLERS = ("Dwight", "Jim", "Stanley", "Phillips", "Michael")
enterprises = ([], [], [], [], [])
NO_SALES_MESSAGES = (
    "Dwight fez zero vendas hoje. Mais sorte amanhã!",
    "Jim passou o dia fazendo pegadinhas e não concluiu nenhuma venda!",
    "Stanley acabou dormindo em serviço, amanhã ele estará mais descansado!",
    "Phillips se distraiu e acabou não fazendo vendas hoje!",
    "Michael não trabalhou como vendedor hoje, apenas foi um bom chefe.",
)

running = True
while running:
    seller = input()

    if seller.lower() == "fim":
        running = False
    else:
        enterprise = input()
        # se não estiver cadastrado, vai para a lista do Michael
        index = SELLERS.index(seller) if seller in SELLERS else 4
        enterprises[index].append(enterprise)

for i in range(5):  # há 5 vendedores cadastrados
    if enterprises[i]:
        # se for Michael
        if i == 4:
            print("Michael realizou vendas hoje!")

        print(f"{SELLERS[i]} : {enterprises[i]}")
    else:
        print(NO_SALES_MESSAGES[i])
