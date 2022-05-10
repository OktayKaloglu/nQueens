
<H1>N Queens Problem</h1>

<p>The n queens puzzle is the problem of placing n chess queens on an nXn chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal.</p> 
<p>For 8 queens, there are 92 solutions. The problem was first posed in the mid-19th century. In the modern era, it is often used as an example problem for various computer programming techniques.</p>

<h3> Python Solution</h3>

  <p> Gradient decent approach is used to find solutions for the problem. Every queens start at different coloumns with random start. Then the next state will be chosen until queens no more collide. If no next state has less collisions than the current state, we reach a plato o r local minima so we make a new random start.</p>
<h3> How to Use </h3>

<P>First we need to specify how many queens we want by modifying the numberOfqueens in the main function.Then we can execute the code.We can modify the random seed at the line 3.</P>
<p>We can return the solutions from gradientDecent function.If we want to display the boards state we can use viewTable function</p>



<h3> Outputs</h3>
![image](https://user-images.githubusercontent.com/101494182/167722007-ac1862a6-e798-494c-980d-a0c4058bb2be.png)
