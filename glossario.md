# Glossário

## Grafos

* [grafo simples](#gsimples)

  Grafo que não tem laços nem arestas paralelas.

* [grafo completo](#gcompleto)

  Grafo simples em que todo par de vértices é adjacente. Denotado por K_n.

* [caminho](#caminho)

  Grafo simples cujos vértices podem ser listados numa sequeência linear, tal que dois vértices são adjacentes se, e só se, são consecutivos na sequência. Denotado por P_n.
  
* [ciclo](#ciclo)

  Grafo simples com três ou mais vértices, cujos vértices podem ser listados numa sequência cíclica tal que dois vértices são adjacentes se, e só se, são consecutivos na sequência. Denotado por C_n.

  C_1 é um vértice com um laço.

  C_2 é um par de vértices ligados por um par de arestas paralelas.
  
* [comprimento](#comprimento) (de um caminho ou de um ciclo)

  Número de arestas no caminho/ciclo.

    k-caminho/k-ciclo é o caminho/cilco de comprimento k.

    3-ciclo também é chamado de triângulo, assim como o 4-ciclo de quadrilátero e assim por diante.
    
* [grafo conexo](#gconexo)

  Grafo em que toda partição de V em dois conjuntos não vazios X e Y, existe uma aresta com um extremo em X e o outro em Y.

  O grafo é *desconexo* se é possível achar uma partição de V em dois conjuntos não vazios X e Y, em que não há arestas com um extremo em X e outro em Y.
  
* [grafos disjuntos](#disjunto)

  Dois grafos que não têm vértices em comum.

  Ver [grafos aresta-disjuntos](#adisjunto).
  
* [grafos aresta-disjuntos](#adisjunto)

  Dois grafos que não têm arestas em comum.

  Ver [grafos disjuntos](#disjunto).

* [componente conexa](#componente)

  Cada grafo da união disjunta de um ou mais grafos.
  
  c(G) é o número de componentes conexas de um grafo. 
  
* [grafo bipartido](#bipartido)

  Grafo cujo conjunto de vértices V pode ser particionado em dois conjuntos X e Y tais que cada aresta de G tem um extremo em X e o outro em Y. (X, Y) é uma *bipartição* do grafo G[X, Y] e X e Y são suas *partes*.
  
  Se G[X, Y] é simples e todo vértice em X é adjacente a todo vértice em Y, G[X, Y] é *bipartido completo*.
  
  K_x,y é o grafo bipartido completo em que x = |X| e y = |Y|.
  
  K_1,y ou K_x,1 é chamado *estrela*. 
  
* [grau](#grau) (de um vértice)

  Número de arestas incidentes em v, cada laço contado duas vezes. Denotado por d_G(v).
  
  Grau mínimo de G é o grau do vértice de menor grau de G. Grau máximo é o grau do vértice de maior grau de G.
  
* [grafo regular](#regular)

  Grafo k-regular, onde d(v) = k para todo v em V, para algum valor de k.
  
  Grafos 3-regulares são chamados *grafos cúbicos*.
  
* [grafo direcionado](#digraph)

  Grafo D formado por um conjunto de vértices V e outro de arcos A, além de uma função de incidência que associa cada arco de A com um par **ordenado** de vértices.
  
  Grafos direcionados *estritos*, são aqueles que não possuem laços nem arcos paralelos.
  
* [grafo orientado](#orientado)

  Orientação de um grafo simples. D é uma *orientação* de G se é obtido a partir de G pela substituição das arestas por arcos correspondentes.

* [ordem](#odeg) (de um grafo)

  Número de vértices de um grafo.
 
* [tamanho](#tdeg) (de um grafo)

  Número arestas de um grafo.
  
* [torneio](#torneio)

  Qualquer orientação de um grafo completo.
  
  Veja [grafo orientado](#orientado).

