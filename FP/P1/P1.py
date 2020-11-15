#Rodrigo de Melo Pinto Numero: 95666
def eh_labirinto(maze):
 
 """Funcao que recebe um argumento e retorna True se\
 esse argumento for um labirinto valido"""

 if not isinstance (maze,tuple):
                 return False
 if len(maze) < 3:
                 return False
 for i in range(len(maze)):
                 if not isinstance (maze[i],tuple) or len(maze[i]) < 3 or len(maze[0]) != len(maze[i]):
                                 return False
                 if maze[i][0] != 1 or maze[i][-1] != 1 or type(maze[i][0]) != int or type(maze[i][-1]) != int:
                                 return False                                
                 for j in range(len(maze[i])-1):
                                 if (maze[i][j] != 0 and maze[i][j] != 1) or type(maze[i][j]) != int:
                                                 return False
                                 elif  maze[0][j] != 1 or maze[-1][j] != 1 or type (maze[0][j]) != int or type(maze[-1][j]) != int:
                                                 return False
 return True

def eh_posicao(pos):

 """Funcao que recebe um argumento e retorna True se\
 esse argumento for uma posicao valida"""
 
 if not isinstance (pos,tuple):
                 return False
 if len(pos) != 2:
                 return False                
 for i in pos:
                 if not type(i) == int:
                                 return False
                 if  i < 0:
                                 return False
 return True

                
def eh_conj_posicoes(conj_pos):
 
 """Funcao que recebe um argumento e retorna True se\
 esse argumento for um conjunto de posicoes valido"""
 
 if not isinstance (conj_pos,tuple):
                 return False
 for i in range(len(conj_pos)):
                 if not eh_posicao(conj_pos[i]):
                                 return False
                 elif conj_pos[i] in conj_pos[i+1: ]:
                                 return False
                 elif  conj_pos[i][0]  < 0: 
                                 return False
                 elif conj_pos[i][-1] < 0:
                                 return False
 return True
                 


def tamanho_labirinto(maze):
 
 """Funcao que recebe como argumento um labirinto e retorna um tuplo\
 com dois valores inteiros que correspondem as dimensoes do labirinto"""
 
 if not eh_labirinto(maze):
                 raise ValueError ('tamanho_labirinto: argumento invalido')
 res1 = ()
 res2 = ()
 i = 1                
 while i < len(maze): 
                 res1 = (len(maze),)
                 res2 = (len(maze[0]),)
                 i = i + 1
 return res1 + res2

def eh_mapa_valido(maze,conj_pos):
 
 """Funcao que recebe como argumento um labirinto e um conjunto de posicoes devolvendo True\
 se o segundo argumento sao posicoes compativeis(nao paredes) dentro do labirinto"""
 
 if not tamanho_labirinto(maze) or not eh_labirinto(maze) or not eh_conj_posicoes(conj_pos):
                 raise ValueError ('eh_mapa_valido: algum dos argumentos e invalido')
 dim = tamanho_labirinto(maze) #variavel correspondente a dimensao do maze
 for i in range(len(conj_pos)):
                 if conj_pos[i][0] > dim[0]:
                                 return False
                 if conj_pos[i][-1] > dim[-1]:
                                 return False                                
                 if maze[conj_pos[i][0]][conj_pos[i][-1]] != 0: #condicao para verificar se as posicoes dentro do conjunto de posicoes correspondem a paredes do maze
                                 return False
                 
 return True

def eh_posicao_livre(maze,unidades,pos):
 
 """Funcao que recebe como argumentos um labirinto um conjunto de posicoes e uma posicao\
 e retorna True se a posicao corresposnde a uma\
 posicao livre(nao ocupada por paredes ou por outras posicoes)"""
 
 if not eh_labirinto(maze) or not eh_conj_posicoes(unidades)\
    or not eh_posicao(pos) or not eh_mapa_valido(maze,unidades):
                 raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')
 for i in range(len(unidades)):
                 if pos == unidades[i]: #condicao para verificar se a posicao nao se encontra ocupada por outra posicao
                                 return False
 if maze[pos[0]][pos[1]] == 1: #condicao para verificar se a posicao se encontra numa parede do maze
                 return False
 return True
                
def posicoes_adjacentes(pos):
 
 """Funcao que recebe como argumento uma posicao e retorna\
 um tuplo correspondente as posicoes adjacentes a essa posicao"""
 
 pos_adj1 = ()
 pos_adj2 = ()
 pos_adj3 = ()
 pos_adj4 = ()
 if not eh_posicao(pos):
                 raise ValueError ('posicoes_adjacentes: argumento invalido')
 for i in range(len(pos)):
                 if pos[0] == 0 and pos[-1] != 0:
                                 pos_adj1 = ((pos[0],pos[-1]-1),) + pos_adj1
                                 pos_adj3 = ((pos[0]+1,pos[-1]),) + pos_adj3
                                 pos_adj4 = ((pos[0],pos[-1]+1),) + pos_adj4
                                 return pos_adj1 + pos_adj3 + pos_adj4
                 elif pos[0] != 0 and pos[-1] == 0:
                                 pos_adj2 = ((pos[0]-1,pos[-1]),) + pos_adj2
                                 pos_adj3 = ((pos[0]+1,pos[-1]),) + pos_adj3
                                 pos_adj4 = ((pos[0],pos[-1]+1),) + pos_adj4
                                 return pos_adj2 + pos_adj3 + pos_adj4
                 elif pos[0] == 0 and pos[-1] == 0:
                                 pos_adj3 = ((pos[0]+1,pos[-1]),) + pos_adj3
                                 pos_adj4 = ((pos[0],pos[-1]+1),) + pos_adj4
                                 return pos_adj3 + pos_adj4 
                 elif pos[0] != 0 and pos[-1] != 0:
                                 pos_adj1 = ((pos[0],pos[-1]-1),) + pos_adj1
                                 pos_adj2 = ((pos[0]-1,pos[-1]),) + pos_adj2
                                 pos_adj3 = ((pos[0]+1,pos[-1]),) + pos_adj3
                                 pos_adj4 = ((pos[0],pos[-1]+1),) + pos_adj4
                                 return pos_adj1 + pos_adj2 + pos_adj3 + pos_adj4

