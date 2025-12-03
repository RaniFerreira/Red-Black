# ================================================
# ÁRVORE RUBRO-NEGRA (RED-BLACK TREE)
# Implementação simples e didática
# com muitos comentários explicativos.
# ================================================


# Cores possíveis dos nós
RED = True
BLACK = False


# ----------------------------------------
# Classe do Nó da Árvore Rubro-Negra
# ----------------------------------------
class Node:
    def __init__(self, value):
        self.value = value      # valor guardado no nó
        self.color = RED        # novos nós sempre nascem VERMELHOS
        self.left = None        # filho esquerdo
        self.right = None       # filho direito
        self.parent = None      # pai do nó


# ----------------------------------------
# Classe da Árvore Rubro-Negra
# ----------------------------------------
class RedBlackTree:
    def __init__(self):
        self.root = None  # início: árvore vazia

    # ---------------------------
    # Função auxiliar:
    # Retorna a cor do nó, sendo
    # PRETO para None
    # ---------------------------
    def color_of(self, node):
        if node is None:
            return BLACK
        return node.color

    # ---------------------------------------
    # ROTAÇÃO À ESQUERDA
    # ---------------------------------------
    def rotate_left(self, x):
        """
        Rotação à esquerda:
        
               x                      y
                \                    / \
                 y     ---->       x   C
                / \                / \
               B   C              A   B
              /
             A
        """
        y = x.right
        x.right = y.left

        if y.left:
            y.left.parent = x

        y.parent = x.parent

        # liga y no pai antigo de x
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        # sobe x
        y.left = x
        x.parent = y

    # ---------------------------------------
    # ROTAÇÃO À DIREITA
    # ---------------------------------------
    def rotate_right(self, y):
        """
        Rotação à direita:
        
                 y                 x
                /                 / \
               x       --->      A   y
              / \                   / \
             A   B                 B   C
        """
        x = y.left
        y.left = x.right

        if x.right:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    # ---------------------------------------
    # INSERÇÃO COM AJUSTES
    # ---------------------------------------
    def insert(self, value):
        """
        Insere um valor na árvore, inicialmente como nó VERMELHO.
        Depois chama o "fix_insert" para restaurar as regras da árvore.
        """
        new_node = Node(value)

        # caso a árvore esteja vazia
        if self.root is None:
            new_node.color = BLACK  # raiz deve ser preta
            self.root = new_node
            return

        # 1) Insere como numa ABB normal
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

        new_node.parent = current

        # 2) Corrige violações da árvore Rubro-Negra
        self.fix_insert(new_node)

    # ---------------------------------------
    # REPARAÇÃO APÓS INSERÇÃO
    # ---------------------------------------
    def fix_insert(self, node):
        """
        Ajusta cores e executa rotações para manter as
        propriedades da árvore rubro-negra.
        """
        while node != self.root and self.color_of(node.parent) == RED:

            # Se o pai está à esquerda do avô
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right  # tio

                # Caso 1: tio vermelho → recolorir
                if self.color_of(uncle) == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent

                else:
                    # Caso 2: nó na direita → rotação esquerda
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    # Caso 3: nó na esquerda → rotação direita
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_right(node.parent.parent)

            # Pai está à direita do avô (espelho do caso anterior)
            else:
                uncle = node.parent.parent.left

                if self.color_of(uncle) == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent

                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_left(node.parent.parent)

        # raiz sempre deve ser preta
        self.root.color = BLACK


# ---------------------------------------
# TESTE SIMPLES
# ---------------------------------------
if __name__ == "__main__":
    tree = RedBlackTree()

    valores = [10, 20, 30, 15, 25, 5, 1]
    for v in valores:
        print(f"Inserindo {v}...")
        tree.insert(v)

    print("Inserções concluídas!")