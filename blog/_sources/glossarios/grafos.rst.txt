.. Glossário de Teoria dos Grafos

==============================
Glossário de Teoria dos Grafos
==============================

Definições
==========

.. _grafo:

grafo
-----

Um par ordenado G = (V(G), E(G)), onde V(G) e E(G) são conjuntos disjuntos,
V(G) um conjunto de vértices, E(G) um conjunto de arestas juntamente com uma
função de incidência ψ :sub:`G` que a associa cada aresta de G um par não
ordenado de vértices de G.

``ψ(e) = {u, v}``, se a aresta ``e`` **liga** os vértices ``u`` e ``v`` -
``u`` e ``v`` são **extremos** de ``e``.

.. _incidencia:

incidência
----------

Os extremos de uma aresta **incidem** na aresta e a aresta **incide** em seus
extremos.

.. _adjacencia:

adjacência
----------

Dois vértices são **adjacentes** se `incidem <incidencia_>`_ numa mesma aresta.

Duas arestas são **adjacentes** se  `incidem <incidencia_>`_ num mesmo vértice.

.. _vizinhanca:

vizinhança
----------

Dois vértices distintos `adjacentes <adjacencia_>`_ são chamados de
**vizinhos**.

N :sub:`G` (v) é o conjunto de vizinhos do vértice ``v``.

.. _finito:

finito
------

Grafo onde ambos V(G) e E(G) são finitos.

.. _ordem:

ordem
-----

De um grafo G, é o seu número de vértices. Denotado por: ``v(G)``, ``|V(G)|``
ou ``n`` (simplificado).

.. _tamanho:

tamanho
-------

De um grafo G, é o seu número de arestas. Denotado por: ``e(G)``, ``|E(G)|``
ou ``m`` (simplificado).

.. _loop:

laço
----

Aresta com extremos idênticos.

.. _links:

ligações
--------

Aresta com extremos distintos.

.. _parallel:

arestas paralelas
-----------------

Duas ou mais `ligações <links_>`_ de um mesmo par de vértices.

.. _simples:

grafo simples
-------------

Grafo que não tem `laços <links_>`_ nem `arestas paralelas <parallel_>`_.

.. _completo:

grafo completo
--------------

Grafo simples em que todo par de vértices é adjacente. Denotado por
K :sub:`n`.


.. _caminho:

caminho
-------

Grafo simples cujos vértices podem ser listados numa sequeência linear, tal
que dois vértices são adjacentes se, e só se, são consecutivos na sequência.
Denotado por P :sub:`n`.

.. _ciclo:

ciclo
-----

Grafo simples com três ou mais vértices, cujos vértices podem ser listados
numa sequência cíclica tal que dois vértices são adjacentes se, e só se, são
consecutivos na sequência. Denotado por C :sub:`n`.

C :sub:`1` é um vértice com um laço.

C :sub:`2` é um par de vértices ligados por um par de arestas paralelas.

.. _length:

comprimento (de um caminho ou de um ciclo)
------------------------------------------

Número de arestas no caminho/ciclo.

k-caminho/k-ciclo é o caminho/ciclo de comprimento k.

3-ciclo também é chamado de triângulo, assim como o 4-ciclo de quadrilátero e
assim por diante.

**Teorema:** Seja G um grafo tal que `δ(G) <degree_>`_ ≥ 2. Então G contém um
ciclo.

.. _conexo:

grafo conexo
------------

Grafo em que toda partição de V em dois conjuntos não vazios X e Y, existe uma
aresta com um extremo em X e o outro em Y.

O grafo é *desconexo* se é possível achar uma partição de V em dois conjuntos
não vazios X e Y, em que não há arestas com um extremo em X e outro em Y.

.. _disjunto:

grafos disjuntos
----------------

Dois grafos que não têm vértices em comum.

Ver `grafos aresta-disjuntos <adisjunto_>`_.

.. _adisjunto:

grafos aresta-disjuntos
-----------------------

Dois grafos que não têm arestas em comum.

Ver `grafos disjuntos <disjunto_>`_.

.. _union:

união
-----

De dois grafos simples G e H, denotada G ∪ H tem como vétices V(G) ∪ V(H) e
arestas E(G) ∪ E (H).

.. _componente:

componente conexo
-----------------

Cada grafo resultante da união disjunta de um ou mais grafos.