def mapa_str(maze,unidades):

 """Funcao que recebe como argumentos um labirinto e um conjunto de posicoes\
 e retorna a cadeia de caracteres que as repesenta"""
 
 if not eh_labirinto(maze) or not eh_conj_posicoes(unidades) or not eh_mapa_valido(maze,unidades):
                 raise ValueError ('mapa_str: algum dos argumentos e invalido') 
 mapa_str = ''
 i = 0
 j = 0                
 for i in range(len(maze[j])):
                 for j in range(len(maze)):
                                 if (j,i) in unidades: #condicao que verifica se alguma das posicoes o labirinto correnponde a alguma posicao do conjunto de posicoes
                                                 mapa_str = mapa_str + 'O'
                                 elif maze[j][i] == 1:
                                                 mapa_str = mapa_str + '#'
                                 elif maze[j][i] == 0:
                                                 mapa_str = mapa_str + '.'
                 mapa_str = mapa_str + '\n'
 mapa_str = mapa_str[:-1]       
 return mapa_str


def obter_objetivos(maze,unidades,pos):

 """Funcao que recebe como argumentos um labirinto um conjunto de posicoes \
 e uma posicao e retorna um conjunto de posicoes que corresponde a todos o possiveis objetivos para a posicao"""
 
 if not eh_labirinto(maze) or not eh_conj_posicoes(unidades) or not eh_posicao(pos)\
    or pos not in unidades or not tamanho_labirinto(maze) or not eh_mapa_valido(maze,unidades):
                 raise ValueError ('obter_objetivos: algum dos argumentos e invalido')
 res = ()
 for i in unidades:
                 if i != pos:
                                 pos_adj = posicoes_adjacentes(i)
                                 for j in pos_adj:
                                                 if eh_posicao_livre(maze,unidades,j):
                                                                 if j not in res: #condicao que garante que nenhuma posicao adjacente repetida apareca no resultado
                                                                                 res = res + (j,)
 return res

def obter_caminho(maze,unidades,pos):
 
 """Funcao que recebe como argumentos um labirinto um conjunto de posicoes e uma posicao e retorna\
 o caminho de numero minimo de passos ate a posicao objetivo"""
 
 if not eh_labirinto(maze) or not eh_conj_posicoes(unidades) or not eh_posicao(pos)\
    or pos not in unidades or not eh_mapa_valido(maze,unidades):
                 raise ValueError ('obter_caminho: algum dos argumentos e invalido')
 objetivos = obter_objetivos(maze,unidades,pos)
 lst_expl = [(pos,())]
 pos_visitadas = ()
 for i in unidades:
                 if i != pos and i in posicoes_adjacentes(pos): #condicao que verifica se a posicao se encontra dentro do conjunto de posicoes\
                                                                #e se alguma das posicoes so conjunto de poiscoes e adjacente a posicao
                                 return ()
 #Algoritmo BFS                              
 while lst_expl != []:
                 pos_atual , caminho_atual = lst_expl[0]
                 del(lst_expl[0]) #retira da lista de exploracao os antigos posicao_atual e caminho_atual
                 if pos_atual not in pos_visitadas:
                                 pos_visitadas = pos_visitadas + (pos_atual,)
                                 caminho_atual = caminho_atual + (pos_atual,)
                                 if pos_atual in objetivos:
                                                 return caminho_atual
                                 else:
                                                 
                                                 for j in posicoes_adjacentes(pos_atual):
                                                                 if eh_posicao_livre(maze,unidades,j):
                                                                                 lst_expl.append((j, caminho_atual)) #atualiza a lista de exploracao com as novas posicoes_adjacentes
 return ()
                
                
def mover_unidade(maze,unidades,pos):
 
 """Funcao que recebe como argumentos um labirinto um conjunto de posicoes e uma posicao\
 e retorna o conjunto de poisicoes atualizado apos a posicao ter realizado um movimento"""
 
 if not eh_labirinto(maze) or not eh_conj_posicoes(unidades) or not eh_posicao(pos)\
    or pos not in unidades or not eh_mapa_valido(maze,unidades):
                 raise ValueError ('mover_unidade: algum dos argumentos e invalido')
 caminho = obter_caminho(maze,unidades,pos) 
 if len(caminho) < 2: #se a unica posicao no conjunto de posicoes for a propria posicao esta nao se move
                 return unidades
 else:
                 for i in range(len(unidades)):
                                 if unidades[i] == pos: #verifica se a posicao se encontra no conjunto de posicoes
                                                 return unidades[:i] + (caminho[1],) + unidades[i+1:] #devolde o conjunto de posicoes anterior mais o segundo elemento do caminho
