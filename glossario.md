# Glossário de Teoria dos Grafos

## Definições

* <a id="simples" />[grafo simples](#simples)

  Grafo que não tem laços nem arestas paralelas.

* <a id="completo" />[grafo completo](#gcompleto)

  Grafo simples em que todo par de vértices é adjacente. Denotado por K_n.

* <a id="caminho" />[caminho](#caminho)

  Grafo simples cujos vértices podem ser listados numa sequeência linear, tal que dois vértices são adjacentes se, e só se, são consecutivos na sequência. Denotado por P_n.
  
* <a id="ciclo" />[ciclo](#ciclo)

  Grafo simples com três ou mais vértices, cujos vértices podem ser listados numa sequência cíclica tal que dois vértices são adjacentes se, e só se, são consecutivos na sequência. Denotado por C_n.

  C_1 é um vértice com um laço.

  C_2 é um par de vértices ligados por um par de arestas paralelas.
  
* <a id="length" />[comprimento](#length) (de um caminho ou de um ciclo)

  Número de arestas no caminho/ciclo.

    k-caminho/k-ciclo é o caminho/cilco de comprimento k.

    3-ciclo também é chamado de triângulo, assim como o 4-ciclo de quadrilátero e assim por diante.
    
* <a id="conexo" />[grafo conexo](#conexo)

  Grafo em que toda partição de V em dois conjuntos não vazios X e Y, existe uma aresta com um extremo em X e o outro em Y.

  O grafo é *desconexo* se é possível achar uma partição de V em dois conjuntos não vazios X e Y, em que não há arestas com um extremo em X e outro em Y.
  
* <a id="disjunto" />[grafos disjuntos](#disjunto)

  Dois grafos que não têm vértices em comum.

  Ver [grafos aresta-disjuntos](#adisjunto).
  
* <a id="adisjuto" />[grafos aresta-disjuntos](#adisjunto)

  Dois grafos que não têm arestas em comum.

  Ver [grafos disjuntos](#disjunto).

* <a id="componente" />[componente conexa](#componente)

  Cada grafo da união disjunta de um ou mais grafos.
  
  c(G) é o número de componentes conexas de um grafo. 
  
* <a id="bipartido" />[grafo bipartido](#bipartido)

  Grafo cujo conjunto de vértices V pode ser particionado em dois conjuntos X e Y tais que cada aresta de G tem um extremo em X e o outro em Y. (X, Y) é uma *bipartição* do grafo G[X, Y] e X e Y são suas *partes*.
  
  Se G[X, Y] é simples e todo vértice em X é adjacente a todo vértice em Y, G[X, Y] é *bipartido completo*.
  
  K_x,y é o grafo bipartido completo em que x = |X| e y = |Y|.
  
  K_1,y ou K_x,1 é chamado *estrela*. 
  
* <a id="grau" />[grau](#grau) (de um vértice)

  Número de arestas incidentes em v, cada laço contado duas vezes. Denotado por d_G(v).
  
  Grau mínimo de G é o grau do vértice de menor grau de G. Grau máximo é o grau do vértice de maior grau de G.
  
* <a id="regular" />[grafo regular](#regular)

  Grafo k-regular, onde d(v) = k para todo v em V, para algum valor de k.
  
  Grafos 3-regulares são chamados *grafos cúbicos*.
  
* <a id="digraph" />[grafo direcionado](#digraph)

  Grafo D formado por um conjunto de vértices V e outro de arcos A, além de uma função de incidência que associa cada arco de A com um par **ordenado** de vértices.
  
  Grafos direcionados *estritos*, são aqueles que não possuem laços nem arcos paralelos.
  
* <a id="orientado" />[grafo orientado](#orientado)

  Orientação de um grafo simples. D é uma *orientação* de G se é obtido a partir de G pela substituição das arestas por arcos correspondentes.

* <a id="odeg" />[ordem](#odeg) (de um grafo)

  Número de vértices de um grafo.
 
* <a id="tdeg" />[tamanho](#tdeg) (de um grafo)

  Número arestas de um grafo.
  
* <a id="torneio" />[torneio](#torneio)

  Qualquer orientação de um grafo completo.
  
  Ver [grafo orientado](#orientado).

## Isomorfismo

* <a id="isomorfism" />[isomorfismo](#isomorfismo)

  Função que mapeia os vértices e aresta de dois grafos que têm a mesma estrutura, diferindo apenas nos rótulos dos vértices e das arestas.

* <a id="complemento" />[complemento](#complemento)

  Grafo simples G' cujo conjunto de vértices é V e o conjunto de arestas é dado pelos pares de vértices não adjacentes em G.

* <a id="autocomplementar" />[autocomplementar](#autocomplementar)

  Grafo isomorfo ao seu complemento.

* <a id="automorfism" />[automorfismo](#automorfism)

  [Isomorfismo](#isomorfos) do grafo consigo mesmo.

  Aut(G) conjunto de automorfismos de G.

* <a id="similarity" />[similaridade](#similarity)

  Dois vértices u e v de um grafo simples são similares se existe [automorfismo](#automorfism) que mapeia u em v.

  Duas arestas uv e xy são similares se existe [automorfismo](#automorfism) que mapeia uv em xy.

* <a id="vtransitivo" />[grafo vértice-transitivo](#vtransitivo)

  Grafo em que todo par de vértices é [similar](#similarity).

* <a id="atransitivo" />[grafo aresta-transitivo](#atransitivo)

  Grafo em que todo par de vértices é [similar](#similarity)

## Subgrafos

* <a id="spanningsubgraph" />[subgrafo gerador](#spanningsubgraph)

  Subgrafo F obtido a partir de um grafo G pela remoção de **arestas**.
  
  Se S é o conjunto de arestas removidas F é o grafo G \ S. 
  
  V(F) = V(G).
  
* <a id="hamiltoniano" />[hamiltoniano](#hamiltoniano)

  Um *caminho hamiltoniano* ou *ciclo hamiltoniano* é aquele que é gerador de um dado grafo. 
  
  O grafo hamiltoniano possui um ciclo hamiltoniano.
  
* <a id="kfactor" />[k-fator](#kfactor)

  Subgrafo gerador k-regular. 1-fator também é chamado *emparelhamento perfeito*.

* <a id="inducedsubgraph" />[subgrafo induzido](#inducedsubgraph)

  Subgrafo induzido/gerado F obtido a partir de G pela remoção de **vértices**.
  
  Toda aresta de E(G) com ambos os extremos em V(F) também é aresta de E(F).

  Se X é o conjunto de vértices removidos F é o grafo G − X.
  
* <a id="ponderado" />[grafo ponderado](#ponderado)

  Grafo no qual cada aresta tem um número real denominado *peso* w(e) associado à ela.
  
* <a id="peso" />[peso](#peso)

  De um grafo G, d(G), é a somatória dos pesos de suas arestas.
  
  De uma aresta é o número real associado à ela.

* <a id="identificacao" />[identificação](#identificacao)

  Operação de substituição de **dois vértices** *x* e *y* por um único vértice incidente em todas as arestas em que *x* e *y* incidiam. O grafo resultante é denotado por G/{x, y}.
  
* <a id="contracao" />[contração](#contracao)

  Operação de remoção de **uma aresta** *e* seguida da [contração](#contracao) de seus extremos. O grafo resultante é denotado por G/e.
  
* <a id="decomposicao" />[decomposição](#decomposicao)

  Família de subgrafos aresta-disjuntos de G tais que a união do conjunto de arestas de cada subgrafo da família resulta no conjnto de arestas do grafo original G.
  
* <a id="cobertura" />[cobertura](#cobertura)

  Família de subgrafos **não necessariamente** aresta-disjuntos de G tais que a união do conjunto de arestas de cada subgrafo da família resulta no conjnto de arestas do grafo original G.
  
  É chamada *uniforme* se cobre cada aresta de G o mesmo número de vezes. Se k é o número de vezes, a cobertura é denominada *k-cobertura*.

* <a id="cut" />[corte](#cut)

  Seja E[X, Y] o conjunto de arestas de G com um extremo em X e o outro em Y.
  
  Quando Y = V − X, E[X , Y] ́é chamado de corte (*cut*) de X em G e denotado por ∂(X).

* <a id="trivialcut" />[corte trivial](#trivialcut)

  É dado por todas as arestas incidentes em v e denotado por ∂(v).
 
## Conexidade

* <a id="walk" />[passeio](#walk)

  Sequência W = v_0 e_1 v_1 ... e_l v_l cujos elementos são vértices e arestas **não necessariamente** distintos, tal que para todo 1 ≤ i ≤ l, v_i-1 e v_i são extremos de e.

  Se v_0 = x e v_l = y, W conecta x a y e é um *passeio* de x a y.

  Qualquer subsequência com vértice de *início* u e vértice de *término* v é chamada *segmento* de W e denotada por uWv.

  Um passeio é *fechado* (*closed*) se os vértices de início e término cincidem.

* <a id="trail" />[trilha](#trail)

  [Passeio](#walk) em que não existe repetiçào de arestas.

* <a id="path" />[caminho](#path)

  [Passeio](#walk) em que não existe repetição de vértices, nem arestas.

* <a id="conexity" />[conexidade](#conexity)

  Dois vértices u e v estão conectados se existe um passeio de u a v no grafo.

  O grafo é conexo se todo par de vértices está conectado.

* <a id="distance" />[distância](#distance)

  Comprimento do menor caminho de u a v em G, denotado por d_G(u, v).

* <a id="cutedge" />[aresta de corte](#cutedge)

  Aresta *e* que quando removida aumenta o número de componentes conexas de G, ou seja, c(G \ e) = c(G) + 1.

* <a id="euleriantrail" />[trilha euleriana](#euleriantrail)

  [Trilha](#trail) que passa por cada aresta do grafo exatamente uma vez.

* <a id="euleriancirc" />[circuito euleriano](#euleriancirc)

  [Trilha Euleriana](#euleriantrail) fechada.

* <a id="eulerian" />[grafo euleriano](#eulerian)

  Grafo conexo e que possui um [circuito Euleriano](#euleriancirc).

## Árvores

* <a id="tree" />[árvore](#tree)

  Grafo T conexo e acíclico.

* <a id="forest" />[floresta](#forest)

  Grafo acíclico não necessariamente conexo.

* <a id="spanningtree" />[árvore geradora](#spanningtree)

  Árvore subgrafo gerador de um grafo.

* <a id="rootedtree" />[árvore com raiz](#rootedtree)

  Árvore com um vértice x chamado de *raiz*, denotado por T(x).

* <a id="branching" />[arborescência](#branching)

  [Orientação](#orientacao) de uma árvore com raiz em que todo vértice exceto a raiz tem grau de entrada 1.

