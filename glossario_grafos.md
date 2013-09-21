# Glossário de Teoria dos Grafos

## Definições

- <a id="graph" />[grafo](#graph)

  Um par ordenado G = (V(G), E(G)), onde V(G) e E(G) são conjuntos disjuntos, V(G) um conjunto de vértices, E(G) um conjunto de arestas juntamente com uma função de incidência ψ<sub>G</sub> que a associa cada aresta de G um par não ordenado de vértices de G.
  
  ψ(e) = {u, v}, se a aresta *e* **liga** os vértices *u* e *v* - *u* e *v* são **extremos** de *e*.

- <a id="incidencia" />[incidência](#incidencia)

  Os extremos de uma aresta **incidem** na aresta e a aresta **incide** em seus extremos.
  
- <a id="adjacencia" />[adjacência](#adjacencia)

  Dois vértices são **adjacentes** se [incidem](#incidencia) numa mesma aresta.
  
  Duas arestas são **adjacentes** se  [incidem](#incidencia) num mesmo vértice.
  
- <a id="vizinhanca" />[vizinhança](#vizinhanca)

  Dois vértices distintos [adjacentes](#adjacencia) são chamados de **vizinhos**.
  
  N<sub>G</sub>(v) é o conjunto de vizinhos do vértice *v*.
  
- <a id="finito" />[finito](#finito)

  Grafo onde ambos V(G) e E(G) são finitos.
  
- <a id="ordem" />[ordem](#ordem)

  De um grafo G, é o seu número de vértices. Denotado por: v(G), |V(G)| ou *n* (simplificado).

- <a id="tamanho" />[tamanho](#tamanho)

  De um grafo G, é o seu número de arestas. Denotado por: e(G), |E(G)| ou *m* (simplificado).
  
- <a id="loop" />[laço](#loop)

  Aresta com extremos idênticos.
  
- <a id="links" />[ligações](#links)

  Aresta com extremos distintos.

- <a id="parallel" />[arestas paralelas](#parallel)

  Duas ou mais [ligações](#links) de um mesmo par de vértices.

- <a id="simples" />[grafo simples](#simples)

  Grafo que não tem [laços](#links) nem [arestas paralelas](#parallel).

- <a id="completo" />[grafo completo](#gcompleto)

  Grafo simples em que todo par de vértices é adjacente. Denotado por K<sub>n</sub>.

- <a id="caminho" />[caminho](#caminho)

  Grafo simples cujos vértices podem ser listados numa sequeência linear, tal que dois vértices são adjacentes se, e só se, são consecutivos na sequência. Denotado por P<sub>n</sub>.
  
- <a id="ciclo" />[ciclo](#ciclo)

  Grafo simples com três ou mais vértices, cujos vértices podem ser listados numa sequência cíclica tal que dois vértices são adjacentes se, e só se, são consecutivos na sequência. Denotado por C<sub>n</sub>.

  C<sub>1</sub> é um vértice com um laço.

  C<sub>2</sub> é um par de vértices ligados por um par de arestas paralelas.
  
- <a id="length" />[comprimento](#length) (de um caminho ou de um ciclo)

  Número de arestas no caminho/ciclo.

    k-caminho/k-ciclo é o caminho/cilco de comprimento k.

    3-ciclo também é chamado de triângulo, assim como o 4-ciclo de quadrilátero e assim por diante.
  
  Teorema: Seja G um grafo tal que [δ(G)](#degree) ≥ 2. Então G contém um ciclo.
    
- <a id="conexo" />[grafo conexo](#conexo)

  Grafo em que toda partição de V em dois conjuntos não vazios X e Y, existe uma aresta com um extremo em X e o outro em Y.

  O grafo é *desconexo- se é possível achar uma partição de V em dois conjuntos não vazios X e Y, em que não há arestas com um extremo em X e outro em Y.
  
- <a id="disjunto" />[grafos disjuntos](#disjunto)

  Dois grafos que não têm vértices em comum.

  Ver [grafos aresta-disjuntos](#adisjunto).
  
- <a id="adisjuto" />[grafos aresta-disjuntos](#adisjunto)

  Dois grafos que não têm arestas em comum.

  Ver [grafos disjuntos](#disjunto).

- <a id="union" />[união](#union)

  De dois grafos simples G e H, denotada G ∪ H tem como vétices V(G) ∪ V(H) e arestas E(G) ∪ E (H).

- <a id="componente" />[componente conexo](#componente)

  Cada grafo resultante da união disjunta de um ou mais grafos.
  
  c(G) é o número de componentes conexas de um grafo. 
  
- <a id="intersection" />[interseção](#intersection)

  De dois grafos simples G e H, denotada G ∩  H tem como vétices V(G) ∩ V(H) e arestas E(G) ∩ E (H).

- <a id="null" />[grafo nulo](#null)

  Grafo sem vértices.
  
- <a id="bipartido" />[grafo bipartido](#bipartido)

  Grafo cujo conjunto de vértices V pode ser particionado em dois conjuntos X e Y tais que cada aresta de G tem um extremo em X e o outro em Y. (X, Y) é uma *bipartição- do grafo G[X, Y] e X e Y são suas *partes*.
  
  Se G[X, Y] é simples e todo vértice em X é adjacente a todo vértice em Y, G[X, Y] é *bipartido completo*.
  
  K<sub>x,y</sub> é o grafo bipartido completo em que x = |X| e y = |Y|.
  
  K<sub>1,y</sub> ou K<sub>x,1</sub> é chamado *estrela*. 
  
  Teorema: Um grafo é bipartido se e somente se não tem ciclo ımpar.
  
- <a id="grau" />[grau](#grau) (de um vértice)

  Número de arestas incidentes em v, cada laço contado duas vezes. Denotado por d<sub>G(v)</sub>.
  
  Um vértice de grau zero é chamado **vértice isolado**.
  
  Grau **mínimo** de G é o grau do vértice de menor grau de G, denotado por δ(G). Grau **máximo** é o grau do vértice de maior grau de G, denotado por ∆(G).
  
- <a id="regular" />[grafo regular](#regular)

  Grafo k-regular, onde d(v) = k para todo v em V, para algum valor de k.
  
  Grafos 3-regulares são chamados *grafos cúbicos*.
  
- <a id="digraph" />[grafo direcionado](#digraph)

  Grafo D formado por um conjunto de vértices V e outro de arcos A, além de uma função de incidência que associa cada arco de A com um par **ordenado** de vértices.
  
  Se ψ<sub>D</sub>(a) = uv, dizemos que *a* liga *u* a *v*; ou *u* **domina** *v*. *u* é sua **origem** (*tail*) e *v* o **destino** (*head*)
  
  Vértices que dominam *v* são chamados **vizinhos de entrada**, N<sub>D</sub><sup>-</sup>(v). Vértices dominados por *v* são chamados **vizinhos de saída**, N<sub>D</sub><sup>+</sup>(v).
  
  Grafos direcionados *estritos*, são aqueles que não possuem laços nem arcos paralelos.

- <a id="orientacao" />[orientação](#orientacao)

  Grafo D resultante da substituição das arestas de um grafo G por arcos correspondentes.
  
- <a id="orientado" />[grafo orientado](#orientado)

  [Orientação](#orientacao) de um grafo simples. 

- <a id="odeg" />[ordem](#odeg) (de um grafo)

  Número de vértices de um grafo.
 
- <a id="tdeg" />[tamanho](#tdeg) (de um grafo)

  Número arestas de um grafo.
  
- <a id="torneio" />[torneio](#torneio)

  Qualquer [orientação](#orientacao) de um grafo completo.

## Isomorfismo

- <a id="isomorfism" />[isomorfismo](#isomorfismo)

  Função que mapeia os vértices e aresta de dois grafos que têm a mesma estrutura, diferindo apenas nos rótulos dos vértices e das arestas.

- <a id="complemento" />[complemento](#complemento)

  Grafo simples G' cujo conjunto de vértices é V e o conjunto de arestas é dado pelos pares de vértices não adjacentes em G.

- <a id="autocomplementar" />[autocomplementar](#autocomplementar)

  Grafo isomorfo ao seu complemento.

- <a id="automorfism" />[automorfismo](#automorfism)

  [Isomorfismo](#isomorfos) do grafo consigo mesmo.

  Aut(G) conjunto de automorfismos de G.

- <a id="similarity" />[similaridade](#similarity)

  Dois vértices u e v de um grafo simples são similares se existe [automorfismo](#automorfism) que mapeia u em v.

  Duas arestas uv e xy são similares se existe [automorfismo](#automorfism) que mapeia uv em xy.

- <a id="vtransitivo" />[grafo vértice-transitivo](#vtransitivo)

  Grafo em que todo par de vértices é [similar](#similarity).

- <a id="atransitivo" />[grafo aresta-transitivo](#atransitivo)

  Grafo em que todo par de vértices é [similar](#similarity)

## Subgrafos

- <a id="remocoes" />[remoções](#remocoes)

  Remoção de uma **aresta** *e* de um grafo G resulta no grafo denotado G \ e.
  
  Remoção de um **vértice** *v* de um grafo G resulta no grafo denotado G − v.

- <a id="subgraph" />[subgrafo](#subgraph)

  Um grafo F é subgrafo de G se V(F) ⊆ V(G), E(F) ⊆ E(G) e ψ<sub>F</sub> é a restrição de ψ<sub>G</sub> a E(F).

  G contém F e F está contido em G, denotado G ⊇ F e F ⊆ G respectivamente.

  F pode ser obtido a partir de operações de [remoção de vértices e arestas](#remocoes).
  
- <a id="supgraph" />[supergrafo](#supgraph)

  Um grafo H é supergrafo de G se contém G, H ⊇ G.
  
  Todo grafo é supergrafo de si mesmo.

- <a id="proprio" />[subgrafo ou supergrafo próprio](#proprio)

  Subgrafos F e supergrafos H de G, denotados por F ⊂ G e G ⊃ H, respectivamente.
  
- <a id="spanningsubgraph" />[subgrafo gerador](#spanningsubgraph)

  Subgrafo F obtido a partir de um grafo G pela remoção de **arestas**.
  
  Se S é o conjunto de arestas removidas F é o grafo G \ S. 
  
  V(F) = V(G).
  
- <a id="hamiltoniano" />[hamiltoniano](#hamiltoniano)

  Um *caminho hamiltoniano* - ou *ciclo hamiltoniano* - é aquele que é gerador de um dado grafo. 
  
  O grafo hamiltoniano possui um ciclo hamiltoniano.
  
  Teorema de Rédei: Todo [torneio](#torneio) tem um caminho hamiltoniano direcionado.
  
  ### Problema do Caixeiro Viajante
  
    Dado um grafo ponderado (G , w ), encontre um ciclo hamiltoniano de G de peso mínimo.
  
- <a id="kfactor" />[k-fator](#kfactor)

  Subgrafo gerador k-regular. 1-fator também é chamado *emparelhamento perfeito*.

- <a id="inducedsubgraph" />[subgrafo induzido](#inducedsubgraph)

  Subgrafo induzido/gerado F obtido a partir de G pela remoção de **vértices**.
  
  Toda aresta de E(G) com ambos os extremos em V(F) também é aresta de E(F).

  Se X é o conjunto de vértices removidos F é o grafo G − X.
  
- <a id="ponderado" />[grafo ponderado](#ponderado)

  Grafo no qual cada aresta tem um número real denominado *peso- w(e) associado à ela.
  
- <a id="peso" />[peso](#peso)

  De um grafo G, d(G), é a somatória dos pesos de suas arestas.
  
  De uma aresta é o número real associado à ela.

- <a id="identificacao" />[identificação](#identificacao)

  Operação de substituição de dois vértices - *x* e *y* - por um único vértice incidente em todas as arestas em que *x* e *y* incidiam. O grafo resultante é denotado por G/{x, y}.
  
- <a id="contracao" />[contração](#contracao)

  Operação de remoção de uma aresta *e* seguida da [contração](#contracao) de seus extremos. O grafo resultante é denotado por G/e.
  
- <a id="decomposicao" />[decomposição](#decomposicao)

  Família de subgrafos aresta-disjuntos de G tais que a união do conjunto de arestas de cada subgrafo da família resulta no conjnto de arestas do grafo original G.

- <a id="even" />[grafo par](#even)

  Grafo em que todo vértice tem [grau](#degree) par.
  
  Teorema de Veblen: Um grafo admite uma decomposição em ciclos se e somente se é par.

  Teorema: Um grafo é par se e somente se [|∂(X)|](#cut) é par para todo subconjunto X de V.

- <a id="cobertura" />[cobertura](#cobertura)

  Família de subgrafos **não necessariamente*- aresta-disjuntos de G tais que a união do conjunto de arestas de cada subgrafo da família resulta no conjnto de arestas do grafo original G.
  
  É chamada *uniforme- se cobre cada aresta de G o mesmo número de vezes. Se k é o número de vezes, a cobertura é denominada *k-cobertura*.

- <a id="cut" />[corte](#cut)	

  Seja E[X, Y] o conjunto de arestas de G com um extremo em X e o outro em Y.
  
  Quando Y = V − X, E[X, Y] ́é chamado de corte (*cut*) de X em G e denotado por ∂(X).
  
  Um corte ∂(X) **respeita** um conjunto de arestas A se A ∩ ∂(X) = ⦰.

- <a id="lightedge" />[aresta leve](#lightedge)

  Em um corte ∂(S) se w<sub>uv</sub> := min<sub>(x,y) ∊ ∂(S)</sub>{w<sub>xy</sub>} - (u,v) é a aresta de menor peso no corte ∂(S).

- <a id="trivialcut" />[corte trivial](#trivialcut)

  É dado por todas as arestas incidentes em v e denotado por ∂(v).
 
## Conexidade

- <a id="walk" />[passeio](#walk)

  Sequência W = v<sub>0</sub> e<sub>1</sub> v<sub>1</sub> ... e<sub>l</sub> v<sub>l</sub> cujos elementos são vértices e arestas **não necessariamente*- distintos, tal que para todo 1 ≤ i ≤ l, v<sub>i-1</sub> e v<sub>i</sub> são extremos de e.

  Se v<sub>0</sub> = x e v<sub>l</sub> = y, W conecta x a y e é um *passeio* de x a y.

  Qualquer subsequência com vértice de *início* u e vértice de *término* v é chamada *segmento- de W e denotada por uWv.

  Um passeio é *fechado* (*closed*) se os vértices de início e término coincidem.

- <a id="trail" />[trilha](#trail)

  [Passeio](#walk) em que não existe repetiçào de arestas.

- <a id="path" />[caminho](#path)

  [Passeio](#walk) em que não existe repetição de vértices, nem arestas.

- <a id="conexity" />[conexidade](#conexity)

  Dois vértices u e v estão conectados se existe um passeio de u a v no grafo.

  O grafo é conexo se todo par de vértices está conectado.

- <a id="distance" />[distância](#distance)

  Comprimento do menor [caminho](#path) de u a v em G, denotado por d<sub>G(u, v)</sub>.

- <a id="cutedge" />[aresta de corte](#cutedge)

  Aresta *e- que quando removida aumenta o número de componentes conexas de G, ou seja, c(G \ e) = c(G) + 1.
  
  Preposição: Uma aresta e de um grafo G é uma aresta de corte se e somente se e não pertence a um ciclo de G.

- <a id="euleriantrail" />[trilha euleriana](#euleriantrail)

  [Trilha](#trail) que passa por cada aresta do grafo exatamente uma vez.

- <a id="euleriancirc" />[circuito euleriano](#euleriancirc)

  [Trilha Euleriana](#euleriantrail) fechada.

- <a id="eulerian" />[grafo euleriano](#eulerian)

  Grafo conexo e que possui um [circuito Euleriano](#euleriancirc).
  
  Teorema: Um grafo conexo é euleriano se e somente se é par.

## Árvores

- <a id="tree" />[árvore](#tree)

  Grafo T conexo e acíclico.
  
  Preposição: Em uma árvore, quaisquer dois vértices são conectados por precisamente um caminho.
  
  Teorema: Se T é uma árvore, então e(T) = v (T) − 1.
  
- <a id="forest" />[floresta](#forest)

  Grafo acíclico não necessariamente conexo.

- <a id="leaf" />[folha](#folha)

  Vértice de grau um em uma árvore.

  Preposição: Toda árvore nào trivial tem pelo menos duas folhas.

- <a id="spanningtree" />[árvore geradora](#spanningtree)

  Árvore subgrafo gerador de um grafo.
  
  Teorema: Um grafo é conexo se e somente se tem uma árvore geradora.

- <a id="rootedtree" />[áarrvore com raiz](#rootedtree)

  Árvore com um vértice x chamado de *raiz*, denotado por T(x).

- <a id="branching" />[arborescência](#branching)

  [Orientação](#orientacao) de uma árvore com raiz em que todo vértice exceto a raiz tem grau de entrada 1.

## Buscas em Grafos

- <a id="reach" />[alcance](#reach)

  Um vértice *u* é **alcançável** a partir de um vértice *v* de um grafo G se existe um [caminho](#path) de *v* para *u* em G.

- <a id="distance" />[distância](#distance)

  Um vértice *u* está a uma **distância** *k* de um vértice *v* se *k* é o comprimento do menor [caminho](#path) que começa em *v* e termina em *u*.
  
  Se *u* **não é alcançável** a partir de *v*, determina-se que a distância entre eles é **infinita**.

- <a id="bsf" />[busca em largura](#bfs)

   Busca em largura ou BFS (*Breadth First Search*) em um grafo G = (V, E).
   
   Método em que, partindo-se de um vértice especial *u*, denominado raiz da busca, percorre-se G visitando todos os vértices alcançáveis a partir de *u* em **ordem crescente de distância**.
   
  Complexidade: O(|V| + |E|)

- <a id="dfs" />[busca em profundidade](#dfs)

   Busca em profundidade ou DFS (*Depth First Search*) em um grafo G = (V, E).
   
   Método em que, partindo-se de um vértice especial *u*, denominado raiz da busca, percorre-se G visitando todos os vértices alcançáveis a partir de *u* tendo como meta atingir primeiramente as folhas, retornando quando isso acontecer. Generalização do percurso em **pré-ordem**.
   
   <a id="timestamps" />Variáveis podem ser usadas para a marcação de `tempo` como instante de descoberta `d` e de exploração `f`.
   
   Complexidade: O(|V| + |E|)
   
   **Classificação de arestas**
   
   Dada uma floresta G<sub>pred</sub> construída pela [DFS](#dfs):

  + <a id="forest_edge" />[aresta da floresta](#forest_edge)

     Toda aresta em G<sub>pred</sub>.

  + <a id="back_edge" />[aresta de retorno](#back_edge)

     É uma aresta (u, v) onde *v* é **ancestral** de *u* em G<sub>pred</sub>.
     
  + <a id="forward_edge" />[aresta direta](#forward_edge)

     É uma aresta (u, v) que não está em G<sub>pred</sub> onde *v* é descendente de *u* em uma árvore contruída pela DFS.

  + <a id="cross_edge" />[aresta cruzada](#cross_edge)

     Todas as arestas que não podem ser classificadas como [de retorno](#back_edge) ou [diretas](#forward_edge).

  Teorema: Em uma DFS de um grafo **não direcionado** G = (V, E) toda aresta é da árvore ou é de retorno.

## Ordenação Topológica

- <a id="topsort" />[ordenação topológica](#topsort)

    Em um [grafo direcionado acíclico](#dag) G = (V, E), é uma ordem linear dos vértices tal que, para todo arco (u, v) em E, *u* _antecede_ *v* na ordem.
  
  Lema: Um grafo direcionado G é acíclico *se e somente se* uma bisca em peofundidade em G não classifica nenhum arco como sendo de retorno.
  
  Teorema: Rotular os vértices do grafo em ordem decrescente dos valores [f](#timestamps) obtidos em uma DFS resulta em uma ordenação topológica correta de um grafo direcionado acíclico G.

## Componentes Fortemente Conexas

- <a id="cfc" />[componentes fortemente conexas](#cfc)

  Uma componente fortemente conexa (CFC) *H* de um grafo *G = (V, E)* é um subconjunto de vértices tal que, para todo par de vértices *u* e *v* de *H*, existe um [caminho](#path) de *u* para *v* e vice-versa. *H* também é **maximal** com relação a inclusão de vértices.

- <a id="transposed" />[grafo transposto](#transposed)

  É o grafo G<sup>T</sup> = (V, E<sup>T</sup>) de um grafo direcionado G = (V, E) onde:
  
       E<sup>T</sup> = {(u, v) ∊ V x V: (v, u) ∊ E}
  
  o grafo obtido invertendo-se a orientação de seus arcos.

  + G e G<sup>T</sup> têm as mesmas componentes fortemente conexas.

## Árvore Geradora Mínima

- <a id="agm" />[árvore geradora mínima](#agm)

  Árvore gerada pelo problema da Árvore Geradora Mínima:

  Dado um grafo não orientado ponderado G = (V, E), onde w: E → &#x211D;<sup>+</sup> define os custos das arestas, encontrar um subgrafo gerador conexo T de G tal que, para todo subgrafo gerador conexo T'de G

      &sum;<sub>e ∊ T</sub> w<sub>e</sub> ≤ &sum;<sub>e ∊ T'</sub> w<sub>e</sub>.

  **Características**

  + Só tem solução se G é conexo.
  + Resulta em uma árvore - a *Árvore Geradora Mínima* (AGM) - dado que tal subgrafo não conterá ciclos.

  **Algoritmos**
  
  - Algoritmo genérico: estratégia gulosa.
  
      **Invariante**: Antes de cada iteração A é um subconjunto de arestas de uma AGM.
      A cada iteração A ∪ {(u, v)}, (u, v) é chamada aresta **segura**.
      
      AGM-Generico(G, w)
      
              A ← 0;
              enquanto A não forma uma árvore geradora faça
                  encontre aresta segura (u, v);
                  A ← A ∪ {(u, v)};
              retorne A.

  Teorema: Seja G = (V, E) um grafo conexo não orientado ponderado nas arestas por uma função w: E → &#x211D;. Seja A um subconjunto de E que está contido em alguma AGM de G, seja ainda ∂(S) um [corte](#cut) de G que respeita A e (u, v) uma [aresta leve](#lightedge) de ∂(S). Então, (u, v) é uma **aresta segura** para A.
  
  <a id="corollary23_2" />Corolário: Seja G = (V, E) um grafo conexo não orientado ponderado nas arestas por uma função w: E → &#x211D;<sup>+</sup>. Seja A um subconjunto de E que está contido em alguma AGM de G, e seja C = (V<sub>C</sub>, E<sub>C</sub>) uma componente conexa (árvore) da floresta G<sub>A</sub> = (V, A). Se (u, v) uma [aresta leve](#lightedge) de ∂(C), então (u, v) é **segura** para A.
  
  Os algoritmos de [Prim](#prim) e de [Kruskal](#kruskal) especializam o algoritmo genérico usando o Colorário.

- <a id="prim" />[Prim](#prim)

    Dado o [colorário](#corollary23_2).
  
    A é sempre uma [árvore](#tree). A **aresta segura** adicionada a A é sempre uma [aresta leve](#lightedge) do corte ∂(C), onde C é o conjunto de vértices que sÃo extremidades de arestas em A.
  
- <a id="kruskal" />[Kruskal](#kruskal)

    Dado o [colorário](#corollary23_2).
  
    A é sempre uma [floresta](#forest). A **aresta segura** adicionada a A é sempre uma aresta de menor peso dentre todas as arestas ligando dois vértices de componentes distintas de G<sub>A</sub>.

## Caminhos Mínimos

- <a id="minpath" />[caminhos mínimos](#minpath)

  [Caminhos](#path) que se deseja encontrar no problema de Caminhos Mínimos:

  Dados um grafo conexo ponderado G = (V, E), direcionado ou não, onde d: E → &#x211D;<sup>+</sup> define as distâncias entre os extremos das arestas, e um vértice *r* de G, queremos encontrar, para todo vértice *u* de G um caminho C de distância mínima de *r* a *u*, ou seja, o caminho C deve ser tal que, para todo caminho C de *r* a *u* em G :

    &sum;<sub>e ∊ C</sub> d<sub>e</sub> ≤ &sum;<sub>e ∊ C'</sub> d<sub>e</sub>.

  **Algoritmos**
  
  - [Dijkstra](#dijkstra)
  
    Grafos direcionados ou não direcionados sem arestas de peso negativo.
  
  - [Bellman-Ford](#bellman_ford)
  
    Grafos direcionados com arestas de peso negativo e sem ciclos negativos.
  
  - [Ordenação topológica](#topsort)
  
    Para [DAGs](#dag), basta calcular os caminhos mínimos analisando os vértices segundo a ordenação topológica. Funciona mesmo com arestas de peso negativo.
    
  **Caminhos mínimos entre todos os pares de vértices**
  
  - [Dijkstra](#dijkstra)
  
    Entre todos os vértices quando o grafo é esparso.
  
  - [Floyd-Warshall](#floyd_warshall)
  
    Quando o grafo é denso.
    
- <a id="dijkstra" />[Dijkstra](#dijkstra)

  Algoritmo para encontrar [caminhos mínimos](#minpath) a partir de um vértice *r*. Resulta numa [árvore geradora](#spanningtree) com raiz em *r* - árvore de caminhos mínimos para *r*: ACM(r).
  
  **Características**
  
  + Funciona para grafos direcionados e não direcionados desde que não haja arestas de peso negativo.
  
  Ver [Algoritmo de Prim](#prim).

- <a id="bellman_ford" />[Bellman-Ford](#bellman_ford)

  Algoritmo para encontrar [caminhos mínimos](#minpath) a partir de um vértice *r*.
  
  **Características**
  
  + Funciona para grafos direcionados não haja ciclos negativos.
  + Detecta a existência de ciclos negativos.

- <a id="floyd_warshall" />[Floyd-Warshall](#floyd_warshall)

  Algoritmo para encontrar [caminhos mínimos](#minpath) entre todos os pares de vértices de um grafo.
  
  **Características**

  + Usado quando o grafo é denso
  + Funciona mesmo na presença de arestas de peso negativo, desde que não haja ciclos negativos
  + É possível detectar a existência de ciclo negativo analisando a matriz resultado do algoritmo.