c(G) é o número de componentes conexas de um grafo. 

.. _intersection:

interseção
----------

De dois grafos simples G e H, denotada G ∩  H tem como vétices V(G) ∩ V(H) e
arestas E(G) ∩ E (H).

.. _null:

grafo nulo
----------

Grafo sem vértices.

.. _bipartido:

grafo bipartido
---------------

Grafo cujo conjunto de vértices V pode ser particionado em dois conjuntos X e
Y tais que cada aresta de G tem um extremo em X e o outro em Y. (X, Y) é uma
*bipartição* do grafo G[X, Y] e X e Y são suas *partes*.

Se G[X, Y] é simples e todo vértice em X é adjacente a todo vértice em Y, G[X,
Y] é *bipartido completo*.

K :sub:`x,y` é o grafo bipartido completo em que ``x = |X|`` e ``y = |Y|``.

K :sub:`1,y` ou K :sub:`x,1` é chamado *estrela*.

Teorema: Um grafo é bipartido se e somente se não tem ciclo ımpar.

.. _degree:

grau (de um vértice)
--------------------

Número de arestas incidentes em v, cada laço contado duas vezes. Denotado por
d :sub:`G(v)`.

Um vértice de grau zero é chamado **vértice isolado**.

Grau **mínimo** de G é o grau do vértice de menor grau de G, denotado por
δ(G). Grau **máximo** é o grau do vértice de maior grau de G, denotado por
∆(G).

.. _regular:

grafo regular
-------------

Grafo k-regular, onde d(v) = k para todo v em V, para algum valor de k.

Grafos 3-regulares são chamados *grafos cúbicos*.

.. _digraph:

grafo direcionado
-----------------

Grafo D formado por um conjunto de vértices V e outro de arcos A, além de uma
função de incidência que associa cada arco de A com um par **ordenado** de
vértices.

Se ψ :sub:`D`(a) = uv, dizemos que ``a`` liga ``u`` a ``v``; ou ``u``
**domina** ``v``. ``u`` é sua **origem** (*tail*) e ``v`` o **destino**
(*head*)

Vértices que dominam ``v`` são chamados **vizinhos de entrada**, N :sub:`D`
:sup:`-` (v). Vértices dominados por ``v`` são chamados **vizinhos de saída**,
N :sub:`D` :sup:`+` (v).

Grafos direcionados *estritos*, são aqueles que não possuem laços nem arcos
paralelos.

.. _dag:

grafo direcionado acíclico
--------------------------

Grafo `dirigido <digraph_>`_ sem ciclo; isto é, para qualquer vértice v, não
há nenhuma ligação dirigida começando e acabando em v.

.. _orientacao:

orientação
----------

Grafo D resultante da substituição das arestas de um grafo G por arcos correspondentes.

.. _orientado:

grafo orientado
---------------

`Orientação <orientacao_>`_ de um grafo simples. 

.. _odeg:

ordem (de um grafo)
-------------------

Número de vértices de um grafo.

.. _tdeg:

tamanho (de um grafo)
---------------------

Número arestas de um grafo.

.. _torneio:

torneio
-------

Qualquer `orientação <orientacao_>`_ de um grafo completo.

Isomorfismo
===========

.. _isomorfism:

isomorfismo
-----------

Função que mapeia os vértices e aresta de dois grafos que têm a mesma
estrutura, diferindo apenas nos rótulos dos vértices e das arestas.

.. _complemento:

complemento
-----------

Grafo simples G' cujo conjunto de vértices é V e o conjunto de arestas é dado
pelos pares de vértices não adjacentes em G.

.. _autocomplementar:

autocomplementar
----------------

Grafo isomorfo ao seu complemento.

.. _automorfism:

automorfismo
------------

`Isomorfismo <isomorfism_>`_ do grafo consigo mesmo.

Aut(G) conjunto de automorfismos de G.

.. _similarity:

similaridade
------------

Dois vértices u e v de um grafo simples são similares se existe `automorfismo
<automorfism_>`_ que mapeia u em v.

Duas arestas uv e xy são similares se existe `automorfismo <automorfism_>`_
que mapeia uv em xy.

.. _vtransitivo:

grafo vértice-transitivo
------------------------

Grafo em que todo par de vértices é `similar <similarity_>`_.

.. _atransitivo:

grafo aresta-transitivo
-----------------------

