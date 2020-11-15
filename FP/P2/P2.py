#Rodrigo de Melo Pinto Numero: 95666
#TAD Posicao

#Construtores:
def cria_posicao(x,y):
    """
    Funcao que recebe os valores correspondentes as coordenadas de uma posicao
    e devolve a posicao correspondente, repesentada numa lista.
    
    cria_posicao: N x N -> posicao
    
    """
    if not isinstance(x,int) or not isinstance(y,int) or x < 0 or y < 0 :
        raise ValueError('cria_posicao: argumentos invalidos')
    return [x,y]

def cria_copia_posicao(p):
    """
    Funcao que recebe uma posicao e devolve uma copia dessa posicao, repesentada
    numa lista
    
    cria_copia_posicao: posicao -> posicao
    
    """    
    return p.copy()

#Seletores:
def obter_pos_x(p):
    """
    Funcao que recebe uma posicao e devolve a componete x dessa posicao.
    
    obter_pos_x: posicao -> N
    
    """    
    return p[0]

def obter_pos_y(p):
    """
    Funcao que recebe uma posicao e devolve a componete y dessa posicao.
    
    obter_pos_y: posicao -> N
    
    """        
    return p[1]

#Reconhecedores:
def eh_posicao(arg):
    """
    Funcao que recebe um argumento e devolve True cajo o seu argumento
    seja um TAD posicao e False caso contrario.
    
    eh_posicao: universal -> booleano
    
    """        
    return isinstance(arg,list) and len(arg) == 2 and isinstance(arg[0],int) and isinstance(arg[1],int) and arg[0] >= 0 and arg[1] >= 0

#Testes:
def posicoes_iguais(p1,p2):
    """
    Funcao que recebe duas posicoes e devolve True apenas se p1 e p2
    sao posicoes iguais.
    
    posicoes_iguais: posicao x posicao -> booleano
    
    """        
    return p1[0] == p2[0] and p1[1] == p2[1]

#Transformadores:
def posicao_para_str(p):
    """
    Funcao que recebe uma posicao e devolve a cadeia de caracteres '(x, y)'
    que representa o seu argumento,sendo os valores x e y as coordenadas de p.
    
    posicao_para_str: posicao -> str
    
    """        
    return '(' + str(p[0]) + ',' + ' ' +  str(p[1]) + ')'

#Funcoes de alto nivel:
def obter_posicoes_adjacentes(p):
    """
    Funcao que recebe uma posicao e devolve um tuplo com as posicoes adjacentes
    a posicao p de acordo com a ordem de leitura de um labirinto.
    
    obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    
    """        
    pos_adj1 = ()
    pos_adj2 = ()
    pos_adj3 = ()
    pos_adj4 = ()
    for i in range(len(p)):
        if obter_pos_x(p) == 0 and obter_pos_y(p) != 0:
            pos_adj1 = ([obter_pos_x(p),obter_pos_y(p)-1],) + pos_adj1
            pos_adj3 = ([obter_pos_x(p)+1,obter_pos_y(p)],) + pos_adj3
            pos_adj4 = ([obter_pos_x(p),obter_pos_y(p)+1],) + pos_adj4
            return pos_adj1 + pos_adj3 + pos_adj4
        elif obter_pos_x(p) != 0 and obter_pos_y(p) == 0:
            pos_adj2 = ([obter_pos_x(p)-1,obter_pos_y(p)],) + pos_adj2
            pos_adj3 = ([obter_pos_x(p)+1,obter_pos_y(p)],) + pos_adj3
            pos_adj4 = ([obter_pos_x(p),obter_pos_y(p)+1],) + pos_adj4
            return pos_adj2 + pos_adj3 + pos_adj4
        elif obter_pos_x(p) == 0 and obter_pos_y(p) == 0:
            pos_adj3 = ([obter_pos_x(p)+1,obter_pos_y(p)],) + pos_adj3
            pos_adj4 = ([obter_pos_x(p),obter_pos_y(p)+1],) + pos_adj4
            return pos_adj3 + pos_adj4 
        elif obter_pos_x(p) != 0 and obter_pos_y(p) != 0:
            pos_adj1 = ([obter_pos_x(p),obter_pos_y(p)-1],) + pos_adj1
            pos_adj2 = ([obter_pos_x(p)-1,obter_pos_y(p)],) + pos_adj2
            pos_adj3 = ([obter_pos_x(p)+1,obter_pos_y(p)],) + pos_adj3
            pos_adj4 = ([obter_pos_x(p),obter_pos_y(p)+1],) + pos_adj4
            return pos_adj1 + pos_adj2 + pos_adj3 + pos_adj4 

