

---

# Tiro espacial em Python

Este projeto é um jogo 2D simples, inspirado em shooters retrô (8-bit). O jogador controla uma nave que precisa destruir os inimigos antes que eles colidam ou cheguem à parte inferior da tela.

## Sumário
- [Descrição](#descrição)
- [Dependências](#dependências)
- [Instalação](#instalação)
- [Como Rodar](#como-rodar)
- [Funcionamento Básico](#funcionamento-básico)
- [Créditos](#créditos)
- [Desculpas](#desculpas)

---

## Descrição
- **Linguagem**: Python 3  
- **Módulos principais**: 
  - **turtle** para exibir a interface gráfica (nave, inimigos, projéteis)
  - **pygame** para tocar sons (laser, explosão etc.)

Inicialmente, o jogo usava `winsound`, exclusivo do Windows. Para funcionar também no Linux (e outros SOs), substituímos esse módulo por chamadas do `pygame.mixer.Sound`.

---

## Dependências
1. **Python 3.x**  
2. **Tkinter** (para o turtle)  
3. **PyGame** (para sons)  

No Ubuntu/Debian, por exemplo, você pode instalar assim:
```bash
sudo apt-get update
sudo apt-get install python3-tk
pip install pygame
```
Em outras plataformas, verifique a forma de instalar o `tkinter`.

---

## Instalação
1. Clone o repositório ou baixe o código-fonte:
   ```bash
   git clone <URL_DO_SEU_REPO>
   cd <NOME_DA_PASTA>
   ```

2. (Opcional, mas recomendado) Crie um ambiente virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # No Windows: .\.venv\Scripts\activate
   ```

3. Instale o PyGame e garanta que o Tkinter esteja instalado:
   ```bash
   pip install pygame
   # Se precisar no Linux:
   # sudo apt-get install python3-tk
   ```

---

## Como Rodar
1. Verifique se os arquivos de imagem (`.gif`) e áudio (`.wav`) estão na **mesma pasta** do código `SpaceWars.py`.
2. Em um terminal (ou prompt de comando), rode:
   ```bash
   python SpaceWars.py
   ```

3. A janela do **turtle** abrirá:
   - Use as setas **Esquerda** e **Direita** para mover a nave.
   - Use **Espaço** para atirar.

---

## Funcionamento Básico
- **Jogador**: Nave controlada pelo usuário.
- **Inimigos**: Vários inimigos se deslocam na horizontal, e descem gradualmente quando atingem as bordas.
- **Projétil (Tiro)**: Ao apertar **Espaço**, um tiro é disparado, e ao colidir com um inimigo, o inimigo respawna no topo e a pontuação aumenta.
- **Pontuação**: Exibida no canto superior esquerdo da tela.
- **Game Over**: Ocorre se um inimigo desce demais ou colide diretamente com a nave.

---

## Créditos
- **Autor**: Kauan Lopes  
- **Disciplina**: Estrutura de Dados

---
---

## Desculpas
- Estou entregando após o prazo, pois pensei em largar a matéria durante o semestre com a frustração da primeira prova, mas estou entregando no dia de abertura para envio de tarefas atrasadas e estarei alinhando todas as atividades que possam estar atrasadas, peço perdão novamente se no momento pareceu ter sido algo desrespeitoso, mas eu estava com grandes problemas no meu trabalho e ele começou a vibrar e deixei ali para entender o que estava acontecendo, entendendo que independente dos motivos a regra é justa a todos irei retornar estudando o máximo para recuperar a nota perdida, já que consegui demonstrar durante os dias o interesse na matéria e no aprendizado.

---