Grafo em que todo par de vértices é `similar <similarity_>`_

Subgrafos
=========

.. _remocoes:

remoções
--------

Remoção de uma **aresta** ``e`` de um grafo G resulta no grafo denotado G \ e.

Remoção de um **vértice** ``v`` de um grafo G resulta no grafo denotado G − v.

.. _subgraph:

subgrafo
--------

Um grafo F é subgrafo de G se V(F) ⊆ V(G), E(F) ⊆ E(G) e ψ :sub:`F` é a
restrição de ψ :sub:`G` a E(F).

G contém F e F está contido em G, denotado G ⊇ F e F ⊆ G respectivamente.

F pode ser obtido a partir de operações de `remoção de vértices e arestas
<remocoes_>`_.

.. _supgraph:

supergrafo
----------

Um grafo H é supergrafo de G se contém G, H ⊇ G.

Todo grafo é supergrafo de si mesmo.

.. _proprio:

subgrafo ou supergrafo próprio
------------------------------

Subgrafos F e supergrafos H de G, denotados por F ⊂ G e G ⊃ H, respectivamente.

.. _spanningsubgraph:

subgrafo gerador
----------------

Subgrafo F obtido a partir de um grafo G pela remoção de **arestas**.

Se S é o conjunto de arestas removidas F é o grafo G \ S. 

V(F) = V(G).

.. _hamiltoniano:

hamiltoniano
------------

Um *caminho hamiltoniano* - ou *ciclo hamiltoniano* - é aquele que é gerador
de um dado grafo. 

O grafo hamiltoniano possui um ciclo hamiltoniano.

Teorema de Rédei: Todo `torneio <torneio_>`_ tem um caminho hamiltoniano
direcionado.

Problema do Caixeiro Viajante
-----------------------------

Dado um grafo ponderado (G , w ), encontre um ciclo hamiltoniano de G de peso mínimo.

.. _kfactor:

k-fator
-------

Subgrafo gerador k-regular. 1-fator também é chamado *emparelhamento perfeito*.

.. _inducedsubgraph:

subgrafo induzido
-----------------

Subgrafo induzido/gerado F obtido a partir de G pela remoção de **vértices**.

Toda aresta de E(G) com ambos os extremos em V(F) também é aresta de E(F).

Se X é o conjunto de vértices removidos F é o grafo G − X.

.. _ponderado:

grafo ponderado
---------------

Grafo no qual cada aresta tem um número real denominado `peso <peso_>`_ w(e)
associado à ela.

.. _peso:

peso
----

De um grafo G, d(G), é a somatória dos pesos de suas arestas.

De uma aresta é o número real associado à ela.

.. _identificacao:

identificação
-------------

Operação de substituição de dois vértices - ``x`` e ``y`` - por um único
vértice incidente em todas as arestas em que ``x`` e ``y`` incidiam. O grafo
resultante é denotado por G/{x, y}.

.. _contracao:

contração
---------

Operação de remoção de uma aresta ``e`` seguida da `contração <contracao_>`_
de seus extremos. O grafo resultante é denotado por G/e.

.. _decomposicao:

decomposição
------------

Família de subgrafos `aresta-disjuntos <adisjunto_>`_ de G tais que a união do
conjunto de arestas de cada subgrafo da família resulta no conjnto de arestas
do grafo original G.

.. _even:

grafo par
---------

Grafo em que todo vértice tem `grau <degree_>`_ par.

Teorema de Veblen: Um grafo admite uma decomposição em ciclos se e somente se
é par.

Teorema: Um grafo é par se e somente se `|∂(X)| <cut_>`_ é par para todo
subconjunto X de V.

.. _cobertura:

cobertura
---------

Família de subgrafos **não necessariamente** `aresta-disjuntos <adisjunto_>`_
de G tais que a união do conjunto de arestas de cada subgrafo da família
resulta no conjunto de arestas do grafo original G.

É chamada *uniforme* se cobre cada aresta de G o mesmo número de vezes. Se k é
o número de vezes, a cobertura é denominada *k-cobertura*.

.. _cut:

corte
-----

Seja E[X, Y] o conjunto de arestas de G com um extremo em X e o outro em Y.

Quando Y = V − X, E[X, Y] ́é chamado de corte (*cut*) de X em G e denotado por ∂(X).

