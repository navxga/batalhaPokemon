from time import sleep
import random

linha = '=-'*20
fimDoPrograma = 's' #!! Perguntar usando `.lower().strip()`
Iniciais = ['#', 'Sceptile', 'Blaziken', 'Swampert']
turno = 1
num = random.randint(0, 3)
ataquesRayquaza = [25, 50, 100, 150]
ataquesPokemon = [25, 25, 50, 100]
danoToRayquaza = ataquesPokemon[num]
danoToPokemon = ataquesRayquaza[num]
vidaRayquaza = 100
vidaPokemon = 100

# Introdução
print('\n')
print('Seja Bem-vindo ao Ginásio de DRAGÃO')
print('Tenho certeza que você veio em busca da Insígnia. Então, para consegui-la é fácil.')
nome = input('Antes de mais nada, diga-me o seu nome: ').strip().capitalize()
sleep(1)
print(f'Certo, {nome}... Você precisa apenas derrotar...')
sleep(1)
print('\n')
print('O NOSSO REI RAYQUAZA!!! QUE A BATALHA COMEÇE!')
print(linha)


while fimDoPrograma == 's':

    #!! ADICIONAR TEMPO
    sleep (0)

    # Batalha
    print('Escolha o seu pokémon:')
    escolhaPokemon = int(input('[1] Sceptile\n[2] Blaziken\n[3] Swampert\nDigite sua escolha: '))
    print(linha)
    if 0 < escolhaPokemon < 4:
        pokemon = Iniciais[escolhaPokemon]

        print(f'O Rayquaza, como o Rei do Ginásio. Permite que {pokemon} inicie a batalha:\n')

        escolhaBatalha = 1

        # Enquanto Atacar ou Curar
        while 0 < escolhaBatalha < 3:
            print('\n')
            print(f'-----{turno}º Turno-----')
            print('Qual ação você quer realizar? ')

            escolhaBatalha = int(input('[1] Atacar\n[2] Curar\n[3] Fugir\n'))

            # ATACAR
            if escolhaBatalha == 1:

                print(linha)
                print(f'Rayquaza: {vidaRayquaza}HP')
                print(f'{pokemon}: {vidaPokemon}HP')
                print(linha)
                sleep(2)

                print(f'{pokemon} vai atacar o Rayquaza!')
                sleep(1)
                print(f'{pokemon} tirou {danoToRayquaza}HP')
                vidaRayquaza -= danoToRayquaza
                sleep(2)
                if vidaRayquaza <= 0:
                    print('RAYQUAZA ESTÁ MORTO!!!')
                    break

                print(f'Rayquaza vai atacar {pokemon}')
                sleep(1)
                print(f'Rayquaza tirou {danoToPokemon}HP')
                vidaPokemon -= danoToPokemon
                sleep(2)
                if vidaPokemon <= 0:
                    print(f'{pokemon.upper()} ESTÁ MORTO!!!')
                    break
                
                turno += 1

                print(linha)
                print(f'Rayquaza: {vidaRayquaza}HP')
                print(f'{pokemon}: {vidaPokemon}HP')
                print(linha)
                sleep(2)

            # CURAR
            elif escolhaBatalha == 2:
                if turno == 1:
                    print('HP Cheio! Impossível se curar.')
                elif turno > 1:
                    print(linha)
                    print(f'{pokemon} curou {danoToRayquaza}HP')
                    vidaPokemon += danoToRayquaza
                    print(f'{pokemon}: {vidaPokemon}HP')
                    print(linha)
                    sleep(2)
        # FUGIR          
        print('Ok, você conseguiu fugir!')
        fimDoPrograma = str(input('Deseja desafiar Rayquaza outra vez? [s/n] ')).strip().lower()
    else:
        print('Po meu mestre, escolhe o número direito ai. É 1, 2 OU 3!')
