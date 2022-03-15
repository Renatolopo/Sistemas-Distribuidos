""""
Laboratório Prático da Semana
Vamos capturar Pokémons?

Utilize o repositório abaixo como fonte do scrap:
○ https://pokemondb.net/pokedex/shiny
■ Implemente um script para fazer o download da imagem representativa de todos os pokémons listados e salvar em um diretório local. 
■ Implemente um pool de processos para paralelizar a tarefa.
■ Meça o tempo de processamento com e sem paralelização.

"""
import requests
from bs4 import BeautifulSoup
import multiprocessing
import time


def download_img(pokemon):
    name_img = pokemon.split('/').pop()
    url_img = pokemon
    f = open(f"C:/Users/renat/Documentos fora da nuvem/pokemons/{name_img}",'wb')
    response = requests.get(url_img)
    f.write(response.content)
    f.close()

def main():
    url ='https://pokemondb.net/pokedex/shiny'
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    pokemons = soup.find_all('span', attrs={'class':'img-fixed shinydex-sprite shinydex-sprite-normal'})
    pokemons = [x.get("data-src") for x in pokemons]
    # pokemons = pokemons[:50]

    ###  Com Pool
    pool = multiprocessing.Pool()
    pool.map(download_img,pokemons)

    ### Sem Pool
    # for pokemon in pokemons:
    #     download_img(pokemon)


if __name__ == '__main__':
    inicio = time.time()
    main()
    fim = time.time()
    tempo = fim - inicio
    print(f"Funalizado em {tempo:.2f} Segundos!")