from aigyminsper.search.graph import State 
from aigyminsper.search.search_algorithms import BuscaLargura

class AspiradorDePo(State):

    def __init__(self,
                op,
                pos_robo,
                condicao_esq = 'sujo',
                condicao_dir = 'sujo',
                ) -> None:
    
        super().__init__(op)
        self.pos_robo       = pos_robo      # Posição robo = esq ou dir
        self.condicao_esq   = condicao_esq  # Condição cômodo esquerdo = sujo ou limpo
        self.condicao_dir   = condicao_dir  # Condição cômodo direito = sujo ou limpo


    def successors(self):
        successors = [] # Lista de objetos da classe AspiradorDePo

        # Mover para Esquerda
        successors.append(AspiradorDePo('Ir p/ a esquerda' , 'esq' , self.condicao_esq , self.condicao_dir ))

        # Mover para Direita
        successors.append(AspiradorDePo('Ir p/ a direta'   , 'dir' , self.condicao_esq , self.condicao_dir ))

        # Limpar 
        if self.pos_robo == 'esq':
            successors.append(AspiradorDePo('limpar', self.pos_robo ,'limpo' , self.condicao_dir))

        if self.pos_robo =='dir':
            successors.append(AspiradorDePo('limpar', self.pos_robo ,self.condicao_esq , 'limpo'))

        return successors
    
    def is_goal(self):
        return self.condicao_esq == 'limpo' and self.condicao_dir == 'limpo' # Os dois espaços possíveis limpos 

    def description(self):
        return """Aspirador de pó em um ambiente com 2 cômodos.
                O aspirador pode estar em um dos cômodos, e cada cômodo pode estar sujo ou limpo. 
                O objetivo é limpar ambos os cômodos."""
    
    def cost(self):
        return 1
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #

        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        None


def main():
    print('Busca em profundidade iterativa')
    state = AspiradorDePo('' , 'esq', 'sujo', 'sujo')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':    
    main()