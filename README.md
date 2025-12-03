## 🟥⬛ Red-Black Tree (Árvore Rubro-Negra)

Este repositório contém uma implementação simples, didática e totalmente comentada de uma Árvore Rubro-Negra em Python.
O objetivo é facilitar o estudo de como esse tipo de estrutura funciona internamente.

## 📘 O que é uma Árvore Rubro-Negra?

Uma Árvore Rubro-Negra (Red-Black Tree) é uma árvore binária de busca balanceada, desenvolvida por Rudolf Bayer (1972) e posteriormente aperfeiçoada por Guibas & Sedgewick, que definiram seu nome atual.

Ela garante que operações como:

🔍 Busca

➕ Inserção

➖ Remoção

tenham complexidade O(log n) mesmo no pior caso.

Isso é possível porque ela se reorganiza automaticamente usando:

Regras de cores (vermelho/preto)

Rotações esquerda/direita

## 📌 Propriedades da Árvore Rubro-Negra

Uma Red-Black Tree precisa respeitar 5 regras fundamentais:

Todo nó é vermelho ou preto.

A raiz é sempre preta.

Nós vermelhos não podem ter filhos vermelhos
(não pode haver dois vermelhos consecutivos).

Toda folha nula (None) é preta.

Em todo caminho da raiz até as folhas, o número de nós pretos é sempre igual.

Essas regras garantem que a árvore permaneça balanceada.


## ⚙️ Como funciona a inserção?

Quando um novo valor é inserido:

Ele entra como em uma árvore binária de busca comum (BST).

O novo nó começa como vermelho.

Se alguma regra da Red-Black Tree for violada, o algoritmo:

recolore nós,

aplica rotações (esquerda/direita),

e ajusta a estrutura.

## 📂 Estrutura do Código
Node

Representa um nó da árvore:

<img width="476" height="227" alt="image" src="https://github.com/user-attachments/assets/944d7b98-f4a5-4fc7-922d-52dd9d17318a" />


## 📚 Benefícios dessa Estrutura

🔥 Sempre balanceada

⚡ Operações rápidas (O(log n))


## 🏁 Conclusão

Esta implementação demonstra, de forma simples e totalmente comentada, como funciona internamente uma Árvore Rubro-Negra, uma das estruturas de dados balanceadas mais importantes da Ciência da Computação.

Com ela, é possível entender:

como os nós são inseridos,

como as regras de cores garantem equilíbrio,

como as rotações corrigem violações,

e por que a árvore mantém sempre operações eficientes.

