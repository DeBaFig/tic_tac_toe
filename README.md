# Tic-Tac-Toe (Jogo da Velha)

Pequeno jogo de Tic-Tac-Toe (Jogo da Velha) implementado em Python. O jogador humano joga com "O" e a IA joga com "X". A IA usa o algoritmo Minimax para escolher jogadas ótimas.


Visão geral do código
- Funções principais:
  - [`create_board`](main.py) — inicializa o tabuleiro.
  - [`display_board`](main.py) — imprime o tabuleiro no console.
  - [`check_win`](main.py) — verifica condições de vitória.
  - [`is_board_full`](main.py) — detecta empate.
  - [`get_available_moves`](main.py) — retorna movimentos livres.
  - [`minimax`](main.py) — implementação do algoritmo Minimax.
  - [`find_best_move`](main.py) — percorre jogadas possíveis e usa Minimax.
  - [`play_game`](main.py) — loop principal do jogo.
- Constantes:
  - [`SCORE_MAP`](main.py) — mapeamento de pontuações usado pelo Minimax.

Requisitos
- Python 3.x

Como executar
1. Abra um terminal no diretório do projeto.
2. Execute:
```sh
python [main.py](http://_vscodecontentref_/0)

> Controles e regras
>
> O tabuleiro é indexado de 0 a 8:
> 0 | 1 | 2
> 3 | 4 | 5
> 6 | 7 | 8
> Você controla "O". Informe um número de 0 a 8 para fazer sua jogada.
> O jogo termina quando alguém vence ou quando há empate.
>  
> Observações de implementação
> 
> O Minimax usa math.inf como sentinela para inicializar os melhores piores resultados (veja > minimax).
> Para melhorar performance em tabuleiros maiores, poderia ser adicionada poda alpha-beta e > memorização

Licença MIT

Código de exemplo, sinta-se à vontade para adaptar.