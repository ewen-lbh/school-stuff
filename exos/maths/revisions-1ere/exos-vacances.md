---
export_on_save:
    html: true
---

# Test
**Exercice 1** Résoudre les équations suivantes
1. $(x^2 - 4) - 3(x+2)(x-1) > 0$
1. $x^2+3x-5< x+4$
1. $2(x+1)^2 - 3x > 2$
1. $3x + 1/(2x) < 5/2$
1. $(-3x^ 2+x+10)/(-4x^ 2-11x+3)>0$

----
#### 1
$0=(x^2-4)-3(x+2)(x-1)$
$0=x^2-4+4-3x-6(x-1)$
$0=x^2-3x-6x+1$
$0=x^2-9x+1$

$Delta = b^2-4ac$
<br>
$81-4=77>0$, donc 2 racines $x_1$ et $x_2$:

$x_(1//2) = -(b^2 +- sqrt Delta)/(4a)$
$x_1 = -(81 - sqrt 77)/(4)$

$x_2 = -(81+sqrt 77)/4$

D'après la règle des signes, $f$ est du signe de $a$ pour $x in [x_1; x_2]$. Pour $x !in [x_1; x_2]$ $("ou " x in RR setminus [x_1; x_2])$, $x$ est du signe de $-a$:

|                   $x$ | $-oo$ |     | $-(81 - sqrt 77)/(4)$ |     | $-(81+sqrt 77)/4$ | $+oo$ |  |
|----------------------:|-------|-----|-----------------------|-----|-------------------|-------|--|
| $f:x mapsto x^2-9x+1$ |       | $+$ | $-$                   | $+$ |                   |       |  |

<center>

**Donc $f(x) > 0$ pour $x in RR setminus [-(81 - sqrt 77)/(4); -(81+sqrt 77)/4]$**
</center>

#### 2
$x^2+3x-5 = x+4$
$x^2+3x-5-x-4 = 0$
$x^2+2x-9 = 0$

$Delta = b^2 - 4ac$

$4+36=40>0$, donc 2 racines $x_1$ et $x_2$
$x_(1//2) = -(b^2 +- sqrt Delta)/(4a)$

$x_1 = -(4+sqrt 40)/4$
$x_1 = -(4+2 sqrt 10)/4$

$x_2 = -(4-sqrt 40)/4$
$x_2 = -(4-2 sqrt 10)/4$

D'après la règle des signes, $f$ est du signe de $a$ pour $x in [x_1; x_2]$. Pour $x !in [x_1; x_2]$ $("ou " x in RR setminus [x_1; x_2])$, $x$ est du signe de $-a$:

|                   $x$ | $-oo$ |     | $x_1$ |     | $-8$ | $+oo$ |  |
|----------------------:|-------|-----|-------|-----|------|-------|--|
| $f:x mapsto x^2+2x-9$ |       | $+$ | $-$   | $+$ |      |       |  |

<center>

**$x^2+3x-5 < x+4$ si $x^2+2x-9 < 0$, donc $x^2+2x-9 < 0$ pour $x in ]x_1;-8[$**

</center>

#### 3
$2(x+1)^2 - 3x > 2$
$2(x+1)^2 - 3x - 2 > 0$
$2(x^2+2x+1) - 3x-2 > 0$
$2x^2 + 4x + 2 - 3x - 2>0$
$2x^2 - x>0$

$Delta = b^2 - 4ac$

$1 - 4 * 2 * 0=1>0$

$x_(1//2) = -(b^2 +- sqrt Delta)/(4a)$

$x_1 = -(1 - sqrt 1)/4$
$x_1 = -2/4 = -1/2$

$x_2 = -(1 + sqrt 1)/4$
$x_2 = 0$

D'après la règle des signes, $f$ est du signe de $a$ pour $x in [x_1; x_2]$. Pour $x !in [x_1; x_2]$ $("ou " x in RR setminus [x_1; x_2])$, $x$ est du signe de $-a$:

|                   $x$ | $-oo$ | $-1/2$ |     | $0$ | $+oo$ |
|----------------------:|:-----:|:------:|:---:|:---:|:-----:|
| $f:x mapsto 2x^2 - x$ |  $+$  |  $0$   | $-$ | $0$ |  $+$  |

<center>

**$2(x+1)^2 - 3x > 2$ si $x^2 - x > 0$, donc $x^2 - x > 0$ pour $x in RR setminus [-1/2; 0]$**

</center>

#### 4
$3x + 1/(2x) < 5/2$
$3x + 1/(2x) - 5/2< 0$
$(3x)/1 + 1/(2x) - 5/2 < 0$
$(3x + 1 - 5)/(1 * 2x * 2) < 0$
$(3x - 4)/(4x) < 0$

$f_1:x |-> 3x - 4$
$f_2:x |-> 4x$

$f_1(x) = 0$ pour...
$3x - 4 = 0$
$x = 4/3$

$f_2(x) = 0$ pour...
$4x = 0$
$x = 0$

|             $x$ | $-oo$ | $0$ |     | $4/3$ | $+oo$ |
|----------------:|:-----:|:----|:---:|:-----:|:-----:|
|        $f_1(x)$ |  $-$  | $-$ | $-$ |  $0$  |  $+$  |
|        $f_2(x)$ |  $-$  | $0$ | $+$ |  $+$  |  $+$  |
| $(3x - 4)/(4x)$ |  $+$  | $0$ | $-$ |  $0$  |  $+$  |

<center>

**$3x + 1/(2x) < 5/2$ si $(3x - 4)/(4x) < 0$, Donc $S in ] 0;4/3 [$**

</center>