#TAD unidades

#Construtores:
def cria_unidade(p,v,f,string):
    """
    Funcao que recebe uma posicao p, dois valores inteiros maiores que 0
    correspondentes a vida e forca da unidade, e uma cadeia de caracteres
    nao vazia correspondente ao exercito da unidade
    e devolve uma lista correspondente a unidade.
    
    cria_unidade: posicao x N x N x str -> unidade
    
    """        
    if not eh_posicao(p) or not isinstance(v, int) or v <= 0 or not isinstance(f,int)\
       or f <= 0 or not isinstance(string,str) or string == '':
        raise ValueError('cria_unidade: argumentos invalidos')
    return [p,v,f,string]

def cria_copia_unidade(u):
    """
    Funcao que recebe uma unidade u e devolve uma nova copia da unidade.
    
    cria_copia_unidade: unidade -> unidade
    
    """        
    return u.copy()

#Seletores:
def obter_posicao(u):
    """
    Funcao que recebe uma unidade e devolve a posicao dessa unidade.
    
    obter_posicao: unidade -> posicao
    
    """        
    return u[0]

def obter_exercito(u):
    """
    Funcao que recebe uma unidade e devolve a cadeia de caracteres
    correspondente ao exercito da unidade.
    
    obter_exercito: unidade -> str
    
    """        
    return u[3]

def obter_forca(u):
    """
    Funcao que recebe uma unidade e devolve o valor correspondente a
    forca de ataque da unidade.
    
    obter_forca: unidade -> N
    
    """            
    return u[2]

def obter_vida(u):
    """
    Funcao que recebe uma unidade e devolve o valor correspondente aos
    pontos de vida da unidade.
    
    obter_vida: unidade -> N
    
    """            
    return u[1]

#Modificadores:
def muda_posicao(u,p):
    """
    Funcao que recebe uma unidade e uma posicao e modifica destrutivamente
    a unidade u alterando a sua posicao com o novo valor p, e devolve
    a propria unidade.
    
    muda_posicao: unidade x posicao -> unidade
    
    """            
    u[0] = p
    return u

def remove_vida(u,v):
    """
    Funcao que recebe uma unidade e um valor, modificando destrutivamente
    a unidade u e alterando os seus pontos de vida subtraindo o valor v,
    e devolve a propria unidade.
    
    remove_vida: unidade x N -> unidade
    
    """            
    u[1] = u[1] - v
    return u

#Reconhecedores:
def eh_unidade(arg):
    """
    Funcao que recebe um argumento e devolve True caso o seu argumento
    seja um TAD unidade e False caso contrario.
    
    eh_unidade: universal -> booleano
    
    """            
    return isinstance(arg,list) and len(arg) == 4 and eh_posicao(arg[0])\
           and isinstance(arg[1],int) and arg[1] > 0 and isinstance(arg[2],int)\
           and arg[2] > 0 and isinstance(arg[3],str) and arg[3] != ''

#Testes:
def unidades_iguais(u1,u2):
    """
    Funcao que recebe duas unidades e devolve True apenas se u1 e u2 sao
    unidades iguais.
    
    unidades_iguais: unidade x unidade -> booleano
    
    """            
    return u1[0] == u2[0] and u1[1] == u2[1] and u1[2] == u2[2] and u1[3] == u2[3]

