# PegaPega Turtlesim

O objetivo deste desafio e desenvolver um algoritmo capaz de fugir das outras tartarugas. Se alguma te pegar o jogo acaba!

## Orientações

1. Altere o arquivo tf_listener1.py para controlar a tartaruga principal.

2. Crie listeners dentro deste node para verificar as posições e orientações das outras tartarugas e buscar a melhor trajeto de fuga.

## Para execução

1. Baixar o repositorio no seu atual workspace, dentro da pasta /src 

        git clone https://github.com/AVANT-UFMG/pegapega-turtlesim.git
    
2. Na raiz, executar   

        catkin_make 
    
3. Executar 

        roslaunch pegapega_ws final.launch
        
    ***obs:*** podem acontecer erros durante a execução do arquivo launch. Para os seguintes erros executar o seguinte comando:

    1.  *RLException: [ ] is neither a launch file in package [pk_name] nor is [pkg_name] a launch file name.*
        
        Executar o comando na raiz da workspace
            
            source devel/setup.bash
    
    2. *Cannot locate node of type ...*

        Executar o comando dentro da pasta nodes do repositorios

            chmod +x tf_broadcaster.py tf_listener1.py tf_listener2.py tf_listener3.py tf_listener4.py  tf_listener5.py

---
Projeto Original Referência: [Catch-me-if-you-can-Turtlesim](https://github.com/jatinarora30/Catch-me-if-you-can-Turtlesim-.git)