Um corte ∂(X) **respeita** um conjunto de arestas A se A ∩ ∂(X) = ⦰.

.. _lightedge:

aresta leve
-----------

Em um corte ∂(S) se w :sub:`uv`  := min :sub:`(x,y) ∊ ∂(S)` {w :sub:`xy` } - (u,v)
é a aresta de menor peso no corte ∂(S).

.. _trivialcut:

corte trivial
-------------

É dado por todas as arestas incidentes em v e denotado por ∂(v).

Conexidade
==========

.. _walk:

passeio
-------

Sequência W = v :sub:`0`  e :sub:`1`  v :sub:`1`  ... e :sub:`l`  v :sub:`l`
cujos elementos são vértices e arestas **não necessariamente* distintos, tal
que para todo ``1 ≤ i ≤ l``, v :sub:`i-1`  e v :sub:`i`  são extremos de e.

Se v :sub:`0`  = x e v :sub:`l`  = y, W conecta x a y e é um *passeio* de x a
y.

Qualquer subsequência com vértice de *início* u e vértice de *término* v é
chamada *segmento* de W e denotada por uWv.

Um passeio é *fechado* (*closed*) se os vértices de início e término
coincidem.

.. _trail:

trilha
------

`Passeio <walk_>`_ em que não existe repetiçào de arestas.

.. _path:

caminho
-------

`Passeio <walk_>`_ em que não existe repetição de vértices, nem arestas.

.. _conexity:

conexidade
----------

Dois vértices u e v estão conectados se existe um passeio de u a v no grafo.

O grafo é conexo se todo par de vértices está conectado.

.. _distance1:

distância
---------

Comprimento do menor `caminho <path_>`_ de u a v em G, denotado por
d :sub:`G(u, v)` .

.. _cutedge:

aresta de corte
---------------

Aresta ``e`` que quando removida aumenta o número de componentes conexas de G,
ou seja, c(G \ e) = c(G) + 1.

Preposição: Uma aresta e de um grafo G é uma aresta de corte se e somente se e
não pertence a um ciclo de G.

.. _euleriantrail:

trilha euleriana
----------------

`Trilha <trail_>`_ que passa por cada aresta do grafo exatamente uma vez.

.. _euleriancirc:

circuito euleriano
------------------

`Trilha Euleriana <euleriantrail_>`_ fechada.

.. _eulerian:

grafo euleriano
---------------

Grafo conexo e que possui um `circuito Euleriano <euleriancirc_>`_.

Teorema: Um grafo conexo é euleriano se e somente se é par.

Árvores
=======

.. _tree:

árvore
------

Grafo T conexo e acíclico.

Preposição: Em uma árvore, quaisquer dois vértices são conectados por
precisamente um caminho.

Teorema: Se T é uma árvore, então e(T) = v (T) − 1.

.. _forest:

floresta
--------

Grafo acíclico não necessariamente conexo.

.. _leaf:

folha
-----

Vértice de grau um em uma árvore.

Preposição: Toda árvore nào trivial tem pelo menos duas folhas.

.. _spanningtree:

árvore geradora
---------------

Árvore subgrafo gerador de um grafo.

Teorema: Um grafo é conexo se e somente se tem uma árvore geradora.

.. _rootedtree:

áarrvore com raiz
-----------------

Árvore com um vértice x chamado de *raiz*, denotado por T(x).

.. _branching:

arborescência
-------------

`Orientação <orientacao_>`_ de uma árvore com raiz em que todo vértice exceto
a raiz tem grau de entrada 1.

Buscas em Grafos
================

.. _reach:

alcance
-------

Um vértice ``u`` é **alcançável** a partir de um vértice ``v`` de um grafo G
se existe um `caminho <path_>`_ de ``v`` para ``u`` em G.

.. _distance2:

distância
---------

Um vértice ``u`` está a uma **distância** ``k`` de um vértice ``v`` se ``k`` é
o comprimento do menor `caminho <path_>`_ que começa em ``v`` e termina em
``u``.

Se ``u`` **não é alcançável** a partir de ``v``, determina-se que a distância
entre eles é **infinita**.

.. _bsf:

busca em largura
----------------

Busca em largura ou BFS (*Breadth First Search*) em um grafo G = (V, E).

Método em que, partindo-se de um vértice especial ``u``, denominado raiz da
busca, percorre-se G visitando todos os vértices alcançáveis a partir de ``u``
em **ordem crescente de distância**.