#Transformadores:
def unidade_para_char(u):
    """
    Funcao que recebe uma unidade e devolve a cadeia de caracteres
    de um unico elemento, correspondente ao primeiro carcter em 
    maiuscula do exercito da unidade passada por arguemento.
    
    unidade_para_char: unidade -> str
    
    """            
    return str(u[3][0].upper())

def unidade_para_str(u):
    """
    Funcao que recebe uma unidade e devolve a cadeia de caracteres
    que representa a unidade.
    
    unidade_para_str: unidade -> str
    
    """            
    return unidade_para_char(u) + '[' + str(u[1]) + ',' + ' ' + str(u[2]) + ']'\
           + '@' + posicao_para_str(u[0])

#Funcoes de alto nivel:
def unidade_ataca(u1,u2):
    """
    Funcao que recebe duas unidades e modifica destrutivamente a unidade
    u2 retirando o valor de pontos de vida correspondentes a forca da
    unidade u1.
    A funcao devolve True se a unidade u2 for destruida ou False caso
    contrario.
    
    unidade_ataca: unidade x unidade -> booleano
    
    """            
    if obter_vida(remove_vida(u2,obter_forca(u1))) <= 0:
        return True
    else:
        return False
    
def ordenar_unidades(t):
    """
    Funcao que recebe um tuplo de unidades e devolve um tuplo contendo as
    mesmas unidades do tuplo fornecido como argumento, ordenadas de acordo
    com a ordem de leitura do labirinto.
    
    ordenar_unidades: tuplo de unidades -> tuplo de unidades
    
    """            
    l = list(t)
    l.sort(key=lambda x: [x[0][1], x[0][0]]) # ordena as unidades primeiro pela
                                             # coordenada do y e depois pela 
                                             # coordanda do x
    return tuple(l)

#TAD mapa:

#Construtores:
def cria_mapa(d,w,e1,e2):
    """
    Funcao que recebe um tuplo d de 2 valores inteiros correspondentes
    as dimensoes Nx e Ny do labirinto seguindo as restricoes do 1 projeto,
    um tuplo w de 0 ou mais posicoes correspondentes as paredes que nao sao
    dos limites exteriores do labirinto, um tuplo e1 de 1 ou mais unidades do
    mesmo exercito, e um tuplo e2 de 1 ou mais unidades de outro exercito;
    e devolve uma lista que representa o mapa.
    
    cria_mapa: tuplo x tuplo x tuplo x tuplo -> mapa
    
    """            
    if not isinstance(d,tuple) or not isinstance(w,tuple) or not isinstance(e1,tuple)\
       or not isinstance(e2,tuple):
        raise ValueError('cria_mapa: argumentos invalidos')
    
    elif len(d) != 2 or e1 == () or e2 == ():
        raise ValueError('cria_mapa: argumentos invalidos')
    
    elif not isinstance(d[0],int)\
         or not isinstance(d[1],int) or d[0] < 3 or d[1] < 3:
        raise ValueError('cria_mapa: argumentos invalidos')
    
    if w != ():
        for i in range(len(w)):
            if not eh_posicao(w[i]):
                raise ValueError('cria_mapa: argumentos invalidos')
            elif w[i][0] > d[0] or w[i][1] > d[1]\
                 or w[i][0] == 0 or w[i][0] == d[0] or w[i][1] == 0 or w[i][1] == d[1]:
                raise ValueError('cria_mapa: argumentos invalidos')
    
    for j in range(len(e1)):
        if not eh_unidade(e1[j]):
            raise ValueError('cria_mapa: argumentos invalidos')
        
    for k in range(len(e2)):
        if not eh_unidade(e2[k]):
            raise ValueError('cria_mapa: argumentos invalidos')
    
    return [d,w,e1,e2]

def cria_copia_mapa(m):
    """
    Funcao que recebe um mapa e devolve uma copia do mapa.
    
    cria_copia_mapa: mapa-> mapa
    
    """            
    d = (m[0][0],m[0][1])
    w = ()
    e1 = ()
    e2 = ()
    for i in range(len(m[1])):
        w = w + (cria_copia_posicao(m[1][i]),)
    for j in range(len(m[2])):
        e1 = e1 + (cria_copia_unidade(m[2][j]),)
    for k in range(len(m[3])):
        e2 = e2 + (cria_copia_unidade(m[3][k]),)          
    return cria_mapa(d,w,e1,e2)

