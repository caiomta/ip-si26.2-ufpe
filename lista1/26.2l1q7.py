remarkable1 = input()
veredict1 = input()
remarkable2 = input()
veredict2 = input()

did_not_count = 0
liked = 0

print(
    "Depois que a Série A e a Libertadores ficaram só no sonho do Santa, Byte pendura a chuteira de ídolo tricolor e parte pro interior: começa a Excursão Interiorana em busca do time da sua vida!"
)

# PRIMEIRA VIAGEM
if "Catende" in remarkable1:
    did_not_count += 1
    print(
        "Catende!!! Aqui já rodou a maior usina de açúcar e álcool da América Latina, Byte sente o orgulho no ar."
    )
elif "Palmares" in remarkable1:
    did_not_count += 1
    print(
        "Palmares, a Terra dos Poetas! Berço de nomes como Ascenso Ferreira, aqui até o futebol merece um verso."
    )
elif "Carcará" in remarkable1:
    print(
        "Carcará no peito! Essa é terra de Salgueiro, o primeiro clube do interior a ser campeão pernambucano, Byte sente o chamado do Sertão!"
    )
elif "Patativa" in remarkable1:
    print(
        "Show da Patativa! Caruaru e o Central esperam Byte de braços abertos, direto da maior feira a céu aberto do mundo!"
    )
elif "Azulão" in remarkable1:
    print(
        "Ar puro de serra! O Azulão de Bonito, sensação recente do Pernambucano, pode ser o novo lar de Byte!"
    )
elif "fruticultura" in remarkable1:
    print(
        "Margens do Velho Chico! Petrolina, a maior cidade do interior, com direito a manga, uva e muita irrigação, chama Byte pro time!"
    )
elif "Pássaro Preto" in remarkable1:
    print(
        "Pertinho de casa! O Pássaro Preto, orgulhosamente um dos times mais folclóricos do planeta, também está de olho em Byte!"
    )

if veredict1 == "GOSTOU":
    liked += 1
    print(
        "Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar."
    )
else:
    print("Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.")

# SEGUNDA VIAGEM
if "Catende" in remarkable2:
    did_not_count += 1
    print(
        "Catende!!! Aqui já rodou a maior usina de açúcar e álcool da América Latina, Byte sente o orgulho no ar."
    )
elif "Palmares" in remarkable2:
    did_not_count += 1
    print(
        "Palmares, a Terra dos Poetas! Berço de nomes como Ascenso Ferreira, aqui até o futebol merece um verso."
    )
elif "Carcará" in remarkable2:
    print(
        "Carcará no peito! Essa é terra de Salgueiro, o primeiro clube do interior a ser campeão pernambucano, Byte sente o chamado do Sertão!"
    )
elif "Patativa" in remarkable2:
    print(
        "Show da Patativa! Caruaru e o Central esperam Byte de braços abertos, direto da maior feira a céu aberto do mundo!"
    )
elif "Azulão" in remarkable2:
    print(
        "Ar puro de serra! O Azulão de Bonito, sensação recente do Pernambucano, pode ser o novo lar de Byte!"
    )
elif "fruticultura" in remarkable2:
    print(
        "Margens do Velho Chico! Petrolina, a maior cidade do interior, com direito a manga, uva e muita irrigação, chama Byte pro time!"
    )
elif "Pássaro Preto" in remarkable2:
    print(
        "Pertinho de casa! O Pássaro Preto, orgulhosamente um dos times mais folclóricos do planeta, também está de olho em Byte!"
    )

if veredict2 == "GOSTOU":
    liked += 1
    print(
        "Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar."
    )
else:
    print("Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.")

if did_not_count == 2:
    print(
        "Catende e Palmares na excursão? Aí sim Byte tá garimpando ouro puro da Zona da Mata Sul! Pena que acabou por aqui."
    )

# RELATÓRIO
print()
print("RELATÓRIO DA EXCURSÃO SERTANEJA DO BYTE:")
print(f"- Visitas que contaram: {2 - did_not_count}")
print(f"- Gostou: {liked}")
print(f"- Não gostou: {2 - liked}")
print()
print(
    "E assim termina a Excursão Interiorana de Byte em Pernambuco. Anotar tudo isso na unha, sem laço nem lista, dá um trabalhão! Nas próximas férias, Byte espera que a molecada já saiba de laços, listas e funções pra dar conta do recado com estilo :)"
)
