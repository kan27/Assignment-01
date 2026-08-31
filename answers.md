# CMPS 2200 Assignment 01
## Answers

**Name:**_Srikanya Balaji Garuda_______________________


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

  - 1a (2 pts): Yes it is. Since 2^(n+1) can be reduced to 2*(2^n), it becomes a factor of 2^n. By taking a limit of the ratio of the functions we get 2*2^n/2^n = 2. Simply multipling by a factor doesn't increase the asymptotic growth rate
 
  - 1b (2 pts): It is not.  By taking a limit of the ratio we get 2^(2^n)/2^n = 2^(2^n - n), which when n approaches infinity, also approaches infinity. Thus it is not because 2^(2^n) grows faster than any constant multiple of 2^n

  - 1c (2 pts): It is not. By taking a limit of the ratio we get n^1.01/(log(n))^2. Since the limit of this ratio is not straightforward, we can employ l'hopitals. By that we get 1.01*n^0.01/2*log(n)*(1/n) = 1.01*n^1.01/2*log(n). We complete l'hopital's once more to get (1.01*1.01*n^0.01)/2*(1/n) = 
  (1.01^2)*(n^1.01)/2. Taking the limit of this we approach infinity. Thus it is not as n^1.01 has a faster asymptotic growth rate than (log n)^2.

  - 1d (2 pts): Referring to the previous answer, the limit of the ratio of the functions is infinity. Since it is infinity, n^1.01 is omega to (log(n))^2, n^1.01 grows strictly faster than (log(n))^2

  - 1e (2 pts): It is not. By taking a limit of the ratio we get (n^1/2)/(log n)^3, we see the limit is not obvious, so we perform l'hopitals to get 1/2*n^(-1/2)/(3*(log n)^2*1/n)=(n^1/2)/(6*(log n)^2). Take l'hopitals again to get (1/2*n^-1/2)/(6*(log n)*1/n)=(n^1/2)/(12*(log n)). Take l'hopitals again to get (1/2*n^-1/2)/(12*1/n)=(n^1/2)/24. Thus when n approaches infinity, so does the ratio. Thus it is not because (n^1/2) grows faster than (log n)^3

  - 1f (2 pts): Referring to the previous answer, the limit of the ratio of the functions is infinity. Since it is infinity, n^1/2 is omega to (log n)^3, n^1/2 grows strictly faster than (log n)^3.

  - 1g: We will prove by contradiction. Thus assume that the intersection of the sets is not empty. That means there exists some function $f(n)$ s.t $f(n) \in o(g(n))$ and $f(n) \in w(g(n))$. Since for both the definition of little-o and little w, they must work for all constants c. Since the conditions...

2. **SPARC to Python**

  - 2b (3 pts):
  This function finds the xth term of the fibonnaci sequence, with 0th being 0, and 1st being 1


3. **Parallelism and recursion**

  - 3b (4 pts):
  

  - 3d (4 pts):

  - 3e (5 pts):