#Seletores:
def obter_tamanho(m):
    """
    Funcao que recebe um mapa e devolve um tuplo de dois valores inteiros
    o primeiro corresponde a dimensao Nx e o segundo a dimensao Ny.
    
    obter_tamanho: mapa-> tuplo
    
    """            
    return m[0]

def obter_nome_exercitos(m):
    """
    Funcao que recebe um mapa e devolve um tuplo ordenado com duas cadeias
    de caracteres correspondendo aos nomes dos exercitos do mapa.
    
    obter_nome_exercitos: mapa-> tuplo
    
    """          
    lst = [m[2][0][3],m[3][0][3]]
    return tuple(sorted(lst))

def obter_unidades_exercito(m,e):
    """
    Funcao que recebe um mapa e devolve um tuplo contendo as unidades do mapa
    pertencentes ao exercito indicado pela cadeia de caracteres e, ordenadas
    em ordem de leitura do labirinto.
    
    obter_unidade_exercito: mapa-> tuplo
    
    """          
    if  m[2] != () and m[2][0][3] == e:
        return ordenar_unidades(m[2])
    elif  m[3] != () and m[3][0][3] == e:
        return ordenar_unidades(m[3])
    else:
        return ()

def obter_todas_unidades(m):
    """
    Funcao que recebe um mapa e devolve um tuplo contendo todas as unidades
    do mapa, ordenadas em ordem de leitura do labirinto.
    
    obter_todas_unidades: mapa-> tuplo
    
    """          
    t1 = obter_unidades_exercito(m,obter_exercito(m[2][0]))
    t2 = obter_unidades_exercito(m,obter_exercito(m[3][0]))
    res = t1 + t2
    return ordenar_unidades(res)

def obter_unidade(m,p):
    """
    Funcao que recebe um mapa e uma posicao e devolve a unidade do mapa
    que se encontra na posicao p.
    
    obter_unidade mapa x posicao -> unidade
    
    """          
    for i in range(len(m[2])):
        if m[2][i][0] == p:
            res = m[2][i]
    for j in range(len(m[3])):
        if m[3][j][0] == p:
            res = m[3][j]
    return res

#Modificadores:
def eliminar_unidade(m,u):
    """
    Funcao que recebe um mapa e uma unidade e modifica destrutivamente
    o mapa m eliminando a unidade u do mapa e deixando livre a posicao
    onde se encontrava a unidade.
    Devolve o proprio mapa
    
    eliminar_unidade: mapa x unidade -> mapa
    
    """          
    for i in range(len(m[2])):
        if unidades_iguais(m[2][i], u):
            m[2] = m[2][:i] + m[2][i+1:]
            return m
    for i in range(len(m[3])):
        if unidades_iguais(m[3][i], u):
            m[3] = m[3][:i] + m[3][i+1:]
            return m

def mover_unidade(m,u,p):
    """
    Funcao que recebe um mapa e uma unidade e modifica destrutivamente
    o mapa m e a unidade u alterando a posicao da unidade no mapa para
    a nova posicao p e deixando livre a posicao onde se encontra.
    Devolve o proprio mapa.
    
    mover_unidade: mapa x unidade x posicao -> mapa
    
    """          
    for i in range(len(m[2])):
        if m[2][i] == u:
            m[2][i][0] = p
            return m
    for i in range(len(m[3])):
        if m[3][i] == u:
            m[3][i][0] = p
            return m

#Reconhecedores:
def eh_posicao_unidade(m,p):
    """
    Funcao que recebe um mapa e uma posicao e devolde True apenas no
    caso da posicao p do mapa estar ocupada por uma unidade.
    
    eh_posicao_unidade: mapa x posicao -> booleano
    
    """          
    for i in range(len(m[2])):
        if m[2][i][0] == p:
            return True
    for i in range(len(m[3])):
        if m[3][i][0] == p:
            return True
    return False
        
