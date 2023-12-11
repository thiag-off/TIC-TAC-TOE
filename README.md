# TIC-TAC-TOE - IA Invencível

TIC-TAC-TOE, também conhecido como Jogo da Velha.

Este projeto foi desenvolvido em **Python**, utilizando a biblioteca gráfica [**CustomTkinter**](https://github.com/TomSchimansky/CustomTkinter), com o propósito de aplicar os conceitos do algoritmo **Minimax**.

O algoritmo **Minimax** é amplamente utilizado para avaliar as melhores jogadas em jogos de turnos, garantindo que a inteligência artificial (AI) seja capaz de tomar decisões estratégicas imbatíveis.

### Características Principais:

- **Minimax Algorithm:** A lógica por trás da inteligência artificial do jogo é baseada no algoritmo Minimax, permitindo que a AI tome decisões ótimas a cada jogada.
  
- **CustomTkinter Graphics:** A interface gráfica foi desenvolvida utilizando a biblioteca CustomTkinter, proporcionando uma experiência visual agradável para os jogadores.



## Minimax Algorithm 

![image](https://github.com/thiag-off/TIC-TAC-TOE/assets/87951363/aedc2079-13d5-4791-967e-faf4cc07de96)


O algoritmo recebe qualquer estado de jogo e calcula as repercussões de todas as jogadas possíveis.

No código este processo é alcançado através de um método recursivo, ou seja, um método que chama a si mesmo repetidamente até que sua condição base seja cumprida.

Neste caso, a condição base é o fim do jogo, indicado pelos valores 1, -1 e 0, que representam a *vitória de X*, *vitória de O* e *empate*, respectivamente.

Após analisar todos os possíveis jogos a partir de uma posição, o método executa o movimento levando em conta a melhor pontuação de cada jogada.

![image](https://github.com/thiag-off/TIC-TAC-TOE/assets/87951363/d3edaf82-5174-4f88-9580-73dd6a3cf41f)

