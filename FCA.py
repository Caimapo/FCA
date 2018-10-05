import itertools
import numpy
import pandas

def powerset(X):
    pset = set()
    for r in range(len(X)+1):
        nset = itertools.chain(itertools.combinations(X,r))
        pset = itertools.chain(pset,nset)
    return pset

def A_prime(g,G,M,I):
    '''A subconjunto de objetos'''
    '''A' subconjunto de atributos'''
    ''' A' : {m \in M / \forall g \in A, (g,m)\in I}'''
    if len(g)==0:
        return set(M)
    s = set()
    for name, values in I.loc[g].iteritems():
        #print('{name}: {value}\n'.format(name=name, value=values))
        if (all(values)):
            #print('Columna: {name}'.format(name=name))
            s.add(name)
    # print(pandas.DataFrame.multiply(df.loc[g],axis=0))
    # set(s1).intersection(set(s2))
    return s

def B_prime(m,G,M,I):
    '''B subconjunto de atributos'''
    '''B' subconjunto de objetos'''
    ''' A' : {g \in G / \forall m \in B, (g,m)\in I}'''
    if len(m)==0:
        return set(G)
    s = set()
    for name, values in I.loc[:,m].iterrows():
        #print('{name}: {value}\n'.format(name=name, value=values))
        if (all(values)):
            #print('Columna: {name}'.format(name=name))
            s.add(name)
    return s

if __name__ == '__main__':
    '''Se calcula el mapa A = A' '''
    M = ['I','II','V','X']
    G = [1,2,5,10]
    I = numpy.matrix([[1,1,1,1],
                     [0,1,0,1],
                     [0,0,1,1],
                     [0,0,0,1]])

    df = pandas.DataFrame(I,G,M)
    #print([x for x in powerset(G)])
    '''
    #intento de a'
    g = {1,5}
    m = {'A','D'}
    #for g_ in g:
    print(df.loc[g])
    #print(df.loc[:,m])
    for name, values in df.loc[g].iteritems():
        print('{name}: {value}\n'.format(name=name,value=values))
        if(all(values)):
            print('Columna: {name}'.format(name=name))
    #print(pandas.DataFrame.multiply(df.loc[g],axis=0))
    #set(s1).intersection(set(s2))

    m = {'A', 'D'}
    print(df.loc[:, m])
    print(B_prime(m,G,M,df))
    
'''

    '''calcula A' = B y B'=A para todo el mapa'''
    fc = []
    for elem in powerset(G):
        m = A_prime(set(elem),G,M,df)
        #print('A: {}, A": {}'.format(set(elem),sorted(m)))
        if B_prime(m,G,M,df) == set(elem):
            fc.append((elem,m))

    [print(c) for c in fc]