def eh_posicao_corredor(m,p):
    """
    Funcao que recebe um mapa e uma posicao e devolde True apenas no
    caso da posicao p do mapa corresponder a um corredor no labirinto.
    
    eh_posicao_corredor: mapa x posicao -> booleano
    
    """            
    if p in m[1] or p[0] == 0 or p[0] >= (m[0][0]-1) or p[1] == 0 or p[1] >= (m[0][1]-1):
            return False
    return True

def eh_posicao_parede(m,p):
    """
    Funcao que recebe um mapa e uma posicao e devolde True apenas no
    caso da posicao p do mapa corresponder a uma parede no labirinto.
    
    eh_posicao_parede: mapa x posicao -> booleano
    
    """           
    return not eh_posicao_corredor(m,p)

#Testes:
def mapas_iguais(m1,m2):
    """
    Funcao que recebe dois mapas e devolde True apenas se m1
    e m2 forem iguais.
    
    mapas_iguais: mapa x mapa-> booleano
    
    """           
    return m1[0] == m2[0] and m1[1] == m2[1]\
           and m1[2] == m2[2] and m1[3] == m2[3]

#Transformadores:
def mapa_para_str(u):
    """
    Funcao que recebe um mapa e devolde uma cadeia de carcteres que representa
    o mapa como descrito no primeiro projeto, neste caso, com as unidades
    representadas pela sua representacao externa.
    
    mapa_para_str: mapa -> str
    
    """           
    mapa_str = ''
    linhas = u[0][1]
    colunas = u[0][0]
    contador = linhas * colunas
    i = 0
    l = []
    # ciclo que imprime o mapa sem as unidades e as paredes internas
    while i < contador:
        # verifica se o i corresponde a alguma parede exterior
        if i < colunas or i >= contador - colunas or i % colunas == 0\
           or i % colunas == colunas - 1:
            mapa_str += '#'
        else:
            mapa_str += '.'
        i += 1
    # ciclo que verifica a posicao na string onde estao as pardes internas
    for i in range(len(u[1])):
        mapa_str = mapa_str[:u[1][i][1]*colunas + u[1][i][0]] + '#'\
            + mapa_str[u[1][i][1]*colunas + u[1][i][0] + 1:]
    # ciclo que verifica a posicao na string onde estao as unidades\
    # do primeiro exercito
    for i in range(len(u[2])):
        mapa_str = mapa_str[:u[2][i][0][1]*colunas + u[2][i][0][0]] + \
            unidade_para_char(u[2][i]) + mapa_str[u[2][i][0][1]*colunas + u[2][i][0][0]+1:]
    # ciclo que verifica a posicao na string onde estao as unidades\
    # do segundo exercito    
    for i in range(len(u[3])):
        mapa_str = mapa_str[:u[3][i][0][1]*colunas + u[3][i][0][0]] + \
            unidade_para_char(u[3][i]) + mapa_str[u[3][i][0][1]*colunas + u[3][i][0][0]+1:]
    # ciclo que adiciona a string os \n apos cada uma das linhas do mapa
    for i in range(1,len(mapa_str)+1):
        if i % colunas == 0:
            l.append(mapa_str[:colunas] + '\n')
            mapa_str = mapa_str[colunas:]
    for i in range(len(l)):
        mapa_str += l[i]
    return mapa_str[:-1]

#Funcoes de alto nivel:
def obter_inimigos_adjacentes(m,u):
    """
    Funcao que recebe um mapa e uma unidade e devolde um tuplo contendo
    as unidades inimigas adjacentes a unidade u de acordo com a ordem de
    leitura do labirinto.
    
    obter_inimigos_adjacentes: mapa x unidade -> tuplo de unidades
    
    """          
    t = ()
    inimigos = obter_posicoes_adjacentes(obter_posicao(u))
    if u in m[2]:
        for i in range(len(m[3])):
            if obter_posicao(m[3][i]) in inimigos:
                t = t + (m[3][i],)
    elif u in m[3]:
        for i in range(len(m[2])):
            if obter_posicao(m[2][i]) in inimigos:
                t = t + (m[2][i],)
    return ordenar_unidades(t)

