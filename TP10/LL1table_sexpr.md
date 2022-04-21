# Tabela LL1

-> É topdown, então, neste tipo de tabelas só colocamos produções nos símbolos que pertencem aos First dos símbolos da esquerda ou Follow nos casos em que é vazio.

|     | pal | num | (   | )   |
| --- | --- | --- | --- | --- |
| L   | p1  | p1  | p1  | -   |
| S   | p2  | p3  | p4  | -   |
| SL  | p5  | p5  | p5  | p6  |

-> A tabela LL1 completa tem ainda todos os símbolos terminais e o símbolo final (geralmente o $), mas esta parte é sempre igual:

| --- | --- | --- | --- | --- | --- |
|     | pal | num | (   | )   | $   |
| --- | --- | --- | --- | --- | --- |
| L   | p1  | p1  | p1  | -   | -   |
| S   | p2  | p3  | p4  | -   | -   |
| SL  | p5  | p5  | p5  | p6  | -   |
| --- | --- | --- | --- | --- | --- |
| pal | s   | -   | -   | -   | -   |
| num | -   | s   | -   | -   | -   |
| (   | -   | -   | s   | -   | -   |
| )   | -   | -   | -   | s   | -   |
| $   | -   | -   | -   | -   | AC  |
