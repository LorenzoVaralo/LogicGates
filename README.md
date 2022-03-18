# LogicGates

Durante meus estudos da faculdade, me foi introduzido o conceito de portas lógicas e sua implementação em circúitos para fazer cálculos booleanos, criei este programa pra facilitar drasticamente o processo manual de fazer a tabela verdade de um circúito. É apenas um simples programa CLI, que serve bem seu propósito.

---
### Como Usar:
O programa é iniciado por terminal, e deve conter `-i` ou `--input`, e em seguida a representação do circúito como uma string.

Para fazer a tabela verdade, devemos transcrever o circúito para que o programa entenda, tentei fazer da maneira mais simples e didática possível, utilizando as seguintes portas lógicas da seguinte forma:
```
NOT( <input> )
( <input1> )AND( <input2> )
( <input1> )OR( <input2> )
( <input1> )XOR( <input2> )
```

---
### Exemplo
Utilizando a notação apresentada anteriormente, o seguinte circúito pode ser representado por:
`NOT((((A)AND(B))OR(NOT(C)))AND(D))`

!["((A)OR(C))AND((A)XOR(B))"](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/5/example_circuit.png)

Para iniciar o programa no circúito acima faremos:
```
python logicGates.py -i "NOT((((A)AND(B))OR(NOT(C)))AND(D))"
```