###########################################
# FP2019/2020 @ IST                       #
# Projeto 2 - Tecnico Battle Simulator    #
#                                         #
###########################################
# TAD mapa - Funcao de alto nivel         #
#            obter_movimento              #
###########################################


def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)

#Funcoes adicionais:
def calcula_pontos(m,string):
    """
    Funcao auxiliar que recebe um mapa e uma cadeia de carcteres
    correspondente ao nome de um dos exercitos do mapa e devolve a sua pontuacao.
    A pontuacao dum exercito e o total dos pontos de vida de todas as unidades
    do exercito.
    
    calcula_pontos: mapa x str -> int
    
    """           
    res = 0
    for unidade in obter_unidades_exercito(m,string):
        res += obter_vida(unidade)
    return res

def simula_turno(m):
    """
    Funcao auxiliar que modifica o mapa fornecido como argumento de acordo com
    a simulacao de um turno de batalha completo, e devolve o proprio mapa.
    
    simula_turno: mapa -> mapa
    
    """               
    i = 0
    # lista com todas a unidades do mapa ordenadas
    unidades_por_mover = list(ordenar_unidades(obter_todas_unidades(m)))
    e1,e2 = obter_nome_exercitos(m)
    while unidades_por_mover != [] and calcula_pontos(m,e1) != 0\
          and calcula_pontos(m,e2) != 0:
        # mover a primeira unidade do unidades_por_mover
        muda_posicao(unidades_por_mover[0],obter_movimento(m,unidades_por_mover[0]))
        # tem algum inimigo adjacente?
        if obter_inimigos_adjacentes(m,unidades_por_mover[0]) != ():
            # se sim ataca esse inimigo
            inimigos = obter_inimigos_adjacentes(m,unidades_por_mover[0])
            # o inimigo ficou com a vida a 0?
            if unidade_ataca(unidades_por_mover[0],inimigos[0]):
                # se sim eliminar o inimigo do mapa
                eliminar_unidade(m,inimigos[0])
                # retirar o inimigo da lista de unidades do mapa
                while i < len(unidades_por_mover):
                    if inimigos[0] == unidades_por_mover[i]:
                        del unidades_por_mover[i]
                    else:
                        i += 1
                i = 0
        #remover da lista a unidade movida                 
        del unidades_por_mover[0]
    return m