Complexidade: ``O(|V| + |E|)``

.. _dfs:

busca em profundidade
---------------------

Busca em profundidade ou DFS (*Depth First Search*) em um grafo G = (V, E).

Método em que, partindo-se de um vértice especial ``u``, denominado raiz da
busca, percorre-se G visitando todos os vértices alcançáveis a partir de ``u``
tendo como meta atingir primeiramente as folhas, retornando quando isso
acontecer. Generalização do percurso em **pré-ordem**.

.. _timestamps:

Variáveis podem ser usadas para a marcação de `tempo` como instante de descoberta `d` e de exploração `f`.

Complexidade: ``O(|V| + |E|)``

**Classificação de arestas**

Dada uma floresta G :sub:`pred`  construída pela `DFS <dfs_>`_:

.. _forest_edge:

- aresta da floresta

  Toda aresta em G :sub:`pred` .

.. _back_edge:

- aresta de retorno
  
  É uma aresta (u, v) onde ``v`` é **ancestral** de ``u`` em G :sub:`pred` .

.. _forward_edge:

- aresta direta

  É uma aresta (u, v) que não está em G :sub:`pred`  onde ``v`` é descendente
  de ``u`` em uma árvore contruída pela DFS.

.. _cross_edge:

- aresta cruzada
  
  Todas as arestas que não podem ser classificadas como `de retorno
  <back_edge_>`_ ou `diretas <forward_edge_>`_.

Teorema: Em uma DFS de um grafo **não direcionado** G = (V, E) toda aresta é
da árvore ou é de retorno.

.. _topsort:

ordenação topológica
--------------------

Em um `grafo direcionado acíclico <dag_>`_ G = (V, E), é uma ordem linear dos
vértices tal que, para todo arco (u, v) em E, ``u`` _antecede_ ``v`` na ordem.

Lema: Um grafo direcionado G é acíclico *se e somente se* uma bisca em
peofundidade em G não classifica nenhum arco como sendo de retorno.

Teorema: Rotular os vértices do grafo em ordem decrescente dos valores `f
<timestamps_>`_ obtidos em uma DFS resulta em uma ordenação topológica correta
de um grafo direcionado acíclico G.

Componentes Fortemente Conexas
==============================

.. _cfc:

componentes fortemente conexas
------------------------------

Uma componente fortemente conexa (CFC) ``H`` de um grafo *G = (V, E)* é um
subconjunto de vértices tal que, para todo par de vértices ``u`` e ``v`` de
``H``, existe um `caminho <path_>`_ de ``u`` para ``v`` e vice-versa. ``H``
também é **maximal** com relação a inclusão de vértices.

.. _transposed:

grafo transposto
----------------

É o grafo G :sup:`T`  = (V, E :sup:`T` ) de um grafo direcionado G = (V, E) onde:

   E :sup:`T`  = {(u, v) ∊ V x V: (v, u) ∊ E}

o grafo obtido invertendo-se a orientação de seus arcos.

+ G e G :sup:`T`  têm as mesmas componentes fortemente conexas.

Árvore Geradora Mínima
======================

.. _agm:

árvore geradora mínima
----------------------

Árvore gerada pelo problema da Árvore Geradora Mínima:

Dado um grafo não orientado ponderado G = (V, E), onde w: E →  ℝ :sup:`+`
define os custos das arestas, encontrar um subgrafo gerador conexo T
de G tal que, para todo subgrafo gerador conexo T' de G

  Σ :sub:`e ∊ T`  w :sub:`e`  ≤ Σ :sub:`e ∊ T'`  w :sub:`e` .

**Características**

+ Só tem solução se G é conexo.  + Resulta em uma árvore - a *Árvore Geradora
  Mínima* (AGM) - dado que tal subgrafo não conterá ciclos.

**Algoritmos**

- Algoritmo genérico: estratégia gulosa.

  **Invariante**: Antes de cada iteração A é um subconjunto de arestas de uma
  AGM.  A cada iteração A ∪ {(u, v)}, (u, v) é chamada aresta **segura**.
  
  AGM-Generico(G, w)
  
          A ← 0; enquanto A não forma uma árvore geradora faça encontre aresta
          segura (u, v); A ← A ∪ {(u, v)}; retorne A.