def simula_batalha(string, booleano):
    """
    Funcao principal que permite simular uma batalha completa. A batalha termina
    quando um dos exercitos vence ou, se apos completar um turno de batalha, nao
    ocorreu nenhuma alteracao ao mapa e as unidades.
    A funcao simula_batalha recebe uma cadeia de caracteres e um valor booleano
    e devolve o nome do exercito ganhador. Em caso de empate, a funcao deve
    devolver a cadeia de caracteres 'EMPATE'.
    O argumento booleano ativa o modo verboso (True) ou modo quiet (False).
    No modo quiet mostra-se pela saida standard o mapa e a pontuacao no inicio
    da simulacao e apos do ultimo turno de batalha.
    No modo verboso, mostra-se tambem o mapa e a pontuacao apos cada turno de
    batalha.
    
    simula_batalha: str x booleano -> str
    
    """               
    file = open(string,'r')
    d = eval(file.readline()[:-1]) # e necessario retirar o ultimo elemento pois e um \n
    nome_e1 = eval(file.readline()[:-1])# e necessario retirar o ultimo elemento pois e um \n
    nome_e2 = eval(file.readline()[:-1])# e necessario retirar o ultimo elemento pois e um \n
    paredes = eval(file.readline()[:-1])# e necessario retirar o ultimo elemento pois e um \n
    pos_e1 = eval(file.readline()[:-1])# e necessario retirar o ultimo elemento pois e um \n
    pos_e2 = eval(file.readline()) # nao e preciso retirar o ultimo pois o ficheiro acaba
    file.close()
    e1 = ()
    e2 = ()
    w = ()
    # criacao do primeiro exercito
    for posicao in pos_e1:
        e1 = e1 + (cria_unidade(cria_posicao(posicao[0],posicao[1]),nome_e1[1],nome_e1[2],nome_e1[0]),)
    # criacao do segundo exercito    
    for posicao2 in pos_e2:
        e2 = e2 + (cria_unidade(cria_posicao(posicao2[0],posicao2[1]),nome_e2[1],nome_e2[2],nome_e2[0]),)
    # criacao do tuplo com as paredes internas    
    for parede in paredes:
        w = w + (cria_posicao(parede[0],parede[1]),)
    nome_e = [nome_e1[0],nome_e2[0]]
    nome_e.sort()
    m = cria_mapa(d,w,e1,e2)
    
    if booleano == True:
        print(mapa_para_str(m))
        print('[' + ' ' + str(nome_e[0]) + ':' + str(calcula_pontos(m,nome_e[0])) + \
              ' ' + str(nome_e[1]) + ':' + str(calcula_pontos(m,nome_e[1])) + ' ' + \
              ']')
        prev_mapa = []
        pontos_vida = []
        # simula a batalha ate algum do exercitos ficar vazio ou ate nao haver alteracoes no mapa
        while (obter_unidades_exercito(m,nome_e[0]) != () and obter_unidades_exercito(m,nome_e[1]) != ())\
              and (prev_mapa != m or pontos_vida[0] != calcula_pontos(m, nome_e[0]) or pontos_vida[1] != calcula_pontos(m,nome_e[1])):
            pontos_vida = [calcula_pontos(m,nome_e[0]),calcula_pontos(m,nome_e[1])].copy()
            prev_mapa = cria_copia_mapa(m)
            print(mapa_para_str(simula_turno(m)))
            print('[' + ' ' + str(nome_e[0]) + ':' + str(calcula_pontos(m,nome_e[0])) + \
                  ' ' + str(nome_e[1]) + ':' + str(calcula_pontos(m,nome_e[1])) + ' ' + \
                  ']')
        # se o primeiro exercito nao tem unidades
        if obter_unidades_exercito(m,nome_e[0]) == ():
            # ganha o segundo exercito
            return(nome_e[1])
        # se o segundo exercito nao tem unidades
        elif obter_unidades_exercito(m,nome_e[1]) == ():
            # ganha o primeiro
            return(nome_e[0])
        else:
            return 'EMPATE'
        
    elif booleano == False:
        print(mapa_para_str(m))
        print('[' + ' ' + str(nome_e[0]) + ':' + str(calcula_pontos(m,nome_e[0])) + \
              ' ' + str(nome_e[1]) + ':' + str(calcula_pontos(m,nome_e[1])) + ' ' + \
              ']')
        prev_mapa = []
        pontos_vida = []
        # simula a batalha ate algum do exercitos ficar vazio ou ate nao haver alteracoes no mapa
        while (obter_unidades_exercito(m,nome_e[0]) != () and obter_unidades_exercito(m,nome_e[1]) != ())\
              and (prev_mapa != m or pontos_vida[0] != calcula_pontos(m, nome_e[0]) or pontos_vida[1] != calcula_pontos(m,nome_e[1])):
            pontos_vida = [calcula_pontos(m,nome_e[0]),calcula_pontos(m,nome_e[1])].copy()
            prev_mapa = cria_copia_mapa(m)
            simula_turno(m)
        print(mapa_para_str(m))
        print('[' + ' ' + str(nome_e[0]) + ':' + str(calcula_pontos(m,nome_e[0])) + \
                      ' ' + str(nome_e[1]) + ':' + str(calcula_pontos(m,nome_e[1])) + ' ' + \
                      ']')
        # se o primeiro exercito nao tem unidades
        if obter_unidades_exercito(m,nome_e[0]) == ():
            # ganha o segundo exercito
            return(nome_e[1])
        # se o segundo exercito nao tem unidades
        elif obter_unidades_exercito(m,nome_e[1]) == ():
            # ganha o primeiro
            return(nome_e[0])
        else:
            return 'EMPATE'