Teorema: Seja G = (V, E) um grafo conexo não orientado ponderado nas arestas
por uma função w: E → &#x211D;. Seja A um subconjunto de E que está contido em
alguma AGM de G, seja ainda ∂(S) um `corte <cut_>`_ de G que respeita A e (u,
v) uma `aresta leve <lightedge_>`_ de ∂(S). Então, (u, v) é uma **aresta
segura** para A.

.. _corollary23_2:

Corolário: Seja G = (V, E) um grafo conexo não orientado ponderado nas arestas
por uma função w: E → &#x211D; :sup:`+` . Seja A um subconjunto de E que está
contido em alguma AGM de G, e seja C = (V :sub:`C` , E :sub:`C` ) uma
componente conexa (árvore) da floresta G :sub:`A`  = (V, A). Se (u, v) uma
`aresta leve <lightedge_>`_ de ∂(C), então (u, v) é **segura** para A.

Os algoritmos de `Prim <prim_>`_ e de `Kruskal <kruskal_>`_ especializam o
algoritmo genérico usando o Colorário.

.. _prim:

Prim
----

Dado o `colorário <corollary23_2_>`_.

A é sempre uma `árvore <tree_>`_. A **aresta segura** adicionada a A é sempre
uma `aresta leve <lightedge_>`_ do corte ∂(C), onde C é o conjunto de vértices
que sÃo extremidades de arestas em A.

.. _kruskal:

Kruskal
-------

Dado o `colorário <corollary23_2_>`_.

A é sempre uma `floresta <forest_>`_. A **aresta segura** adicionada a A é
sempre uma aresta de menor peso dentre todas as arestas ligando dois vértices
de componentes distintas de G :sub:`A` .

Caminhos Mínimos
================

.. _minpath:

caminhos mínimos
----------------

`Caminhos <path_>`_ que se deseja encontrar no problema de Caminhos Mínimos:

Dados um grafo conexo ponderado G = (V, E), direcionado ou não, onde d:
E → ℝ :sup:`+` define as distâncias entre os extremos das arestas, e um
vértice ``r`` de G, queremos encontrar, para todo vértice ``u`` de G um
caminho C de distância mínima de ``r`` a ``u``, ou seja, o caminho C deve ser
tal que, para todo caminho C de ``r`` a ``u`` em G :

∑ :sub:`e ∊ C`  d :sub:`e`  ≤ ∑ :sub:`e ∊ C'`  d :sub:`e` .

**Algoritmos**

- `Dijkstra <dijkstra_>`_

Grafos direcionados ou não direcionados sem arestas de peso negativo.

- `Bellman-Ford <bellman_ford_>`_

Grafos direcionados com arestas de peso negativo e sem ciclos negativos.

- `Ordenação topológica <topsort_>`_

Para `DAGs <dag_>`_, basta calcular os caminhos mínimos analisando os vértices
segundo a ordenação topológica. Funciona mesmo com arestas de peso negativo.

**Caminhos mínimos entre todos os pares de vértices**

- `Dijkstra <dijkstra_>`_

Entre todos os vértices quando o grafo é esparso.

- `Floyd-Warshall <floyd_warshall_>`_

Quando o grafo é denso.

.. _dijkstra:

Dijkstra
--------

Algoritmo para encontrar `caminhos mínimos <minpath_>`_ a partir de um vértice
``r``. Resulta numa `árvore geradora <spanningtree_>`_ com raiz em ``r`` -
árvore de caminhos mínimos para ``r``: ACM(r).

**Características**

+ Funciona para grafos direcionados e não direcionados desde que não haja
  arestas de peso negativo.

Ver `Algoritmo de Prim <prim_>`_.

.. _bellman_ford:

Bellman-Ford
------------

Algoritmo para encontrar `caminhos mínimos <minpath_>`_ a partir de um vértice ``r``.

**Características**

+ Funciona para grafos direcionados não haja ciclos negativos.
+ Detecta a existência de ciclos negativos.

.. _floyd_warshall:

Floyd-Warshall
--------------

Algoritmo para encontrar `caminhos mínimos <minpath_>`_ entre todos os pares
de vértices de um grafo.

**Características**

+ Usado quando o grafo é denso
+ Funciona mesmo na presença de arestas de peso negativo, desde que não haja
  ciclos negativos
+ É possível detectar a existência de ciclo negativo analisando a matriz
  resultado do algoritmo.
