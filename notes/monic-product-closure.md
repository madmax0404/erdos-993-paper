# Monic product closure experiments

This note tracks the possible product-closure lemma suggested by the two
proved non-log-concave families. The candidate setting is a positive sequence
with constant term and leading coefficient both equal to `1`, log-concavity
through the penultimate coefficient, and a decreasing final tail. The generic
forest case is not covered by this because general tree polynomials need not
be monic.

## Reusable shifted-ratio lemmas

The later product proofs use the same shifted-weight comparisons many times.
Let `x_0,...,x_m` be a positive integer log-concave segment, and put
`X_k=x_k-1`. Then the shifted segment is log-concave:

`X_k^2>=X_{k-1}X_{k+1}`.

Indeed, if `u=sqrt(x_{k-1}x_{k+1})<=x_k`, then

`(x_k-1)^2-(x_{k-1}-1)(x_{k+1}-1)`

`=x_k^2-x_{k-1}x_{k+1}-2x_k+x_{k-1}+x_{k+1}`

`>=(x_k-u)(x_k+u-2)>=0`.

Thus, for shifted weights such as

`A=a-1`, `B=b-1`, `C=c-1`, `D=d-1`, `E=e-1`,

we have

`B^2>=AC`, `C^2>=BD`, and `D^2>=CE`.

On any positive block of shifted weights, the adjacent ratios are monotone.
Equivalently, whenever `i<=j<=k<=l`,

`W_j W_k>=W_i W_l`.

In applications below, any zero denominator is handled separately before
dividing. This cross-product form gives the following adjacent-ratio transfer
rule: multiplying a weighted block by an endpoint adjacent ratio shifts all
weights one step in the appropriate direction. For example,

`(C/D)(CS+BT)>=BS+AT`,

`(D/E)(DR+CS+BT)>=CR+BS+AT`,

and

`(B/A)(Cn+Br+DF)>=Dn+Cr+EF`,

provided the displayed denominators are positive and the variables are
nonnegative.

## Degree `(3,3)`

Let

`P=(1,a,b,1)` and `Q=(1,c,d,1)`,

where `a>=b>=1` and `c>=d>=1`. Write `a=b+x`, `c=d+y`, with
`x,y>=0`. The product coefficients are

`R=(r_0,...,r_6)`,

where

`r_0=1`,

`r_1=a+c`,

`r_2=ac+b+d`,

`r_3=ad+bc+2`,

`r_4=a+bd+c`,

`r_5=b+d`,

`r_6=1`.

The left side rises through `r_2`:

`r_1-r_0=a+c-1>=0`,

`r_2-r_1=bd+x(d-1)+y(b-1)+xy>=0`.

The right side falls from `r_3`:

`r_3-r_4=(b-1)(d-1)+1+x(d-1)+y(b-1)>=0`,

`r_4-r_5=bd+x+y>=0`,

`r_5-r_6=b+d-1>=0`.

Thus either `r_2<=r_3`, in which case the mode is at `r_3`, or `r_2>r_3`,
in which case the mode is at `r_2`. In both cases `PQ` is unimodal.

## Degree `(3,4)`

Let

`P=(1,a,b,1)` with `a>=b>=1`,

and

`Q=(1,c,d,e,1)` with `d>=e>=1`.

Write `a=b+x`, with `x>=0`. The product coefficients are

`r_0=1`,

`r_1=a+c`,

`r_2=b+ac+d`,

`r_3=1+bc+ad+e`,

`r_4=1+c+bd+ae`,

`r_5=a+d+be`,

`r_6=b+e`,

`r_7=1`.

The left side rises through `r_2`:

`r_1-r_0=b+x+c-1>=0`,

`r_2-r_1=c(b-1)+d+x(c-1)>=0`.

The right side falls from `r_4`:

`r_4-r_5=(b-1)(d-1)+c+x(e-1)>=0`,

`r_5-r_6=be+(d-e)+x>=0`,

`r_6-r_7=b+e-1>=0`.

It remains only to rule out a valley at `r_3`.

First,

`r_4-r_3=(b-1)(e-c)-x(d-e)`.

If `e<=c`, then `r_4<=r_3`, so the sequence falls from `r_3` onward.

If `e>c`, then `d>=e>c`, and

`r_2-r_3=-(b-1)(d-1)-e+x(c-d)<0`.

Thus `r_2<r_3` whenever `r_4>r_3`. There is no possible `r_2>r_3<r_4`
valley. Since the sequence rises through `r_2` and falls from `r_4`, this
proves `PQ` is unimodal.

Notably, this `(3,4)` argument does not use the full log-concavity of `Q`; it
only uses the final-tail condition `d>=e>=1`.

## Degree `(4,4)`

For degree `4`, write

`P=(1,a,b,c,1)` and `Q=(1,d,e,f,1)`.

The local hypotheses are

`b>=c>=1`, `a^2>=b`, `b^2>=ac`,

and

`e>=f>=1`, `d^2>=e`, `e^2>=df`.

The product coefficients are

`1`,

`a+d`,

`b+ad+e`,

`c+bd+ae+f`,

`2+cd+be+af`,

`a+d+ce+bf`,

`b+e+cf`,

`c+f`,

`1`.

The first two rises and the final two drops are immediate:

`(a+d)-1>=0`,

`(b+ad+e)-(a+d)=(a-1)(d-1)+b+e-1>=0`,

`(b+e+cf)-(c+f)=b+(e-f)+c(f-1)>=0`,

`(c+f)-1>=0`.

It remains to control the central differences. Put

`b=c+x` and `e=f+y`,

with `x,y>=0`. Let

`A=r_3-r_2`,

`B=r_4-r_3`,

`C=r_5-r_4`.

Then

`A=d(b-a)+af+y(a-1)-x`,

`B=1+(c-1)(f-1)+y(b-a)+x(f-d)`,

`C=a+d-2+c(f-d)-af-xy`.

First, the next difference is always negative:

`r_5-r_6=a+d-1+(c-1)(f-1)+y(c-1)+x(f-1)>0`.

Thus `r_6<r_5`.

We now prove that the signs of `A,B,C` cannot contain a valley.

### If `C>0`, then `B>0`

If `a>b`, then `a>c`, and

`C=d(1-c)+f(c-a)+a-2-xy`

is at most

`(1-c)+(c-a)+a-2-xy=-1-xy<0`,

a contradiction. Hence `a<=b`.

If `f<=d`, then

`C<=a+d-2+f-d-af-xy=a+f-2-af-xy<0`,

again a contradiction. Hence `f>d`.

With `a<=b` and `f>d`,

`B=1+(c-1)(f-1)+y(b-a)+x(f-d)>0`.

### If `B>0`, then `A>=0`

If `a<=b`, then

`A>=d(b-a)+af-x>=(b-a)+af-(b-c)=a(f-1)+c>=0`.

Now suppose `a>b`. Write `h=a-b>0`. The inequality

`b^2>=ac=(b+h)c`

gives

`hc<=b(b-c)=bx`.

In particular `x>0`. Since all variables are integers and `B>0`, we have
`B>=1`, so

`1+(c-1)(f-1)-yh+x(f-d)>=1`.

Equivalently,

`xd<=x f+(c-1)(f-1)-yh`.

Therefore

`A=-dh+af+y(a-1)-x`

is at least

`bf-x+(y h^2)/x+y(a-1)-h(c-1)(f-1)/x`.

Discarding the nonnegative `y` terms, it is enough to check

`bf-x>=h(c-1)(f-1)/x`.

Using `hc<=bx`, the right side is at most

`b(c-1)(f-1)/c`.

Hence

`bf-x-h(c-1)(f-1)/x`

is at least

`bf-(b-c)-b(c-1)(f-1)/c`

`=c+b(f-1)/c>=0`.

So `A>=0`.

Combining the pieces:

- the coefficient sequence rises through `r_2`;
- if it rises from `r_3` to `r_4`, then it did not fall from `r_2` to `r_3`;
- if it rises from `r_4` to `r_5`, then it rose from `r_3` to `r_4`, and then
  also did not fall from `r_2` to `r_3`;
- after `r_5`, it decreases through the end.

Thus the product of two degree-4 factors satisfying the local hypotheses is
unimodal.

The exploratory checks that led to this proof were:

- bounded exact check for all degree-4 factors with coefficients at most `12`:
  628 admissible factors and no non-unimodal pair product;
- random check of 2,000,000 admissible degree-4 pairs with coefficients at
  most `200`: no product failure.

## Degree `(4,5)`

Let

`P=(1,a,b,c,1)`

and

`Q=(1,d,e,f,g,1)`.

The hypotheses are

`b>=c>=1`, `a^2>=b`, `b^2>=ac`,

and

`f>=g>=1`, `d^2>=e`, `e^2>=df`, `f^2>=eg`.

The product coefficients are

`r_0=1`,

`r_1=a+d`,

`r_2=b+ad+e`,

`r_3=c+bd+ae+f`,

`r_4=1+cd+be+af+g`,

`r_5=1+d+ce+bf+ag`,

`r_6=a+e+cf+bg`,

`r_7=b+f+cg`,

`r_8=c+g`,

`r_9=1`.

The first two rises are the same as in degree `(4,4)`. The final three drops
are also immediate:

`r_6-r_7=a+e-1+(c-1)(f-g)+(b-1)(g-1)>0`,

`r_7-r_8=(b-c)+(f-g)+cg>0`,

`r_8-r_9=c+g-1>0`.

So only the four central differences

`r_3-r_2`, `r_4-r_3`, `r_5-r_4`, `r_6-r_5`

can matter.

A bounded exact check with degree-4 coefficients at most `18` and degree-5
coefficients at most `10` found 2,680,170 admissible pairs and no
non-unimodal product. The observed central sign patterns were only

`++++-`, `+++--`, `+++0-`, `++---`, `++0--`, `+----`, `+0---`, `-----`, `0----`.

Equivalently, no sampled product had a later positive central difference after
an earlier negative one.

Put

`x=b-c` and `h=b-a`.

Then `x>=0`, and the central differences are

`A=r_3-r_2=e(c-1)+f+x(e-1)+h(d-e)`,

`B=r_4-r_3=(c-1)(f-1)+g+x(f-d)+h(e-f)`,

`C=r_5-r_4=(c-1)(g-d)+x(g-e)+h(f-g)`.

We prove that positive central differences force all earlier central
differences to be nonnegative.

### If `B>0`, then `A>0`

First suppose `h>=0`. Since `c=a+h-x>=1`, we have `x<=a+h-1`. Also

`A=e(a-1)+f+hd-x`.

Therefore

`A>=(a-1)(e-1)+f+h(d-1)>0`.

Now suppose `h<0`. If `d<=e`, then the displayed formula for `A` immediately
gives `A>0`. It remains to handle `d>e`. Put `t=-h>0`. Since `d>e`, the
inequality `e^2>=df` gives `e>f`. From `B>0`,

`t(e-f)<(c-1)(f-1)+g+x(f-d)`.

Multiplying the desired lower bound for `A` by `e-f>0`, we get

`(e-f)A`

greater than

`(c-1)[e(e-f)-(d-e)(f-1)]`

`+ x[(e-f)(e-1)-(d-e)(f-d)]`

`+ [f(e-f)-g(d-e)]`.

The middle bracket is positive because `f-d<0`. Also `e^2>=df` gives

`d-e<=e(e-f)/f`,

so the first bracket is positive. Finally, using the same bound and
`f^2>=eg`,

`g(d-e)<=ge(e-f)/f<=f(e-f)`,

so the final bracket is nonnegative. Hence `A>0`.

### If `C>0`, then `B>0`

First, `C>0` forces `e>=d`. Indeed, if `e<d`, then `e^2>=df` gives `f<e`,
and hence `g<=f<e<d`. Since `h<=b-1=c+x-1`,

`C<=(c-1)(g-d)+x(g-e)+(c+x-1)(f-g)`

`=(c-1)(f-d)+x(f-e)<0`,

a contradiction.

Now assume `e>=d`.

If `f>=e`, then `B>0` is immediate when `h<=0`. When `h>0`, rewrite

`B=(a-1)(f-1)+g+h(e-1)-x(d-1)`.

Using `x<=a+h-1`,

`B>=(a-1)(f-d)+g+h(e-d)>0`.

It remains to consider `f<e`. Then `f>g`; otherwise `f^2>=eg` would imply
`f>=e`. From `C>0`,

`h(f-g)>(c-1)(d-g)+x(e-g)`.

Since `B` is increasing in `h`, multiplying by `f-g>0` gives `(f-g)B`
greater than

`g(f-g)`

`+ (c-1)[(f-g)(f-1)+(e-f)(d-g)]`

`+ x[(f-g)(f-d)+(e-f)(e-g)]`.

The `x` bracket is nonnegative because `d<=e`:

`(f-g)(f-d)+(e-f)(e-g)>=(f-g)(f-e)+(e-f)(e-g)=(e-f)^2`.

For the `(c-1)` bracket, use `d>=1` to reduce to

`(f-g)(f-1)>=(e-f)(g-1)`.

This is trivial when `g=1`. When `g>1`, `f^2>=eg` gives
`e-f<=f(f-g)/g`, and therefore

`(e-f)(g-1)<=(f-g)f(g-1)/g<=(f-g)(f-1)`.

So `B>0`.

### If `r_6>r_5`, then `C>0`

For this final implication use

`u=b-a` and `v=c-a`.

Then `u>=v`, and

`C=(a-1)(g-d)+u(f-e)+v(e-d)`.

Also

`r_6-r_5=a-1-d-e(c-1)-f(b-c)+g(b-a)`.

If `r_6-r_5>0`, then:

- `c>a`; otherwise, using `g<=f` gives
  `r_6-r_5<=a-1-d-e(c-1)+f(c-a)<=-d`;
- `f>e`; otherwise, with `c>a` and `g<=f<=e`, the same bound gives
  `r_6-r_5<=a-1-d-e(a-1)<=-d`;
- `e>d`, because `e^2>=df` and `f>e`;
- `g>d`; otherwise, with `u>=v>0` and `f>e>d>=g`,
  `r_6-r_5=(a-1)(1-e)-d+v(f-e)+u(g-f)<0`.

Thus `u>=v>0`, `f>e>d`, and `g>d`, so

`C=(a-1)(g-d)+u(f-e)+v(e-d)>0`.

Combining these implications, a later central rise cannot occur after an
earlier central fall. Since the sequence rises through `r_2` and falls from
`r_6` onward, the product of degree `(4,5)` factors satisfying the local
hypotheses is unimodal.

## Degree `(5,5)` first check

Let

`P=(1,a,b,c,d,1)` and `Q=(1,e,f,g,h,1)`.

The hypotheses are

`c>=d>=1`, `a^2>=b`, `b^2>=ac`, `c^2>=bd`,

and

`g>=h>=1`, `e^2>=f`, `f^2>=eg`, `g^2>=fh`.

The product coefficients are

`r_0=1`,

`r_1=a+e`,

`r_2=b+ae+f`,

`r_3=c+be+af+g`,

`r_4=d+ce+bf+ag+h`,

`r_5=2+de+cf+bg+ah`,

`r_6=a+e+df+cg+bh`,

`r_7=b+f+dg+ch`,

`r_8=c+g+dh`,

`r_9=d+h`,

`r_10=1`.

The first two rises are immediate:

`r_1-r_0=a+e-1>=0`,

`r_2-r_1=(a-1)(e-1)+b+f-1>=0`.

The final three drops are also immediate:

`r_7-r_8=(b-c)+(f-g)+d(g-h)+ch>=0`,

`r_8-r_9=(c-d)+(g-h)+dh>=0`,

`r_9-r_10=d+h-1>=0`.

Thus only the five central differences from `r_3-r_2` through `r_7-r_6`
can matter.

A bounded exact check with coefficients at most `12` found 2,588 admissible
degree-5 factors, hence 6,697,744 ordered pairs, and no non-unimodal product.
The observed central sign patterns were only

`+++++`, `++++-`, `++++0`, `+++--`, `+++0-`, `++---`,
`++0--`, `+----`, `+0---`, `-----`, `0----`.

So the next target is again a sign-chain proof: show that each positive
central difference forces the previous central difference to be nonnegative.

Let

`A=r_3-r_2`,

`B=r_4-r_3`,

`C=r_5-r_4`,

`E=r_6-r_5`,

`F=r_7-r_6`.

The first implication has a compact contrapositive proof.

### If `B>0`, then `A>=0`

Suppose instead that `A<0`. If `a<=b`, then

`A=(a-1)(f-1)+(b-a)(e-1)+c+g-1>=0`,

a contradiction. Similarly, if `e<=f`, then

`A=(a-1)(f-e)+(b-1)(e-1)+c+g-1>=0`,

again a contradiction. Thus `a>b` and `e>f`.

The log-concavity inequalities then force `b>c` and `f>g`, since otherwise
`b^2>=ac` or `f^2>=eg` would fail. Write

`alpha=a-b`, `beta=b-c`, `eta=e-f`, `theta=f-g`,

so all four parameters are positive. Then

`A=bf-alpha eta-beta-theta`.

Also, using `d<=c^2/b` and `h<=g^2/f`,

`B<=bf-alpha theta-beta eta-beta f-b theta-beta-theta+beta^2/b+theta^2/f`.

Set `X=beta/b` and `Y=theta/f`. The log-concavity inequalities give

`alpha <= bX/(1-X)` and `eta <= fY/(1-Y)`.

Since `A<0`,

`1-X/f-Y/b < alpha eta/(bf) <= XY/((1-X)(1-Y))`.

Therefore

`1-X-Y < X(1-X)(1-Y)/f + Y(1-X)(1-Y)/b`.

Dropping the negative terms `-alpha theta-beta eta` from the upper bound for
`B`, we get

`B <= bf(1-X-Y)-bX(1-X)-fY(1-Y)`.

Using the preceding strict inequality,

`B < -bXY(1-X)-fXY(1-Y)<0`.

Thus `A<0` implies `B<0`, proving the implication.

### If `F>0`, then `E>0`

This rightmost implication is easiest from the tail. Put

`p=c-d`, `q=d-b`, `r=g-h`, `s=h-f`.

Then `p,r>=0`, and

`F=qs-pr-a-e+1-(b-1)(f-1)`.

If `q` and `s` have opposite signs, or if one is zero, then `F<0`. If
`q<0` and `s<0`, then

`qs=(b-d)(f-h)<=(b-1)(f-1)`,

so again `F<=1-a-e<0`. Hence `F>0` forces `q>0` and `s>0`, i.e.

`d>b` and `h>f`.

Since `c>=d>b`, the log-concavity inequality `b^2>=ac` gives `b>a`.
Similarly, since `g>=h>f`, the inequality `f^2>=eg` gives `f>e`.
Write

`m=b-a` and `n=f-e`,

so `m,n>0`. With

`c=a+m+q+p`, `d=a+m+q`, `g=e+n+s+r`, `h=e+n+s`,

the two central differences become

`F=qs-pr-ae-an-em-mn+m+n`,

and

`E=qs+mn+ms+nq+pr+ps+qr-ae+a+e-2`.

Since `F>0`,

`qs>pr+ae+an+em+mn-m-n`.

Substituting this lower bound in `E` gives

`E>2pr+mn+ms+nq+ps+qr+an+em+mn-m-n+a+e-2`.

Every displayed term is nonnegative: the last part is

`n(a+m-1)+m(e-1)+a+e-2>=0`.

Thus `E>0`.

### Reduction for `E>0 => C>=0`

The next implication starts with a useful forced sign condition: `E>0`
implies `b>=a` and `f>=e`.

By symmetry it is enough to rule out `a>b`. If `a>b`, then `b^2>=ac`
forces `b>c`. Write

`alpha=a-b`, `beta=b-c`, `gamma=c-d`,

with `alpha,beta>0` and `gamma>=0`. Then

`E=alpha(1-h)+beta(1-g)+c(1-e)+gamma(e-f)+e-2`.

If `e<=f`, all terms except `c(1-e)+e-2` are nonpositive, and

`c(1-e)+e-2=-(c-1)(e-1)-1<0`.

If `e>f`, then `gamma<=c-1` and `e-f<=e-1`, so

`gamma(e-f)<= (c-1)(e-1)`.

Again

`c(1-e)+e-2+gamma(e-f)<=-1`.

Thus `a>b` implies `E<0`. Swapping the two factors gives the analogous
conclusion that `e>f` also implies `E<0`. Hence `E>0` forces

`m=b-a>=0` and `n=f-e>=0`.

With

`p=c-b`, `q=d-b`, `r=g-f`, `s=h-f`,

we have `p>=q` and `r>=s`, and

`E=mn+ms+nq+pr-ae+a+e-2`,

while

`C=ae+an+as-a+em+eq-e+mn+mr-m+np-n-q-s+2`.

The remaining target is to prove `C>=0` from these relations and `E>0`.

There is a cleaner equivalent form. Put

`u=c-a`, `v=d-a`, `w=g-e`, `z=h-e`,

and let

`H=(a-1)(e-1)+1`,

`P=u-v=c-d`,

and

`R=w-z=g-h`.

Then

`E=uw-mR-nP-H`,

and

`C=H+w(a-1)+u(e-1)+mw+nu-mn-[(a-1)R+(e-1)P]`.

Since `P,R,m,n>=0`, the inequality `E>0` implies `uw>H`. If exactly one of
`u,w` is negative, then `uw<=0`, impossible. If both are negative, then
`u>=1-a` and `w>=1-e`, so

`uw<=(a-1)(e-1)=H-1`,

also impossible. Hence `E>0` also forces `u,w>=0`. We therefore have

`m,n,u,w>=0`, `u>=v`, and `w>=z`.

Since `E>0` and all quantities are integral,

`mR+nP<=uw-H-1`.

The bounds `d>=1` and `h>=1` give

`0<=P<=u+a-1`, `0<=R<=w+e-1`.

The final log-concavity inequalities give the lower bounds

`(a+m)P >= (a+u)(m-u)`,

and

`(e+n)R >= (e+w)(n-w)`.

Thus the implication `E>0 => C>=0` follows from the following purely
two-variable linear-programming sublemma:

For every `P,R` satisfying the four box bounds above, the two lower bounds
from final log-concavity, and `mR+nP<=uw-H-1`, one has

`(a-1)R+(e-1)P <= H+w(a-1)+u(e-1)+mw+nu-mn`.

This LP sublemma is now the sharp target. It is false if the two final
log-concavity lower bounds on `P` and `R` are removed.

The exact verifier `notes/verify_55_lp.py` checks this reduction by solving
the two-variable LP rationally for every admissible degree-5 pair up to a
coefficient cap. At cap `12` it checks 2,588 factors and 225,709 ordered pairs
with `E>0`; the minimum LP residual is `8`, attained at the same pair as the
minimum value of `C`.

The same exact verifier shows only five active LP vertex types at cap `12`:

- `R` at its lower bound, with the budget inequality tight;
- `P` at its lower bound, with the budget inequality tight;
- `R` at its upper bound, with the budget inequality tight;
- `P` at its upper bound, with the budget inequality tight;
- both `P` and `R` at their upper bounds.

Writing `A=a-1` and `G=e-1`, and temporarily ignoring the final
log-concavity lower shifts, the corresponding residuals are:

`nD_{Rlo}=AG^2+AGn+Anw+Gnu-Guw+2G-mn^2+mnw+n^2u+n`,

`mD_{Plo}=A^2G+AGm+Amw-Auw+2A+Gmu-m^2n+m^2w+mnu+m`,

`nD_{Rhi}=AG^2+G^2m+Gmw+Gnu-Guw+2G-mn^2+mnw+n^2u+n`,

`mD_{Phi}=A^2G+A^2n+Amw+Anu-Auw+2A-m^2n+m^2w+mnu+m`,

`D_{hi,hi}=1-AG-mn+mw+nu`.

The actual lower shifts for `P` and `R` only affect the two lower-bound
budget residuals. Thus the LP proof has become five explicit residual
inequalities, with the first two carrying the final-log-concavity correction
terms.

The vertex with both upper bounds active is already controlled. Write

`x=u-m` and `y=w-n`.

At this vertex the budget condition says

`m(w+G)+n(u+A)<=uw-AG-2`,

or equivalently

`xy>=(A+m)(G+n)+2`.

The second log-concavity inequality for the first factor gives

`x(A+1)<=m(A+1+m)`,

and the second log-concavity inequality for the second factor gives

`y(G+1)<=n(G+1+n)`.

If `mn<=AG`, then

`xy<=mn(A+1+m)(G+1+n)/((A+1)(G+1))`

`<=AG(A+1+m)(G+1+n)/((A+1)(G+1))`

`<=(A+m)(G+n)`,

because `A(A+1+m)<=(A+1)(A+m)` and
`G(G+1+n)<=(G+1)(G+n)`. This contradicts the budget condition, so
`mn>AG`. Therefore

`D_{hi,hi}=1-AG+mn+my+nx>0`.

The two upper-bound budget vertices are controlled by the same idea.

First take `R=w+G` and the budget inequality tight. The corresponding
coordinate

`P=(uw-AG-2-m(w+G))/n`

satisfies `0<=P<=u+A`. With `x=u-m`, the lower inequality `P>=0` gives

`xw>=G(A+m)+2`.

The first factor's second log-concavity inequality gives

`x(A+1)<=m(A+1+m)`,

so

`mw>=xw(A+1)/(A+1+m)>AG`.

At this vertex the residual is

`D=1+Gm+Gx+mw+nx-GP`.

Since `P<=u+A=A+m+x`,

`D>=1+mw+nx-AG>0`.

By symmetry, take `P=u+A` and the budget inequality tight. With `y=w-n`,
the lower inequality `R>=0` gives

`uy>=A(G+n)+2`,

while the second factor's second log-concavity inequality gives

`y(G+1)<=n(G+1+n)`.

Hence

`nu>=uy(G+1)/(G+1+n)>AG`.

At this vertex the residual is

`D=1+An+Ay+my+nu-AR`.

Since `R<=w+G=G+n+y`,

`D>=1+my+nu-AG>0`.

Thus three of the five LP vertex types are now proved. The two remaining
types are the lower-bound budget vertices; these are exactly where the final
log-concavity lower bounds for `P` and `R` must be used.

There is also a substantial easy part of the `R`-lower budget vertex. At this
vertex the objective slope along the budget line is nonpositive, so

`An<=Gm`.

If `w>=n`, then using only `P<=u+A` gives

`D>=1+Aw+mw+nu-mn>=0`.

Now suppose `w<n` but `u>=m`. Write

`u=m+x`, `w=n-y`,

with `x>=0` and `0<y<=n`. The actual residual is linear in `A` on the
interval `0<=A<=Gm/n`. At the two endpoints one gets:

`D(0)n(G+n+1)`

`=2G^2my+G^2xy+2G^2+Gm(n^2+ny-y^2+2y)+Gn^2x+Gnxy+3Gn+Gxy+2G`

`+mn(n+1)(n-y)+n^3x+n^2x+n^2+n>=0`,

and

`D(Gm/n)=`

`[G^3m+G^2mn+Gmn^2+Gnxy+2Gn+mn^2(n-y)+n^3x+n^2]/n^2>=0`.

Thus this lower-bound vertex is proved unless both `u<m` and `w<n`.
The `P`-lower budget vertex has the symmetric reduction. Consequently the
only remaining LP corner is the simultaneous-deficit case in a lower-bound
budget vertex.

We now finish that corner. Consider again the `R`-lower budget vertex. Put

`x=m-u>0`, `y=n-w>0`,

so `m=u+x` and `n=w+y`. Since `y>0`, the inequality `e^2>=f` forces `G>=1`.
Write

`L=G+1+n=G+1+w+y`,

so the lower bound is

`R_0=y(G+1+w)/L`.

The upper bound `P<=u+A` gives the crude residual bound

`D>=1+A(w-R_0)+mw+nu-mn`

`=1+A(w-R_0)+uw-xy`.

Since the budget is tight and `P>=0`,

`uw>=AG+2+mR_0`.

Thus

`D>=3+A(G+w-R_0)+mR_0-xy`.

The same budget inequality also gives `w>0` and

`(m-x)w>=AG+2+mR_0`,

so

`xy<=my-y(AG+2+mR_0)/w`.

Therefore it is enough to check

`3+A(G+w-R_0)+mR_0-my+y(AG+2+mR_0)/w>=0`.

After multiplying by the positive denominator `wL`, the left side becomes

`A[G^2w+G^2y+2Gw^2+(G-1)wy+Gw+Gy^2+Gy+w^3+w^2]`

`+(G+1)my^2+3Gw+2Gy+3w^2+5wy+3w+2y^2+2y`,

which is nonnegative because `A,m,w,y>=0` and `G>=1`. This proves the
simultaneous-deficit case for the `R`-lower budget vertex. The `P`-lower
budget vertex is symmetric.

This proves the two-variable LP sublemma. Consequently `E>0 => C>=0`, and
the right half of the degree `(5,5)` sign chain is complete. The remaining
missing implication for the full `(5,5)` monic product case is

`C>0 => B>=0`.

Equivalently, it remains to rule out a central valley at `r_4`.

In the same notation as above, with

`P=c-d`, `R=g-h`, and `H=(a-1)(e-1)+1`,

the two relevant differences are

`B=ae+aw+eu+mn-P-R`,

and

`C=H+w(a-1)+u(e-1)+mw+nu-mn-(e-1)P-(a-1)R`.

Thus `C>0` gives the budget inequality

`(e-1)P+(a-1)R<=H+w(a-1)+u(e-1)+mw+nu-mn-1`.

The last missing implication is therefore another two-variable LP statement:
under the same box bounds and final-log-concavity lower bounds for `P` and
`R`, this budget inequality should force

`P+R<=ae+aw+eu+mn`.

This last statement has a direct proof.

First suppose `c>=b`, or equivalently `u>=m`. The inequality `b^2>=ac` then
also gives `b>=a`, so `m>=0`. Using only the upper bounds

`P<=c-1=u+A` and `R<=g-1=w+G`,

we get

`B>=AG+1+Aw+Gu+mn`

`=1+A(G+w)+G(u-m)+m(G+n)>=1`,

because `G+w=g-1>=0` and `G+n=f-1>=0`. By symmetry, `g>=f` also gives
`B>=1`. Thus it remains to consider the case

`b>c` and `f>g`.

Put

`x=b-c>0` and `y=f-g>0`.

Then

`u=c-a=c-1-A` and `f-e=g+y-G-1`.

The upper bounds on `P` and `R` give

`B>=cg+y(c-a)+x(f-e)-(c-1)-(g-1)`

`=(b-1)(f-1)+1-Ay-Gx`.

So it is enough to prove

`Ay+Gx<=(b-1)(f-1)+1`.

In these variables,

`C=(c-1)(g-1)+1-xy-GP-AR`.

Since `C>0` and all quantities are integral,

`GP+AR<=S`,

where

`S=(c-1)(g-1)-xy`.

The final log-concavity inequalities give

`P>=cx/(c+x)` and `R>=gy/(g+y)`.

Therefore

`Gcx/(c+x)+Agy/(g+y)<=S`.

It follows that

`Gx+Ay<=S max((c+x)/c,(g+y)/g)`.

Both possible ratios are harmless. Let

`T=(b-1)(f-1)+1=(c+x-1)(g+y-1)+1`.

Then

`cT-(c+x)S=cy(c-1)+x(g-1)+c+2cxy+x^2y>=0`,

and symmetrically

`gT-(g+y)S=gx(g-1)+y(c-1)+g+2gxy+xy^2>=0`.

Thus `S(c+x)/c<=T` and `S(g+y)/g<=T`, proving `Gx+Ay<=T` and hence
`B>=0`.

Combining this with the earlier implications

`B>0 => A>=0`,

`E>0 => C>=0`,

and

`F>0 => E>0`,

there cannot be a positive central difference after a negative central
difference. Since the first two rises and the final three drops were already
immediate, the degree `(5,5)` monic product case is unimodal.

Exact checks through coefficient cap `15`, and random checks with much larger
coefficients, suggest the stronger bound

`C>=a+e+m+n`.

The cap-12 exact minimum of `C` under `E>0` is `8`, occurring for

`P=(1,2,3,4,3,1)` and `Q=(1,2,3,4,4,1)`,

where `E=1`. The stronger bound has cap-12 minimum `2` for

`C-a-e-m-n`,

occurring at

`P=(1,2,3,3,3,1)` and `Q=(1,2,4,5,5,1)`.

## Degree `(5,6)` and `(6,6)` scans

The script `notes/scan_monic_products.py` checks the same monic class in
arbitrary bounded degrees. For degree `d`, the factors are positive integer
sequences

`(1,a_1,...,a_{d-1},1)`,

with

`a_i^2>=a_{i-1}a_{i+1}` for `1<=i<=d-2`,

and final tail

`a_{d-2}>=a_{d-1}>=1`.

At cap `12`, the `(5,6)` scan has

- `2,588` degree-5 factors;
- `7,138` degree-6 factors;
- `18,473,144` ordered products;
- no non-unimodal product.

The observed central sign patterns, after dropping the first two rises and
last three drops, are

`+++---`, `++++--`, `++----`, `+++0--`, `++0---`, `+++++-`, `+-----`,
`++++0-`, `+0----`.

Every sampled adjacent implication

`Delta_{i+1}>0 => Delta_i>=0`

has positive margin. The tightest nontrivial margins are:

- `i=4`: minimum previous difference `5`;
- `i=5`: minimum previous difference `10`.

At cap `12`, the `(6,6)` scan has

- `7,138` degree-6 factors;
- `25,479,091` unordered products;
- no non-unimodal product.

The observed central sign patterns are

`++++---`, `+++----`, `+++++--`, `++-----`, `+++0---`, `++++0--`,
`++0----`, `++++++-`, `+++++0-`, `+------`, `+0-----`.

Again every sampled adjacent implication has positive margin. The tightest
nontrivial margins are:

- `i=5`: minimum previous difference `9`;
- `i=6`: minimum previous difference `16`.

Thus `(5,6)` and `(6,6)` support the same sign-chain strategy as `(5,5)`,
and the next proof target is not a counterexample search but an abstraction of
the sign-chain lemmas.

Random valid-factor scans with larger coefficients show that the cap-12 sign
pattern list is not exhaustive. With `100,000` random valid pairs, first
coefficient cap `200`, and seed `1`, the `(5,6)` scan found no non-unimodal
product but did find the central all-positive pattern `++++++`. One explicit
example is

`P=(1,48,1215,3962,3044,1)`,

`Q=(1,86,7337,525127,28327122,17036164,1)`,

whose product has sign pattern

`++++++++---`.

Similarly, with seed `2`, the `(6,6)` random scan found no non-unimodal
product and did find the central all-positive pattern `+++++++`. The adjacent
sign-chain minima stayed positive in both random scans. Thus the bounded scans
are reliable as counterexample searches at that cap, but not as complete
sign-pattern catalogues for the infinite class.

## Reusable sign-chain template

Let

`R=(r_0,...,r_N)`,

and write

`Delta_i=r_{i+1}-r_i`.

Suppose the endpoints are already controlled:

`Delta_0,Delta_1>=0`,

and

`Delta_{N-3},Delta_{N-2},Delta_{N-1}<=0`.

If every adjacent central implication

`Delta_{i+1}>0 => Delta_i>=0`

holds for `2<=i<=N-4`, then `R` is unimodal. Indeed, a non-unimodal sequence
would have some negative difference followed later by a positive difference;
taking the first positive difference after such a negative one contradicts
one of the adjacent implications.

For the monic class, the first two rises are automatic in every degree. If

`P=(1,a_1,a_2,...)` and `Q=(1,b_1,b_2,...)`,

then

`Delta_0=a_1+b_1-1>=0`,

and

`Delta_1=(a_1-1)(b_1-1)+a_2+b_2-1>=0`.

The degree `(5,5)` proof shows the useful normal form for the hard central
implications. A later positive difference can often be written as

`base - lambda P - mu R > 0`,

where `P` and `R` are final-tail drops of the two factors. The previous
difference is then a residual of the form

`target - alpha P - beta R`.

The final log-concavity inequalities provide lower bounds on `P` and `R`,
while the final-tail condition gives upper bounds. This turns the implication
into a two-variable LP. In `(5,5)`, all LP vertices reduced to:

- lower-bound plus budget;
- upper-bound plus budget;
- both upper bounds.

The `(5,6)` scan suggests the same adjacent-implication strategy, but with one
additional central difference and likely one additional tail-drop variable in
the hardest LP reductions.

## Degree `(5,6)` proof start

Let

`P=(1,a,b,c,d,1)`,

and

`Q=(1,e,f,g,h,i,1)`.

The product coefficients are

`r_0=1`,

`r_1=a+e`,

`r_2=ae+b+f`,

`r_3=af+be+c+g`,

`r_4=ag+bf+ce+d+h`,

`r_5=ah+bg+cf+de+i+1`,

`r_6=ai+bh+cg+df+e+1`,

`r_7=a+bi+ch+dg+f`,

`r_8=b+ci+dh+g`,

`r_9=c+di+h`,

`r_10=d+i`,

`r_11=1`.

The first two rises are automatic:

`r_1-r_0=a+e-1>=0`,

and

`r_2-r_1=(a-1)(e-1)+b+f-1>=0`.

The final three drops are also automatic. First,

`r_8-r_9=b+c(i-1)+d(h-i)+g-h`

`=b+g-1+(c-d)(i-1)+(d-1)(h-1)>=0`.

Also,

`r_9-r_10=(c-d)+(h-i)+d(i-1)>=0`,

and

`r_10-r_11=d+i-1>=0`.

Thus the central differences are `Delta_2,...,Delta_7`. The first adjacent
central implication,

`Delta_3>0 => Delta_2>=0`,

is exactly the same as the `(5,5)` implication `B>0 => A>=0`: the formulas
for `Delta_2` and `Delta_3` only involve `a,b,c,d` and `e,f,g,h`, and the
proof uses the log-concavity inequalities through `g^2>=fh`, not the final
tail position of `h`.

The remaining `(5,6)` implications are

`Delta_4>0 => Delta_3>=0`,

`Delta_5>0 => Delta_4>=0`,

`Delta_6>0 => Delta_5>=0`,

and

`Delta_7>0 => Delta_6>=0`.

### Reduction for `Delta_4>0 => Delta_3>=0`

Put

`x=b-c`, `y=f-g`, `P=c-d`, `R=g-h`, and `T=h-i`.

Then

`Delta_3=bf-ay-ex-P-R`,

and

`Delta_4=cg-c+1-xy-(e-1)P-aR-T`.

First suppose `y<=0`, i.e. `g>=f`. Then `f>=e`: if `g>f`, this follows
from `f^2>=eg`, and if `g=f`, it is immediate from the same inequality.
Using

`Delta_3=a(g-f)+b(f-e)+c(e-1)+d-R`,

and `R<=g-1`, we get

`Delta_3>= (g-f)+(f-e)+(e-1)+1-(g-1)=1`.

Now suppose `y>0` but `x<=0`, i.e. `c>=b`. Then `b>=a`, since
`b^2>=ac` and `c>=b`. Rewriting

`Delta_3=b(g-1)+(c-b)(e-1)+(b-a)y+d-R`,

again with `R<=g-1`, gives

`Delta_3>=1`.

Thus the only unresolved case is

`x>0` and `y>0`,

or equivalently `b>c` and `f>g`.

In this simultaneous-deficit case, `Delta_4>0` and integrality imply

`(e-1)P+aR+T<=c(g-1)-xy`.

Put `S=c(g-1)-xy`. The final log-concavity inequalities give

`P(c+x)>=cx` and `R(g+y)>=gy`.

Also `P>=1`, `R>=1`, `P<=c-1`, and `T>=0`. The first two lower bounds
follow because `x,y>0`; the upper bound on `P` follows from `d>=1`; and
`T>=0` is the decreasing final tail `h>=i`.

Now write

`A=a-1` and `E=e-1`.

The budget becomes

`EP+AR<=S-T-R<=S-R`,

and

`ay+ex+P+R=Ay+Ex+x+y+P+R`.

Let

`M=max(x/P,y/R)`.

Then

`Ay+Ex<=M(EP+AR)<=M(S-R)`.

If `M=x/P`, then `x/P<=b/c`, so it is enough to prove

`(b/c)(S-R)+x+y+P+R<=bf`.

Multiplying by `c`, the residual is

`cbf-b(S-R)-c(x+y+P+R)`

`=-Pc+Rx+c^2y+c^2+2cxy-cy+x^2y`.

Using `P<=c-1` and `R>=0`, this is at least

`c+cy(c-1)+2cxy+x^2y>0`.

If `M=y/R`, then `y/R<=f/g`, so it is enough to prove

`(f/g)(S-R)+x+y+P+R<=bf`.

Multiplying by `g`, the residual is

`gbf-f(S-R)-g(x+y+P+R)`

`=-Pg+Ry+cg+cy+g^2x+2gxy-gx-gy+xy^2`.

Again using `P<=c-1` and `R>=0`, this is at least

`Ry+cy+gx(g-1)+gy(2x-1)+g+xy^2>0`.

Therefore `ay+ex+P+R<=bf`, i.e. `Delta_3>=0`. This proves the remaining
simultaneous-deficit case, hence the implication

`Delta_4>0 => Delta_3>=0`.

The `(5,6)` proof is therefore reduced to the three later central
implications `Delta_5>0 => Delta_4>=0`,
`Delta_6>0 => Delta_5>=0`, and `Delta_7>0 => Delta_6>=0`.

The earlier tempting leading-coefficient-only relaxation is weaker than this
argument and has artificial fractional counterexamples. The exact checks are
kept in `notes/verify_56_delta4.py`, and the full shifted-budget abstraction is
implemented in `notes/verify_56_delta4_full.py`. At cap `25`, the latter
checks `20,075,992` abstract hard states with shifted budget at least zero and
`14,606,971` states with feasible `a,e` ranges; the minimum exact
`Delta_3` margin is `8`.

### Proof of `Delta_5>0 => Delta_4>=0`

Put

`n=f-e`, `r=g-f`, `s=h-g`, and `t=i-h`.

Then

`Delta_4=d(e-1)+1+cn+br+as+t`,

and

`Delta_5=(d-1)n+(c-1)r+(b-1)s+(a-1)t`.

First, `Delta_5>0` forces `n>0`, i.e. `f>e`. Indeed, if `e>=f`, then
log-concavity gives `f>=g`, `g>=h`, and `h>=i`; all four differences
`n,r,s,t` are nonpositive, making `Delta_5<=0`.

Thus the relevant difference vector starts nonnegative. Since the ratios

`f/e`, `g/f`, `h/g`, `i/h`

are nonincreasing, the signs of `n,r,s,t` have at most one change from
positive to nonpositive. Also `t<=0` from the final decreasing tail `h>=i`.

It is useful to rewrite `Delta_4` by absorbing `t` into the positive final
coefficient `i`. Put

`A=a-1`, `B=b-1`, `C=c-1`, `D=d-1`, and `E=e-1`.

Then

`Delta_4=DE+i+Cn+Br+As`,

and

`Delta_5=Dn+Cr+Bs+At`.

By the shifted-ratio lemmas, we may use

`B^2>=AC`, `C^2>=BD`, and `BC>=AD`.

If `s>=0`, then the one-sign-change condition gives `r>=0`; hence

`Delta_4=DE+i+Cn+Br+As>=i>=1`.

It remains to handle `s<0`. Since `t<=0`, write `S=-s>0` and `T=-t>=0`.

If `r>=0`, then

`BS+AT<Dn+Cr`.

Here `B>0`; otherwise `b=1` forces `a=c=d=1`, contradicting
`Delta_5>0`. Thus

`S<(Dn+Cr)/B`.

Therefore

`Delta_4=DE+i+Cn+Br-AS`

`>DE+i+(C-AD/B)n+(B-AC/B)r>=0`,

using `BC>=AD` and `B^2>=AC`.

Finally suppose `r<0`, and put `R=-r>0`. Then

`CR+BS+AT<Dn`,

so `D>0`, and `CR+BS<Dn`. Also, by `C^2>=BD` and `BC>=AD`,

`BR+AS<=(C/D)(CR+BS)<Cn`.

Thus

`Delta_4=DE+i+Cn-BR-AS>DE+i>=1`.

This proves `Delta_5>0 => Delta_4>=0`.

Equivalently, in the shifted-prefix viewpoint, if
`Q_0=(1,e,f,g,h,1)` is obtained by replacing `i` with `1`, and `j=i-1`, then

`Delta_4(5,6)=Delta_4(PQ_0)+j`,

and

`Delta_5(5,6)=Delta_5(PQ_0)+(a-1)j+1`.

The exact verifier `notes/verify_56_delta5.py` checks the full actual degree
`(5,6)` space, not only degree-5 prefixes with `g>=h`. At cap `12`, it checks
`4,790,826` legal states with `Delta_5>0`; there are no failures of
`f>e`, and the minimum value of `Delta_4` under `Delta_5>0` is `5`, attained
at

`P=(1,2,2,2,2,1)` and `Q=(1,2,3,3,3,3,1)`.

The `(5,6)` proof is now reduced to the two rightmost central implications
`Delta_6>0 => Delta_5>=0` and `Delta_7>0 => Delta_6>=0`.

### Proof of `Delta_6>0 => Delta_5>=0`

Keep

`A=a-1`, `B=b-1`, `C=c-1`, `D=d-1`, `E=e-1`,

and

`n=f-e`, `r=g-f`, `s=h-g`, `t=i-h`.

Then

`Delta_5=Dn+Cr+Bs+At`.

Also, since `i=1+E+n+r+s+t`,

`Delta_6=Dr+Cs+Bt-A(i-1)-E-1`.

Thus `Delta_6>0` implies

`K:=Dr+Cs+Bt>0`.

As above, the shifted weights satisfy

`B^2>=AC`, `C^2>=BD`, and `BC>=AD`.

The log-concavity of `Q` says that the ratios

`f/e`, `g/f`, `h/g`, `i/h`

are nonincreasing, so the signs of `n,r,s,t` have at most one change from
nonnegative to nonpositive. Also `t<=0`.

If `s>=0`, then `n,r,s>=0`. Put `T=-t>=0`. Since `K>0`,

`BT<Dr+Cs`.

Here `B>0`, because otherwise `b=1` forces `a=c=d=1`, which would give
`K=0`. Hence

`Delta_5=Dn+Cr+Bs-AT`

`>Dn+(C-AD/B)r+(B-AC/B)s>=0`,

using `BC>=AD` and `B^2>=AC`.

It remains to handle `s<0`. Put `S=-s>0` and again `T=-t>=0`. If `r<0`,
then `K=Dr-CS-BT<=0`, impossible. Thus `r>=0`, and `K>0` gives

`CS+BT<Dr`.

In particular `D>0`. By `C^2>=BD` and `BC>=AD`,

`BS+AT<=(C/D)(CS+BT)<Cr`.

Therefore

`Delta_5=Dn+Cr-BS-AT>Dn>=0`.

This proves `Delta_6>0 => Delta_5>=0`.

The exact verifier `notes/verify_56_delta6.py` checks these formulas directly
on the full degree `(5,6)` space. At cap `12`, it checks `67,671` states with
`Delta_6>0`; the minimum value of `Delta_5` is `10`.

The `(5,6)` proof is now reduced to the final central implication

`Delta_7>0 => Delta_6>=0`.

### Proof of `Delta_7>0 => Delta_6>=0`

In the same notation,

`Delta_7=Ds+Ct-B(i-1)-A-E-n-1`.

Write `T=-t=h-i>=0`. If `Delta_7>0`, then

`Ds>CT+B(i-1)+A+E+n+1`,

so in particular `s>0` and `D>0`. The log-concavity inequality
`g^2>=fh`, with `h=g+s`, forces `r=g-f>0`.

We first record a useful consequence:

`Dr>=E+1`.

Indeed, suppose instead that `Dr<=E`. From `g^2>=fh` we have

`s<=rg/f`,

and from `f^2>=eg`, with `e=E+1` and `g=f+r`, we have

`Er/f < n`.

Therefore

`Ds<=Dr(g/f)<=E(1+r/f)<E+n`,

contradicting `Ds>E+n+1` from `Delta_7>0`.

Now use `Delta_7>0` to bound `T`. Since `C>0` as well (`D>0` and `d<=c`),

`CT<Ds-B(i-1)-A-E-n-1`.

Multiplying by `B/C` and substituting in

`Delta_6=Dr+Cs-BT-A(i-1)-E-1`

gives

`Delta_6>Dr+(C-BD/C)s+(B^2/C-A)(i-1)+B(A+E+n+1)/C-E-1`.

The middle two coefficients are nonnegative by `C^2>=BD` and `B^2>=AC`, and
the `B(A+E+n+1)/C` term is nonnegative. Hence

`Delta_6>Dr-E-1>=0`.

This proves the final implication `Delta_7>0 => Delta_6>=0`.

The exact verifier `notes/verify_56_delta7.py` checks the displayed formulas.
There are no cap-12 exhaustive states with `Delta_7>0`, but a random scan with
`200,000` trials, first coefficient cap `500`, and seed `21` found `65,203`
states with `Delta_7>0`; the minimum observed `Delta_6` in those states was
`26,201`.

Combining

`Delta_3>0 => Delta_2>=0`,

`Delta_4>0 => Delta_3>=0`,

`Delta_5>0 => Delta_4>=0`,

`Delta_6>0 => Delta_5>=0`,

and

`Delta_7>0 => Delta_6>=0`,

there cannot be a positive central difference after a negative central
difference. Since the first two rises and final three drops were already
automatic, the degree `(5,6)` monic product case is unimodal.

## Degree `(6,6)` proof start

Let

`P=(1,a,b,c,d,e,1)`

and

`Q=(1,f,g,h,i,j,1)`.

After the first two automatic rises and final three automatic drops, the
central differences are `Delta_2,...,Delta_8`:

`Delta_2=-af+ag+bf-b+c-g+h`,

`Delta_3=-ag+ah-bf+bg+cf-c+d-h+i`,

`Delta_4=-ah+ai-bg+bh-cf+cg+df-d+e-i+j`,

`Delta_5=-ai+aj-bh+bi-cg+ch-df+dg+ef-e-j+2`,

`Delta_6=-aj+a-bi+bj-ch+ci-dg+dh-ef+eg+f-2`,

`Delta_7=-a-bj+b-ci+cj-dh+di-eg+eh-f+g`,

and

`Delta_8=-b-cj+c-di+dj-eh+ei-g+h`.

Thus the sign-chain target has six adjacent implications:

`Delta_3>0 => Delta_2>=0`,

`Delta_4>0 => Delta_3>=0`,

`Delta_5>0 => Delta_4>=0`,

`Delta_6>0 => Delta_5>=0`,

`Delta_7>0 => Delta_6>=0`,

and

`Delta_8>0 => Delta_7>=0`.

The first implication is inherited from the `(5,5)` proof of `B>0=>A>=0`.
The formulas for `Delta_2` and `Delta_3` only use the first four interior
coefficients of each factor, and that proof only needs the log-concavity
inequalities through `c^2>=bd` and `h^2>=gi`, not the degree-5 final-tail
condition.

The exact verifier `notes/verify_66_implications.py` checks the six adjacent
implications directly. At cap `10`, it checks `4,074,085` unordered pairs of
degree-6 factors and finds no failure. The adjacent minima are:

- `Delta_3>0 => Delta_2>=0`: minimum `1`;
- `Delta_4>0 => Delta_3>=0`: minimum `1`;
- `Delta_5>0 => Delta_4>=0`: minimum `1`;
- `Delta_6>0 => Delta_5>=0`: minimum `9`;
- `Delta_7>0 => Delta_6>=0`: minimum `16`;
- `Delta_8>0 => Delta_7>=0`: no cap-10 states with `Delta_8>0`.

Large random examples do have `Delta_8>0`, so the final implication is not
vacuous. With `200,000` random pairs, first coefficient cap `1000`, and seed
`66`, the verifier found `68,362` states with `Delta_8>0`; the minimum
observed `Delta_7` in those states was `1,031,642`. One explicit example is

`P=(1,73,2556,56963,516424,412591,1)`

and

`Q=(1,457,77082,4296441,231253467,210264873,1)`

have central differences

`11035483, 757315285, 31932247718, 858466203436, 15069749928164, 117213914527891, 70824098959577`.

### Proof of `Delta_8>0 => Delta_7>=0`

Put

`A=a-1`, `B=b-1`, `C=c-1`, `D=d-1`, `E=e-1`,

and

`F=f-1`, `n=g-f`, `r=h-g`, `s=i-h`, `t=j-i`.

Let `T=-t=i-j>=0`. Then

`j-1=F+n+r+s-T`,

and the two rightmost central differences are

`Delta_7=Ds-CT-B(j-1)+Er-A-f`,

and

`Delta_8=Es-DT-C(j-1)-B-g`.

If `Delta_8>0`, then

`Es>DT+C(j-1)+B+g`,

so in particular `s>0`, `E>0`, and `D>0`. Since `s>0`, the log-concavity
inequality `h^2>=gi`, with `i=h+s`, forces `r=h-g>0`.

We first prove

`Er>f`.

Indeed, `Delta_8>0` gives `Es>g`. Also `h^2>=gi` gives `s<=hr/g`, and
`g^2>=fh` gives `g^2/h>=f`. Therefore

`Er>g^2/h>=f`.

Now use `Delta_8>0` to bound `T`:

`DT<Es-C(j-1)-B-g`.

Substituting this into `Delta_7` gives

`Delta_7>Ds-(C/D)(Es-C(j-1)-B-g)-B(j-1)+Er-A-f`

`=(D-CE/D)s+(C^2/D-B)(j-1)+CB/D+Cg/D+Er-A-f`.

The first two coefficients are nonnegative by shifted log-concavity,
`D^2>=CE` and `C^2>=BD`. Also `CB>=AD`, so `CB/D>=A`. Hence

`Delta_7>Er-f+Cg/D>0`.

This proves `Delta_8>0 => Delta_7>=0`.

### Proof of `Delta_7>0 => Delta_6>=0`

Keep the same notation, and put `J=j-1=F+n+r+s-T`. The relevant differences
are

`Delta_6=Dr+Cs-BT-AJ+En-1`

and

`Delta_7=Ds-CT-BJ+Er-A-f`.

By the shifted-ratio lemmas, we will use

`B^2>=AC`, `C^2>=BD`, and `D^2>=CE`,

together with their ratio consequences

`CD>=BE` and `BD>=AE`.

Assume first that `s>=0`. If `C=0`, then `c=1`, and log-concavity forces
`a=b=d=e=1`; this would give `Delta_7=-f<0`. Hence `C>0`, and then
`B>0` as well. Since `Delta_7>0`,

`CT<Ds+Er-BJ-A-f`.

Multiplying by `B/C` and substituting in `Delta_6` gives

`Delta_6>(D-BE/C)r+(C-BD/C)s+(B^2/C-A)J+En+B(A+f)/C-1`.

All three displayed coefficients are nonnegative by `CD>=BE`, `C^2>=BD`,
and `B^2>=AC`. Also `B(A+f)/C>0`. Therefore `Delta_6>-1`, and since
`Delta_6` is an integer, `Delta_6>=0`.

It remains to handle `s<0`. Write `S=-s>0`. Then

`Delta_7=-DS-CT-BJ+Er-A-f>0`,

so `E>0` and `r>0`. The ratio monotonicity of the log-concave sequence
`Q` then gives `n>0`. Also, by adjacent-ratio transfer,

`CS+BT+AJ<=(D/E)(DS+CT+BJ)`.

Using the strict inequality from `Delta_7>0`, we get

`CS+BT+AJ<(D/E)(Er-A-f)=Dr-D(A+f)/E`.

Thus

`Delta_6=Dr+En-CS-BT-AJ-1`

`>En+D(A+f)/E-1>=0`.

This proves `Delta_7>0 => Delta_6>=0`.

### Proof of `Delta_6>0 => Delta_5>=0`

Again keep the same notation. Now

`Delta_5=Dn+Cr+Bs-AT+EF+1`

and

`Delta_6=Dr+Cs-BT-AJ+En-1`.

Assume first that `s>=0`. Then the one-sign-change property for the
differences of `Q` gives `n,r>=0`. Also `B>0`; otherwise log-concavity forces
`a=b=c=d=e=1`, which would give `Delta_6=-1`. Since `Delta_6>0`,

`BT<Dr+Cs+En`.

Therefore

`AT<=(A/B)(Dr+Cs+En)`,

and hence

`Delta_5>=(D-AE/B)n+(C-AD/B)r+(B-AC/B)s+EF+1`.

The three coefficients are nonnegative by `BD>=AE`, `BC>=AD`, and
`B^2>=AC`, so `Delta_5>0`.

Next suppose `s<0`, and write `S=-s>0`. If `r>=0`, then again `n>=0`. The
inequality `Delta_6>0` gives

`CS+BT<Dr+En-AJ-1`.

Here `D>0`, and adjacent-ratio transfer gives

`BS+AT<=(C/D)(CS+BT)`.

Thus

`BS+AT<(C/D)(Dr+En-AJ-1)`,

so

`Delta_5=Dn+Cr-BS-AT+EF+1`

`>(D-CE/D)n+EF+1+(C/D)(AJ+1)>0`,

using `D^2>=CE`.

Finally suppose `r<0`; write `R=-r>0`. Then `Delta_6>0` forces `E>0` and
`n>0`, and

`DR+CS+BT<En-AJ-1`.

By adjacent-ratio transfer,

`CR+BS+AT<=(D/E)(DR+CS+BT)`.

Therefore

`CR+BS+AT<(D/E)(En-AJ-1)=Dn-(D/E)(AJ+1)`,

and

`Delta_5=Dn-CR-BS-AT+EF+1>(D/E)(AJ+1)+EF+1>0`.

This proves `Delta_6>0 => Delta_5>=0`.

### Proof of `Delta_5>0 => Delta_4>=0`

The next pair of differences is

`Delta_4=Cn+Br+As+DF+E+J+1`

and

`Delta_5=Dn+Cr+Bs-AT+EF+1`.

If `s>=0`, then the one-sign-change property gives `n,r>=0`, so
`Delta_4>=DF+E+J+1>0`.

Now suppose `s<0`, and write `S=-s>0`. Since `Delta_5>0` is integral, each
case below gives a non-strict budget without the final `+1`.

First let `r>=0`; then `n>=0`, and

`BS+AT<=Dn+Cr+EF`.

If `B=0`, log-concavity forces `A=C=D=E=0`, so `Delta_4=J+1>0`. Otherwise,
adjacent-ratio transfer gives

`AS<=(A/B)(BS+AT)<=(A/B)(Dn+Cr+EF)<=Cn+Br+DF`.

Hence

`Delta_4=Cn+Br-AS+DF+E+J+1>=E+J+1>0`.

Next let `r<0` but `n>=0`, and write `R=-r>0`. Then

`CR+BS+AT<=Dn+EF`.

If `C=0`, log-concavity forces `A=B=D=E=0`, so again `Delta_4=J+1>0`.
Otherwise, adjacent-ratio transfer gives

`BR+AS<=(B/C)(CR+BS)<=(B/C)(Dn+EF)<=Cn+DF`.

Therefore

`Delta_4=Cn-BR-AS+DF+E+J+1>=E+J+1>0`.

Finally let `n<0`, and write `N=-n>0` and `R=-r>0`. Then

`DN+CR+BS+AT<=EF`.

If `D=0`, then `E=0`, and this budget forces `A=B=C=0`; hence
`Delta_4=J+1>0`. Otherwise, adjacent-ratio transfer gives

`CN+BR+AS<=(C/D)(DN+CR+BS)<=(C/D)EF<=DF`.

Thus

`Delta_4=-CN-BR-AS+DF+E+J+1>=E+J+1>0`.

This proves `Delta_5>0 => Delta_4>=0`.

### Proof of `Delta_4>0 => Delta_3>=0`

This is the same simultaneous-deficit argument used in the `(5,6)` proof, with
one extra tail budget term.

Put

`x=b-c`, `y=g-h`, `u=c-d`, `v=h-i`, and `T=i-j`.

Then

`Delta_3=bg-ay-fx-u-v`

and

`Delta_4=ch-c+1+E-xy-(f-1)u-av-T`.

First suppose `y<=0`, i.e. `h>=g`. Then `g>=f`: if `h>g`, this follows from
`g^2>=fh`, and if `h=g`, it is immediate from the same inequality. Rewriting

`Delta_3=a(h-g)+b(g-f)+c(f-1)+d-v`,

and using `v<=h-1`, gives `Delta_3>=1`.

Next suppose `y>0` but `x<=0`, i.e. `c>=b`. Then `b>=a`, since `b^2>=ac`
and `c>=b`. Rewriting

`Delta_3=b(h-1)+(c-b)(f-1)+(b-a)y+d-v`,

and again using `v<=h-1`, gives `Delta_3>=1`.

It remains to handle the simultaneous-deficit case `x>0` and `y>0`. Then
`u,v>=1`. Also `e<=d=c-u`, so

`E=e-1<=c-u-1`.

Since `Delta_4>0` and all quantities are integral,

`(f-1)u+av+T<=c(h-1)+E-xy`.

Let `S=c(h-1)-xy`. Since `av=(a-1)v+v`, this gives

`(f-1)u+(a-1)v<=S+E-T-v<=S+E-v`.

The log-concavity inequalities `c^2>=bd` and `h^2>=gi` give

`u(c+x)>=cx`

and

`v(h+y)>=hy`.

Let

`M=max(x/u,y/v)`.

Then

`(a-1)y+(f-1)x<=M((f-1)u+(a-1)v)<=M(S+E-v)`.

Thus it is enough to prove

`M(S+E-v)+x+y+u+v<=bg`.

If `M=x/u`, then `x/u<=b/c`. It is enough to prove

`(b/c)(S+E-v)+x+y+u+v<=bg`.

After multiplying by `c`, the residual is

`cbg-b(S-v)-c(x+y+u+v)-bE`.

Using `E<=c-u-1`, this is at least

`vx+c^2y+2cxy-cx-cy+c+ux+x^2y+x`,

which is positive for `x,y,u,v>=1`.

If `M=y/v`, then `y/v<=g/h`. It is enough to prove

`(g/h)(S+E-v)+x+y+u+v<=bg`.

After multiplying by `h`, the residual is

`hbg-g(S-v)-h(x+y+u+v)-gE`.

Again using `E<=c-u-1`, this is at least

`vy+h^2x+2hxy-hx-hy+h+uy+xy^2+y`,

which is positive for `x,y,u,v>=1`.

Therefore `ay+fx+u+v<=bg`, i.e. `Delta_3>=0`. This proves
`Delta_4>0 => Delta_3>=0`.

Combining the inherited implication

`Delta_3>0 => Delta_2>=0`

with

`Delta_4>0 => Delta_3>=0`,

`Delta_5>0 => Delta_4>=0`,

`Delta_6>0 => Delta_5>=0`,

`Delta_7>0 => Delta_6>=0`,

and

`Delta_8>0 => Delta_7>=0`,

there cannot be a positive central difference after a negative central
difference. Since the first two rises and final three drops are automatic, the
degree `(6,6)` monic product case is unimodal.

## Degree-independent reduction

Let `C_m` be the class of positive integer sequences

`P=(p_0,p_1,...,p_m)`

with `p_0=p_m=1`, satisfying

`p_i^2>=p_{i-1}p_{i+1}` for `1<=i<=m-2`,

and the final-tail condition

`p_{m-2}>=p_{m-1}`.

Thus `P` may fail log-concavity only at the final center `p_{m-1}`.

Let `Q=(q_0,...,q_n)` be another such sequence, and let

`R_k=sum_i p_i q_{k-i}`

be the coefficients of the product. Put `N=m+n`, and write

`D_k=R_{k+1}-R_k`.

The first two rises are automatic:

`D_0=p_1+q_1-1>=0`,

and

`D_1=(p_1-1)(q_1-1)+p_2+q_2-1>=0`.

The final three drops are automatic as well. In drop-margin form,

`R_{N-1}-R_N=p_{m-1}+q_{n-1}-1>=0`,

`R_{N-2}-R_{N-1}=(p_{m-2}-p_{m-1})+(q_{n-2}-q_{n-1})+p_{m-1}q_{n-1}>=0`,

and

`R_{N-3}-R_{N-2}`

`=p_{m-3}+q_{n-3}-1+(p_{m-2}-p_{m-1})(q_{n-1}-1)+(p_{m-1}-1)(q_{n-2}-1)>=0`.

So product unimodality is reduced to ruling out a valley among

`D_2,D_3,...,D_{N-4}`.

Extend `q_j` by `0` outside `0<=j<=n`, and put

`delta_j=q_{j+1}-q_j`.

Then the product differences have the convolution form

`D_k=sum_{i=0}^m p_i delta_{k-i}`.

The sequence `delta_j` has at most one sign change from nonnegative to
nonpositive. This follows from the ratio monotonicity

`q_1/q_0 >= q_2/q_1 >= ... >= q_{n-1}/q_{n-2}`,

together with `q_{n-2}>=q_{n-1}>=q_n=1`.

Therefore the remaining degree-independent target is the adjacent implication

`D_{k+1}>0 => D_k>=0`

for every `2<=k<=N-4`.

### Fully log-concave sliding lemma

The obstruction is now isolated. If the kernel `P` were fully log-concave,
including the final inequality `p_{m-1}^2>=p_{m-2}`, then the adjacent
implication would follow immediately.

Indeed, let `W=(w_0,...,w_m)` be positive and log-concave, and let
`eta_j` have one sign change from nonnegative to nonpositive. Define

`S_k=sum_i w_i eta_{k-i}`.

We prove `S_{k+1}>0 => S_k>=0`. Set

`theta_i=eta_{k+1-i}`.

Then `theta_i` has one sign change in the opposite direction: it is
nonpositive for small `i` and nonnegative for large `i`. Also

`S_{k+1}=sum_i w_i theta_i`,

while `S_k` is the same signed sum with weights shifted from `w_i` to
`w_{i-1}`, plus a nonnegative-side boundary term and with a nonpositive-side
boundary term removed.

Since `W` is log-concave, the ratios `w_{i-1}/w_i` are nondecreasing in `i`.
Thus the shift multiplies the nonnegative-side terms by at least as large a
factor as the nonpositive-side terms. A positive signed sum therefore remains
nonnegative after the shift.

This is the degree-independent version of the adjacent-ratio transfer used in
the `(5,6)` and `(6,6)` proofs.

### Endpoint-defect target

For sequences in `C_m`, the prefix

`(p_0,p_1,...,p_{m-1})`

is fully log-concave. The only failure of the sliding lemma can come from the
last monic endpoint `p_m=1`. Equivalently,

`D_k=sum_{i=0}^{m-1}p_i delta_{k-i}+delta_{k-m}`.

The first sum is controlled by the fully log-concave sliding lemma. The
remaining work is to prove that the endpoint term `delta_{k-m}` cannot create
a new positive difference after a negative one. This is exactly what the
right-tail shifted-budget arguments did by hand in the finite `(5,6)` and
`(6,6)` cases.

So the infinite staircase has been replaced by a single endpoint-defect
lemma:

For all `P in C_m`, all `Q in C_n`, and all `k`,

`sum_{i=0}^m p_i delta_{k+1-i}>0`

implies

`sum_{i=0}^m p_i delta_{k-i}>=0`.

The next proof task is to prove this endpoint-defect lemma directly, using the
final-tail inequalities of both factors and the shifted-ratio transfer rule.

### Endpoint-defect proof start

Fix `k`, and put `j=k-m`. If the final endpoint of `P` already satisfies

`p_{m-1}^2>=p_{m-2}`,

then `P` is fully log-concave and the sliding lemma proves
`D_{k+1}>0 => D_k>=0`. Thus assume

`p_{m-1}^2<p_{m-2}`.

Let

`lambda=p_{m-1}^2/p_{m-2}`

and

`epsilon=1-lambda>0`.

Replace the final endpoint `p_m=1` by `lambda`, and define

`W=(p_0,p_1,...,p_{m-1},lambda)`.

Then `W` is fully log-concave, with equality at the final log-concavity
inequality. Put

`S_k=sum_{i=0}^{m-1}p_i delta_{k-i}+lambda delta_{k-m}`.

Then

`D_k=S_k+epsilon delta_j`

and

`D_{k+1}=S_{k+1}+epsilon delta_{j+1}`.

This proves the endpoint-defect lemma in one important case. Suppose
`D_{k+1}>0` and `delta_{j+1}<=0`. First, `delta_j` cannot be negative:
if `delta_j<0`, then the one-sign-change property makes every
`delta_t` with `t>=j` nonpositive, and all terms in `D_{k+1}` would be
nonpositive. Hence `delta_j>=0`.

Since `delta_{j+1}<=0`,

`S_{k+1}=D_{k+1}-epsilon delta_{j+1}>0`.

The fully log-concave sliding lemma applied to `W` gives `S_k>=0`. Therefore

`D_k=S_k+epsilon delta_j>=0`.

So the only remaining case is

`delta_{j+1}>0`.

In this case the endpoint perturbation may be responsible for making
`D_{k+1}` positive. The problem becomes a local boundary-assisted sliding
statement. Put

`theta_i=delta_{k+1-i}` for `0<=i<=m+1`.

Then `theta_i` is nonpositive for small `i` and nonnegative for large `i`,
while

`D_{k+1}=sum_{i=0}^m p_i theta_i`

and

`D_k=theta_{m+1}+sum_{i=1}^m p_{i-1}theta_i`.

The remaining target is therefore:

if `theta_m>0` and `sum_{i=0}^m p_i theta_i>0`, then

`theta_{m+1}+sum_{i=1}^m p_{i-1}theta_i>=0`.

This local statement is where the full log-concavity of `Q`, not just the
one-sign-change property of its difference sequence, still has to be used.

We can prove most of this local statement by the same ratio-transfer argument.
Let `t` be the first index with `theta_t>0`. Put

`r=theta_m`, `n=theta_{m+1}`, `y=p_{m-1}`,

and

`N_0=max(0,-theta_0)`.

Also put

`C=sum_{i=1}^{m-1}p_i theta_i=D_{k+1}+N_0-r`.

This is the middle contribution to `D_{k+1}`, excluding the left boundary
`theta_0` and the endpoint term `theta_m`.

For `1<=i<=m-1`, let

`rho_i=p_{i-1}/p_i`.

The prefix `(p_0,...,p_{m-1})` is log-concave, so the `rho_i` are
nondecreasing. Define

`L=0` if `t<=1`, and `L=rho_{t-1}` otherwise.

Thus `L` is the largest shifted ratio on the nonpositive middle block. If
`U` is the smallest shifted ratio on the positive middle block, then
`L<=U`, and adjacent-ratio transfer gives

`sum_{i=1}^{m-1}p_{i-1}theta_i>=alpha C`

for any `alpha` in `[L,U]`. Hence

`D_k=n+y r+sum_{i=1}^{m-1}p_{i-1}theta_i>=n+y r+alpha C`.

If `C>=0`, choose `alpha=U`. Then `D_k>=n+y r>0`.

If `C<0` and `L<=y`, choose `alpha=L`. Since `D_{k+1}>0` is integral,

`C+r-N_0=D_{k+1}>=1`,

so `C>=N_0+1-r`. Therefore

`D_k>=n+y r+LC>=n+y r+L(N_0+1-r)`

`=n+L(N_0+1)+(y-L)r>=0`.

Thus the hard case is now reduced to showing that the double-bad subcase

`C<0` and `L>y`

cannot occur together with `D_{k+1}>0`.

Diagnostic scans split the adjacent-positive states into the proved case
`delta_{j+1}<=0` and this remaining hard case, with no observed violation of
`delta_j>=0`:

- `(5,6)` at cap `8`: `493,818` proved-case states and `554,422` hard states;
- `(6,6)` at cap `8`: `932,046` proved-case states and `295,007` hard states;
- `(6,7)` at cap `7`: `624,156` proved-case states and `340,055` hard states;
- `(7,7)` at cap `6`: `122,192` proved-case states and `24,770` hard states.

There is a stronger boundary-domination form of the remaining target:

if `C<0` and `L>y`, then

`D_{k+1}=theta_0+C+r<=0`.

This would immediately exclude the only unproved subcase. The verifier
`notes/verify_boundary_domination.py` checks this stronger form directly. It
passes:

- `(5,6)` at cap `8`: `297,371` double-bad local states;
- `(6,6)` at cap `8`: `341,507` double-bad local states;
- `(6,7)` at cap `7`: `248,684` double-bad local states;
- `(7,7)` at cap `6`: `36,181` double-bad local states;
- random `(8,9)` with `100,000` trials, first cap `2000`, seed `891`:
  `5,577` double-bad local states;
- random `(10,12)` with `100,000` trials, first cap `2000`, seed `1012`:
  `14,983` double-bad local states.

There is also a first reduction inside the double-bad target. Since `L>y>=1`,
we necessarily have `t>=2`, and therefore `theta_0<=0`. Since `C<0` and all
data are integral, `C<=-1`. Hence whenever

`theta_0+r<=1`,

we already get

`D_{k+1}=theta_0+C+r<=0`.

So the remaining boundary-domination proof only has to treat states with
`theta_0+r>=2`, where the endpoint rise is too large to be absorbed by the
unit integrality gap alone. The verifier now reports this split with
`--classify`. The bounded exact checks divide as follows:

- `(5,6)` at cap `8`: `163,098` trivial endpoint-sum states and `134,273`
  states still needing weighted domination;
- `(6,6)` at cap `8`: `140,508` trivial endpoint-sum states and `200,999`
  states still needing weighted domination;
- `(6,7)` at cap `7`: `166,986` trivial endpoint-sum states and `81,698`
  states still needing weighted domination;
- `(7,7)` at cap `6`: `19,447` trivial endpoint-sum states and `16,734`
  states still needing weighted domination.

In these same exact checks, the residual weighted-domination states have
strict spare room: the largest value of `D_{k+1}` among residual states is
`-2`, `-4`, `-2`, and `-3`, respectively. Thus the computational evidence now
points to a stronger residual inequality, not a tight boundary case.

A promising way to attack this residual inequality is to separate off the two
monic endpoint spikes. Define

`U_i=p_i-1` for `0<=i<=m`, so `U_0=U_m=0`,

and similarly define `V_i=q_i-1`. By the shifted-ratio lemma, `U` and `V` are
fully log-concave sequences with endpoint zeros. Thus

`P=(1+x^m)+U`, `Q=(1+x^n)+V`,

and

`PQ=(1+x^m)(1+x^n)+(1+x^m)V+(1+x^n)U+UV`.

The term `UV` is fully log-concave by Hoggar's convolution theorem. The
remaining problem is therefore not arbitrary endpoint-defective convolution:
it is the synchronization of two endpoint-spike translates against fully
log-concave shifted interiors. The residual condition `theta_0+r>=2` is exactly
where the endpoint-spike part contributes a genuine rise, so this decomposition
looks aligned with the last gap.

There is an even sharper local split. Since `p_i=1+(p_i-1)` for
`1<=i<=m-1`,

`D_{k+1}=sum_{i=0}^m theta_i + sum_{i=1}^{m-1}(p_i-1)theta_i`.

The first term telescopes to

`q_{k+2}-q_{k+1-m}`.

The second term is the contribution of the shifted interior of `P`. The
verifier now records both terms. In every checked double-bad state, the shifted
middle contribution is nonpositive:

- `(5,6)` at cap `8`: `297,371 / 297,371`;
- `(6,6)` at cap `8`: `341,507 / 341,507`;
- `(6,7)` at cap `7`: `248,684 / 248,684`;
- `(7,7)` at cap `6`: `36,181 / 36,181`;
- random `(8,9)` with `100,000` trials: `5,577 / 5,577`;
- random `(10,12)` with `100,000` trials: `14,983 / 14,983`.

Thus, if `q_{k+2}<=q_{k+1-m}`, the boundary-domination target follows from
this shifted-middle inequality alone. The only states needing a quantitative
version of the shifted-middle bound are those with a positive unweighted
window:

- `(5,6)` at cap `8`: `11,143`;
- `(6,6)` at cap `8`: `38,816`;
- `(6,7)` at cap `7`: `11,487`;
- `(7,7)` at cap `6`: `5,105`;
- random `(8,9)` with `100,000` trials: `16`;
- random `(10,12)` with `100,000` trials: `117`.

This is a much smaller and more structured residual. In `x_i=q_{k+2-i}`
notation, the residual says that `x_0>x_{m+1}` even though the peak of the
log-concave `x`-window lies at or after `i=t`, while the `P` weights have
already entered their forced decreasing tail at `t-1`.

The same split can be expressed more cleanly by writing

`A_m=(1,1,...,1)`, `P=A_m+U`, `Q=A_n+V`,

where `U_i=p_i-1` and `V_i=q_i-1`. Then

`PQ=A_mQ+UA_n+UV`.

In the endpoint-defect case `theta_m=delta_{k+1-m}>0`, we have
`k>=m-2`, so the difference of `UA_n` at this location is nonpositive: it is
just a sliding-sum window of `U` whose right endpoint has already passed the
support of `U`. More explicitly, if `ell=k+1`, then the `ell`th coefficient
of `UA_n` is

`sum_{i=max(1,ell-n)}^{min(m-1,ell)} U_i`.

Since `ell>=m-1`, increasing `ell` by one cannot add a new right-end term. It
can only remove the left-end term `U_{ell-n}`, so

`Delta_ell(UA_n)=-U_{ell-n}<=0`,

with the convention that out-of-range `U` terms are zero. Therefore the
remaining double-bad target follows from

`Delta(A_mQ)+Delta(UV)<=0`.

This core inequality now passes exactly in every checked double-bad state:

- `(5,6)` at cap `8`: `297,371 / 297,371`;
- `(6,6)` at cap `8`: `341,507 / 341,507`;
- `(6,7)` at cap `7`: `248,684 / 248,684`;
- `(7,7)` at cap `6`: `36,181 / 36,181`;
- random `(8,9)` with `100,000` trials: `5,577 / 5,577`;
- random `(10,12)` with `100,000` trials: `14,983 / 14,983`.

This is now the sharp proof target: prove the core inequality for the
all-ones window convolved with `Q` and the product of the two fully
log-concave shifted interiors `U` and `V`.

Equivalently, prove the contrapositive:

if the core difference `Delta(A_mQ)+Delta(UV)` is positive and the middle
contribution `C` is negative, then `L<=y`.

This is exactly the case already handled by the ratio-transfer argument above.
The exact scans support the contrapositive strongly. Among states with
`C<0` and positive core difference, the largest observed `L/y` values were:

- `(5,6)` at cap `8`: `2/3`;
- `(6,6)` at cap `8`: `2/3`;
- `(6,7)` at cap `7`: `4/5`;
- `(7,7)` at cap `6`: `1/3`.

So positive core does not merely fail to coexist with `L>y`; in the checked
range it occurs only when the sign-change boundary is still on an increasing
part of `P`.

The verifier option `--core-contrapositive` checks this target directly,
without first restricting to the double-bad branch. It reports the number of
local states with `C<0` and positive core difference, plus the maximum observed
value of `L/y`. The exact checks above are reproduced by:

- `uv run python notes/verify_boundary_domination.py 5 6 --cap 8 --core-contrapositive`
- `uv run python notes/verify_boundary_domination.py 6 6 --cap 8 --core-contrapositive`
- `uv run python notes/verify_boundary_domination.py 6 7 --cap 7 --core-contrapositive`
- `uv run python notes/verify_boundary_domination.py 7 7 --cap 6 --core-contrapositive`

Random larger-degree checks also pass. One `(10,12)` random scan found the
expected equality case `L/y=1`: the first factor was the all-ones polynomial,
so `U=0`, the core reduced to `Delta(A_mQ)>0`, and the already-proved
`L<=y` branch applies with equality. Thus the remaining proof should aim for
the exact implication `core>0 and C<0 => L<=y`, not a stricter `L<y`.

There is a slightly stronger double-bad form that looks more natural for the
final proof. In the branch `C<0` and `L>y`, the core difference appears to
satisfy

`Delta(A_mQ)+Delta(UV)<=1-y`.

Since `y=p_{m-1}>=1`, this implies the needed core inequality. It is sharp:
for `y=1` the core can be `0`, and for `y=2` the core can be `-1`. The
verifier now treats a violation of this stronger bound as a failure inside the
double-bad scan. It passes all of the exact and random checks listed above.

In local variables, this target is

`sum_{i=0}^m theta_i + sum_{i=1}^{m-1}(p_i-1)(V_{k+2-i}-V_{k+1-i}) <= 1-p_{m-1}`,

under the assumptions `C=sum_{i=1}^{m-1}p_i theta_i<0` and
`p_{t-2}/p_{t-1}>p_{m-1}`. This is currently the best isolated algebraic
lemma: it contains the integrality gain from the strict inequality `L>y`,
whereas the earlier contrapositive only used it qualitatively.

One more useful normalization is to keep `Q=A_n+V`, where
`V_i=q_i-1`. Then

`A_mQ+UV=A_mA_n+PV`.

Thus the core difference is

`Delta(PV)+E`,

where `E=Delta(A_mA_n)`. If `m<=n` and `ell=k+1>=m-1`, then

- `E=1` only at `ell=m-1`;
- `E=0` for `m<=ell<n`;
- `E=-1` for `n<=ell<m+n`.

This corrects the tempting endpoint-spike formula
`Delta(A_m(1+x^n))`: that formula misses the interior all-ones window of
`A_n`, and is not the core term being checked by
`notes/verify_boundary_domination.py`.

With this correction, the core-only target is still true in all checked
adjacent-degree cases, but it is false once the degree gap is at least two.
For example, with

`P=(1,2,2,2,1,1)`, `Q=(1,5,5,5,5,4,3,1)`, and `k=4`,

we have `m=5`, `n=7`,

`theta=(-1,-1,0,0,0,4)`, `C=-2`, `L=2`, `y=1`,

and the core difference is `1>1-y=0`. This is not a counterexample to the
actual adjacent implication: the product differences are

`(6,10,10,9,4,1,-6,-9,-9,-8,-5,-3)`,

so `D_5=1>0` is safely preceded by `D_4=4`.

The verifier has therefore been adjusted to check the actual boundary
statement in the double-bad branch:

`D_{k+1}>0 => D_k>=0`.

The old stronger claim, "double-bad forces `D_{k+1}<=0`", remains valid in
the checked equal and adjacent degree cases:

- `(5,5)` at cap `8`: no positive-next double-bad states;
- `(5,6)` at cap `8`: no positive-next double-bad states;
- `(6,6)` at cap `8`: no positive-next double-bad states;
- `(6,7)` at cap `7`: no positive-next double-bad states;
- `(8,9)` at cap `5`: no positive-next double-bad states.

For degree gap at least two, exact scans show a very narrow exception. The
only positive-next double-bad states occur at `k=m-1`, the first plateau index
of `A_mA_n`, and all are already protected by a positive previous difference:

- `(5,7)` at cap `7`: `342` positive-next states, minimum previous
  difference `4`;
- `(6,8)` at cap `6`: `182` positive-next states, minimum previous
  difference `4`;
- `(7,9)` at cap `5`: `34` positive-next states, minimum previous
  difference `4`;
- `(8,10)` at cap `5`: `40` positive-next states, minimum previous
  difference `4`.

Random scans with larger coefficients found no positive-next double-bad states
for `(8,10)`, `(8,11)`, `(10,12)`, `(10,15)`, or `(15,20)` in `100,000`
trials each. Thus the next proof target is now more precise:

1. prove the old core bound, or directly prove `D_{k+1}<=0`, for every
   double-bad state except the early plateau index `k=m-1`;
2. prove the early plateau sublemma: if `n>=m+2`, `k=m-1`,
   `C<0`, `L>y`, and `D_m>0`, then `D_{m-1}>=0`.

The early plateau sublemma has an especially concrete form. At `k=m-1`,

`theta_{m+1}=1`.

The previous difference is

`D_{m-1}=1+sum_{i=1}^m p_{i-1}theta_i`.

Thus the exact target is the truncated previous-difference inequality

`sum_{i=1}^m p_{i-1}theta_i>=0`.

This is slightly stronger than needed, since `D_{m-1}` only requires the left
side to be at least `-1`.

There is a tempting sufficient condition. Since

`D_{m-1}-D_m=1-theta_0+
sum_{i=1}^{m-1}(p_{i-1}-p_i)theta_i+(y-1)theta_m`,

the shift-gain inequality

`sum_{i=1}^{m-1}(p_{i-1}-p_i)theta_i>=0`

would immediately prove the early plateau sublemma. It holds in many small
scans, and it is sharp in an infinite family: for degree `m`, let

`P=(1,2,2,...,2,1,1)`

with `p_1=...=p_{m-2}=2`, and take degree `m+2`

`Q=(1,A,A-1,A-2,...,A-m,1)`.

At `k=m-1`, this gives

`theta=(-1,-1,...,-1,A-1)`,

`C=-(2m-3)`, `L=2`, `y=1`, `D_m=A-2m+1`,

and shift gain exactly `0`.

However, shift gain is not the final lemma. It can be negative while the
actual previous difference is still safely positive. For example,

`P=(1,2,1,1)`, `Q=(1,15,11,8,5,1)`,

gives

`theta=(-3,-3,-4,14)`, `C=-10`, `L=2`, `y=1`,

with `D_3=1`, `D_2=4`, shift gain `-1`, and truncated previous difference
`3`. So the direct target must remain

`sum_{i=1}^m p_{i-1}theta_i>=0`.

One sufficient reason for the shift gain is sign alignment:

`theta_i<0 => p_{i-1}<=p_i`

for `1<=i<=m-1`. Since `L>y>=1`, every positive index `i>=t` satisfies
`p_{i-1}>p_i`; under the alignment condition, the shift gain is nonnegative
term by term.

This alignment is not universal, however. In the `(3,5)` cap-`12` scan, `115`
early-plateau positive-next states are misaligned; in the `(4,6)` cap-`9`
scan, `26` are misaligned; the explicit `(5,7)` example above is also
misaligned. The alignment condition remains a useful diagnostic, not the
final lemma.

There is also a clean conditional proof of the shift-gain inequality. Let

`a_i=p_{i-1}-p_i`.

Suppose the nonpositive block of `theta` is monotone as it approaches the sign
change:

`theta_1<=theta_2<=...<=theta_{t-1}<=0`.

Put `b_i=-theta_i` for `1<=i<t`. Then `b_i` is nonnegative and
nonincreasing. The prefix sums of `a_i` are

`sum_{i=1}^r a_i=p_0-p_r=1-p_r<=0`.

Abel summation gives

`sum_{i=1}^{t-1} a_i b_i<=0`,

and therefore

`sum_{i=1}^{t-1} a_i theta_i>=0`.

On the positive block, `i>=t`, we have `a_i>=0` because
`p_{i-1}/p_i>=p_{t-2}/p_{t-1}=L>y>=1`; also `theta_i>=0`. Hence every
positive-block term contributes nonnegatively. Therefore the desired
shift-gain inequality follows from this monotone-negative-block condition.

The `(1,15,11,8,5,1)` example shows that the monotone-negative-block condition
is also only sufficient, not necessary: the condition fails, but the
truncated previous-difference inequality still holds.

A better sufficient condition is

`sum_{i=1}^{m-1}(p_{i-1}-p_i)theta_i>=theta_0`.

Indeed,

`D_{m-1}=D_m+1-theta_0+
sum_{i=1}^{m-1}(p_{i-1}-p_i)theta_i+(y-1)theta_m`,

so this condition gives `D_{m-1}>=D_m+1+(y-1)theta_m>0`.
Equivalently, it gives the truncated previous-difference inequality with
spare room.

This condition holds in every checked early-plateau positive-next state. It
is also exactly what the negative-shift example satisfies:

`-1>=-3`.

Abel summation gives one strong sufficient condition. The only negative Abel
contributions come from downward jumps in the negative block of `theta`,
namely from indices with `theta_i>theta_{i+1}`. It would be enough to prove

`sum_{i=1}^{t-2}(p_i-1) max(0,theta_i-theta_{i+1}) <= -theta_0`.

This bound explains why the monotone-negative-block case was easy: then the
left side is zero. It is also true in the terminal sign-change case `t=m`,
including the `(3,5)` proof below. However, it is not the right general lemma.
For example,

`P=(1,11,5,2,1)`, `Q=(1,11,77,68,60,52,1)`

gives

`theta=(-8,-8,-9,66,10)`, `C=-1`, `L=11/5`, `y=2`,

with `D_4=1` and `D_3=244`. The weighted variation is `10`, while
`-theta_0=8`. The state is still safely controlled because the positive block
contributes a large shift gain:

`sum_{i=t}^{m-1}(p_{i-1}-p_i)theta_i=198`.

The corrected sufficient condition is therefore

`sum_{i=1}^{t-2}(p_i-1) max(0,theta_i-theta_{i+1})
<= -theta_0 + sum_{i=t}^{m-1}(p_{i-1}-p_i)theta_i`.

Indeed, Abel summation bounds the negative-block shift loss by the left side,
and the positive-block shift gain is exactly the extra term on the right.

The useful reduction is therefore:

prove directly that, in every early-plateau double-bad state with `D_m>0`,

`sum_{i=1}^{m-1}(p_{i-1}-p_i)theta_i>=theta_0`,

or prove the corrected weighted-variation bound above. Either one implies

`sum_{i=1}^m p_{i-1}theta_i>=0`.

The exact verifier checks these targets via the
`early_plateau_shift_gain_ge_theta0`,
`early_plateau_corrected_variation_controlled`, and
`early_plateau_truncated_previous_nonnegative` buckets.

There is an even cleaner equivalent-looking target at the early plateau. Since
`y=p_{m-1}` and `p_m=1`,

`D_{m-1}-yD_m=1-y theta_0+
sum_{i=1}^{m-1}(p_{i-1}-yp_i)theta_i`.

Thus it is enough to prove

`D_{m-1}>=yD_m`.

When `D_m>0`, this immediately gives `D_{m-1}>0`. The coefficient
`p_{i-1}-yp_i` changes sign exactly when the shifted ratio
`p_{i-1}/p_i` crosses `y`; in the hard case this crossing occurs before the
sign change of `theta`. So the new local picture is a mismatch interval:
`theta_i<0` while `p_{i-1}/p_i>y`. The boundary term `-y theta_0` and the
positive side of `theta` must dominate this mismatch. The verifier tracks this
via the `early_plateau_y_scaled_previous_dominates` bucket.

The new target passes the current exact checks. In particular, all `3509`
positive-next early-plateau states in the `(3,5)` cap-`20` scan and all `905`
such states in the `(4,6)` cap-`10` scan satisfy `D_{m-1}>=yD_m`. A generated
stress search of `1,000,000` admissible `m=4,t=3` shapes with larger
coefficients also found no failure; the smallest observed margin was `21`.

In fact, the positive block is not needed for the checked states. Let

`B_i=-theta_i` for `0<=i<t`.

The negative-block target is

`yB_0+sum_{i=1}^{t-1}(yp_i-p_{i-1})B_i>=0`.

This says that the shifted/original average over the negative block is at most
`y`:

`sum_{i=1}^{t-1}p_{i-1}B_i <= y(B_0+sum_{i=1}^{t-1}p_iB_i)`.

If this holds, then the positive block only helps in
`D_{m-1}-yD_m`, because every positive-block shifted ratio is at least `y`.
The verifier tracks the inequality via
`early_plateau_negative_block_y_margin_holds`; it holds in all current
positive-next early-plateau scans:

- `(3,5)` cap `20`: `3509 / 3509`;
- `(4,6)` cap `10`: `905 / 905`;
- `(5,7)` cap `8`: `1146 / 1146`;
- `(6,8)` cap `6`: `182 / 182`;
- `(8,10)` cap `5`: `40 / 40`.

Abel summation gives the next proof shape. Put

`a_0=y`, and `a_i=yp_i-p_{i-1}` for `1<=i<t`,

and let

`S_r=sum_{i=0}^r a_i`.

Then

`S_r=y sum_{i=0}^r p_i - sum_{i=0}^{r-1}p_i
=(y-1)sum_{i=0}^{r-1}p_i+yp_r>0`.

So

`sum_{i=0}^{t-1}a_iB_i
=S_{t-1}B_{t-1}+sum_{r=0}^{t-2}S_r(B_r-B_{r+1})`.

Only upward jumps `B_{r+1}>B_r` can hurt. Thus the remaining local task is to
show that `D_m>0`, together with log-concavity of `Q`, prevents those upward
jumps from exceeding the terminal and downward-jump Abel credits.

The strongest exact small-degree check so far is `(3,5)` at cap `20`. It has
`3509` early-plateau positive-next states; all `3509` have nonnegative
truncated previous difference. Among them, `9` have negative shift gain and
`50` fail the monotone-negative-block condition, confirming that the direct
truncated inequality is the right target. All `3509` nevertheless satisfy
`shift_gain>=theta_0` and the corrected weighted-variation bound above. In
this smallest degree the uncorrected weighted-variation bound also holds.

Random larger-degree checks continue to find no early-plateau positive-next
states at all; for example `(8,10)` and `(12,15)` with `100,000` trials and
first coefficient cap `5000` had none.

For the smallest nontrivial early-plateau case `m=3`, the weighted-variation
bound has a concrete form. Write

`P=(1,a,y,1)`

and

`theta=(-E,-B,-A,r)`.

Here `t=3`, `L=a/y>y`, and `D_3>0` means

`r>E+aB+yA`.

The sufficient condition `shift_gain>=theta_0` becomes

`E+(a-1)B>=(a-y)A`.

The Abel weighted-variation bound is the stronger but cleaner inequality

`E>=(a-1)max(0,A-B)`.

For `(1,15,11,8,5,1)`, we have `A=4`, `B=3`, `E=3`, and `a=2`, so the bound
is `3>=1`. The proof uses only the two log-concavity constraints

`q_2^2>=q_1q_3` and `q_3^2>=q_2q_4`

together with `D_3>0`; the general weighted-variation bound should be its
higher-degree analogue.

This `(3,5)` inequality has a short proof. If `A<=B`, there is nothing to
prove. Assume `A>B`, and put

`d=A-B`.

Also write `x=q_4` and `u=q_3=x+E`. Then

`q_2=u+B`, `q_1=u+B+A`.

The log-concavity inequality `q_2^2>=q_1q_3` gives

`(u+B)^2>=u(u+B+A)`,

or

`B^2>=u(A-B)=ud`.

Thus

`d<=B^2/u`.

The next log-concavity inequality `q_3^2>=q_2q_4` gives

`u^2>=(u+B)x`,

or

`E u=(u-x)u>=xB`.

Finally, the positive-next condition is

`D_3=x-1-(a-1)B-(y-1)A>0`.

Since `y>=1`, this implies

`x>(a-1)B`.

Combining the three inequalities,

`E>=xB/u>(a-1)B^2/u>=(a-1)d=(a-1)(A-B)`.

Therefore

`E>=(a-1)max(0,A-B)`.

This proves the weighted-variation bound in the smallest nontrivial
early-plateau case.

The first nonterminal early-plateau case also has a short proof of the
negative-block target. Let `m=4`, `t=3`, and write

`P=(1,a,b,y,1)`,

with `a/b>y` and `b>=y`, and

`theta=(-E,-B,-A,s,r)`.

The negative-block target is

`yE+(ya-1)B-(a-yb)A>=0`.

If `A<=B`, this is immediate because

`yE+((ya-1)-(a-yb))B
=yE+(a(y-1)+yb-1)B>=0`.

So assume `A>B`, and put `d=A-B`. Let `x=q_5` and `u=q_4=x+E`; then

`q_3=u+B`, `q_2=u+B+A`, and `q_1=u+B+A-s`.

As before, log-concavity gives

`B^2>=u(A-B)=ud`

and

`Eu>=xB`.

The positive-next condition is

`D_4=x-1-(a-1)B-(b-1)A+(y-1)s>0`,

while `C<0` says

`ys<aB+bA`.

If `y=1`, the positive-next condition gives

`x>(a-1)B>=(a-b)B`.

If `y>1`, combining the two displayed inequalities gives

`x>1+(a/y-1)B+(b/y-1)A`.

Since `b>=y>=1`, this again implies

`x>(a/y-b)B=(a-yb)B/y`.

Therefore, in all cases,

`yE>=yxB/u>(a-yb)B^2/u>=(a-yb)d`.

Adding the nonnegative `B`-coefficient term proves

`yE+(ya-1)B-(a-yb)A>=0`.

Thus the negative-block target is proved for the first nonterminal case
`m=4,t=3`.

The same argument extends to every `t=3` case with `m>=4`. Keep

`p_1=a`, `p_2=b`, `p_{m-1}=y`,

and let `P=p_3`, the largest positive-block coefficient after `p_2`. The ratio
monotonicity of the log-concave prefix gives

`b/P>=a/b>y`.

As above, write `theta=(-E,-B,-A,s_3,...,s_m)`, put `d=A-B>0`, and let
`x=q_{m+1}`, `u=q_m=x+E`. The same two log-concavity inequalities of `Q` give

`d<=B^2/u` and `Eu>=xB`.

The negative-block target is again

`yE+(ya-1)B-(a-yb)A>=0`.

Set

`gamma=a-yb>0`,

and

`delta=ya-1-gamma=a(y-1)+yb-1>=0`.

It is enough to prove

`yE+delta B>=gamma d`.

Since `E>=xB/u` and `d<=B^2/u`, this follows from

`(y+delta)x>=gamma B`.

To get this lower bound on `x`, take

`lambda=1-1/P`.

For every positive middle index `i>=3`, we have `p_i<=P`, hence

`(p_i-1)-lambda p_i<=0`.

Since `D_m>0` and `C<0`, the inequality `D_m-lambda C>0` gives

`x>1+(a/P-1)B+(b/P-1)A`.

Because `A>B`, this implies

`x>((a+b)/P-2)B`.

It remains only to check coefficients. Put `r=a/b` and `s=b/P`. Then
`s>=r>y>=1`, and

`(a+b)/P-2=s(r+1)-2>=r(r+1)-2`.

Also `delta+y>=yb`. Therefore

`(delta+y)((a+b)/P-2)
>=yb(r^2+r-2)`.

Finally,

`y(r^2+r-2) >= r-y`

for every `r>y>=1`; after expanding, the difference is

`yr^2+(y-1)r-y`,

which is nonnegative at `r=y` and increasing for `r>=y`. Multiplying by `b`
gives

`(delta+y)((a+b)/P-2)>=a-yb=gamma`.

Hence `(y+delta)x>gamma B`, and the negative-block target follows for all
`t=3`, `m>=4`.

Together with the terminal sign-change argument below, this proves the needed
early-plateau positivity for every hard branch with `m=4`: the only possible
hard first-positive indices are `t=3` and `t=4`, since `t<=2` has `L<=y` and
was already handled by ratio transfer. The stronger y-scaled target
`D_{m-1}>=yD_m` remains part of the general negative-block program for the
terminal case.

The next new case is `t=4`. Exact small scans often show a monotone negative
block there, but this is not structural. Generated larger examples can have
upward jumps before the sign change; for instance

`P=(1,10,28,12,1,1)`,

`Q=(1,155936,161339,159543,156553,152431,148319,1)`

has

`theta=(-4112,-4122,-2990,-1796,5403,155935)`,

so `B_1>B_0`, while still satisfying `D_5>0`, `C<0`, and
`p_2/p_3>y`. Thus the next proof cannot simply assume monotonicity of the
negative block; it has to use the Abel credits quantitatively.

The useful normalized `t=4` target is now the following. Put

`a=p_1`, `b=p_2`, `c=p_3`, `P=p_4`,

so `a,b,c,P,y>=1`, and define local slopes of `Q` by

`sigma_i=B_i/x_i`, where `x_i=q_{m+1-i}` and `x_{i+1}=x_i+B_i`.

Log-concavity of `Q` is exactly

`sigma_0>=sigma_1>=sigma_2>=sigma_3>=0`

on this negative block. Also put

`F_i=B_i/x_0`.

Taking `lambda=1-1/P` in `D_m-lambda C>0` gives the normalized budget

`(a/P-1)F_1+(b/P-1)F_2+(c/P-1)F_3<1`.

Thus the `t=4` negative-block target would follow from the purely local slope
lemma

`yF_0+(ya-1)F_1+(yb-a)F_2+(yc-b)F_3>=0`,

under the ratio constraints

`1/a<=a/b<=b/c<=c/P` and `b/c>y`.

This formulation is the next concrete proof target. It has no remaining
dependence on the degree `m` or on the rest of the positive block.

The ratio form clarifies what remains. Write

`q=a/b`, `r=b/c`, and `s=c/P`.

Then

`a=qrc`, `b=rc`, and `P=c/s`,

with

`0<q<=r<=s`, `r>y>=1`, and

`c>=c_0:=max(s,1/(q^2r))`.

The budget becomes

`(qrs-1)F_1+(rs-1)F_2+(s-1)F_3<1`,

and the target becomes

`M=yF_0-F_1+cH>=0`,

where

`H=yqrF_1+r(y-q)F_2-(r-y)F_3`.

Thus a negative `H` at fixed ratios would be fatal after scaling `c`, so the
budget must be used to prevent it. It is not a consequence of slope
monotonicity alone: for example, with `y=q=1`, `r=s=2`, and
`sigma_0=sigma_1=sigma_2=sigma_3=1/2`, one has

`F=(1/2,3/4,9/8,27/16)`,

so

`H=2F_1-F_3=-3/16`,

but the budget is `117/16`, far outside the allowed range.

The subcase `q>y` also cannot be discarded. The exact `(4,6)` cap-`6` scan has
the early-plateau state

`P=(1,3,2,1,1)`,

`Q=(1,6,6,6,5,4,1)`,

at `k=3`, with

`theta=(-1,-1,0,0,5)`.

Here `D_4=1`, `D_3=5`, `C=-3`, `p_2/p_3=2>y=1`, and
`q=a/b=3/2>y`. The negative-block margin is still positive, equal to `3`.
So the proof must handle the full ratio range `0<q<=r`.

The next useful reduced form is obtained by taking the worst-looking
specialization `y=1` and `s=r`, and writing

`T=1+F_0`,

`alpha=sigma_1`, `beta=sigma_2`, `gamma=sigma_3`.

Then

`F_1=T alpha`,

`F_2=T beta(1+alpha)`,

`F_3=T gamma(1+alpha)(1+beta)`,

with `T>=1+alpha` and `0<=gamma<=beta<=alpha`. Put

`K=(qr^2-1)alpha+(r^2-1)beta(1+alpha)+(r-1)gamma(1+alpha)(1+beta)`

and

`h=qr alpha+r(1-q)beta(1+alpha)-(r-1)gamma(1+alpha)(1+beta)`.

The budget is `TK<1`, hence `(1+alpha)K<1`, and the target at
`c_0=max(r,1/(q^2r))` is

`T(1-alpha+c_0h)-1>=0`.

A clean sufficient inequality is therefore

`c_0h>=alpha^2/(1+alpha)`.

Indeed, it gives

`1-alpha+c_0h>=1/(1+alpha)`,

and then `T>=1+alpha` proves the target. A direct `5,000,000` sample probe of
this reduced inequality, subject to `(1+alpha)K<1`, found no failure; the
smallest margin was about `1.0e-10`, occurring only near the degenerate limit
`r,q -> 1` and `alpha -> 0`. A separate optimizer search confirms why the
budget matters: if `H<0` is forced with visible relative size, the minimal
budget is already about `3.57`, well above the allowed value `1`.

Half of this reduced sufficient inequality now has a short proof. Put

`u=qr`, `beta=alpha x`, and `gamma=beta z`,

where `0<=x,z<=1`. In the branch `u>=1`, we have `c_0=r`. It is enough to
prove

`rh>=alpha(1-K)`,

because `(1+alpha)K<1` then gives

`rh>alpha^2/(1+alpha)`.

Let

`E=rh-alpha(1-K)`.

After substituting `beta=alpha x`, `gamma=alpha xz`, and `q=u/r`, the
coefficient of `u` in `E` is `alpha r(1-x)>=0`. Thus it is enough to check
`u=1`. At `u=1`, direct expansion gives

`E=alpha(r-1)[alpha r x+alpha x+rx+1+zx(alpha-r)(alpha x+1)]`.

If `alpha>=r`, the bracket is positive. If `alpha<r`, the bracket is minimized
at `z=1`, where it becomes

`alpha^2x^2+alpha r x(1-x)+2alpha x+1>0`.

Therefore `E>=0`, proving the reduced sufficient inequality whenever
`qr>=1`. The only remaining branch of this reduced target is `qr<=1`, where
`c_0=1/(q^2r)`.

The branch `qr<=1` also reduces to a smaller boundary statement. Put

`u=qr`, `B=beta`,

and package the `gamma` term as

`C=(r-1)gamma(1+alpha)(1+B)`.

For fixed `alpha,r,u,B`, the admissible values of `C` satisfy

`0<=C<=C_s:=(r-1)B(1+alpha)(1+B)`

and, from the budget,

`C<L-K_0`,

where

`L=1/(1+alpha)`,

`K_0=(ur-1)alpha+(r^2-1)B(1+alpha)`.

The actual reduced target in this branch is

`h>=alpha^2 u^2/(r(1+alpha))`.

Since `h` decreases with `C`, the worst admissible value is

`C=max admissible = min(C_s,L-K_0)`.

Now set

`K_s=K_0+C_s=(ur-1)alpha+(1+alpha)(r-1)B(r+2+B)`.

If `K_s<=L`, then the margin as a function of `B` is

`u alpha-alpha^2 u^2/(r(1+alpha))+(1+alpha)((1-u)B-(r-1)B^2)`,

a concave quadratic, so its minimum on the structural region occurs at an
endpoint. If `K_s>=L`, then the budget cap is active and the margin is
linear increasing in `B`; its minimum also occurs at the left endpoint. Hence
the only nontrivial endpoint is the boundary

`K_s=L`.

Thus the remaining `qr<=1` proof is equivalent to the boundary inequality

`u alpha+(1+alpha)((1-u)B-(r-1)B^2)
 >= alpha^2 u^2/(r(1+alpha))`,

under

`0<u<=1`, `0<=B<=alpha`, `r>1`, and

`(ur-1)alpha+(1+alpha)(r-1)B(r+2+B)=1/(1+alpha)`.

Random boundary optimization again found no failure; the minimum approaches
`0` only in degenerate limits such as `alpha -> 0`.

This boundary inequality is also provable. Write `A=alpha` and

`w=(r-1)B`.

The boundary margin is

`Au(1-Au/(r(1+A)))+(1+A)B(1-u-w)`.

If `w<=1-u`, then the second term is nonnegative, while the first term is
positive. So assume `w>1-u`, and put

`delta=w+u-1`.

Then `0<delta<=w`, because `u<=1`. Substituting `r=1+w/B` into the boundary
equation and multiplying by `B` gives

`A(1+A)(B+w)delta=B-wM`,

where

`M=A^2B^2+2A^2B+A^2+2AB^2+5AB+Aw+A+B^2+3B+w`.

Since

`M>=A+B(1+A)^2`,

the positivity of `delta` implies

`B>w(A+B(1+A)^2)`.

In particular, since `B<=A`,

`w(A+B(1+A)^2)<A`.

A second direct rearrangement of the same boundary identity gives

`Au-wB(1+A)^2
= [B-wM+(1+A)(B+w)(A-w(A+B(1+A)^2))]/((1+A)(B+w))`,

which is positive by the two displayed inequalities. Hence

`(1+A)Bdelta <= (1+A)Bw <= Au/(1+A)`.

Also `u<r`, so

`Au(1-Au/(r(1+A)))>=Au/(1+A)`.

The positive first term therefore dominates the negative term
`(1+A)Bdelta`, proving the boundary inequality. Consequently the stronger
`qr<=1` target holds, and the reduced sufficient inequality

`c_0h>=alpha^2/(1+alpha)`

is proved in both branches `qr>=1` and `qr<=1`.

It remains to connect this reduced inequality back to the normalized `t=4`
lemma. First take the worst specialization `y=1` and `s=r`, and put

`T=1+F_0`.

The slope formulas give

`F_1=T alpha`,

`F_2=T beta(1+alpha)`,

`F_3=T gamma(1+alpha)(1+beta)`,

so the budget at `s=r` is exactly `TK<1`. The target at
`c=c_0=max(r,1/(q^2r))` is

`T(1-alpha+c_0h)-1`.

Since `c_0h>=alpha^2/(1+alpha)`,

`T(1-alpha+c_0h)-1 >= T/(1+alpha)-1>=0`,

because `T=1+sigma_0>=1+sigma_1=1+alpha`.

Now return to the original parameters. The budget coefficients are increasing
in `s`, so the hypothesis at the actual `s>=r` implies the same budget at
`s=r`. The proved reduced inequality also gives `h>0`, hence `H>0` at
`y=1`; since

`dH/dy=qrF_1+rF_2+F_3>0`,

the bracket `H` remains positive and only grows for every `y>=1`. Finally,
the actual `c` satisfies `c>=c_0`, so increasing `c` only helps. Therefore the
normalized `t=4` local slope lemma is proved, and with it the `t=4`
negative-block target.

Together with the all-`m` proof for `t=3` and the terminal sign-change
argument, this covers every hard early-plateau first-positive index for
`m<=5`. Indeed, for `m=5`, the only remaining index after `t=3,4` is
`t=5`, which is terminal.

The next frontier is `t=5`. The same normalization gives the following
candidate. Let

`q=p_1/p_2`, `r=p_2/p_3`, `s=p_3/p_4`, and `v=p_4/P`,

where `P=p_5`. Then `0<q<=r<=s<=v`, and the hard condition is `s>y>=1`.
Writing the local slopes after `x_1` as

`alpha_1>=alpha_2>=alpha_3>=alpha_4>=0`,

put

`G_1=alpha_1`,

`G_2=alpha_2(1+alpha_1)`,

`G_3=alpha_3(1+alpha_1)(1+alpha_2)`,

`G_4=alpha_4(1+alpha_1)(1+alpha_2)(1+alpha_3)`.

The worst-looking reduced specialization is again `y=1` and `v=s`. It gives

`K=(qrs^2-1)G_1+(rs^2-1)G_2+(s^2-1)G_3+(s-1)G_4`

and

`h=qrsG_1+rs(1-q)G_2+s(1-r)G_3-(s-1)G_4`.

The analogue of the proved `t=4` sufficient inequality is

`c_0h>=alpha_1^2/(1+alpha_1)`,

where

`c_0=max(s,1/(q^2rs))`,

under the budget condition `(1+alpha_1)K<1`. A direct `5,000,000` sample probe
of this reduced `t=5` inequality found no failure; the minimum margin was
about `1.1e-10`, again only near the degenerate limit where all ratios and
slopes are tiny perturbations of the boundary. Exact small product scans also
remain benign: `(5,7)` cap `8` has `607` early-plateau `t=5` states and
`(6,8)` cap `6` has `71`; all have nonnegative negative-block margin, and in
these small states the negative block is monotone.

The same reduced inequality also appears to be the general local statement.
The script `probe_general_slope.py` samples the analogous reduction for
arbitrary first-positive index `t`: the final shifted ratio is specialized to
the last hard ratio, the budget is normalized at `y=1`, and the same
`c_0 h >= alpha_1^2/(1+alpha_1)` margin is tested. With seed `700` and
`1,000,000` samples each, the tested values `t=5,6,7,8,10` had no failures.
The smallest margins remained near zero only in degenerate small-slope
limits. This suggests that the right next proof target is a general slope
budget lemma, not a separate ad hoc proof for every `t`.

The same script now has an optimizer mode for the general reduced target.
Lower-branch optimizers for `t=5,6,7` with seeds `6101,6100,6102` again moved
to the all-ratios-near-`1`, tiny-slope zero limit instead of finding a finite
obstruction. A fresh `500,000`-sample run for `t=6,7` with seed `6103` also
had no failures. This strengthens the evidence that the completed `t=5`
lower-branch proof is exposing a general boundary mechanism.

This general reduced lemma again splits according to which lower bound defines
`c_0`. In the final-ratio branch, `c_0=R`, where `R` is the last ratio, the
same stronger inequality as in the `t=4` proof appears:

`R h >= alpha_1(1-K)`.

This branch does not seem to need the budget condition. A separate
`1,000,000`-sample run for each `t=4,5,6,7,8,10,12` found no failure. There is
also a clean first reduction. If the ratios are

`rho_1<=rho_2<=...<=rho_n=R`,

and `P_2=rho_2...rho_n`, then the derivative of

`R h-alpha_1(1-K)`

with respect to the first ratio `rho_1` is

`R P_2(1+alpha_1)(alpha_1-alpha_2)>=0`.

So the final-ratio branch is minimized when the lower-bound condition
`rho_1^2 rho_2...rho_n R=1` is tight. This is the current best entry point for
an induction or a one-variable boundary argument.

There is also a useful recursive form of the general reduced quantities. Let

`u=rho_1rho_2...rho_n`,

and let `h_tail,K_tail` be the same reduced quantities formed from the tail
ratios

`rho_2<=...<=rho_n=R`

and the tail slope block starting with `G_2`. Then

`h = u(G_1-G_2)+h_tail`

and

`K = (Ru-1)G_1+K_tail`.

This identity is immediate from the coefficient of `G_2`: the tail coefficient
is `rho_2...rho_n`, while the full coefficient is
`(1-rho_1)rho_2...rho_n`. Thus the full quantity is the tail quantity minus
`uG_2`, plus the leading term `uG_1`. The budget has the same clean split
because only the leading coefficient `Ru-1` is new. This recursive split is a
promising way to turn the sampled general lemma into an induction: the
possible loss from inserting the first ratio is exactly `uG_2`, and the
new budget credit is exactly `(Ru-1)G_1`.

The final-ratio branch is now proved by induction. The branch condition is

`R rho_1^2 rho_2...rho_n>=1`.

First note two consequences. If `rho_1<=1`, then

`Ru=R rho_1 rho_2...rho_n>=1/rho_1>=1`,

while if `rho_1>=1`, all ratios are at least `1`, so again `Ru>=1`. Also every
coefficient in `K_tail` is nonnegative. Indeed, for a tail coefficient
`R rho_i...rho_n-1`, either `rho_i>=1`, when it is immediate, or `rho_i<1`,
when removing the earlier tail factors can only increase the product and

`R rho_2...rho_n>=1/rho_1^2>=1`.

Thus `K_tail>=0`.

For the base case `n=1`, write `a=alpha_1`, `b=alpha_2`,
`G_1=a`, and `G_2=(1+a)b`. Direct expansion gives

`Rh-a(1-K)=(R-1)(1+a)[a(R+1)+b(a-R)]`.

If `a>=R` the bracket is positive. If `a<=R`, the bracket is minimized at
`b=a`, where it becomes `a(1+a)`. Hence the base case holds.

For the induction step, put `a=alpha_1`, `b=alpha_2`, and
`G_2=(1+a)b`. The tail branch condition follows from the full one because
`rho_2>=rho_1`. Applying the induction hypothesis to the normalized tail and
then multiplying by `1+a` gives

`R h_tail>=G_2(1-K_tail/(1+a))`.

Using the recursive identities,

`h=u(G_1-G_2)+h_tail`,

`K=(Ru-1)G_1+K_tail`,

we obtain

`Rh-alpha_1(1-K)
 >= (a-b)[K_tail+(1+a)(Ru-1)]`.

The right side is nonnegative because `a>=b`, `K_tail>=0`, and `Ru>=1`.
Therefore

`Rh>=alpha_1(1-K)`

throughout the final-ratio branch. Since this is stronger than the budgeted
target in the branch `c_0=R`, the general reduced lemma is now reduced to the
opposite lower-bound branch

`c_0=1/(rho_1^2 rho_2...rho_n)`.

The same stronger inequality cannot be pushed into this remaining branch. A
quick lower-branch probe already finds failures for `t=4`; one sample has

`rho=(0.8753710171572074,1.0000013365267502)`,

`alpha=(7.637770000257751,3.1648601229378253,0.4085663354128111)`,

with `K=-0.9517769158217555`, `h=10.092900447052976`, and
`c_0=1.3050137658310148`. Here

`c_0h-alpha_1(1-K)<0`,

but the actual target margin

`c_0h-alpha_1^2/(1+alpha_1)`

is still positive. Thus the remaining branch must use the budgeted target
directly, just as the completed `t=4` proof used the active budget boundary in
the subcase `qr<=1`.

The first step of the lower-bound branch is degree-independent. Let
`rho_1<=...<=rho_n=R`, let `u_i=rho_i...rho_n`, and put

`lambda=rho_1u_1`.

In the lower branch the target is

`h>=alpha_1^2 lambda/(1+alpha_1)`.

Package the last harmful term as

`E=(R-1)G_{n+1}`.

For fixed earlier data, the budget is `K=K_0+E`, while the target margin is
decreasing in `E`; hence the worst admissible value is

`E_*=min(E_s,L-K_0)`,

where

`L=1/(1+alpha_1)`,

`E_s=(R-1)(1+alpha_n)G_n`,

and

`K_s=K_0+E_s`.

On the structural side `K_s<=L`, write
`G_n=alpha_n P_n`, where `P_n=(1+alpha_1)...(1+alpha_{n-1})`. The structural
margin is

`S_s=h_0-E_s-alpha_1^2lambda/(1+alpha_1)`,

and as a function of `alpha_n` it has second derivative

`d^2S_s/dalpha_n^2=-2(R-1)P_n<=0`.

Also `K_s` is increasing in `alpha_n`, because

`dK_s/dalpha_n
 =P_n((R^2-1)+(R-1)(1+2alpha_n))>0`.

Thus the structural side reduces to the endpoints `alpha_n=0`,
`alpha_n=alpha_{n-1}`, or the active boundary `K_s=L`. On the active side
`K_s>=L`, the budget cap is active and the margin is

`S_a=h_0+K_0-L-alpha_1^2lambda/(1+alpha_1)`.

The coefficient of `G_n` in `S_a` is

`R^2+R(1-rho_{n-1})-1=R(R-rho_{n-1})+R-1>0`.

Therefore the active side is minimized at its left endpoint, again the
boundary `K_s=L`. This gives the general last-slope reduction:
the lower branch only has to treat `alpha_n=0`, `alpha_n=alpha_{n-1}`, and
the active boundary `K_s=L`.

The general probe now has a `--last-active` mode for the remaining active
boundary. It fixes the earlier ratios and slopes, solves the monotone equation
`K_s=L` for the final slope with `alpha_{n+1}=alpha_n`, and then optimizes
the same lower-branch margin. Saved runs in `logs/993_last_active_*.log`
found valid positive margins for `t=5,6,7,8`; the smallest saved margin was
about `7.1e-3` at `t=6`, with budget exactly active and `c_0>R`. One extra
`t=7` seed stayed outside the feasible active boundary, so it is not evidence
against the target. The closest valid runs again have very small slopes and
`alpha_n` close to `alpha_{n-1}`, while a broader `t=7` active point had
margin about `0.25` with `alpha_n/alpha_{n-1}` about `0.92`. These runs led
to the active-boundary monotonicity calculation below.

On the active boundary `K_s=L=1/(1+alpha_1)`, the target can be rewritten as

`h-alpha_1^2 lambda K_s>=0`.

This is a tempting stronger-looking budget lemma, but the budget condition is
essential: unconstrained optimizers in `logs/993_linearized_lower_*.log`
quickly find huge-slope counterexamples with enormous budget. With the lower
branch and budget cap imposed, the new `--linearized-budget` mode found no
failure for `t=5,6,7,8`, but the minimizers collapse to the easy `K<=0` or
`K≈0` zero limit. Therefore this linearized form is a useful diagnostic, but
the proof below uses the active-boundary monotonicity directly.

The active face has a useful exact shape. Fix the earlier data and put
`x=alpha_n`, `P_n=(1+alpha_1)...(1+alpha_{n-1})`,
`rho=rho_{n-1}`. On the last-slope face `alpha_{n+1}=alpha_n`,

`K_s=K_0+P_n x(R-1)(R+2+x)`

and

`h_s=h_0+P_n x(1-R rho-(R-1)x)`.

Thus on the active boundary `K_s=L`,

`h_s-alpha_1^2 lambda L
 =h_0-alpha_1^2 lambda L
  +(L-K_0)(1-R rho-(R-1)x)/((R-1)(R+2+x))`.

The multiplier

`phi(x)=(1-R rho-(R-1)x)/((R-1)(R+2+x))`

is strictly decreasing, since

`phi'(x)=-(R(R+1-rho)-1)/((R-1)(R+2+x)^2)<0`.

This explains why the closest active-boundary optimizers usually spend the
remaining budget with `alpha_n` close to `alpha_{n-1}`: for fixed earlier data
and fixed active-budget deficit, larger `alpha_n` gives a worse target
contribution.

The simultaneous comparison with the preceding slope is also monotone. Fix all
data before `alpha_{n-1}` and write

`c=alpha_{n-1}`, `x=alpha_n`, `tau=rho_{n-2}`, `rho=rho_{n-1}`,
`P=(1+alpha_1)...(1+alpha_{n-2})`.

On the face `alpha_{n+1}=alpha_n`,

`K_s=K_prev+P(c(R^2 rho-1)+(1+c)x(R-1)(R+2+x))`

and

`h_s=h_prev+P(cR rho(1-tau)+(1+c)x(1-R rho-(R-1)x))`.

Along the active boundary `K_s=L`, implicit differentiation gives

`dx/dc=-(R^2 rho-1+x(R-1)(R+2+x))/((1+c)(R-1)(R+2+2x))`.

Let `T=alpha_1^2 lambda L`. Then

`d(h_s-T)/dc = P N/((R-1)(R+2+2x))`,

where

`N=(R rho(1-tau)+x(1-R rho-(R-1)x))(R-1)(R+2+2x)`

`  -(R^2 rho-1+x(R-1)(R+2+x))(1-R rho-2(R-1)x)`.

This `N` is decreasing in `tau`, so the worst case is `tau=rho`. In that
case `N` is the quadratic

`(R-1)(R^2-R rho+R-1)x^2`

`+2(R-1)(R^2 rho-R rho^2+R rho-1)x`

`+R^3 rho-R^2 rho^2+2R rho^2-3R rho+1`.

If `rho>=1`, then the linear coefficient is nonnegative, and the constant
term is nonnegative because it is increasing in `R` and at `R=rho` equals
`(rho-1)^2(2rho+1)`. If `rho<=1`, the discriminant is

`4R^2(R-1)(rho-1)F`,

where

`F=R^3 rho-2R^2 rho^2+R^2 rho+R rho^3-2R rho-rho^3+3rho^2-2rho+1`.

Here `F>=0`: at `R=1` it is `(rho-1)^2`, and

`dF/dR=rho(3R^2-4R rho+2R+rho^2-2)>=0`,

since the bracket is increasing in `R` and at `R=1` is
`(rho-1)(rho-3)>=0`. Thus `N>=0` in all cases.

Therefore the active-boundary margin is nondecreasing as `c=alpha_{n-1}`
increases. Starting from any interior active-boundary point, decrease `c`
while re-solving `K_s=L`; the margin cannot increase, and the path stops only
when either `x=c` or `x=0`. Consequently the active boundary is reduced to the
same two endpoint families `alpha_n=alpha_{n-1}` and `alpha_n=0`.
The general lower branch is now reduced to these two last-slope endpoints.

The zero endpoint has a useful normalization. If `alpha_n=alpha_{n+1}=0`, put
`m=n-1`, `mu=rho_1^2 rho_2...rho_m`, `theta=R^2`, and
`v_i=rho_i...rho_m`. Then

`lambda=R mu`,

`h=R H_0`,

where

`H_0=v_1G_1+sum_{i=2}^m (1-rho_{i-1})v_iG_i`,

and

`K=theta sum_{i=1}^m v_iG_i-sum_{i=1}^m G_i`.

Thus the target on this endpoint is independent of the final ratio:

`H_0>=alpha_1^2 mu/(1+alpha_1)`.

The final ratio only controls feasibility through

`rho_m^2<=theta<1/mu`

and the budget cap

`theta sum v_iG_i-sum G_i<=1/(1+alpha_1)`.

Unbudgeted random probes of this zero endpoint quickly find failures for
`t>=6`, so the remaining proof must use this budget feasibility, not only the
sign of `H_0`.

There is a cleaner inductive interpretation. If `rho_m<=1`, then all ratios
in the zero endpoint are at most `1`, every coefficient in `H_0` is
nonnegative, and the first term alone gives

`v_1G_1>=alpha_1^2 mu/(1+alpha_1)`,

because `rho_1<=1`. If `rho_m>1`, compare with the same reduced lemma for the
shorter ratio list `rho_1,...,rho_m` and slope list
`alpha_1,...,alpha_m,0`. Its `h` is exactly `H_0`, its lower-branch parameter
is `mu`, and the lower branch holds because

`rho_m^2 mu<=1`.

Moreover its budget is

`K_short=rho_m sum v_iG_i-sum G_i`,

which is at most the endpoint budget

`rho_m^2 sum v_iG_i-sum G_i<=1/(1+alpha_1)`.

Thus the zero endpoint follows immediately from the induction hypothesis on
the number of ratios. The remaining endpoint to prove is
`alpha_n=alpha_{n-1}` with `alpha_{n+1}=alpha_n`.

The script `probe_general_slope.py` now has exact endpoint optimizer modes
`--endpoint zero` and `--endpoint equal`. The exact equal-endpoint runs for
`t=5,6,7,8,10` again found no finite obstruction; the optimizers moved to the
same tiny-slope, tiny-ratio zero limit as the general lower-branch optimizer.

The equal endpoint also has a useful local budget identity. Put
`c=alpha_{n-1}=alpha_n=alpha_{n+1}`, `tau=rho_{n-2}`,
`rho=rho_{n-1}`, and `P=(1+alpha_1)...(1+alpha_{n-2})`. The last three slope
terms contribute

`P c H_tail`

to `h`, where

`H_tail=1-tau rho R+c(2-R(1+rho))-c^2(R-1)`,

and

`P c K_tail`

to the budget, where

`K_tail=R^2(rho+1)+R-3+c(R-1)(R+3)+c^2(R-1)`.

Their sum is linear in `c`:

`H_tail+K_tail
 =R^2rho+R^2+R-2-tau rho R+c(R(R+1-rho)-1)`.

This is nonnegative because `tau<=rho<=R`, so the constant term is at least

`R rho(R-rho)+R^2+R-2>=0`,

and the coefficient of `c` is at least `R-1>=0`. Hence any negative equal-tail
contribution has at least as much budget contribution available. The remaining
gap is quantitative: we still need to combine this local domination with the
positive slack from the already-closed zero endpoint.

More directly, compare the equal endpoint to the closed zero endpoint with the
same `alpha_{n-1}=c`, but with `alpha_n=alpha_{n+1}=0`. The added two slope
terms contribute

`G_n(1-R rho-c(R-1))`

to `h`, and

`G_n(R-1)(R+2+c)`

to the budget. Their sum is

`G_n(R(R-rho)+R-1)>=0`.

Thus any extra loss from turning on the equal tail has budget cost at least
that loss. A focused `500,000`-sample stress run for
`t=5,6,7,8,10,12` found no case where this extra loss exceeded the zero
endpoint margin; the largest observed loss/margin ratio was about `0.9991`.
This is now the concrete remaining equal-endpoint target.

There is an equivalent recursive form of the same target. Let `mu` be the
lower-branch product for the shorter ratio list `rho_1,...,rho_{n-1}`, and let
`h_short,K_short` be the reduced quantities for that shorter list with slopes
`alpha_1,...,alpha_n`. On the equal endpoint,

`h=R h_short-(R-1)G_{n+1}`,

while the target scales as

`alpha_1^2 lambda/(1+alpha_1)
 =R alpha_1^2 mu/(1+alpha_1)`.

Thus the full equal-endpoint margin is

`R(h_short-alpha_1^2 mu/(1+alpha_1))-(R-1)G_{n+1}`.

The shorter state is itself in the lower branch: full lower-branch feasibility
gives `R^2 mu<=1`, and since `rho_{n-1}<=R<=R^2`, this implies
`rho_{n-1}mu<=1`. Its budget is also no larger than the full budget, because

`K-K_short
 =(R^2-rho_{n-1})(sum_{i=1}^{n-1}v_iG_i+G_n)+(R-1)G_{n+1}>=0`.

So ordinary induction proves the nonnegative shorter margin, and the only
missing strengthening is to show that this shorter margin is large enough to
pay the new endpoint loss `(R-1)G_{n+1}` whenever the full budget remains
admissible.

A focused recursive-margin stress test checked exactly this inequality,

`h_short-alpha_1^2mu/(1+alpha_1) >= (R-1)G_{n+1}/R`,

on `500,000` random lower-branch equal-endpoint states for each
`t=5,6,7,8,10,12`. It found no failures. The smallest residuals again occur
in tiny-slope limits; in the most balanced saved case, at `t=8`, the shorter
margin and endpoint loss were about `4.46e-16` and `4.35e-16`. This strongly
suggests that the induction should be strengthened by an endpoint-extension
credit, rather than trying to prove the equal endpoint as a standalone
inequality.

The script now has an `--endpoint-credit` optimizer for this recursive
residual. Runs for `t=5,6,7,8,10` found no obstruction; the optimizer again
prefers the degenerate zero-slope limit. The random stress test remains more
useful for locating balanced near-tight states, while the optimizer is useful
as a direct falsification check for the strengthened invariant.

The budget hypothesis in this strengthened invariant is essential.
Unconstrained endpoint-credit probes fail immediately in large-slope states;
the saved failures in `logs/993_endpoint_credit_unbudgeted_failures.log` all
have enormous normalized budget. Thus the credit induction has to use the
extension budget cap quantitatively.

The candidate strengthened induction is therefore:

Let a lower-branch state with `m` ratios have last ratio `rho`, last two
slopes equal to `c`, and budget `K_m<=L`. Suppose it admits an equal-slope
extension by a final ratio `R>=rho`, meaning

`R^2 mu<=1`

and the extended budget

`K_m+(R^2-rho)(sum_{i=1}^m v_iG_i+G_{m+1})+(R-1)G_{m+2}`

is at most `L`, with `G_{m+2}=(1+c)G_{m+1}`. Then

`h_m-alpha_1^2mu/(1+alpha_1) >= (R-1)G_{m+2}/R`.

This strengthened statement immediately closes the equal endpoint by the
recursive identity above. The zero endpoint is already compatible with this
induction because it reduces to a shorter ordinary lower-branch state.

There is an equivalent scalar threshold form. For the short state put

`M=h_m-alpha_1^2mu/(1+alpha_1)`,

`D=L-K_m`,

`S=sum_{i=1}^m v_iG_i+G_{m+1}`,

and `G=G_{m+2}`. For a fixed short state, the endpoint loss
`(R-1)G/R` is increasing in `R`. If `M>=G`, the credit is automatic. If
`M<G`, the first extension ratio that could fail the credit is

`R_0=G/(G-M)`.

The extension budget used by ratio `R` is

`B(R)=(R^2-rho)S+(R-1)G`.

Therefore it is enough, and in this fixed-state sense equivalent, to prove

`B(R_0)>=D`.

Using `K_m=rho S-T`, this threshold condition is equivalently

`R_0^2S+(R_0-1)G>=T+L`,

where `T=sum_{i=1}^{m+1}G_i`; the dependence on the last short ratio `rho`
cancels.

After clearing denominators this becomes the purely short-state inequality

`(G^2-rho(G-M)^2)S+MG(G-M)-D(G-M)^2>=0`.

A `500,000`-sample stress run for `t=5,6,7,8,10,12` found no failures of this
threshold inequality; the saved best slacks were comfortably positive. This
is the most concrete current form of the endpoint-credit proof obligation.

There is an even simpler sufficient subtarget. Write `u=M/G`. Since
`R_0=1/(1-u)`, the threshold inequality follows from

`S>=(1-u)^2(T+L)`,

where

`T=sum_{i=1}^{m+1}G_i`.

Equivalently,

`G^2S>=(G-M)^2(T+L)`.

A separate `500,000`-sample stress run for `t=5,6,7,8,10,12` found no
failures of this stronger-looking `S`-bound. The closest samples again have
`u` extremely close to `1`, so the right side is tiny. This may be the right
way to prove the endpoint credit: show that whenever the shorter margin is
less than the extension mass `G`, it is nevertheless close enough to `G` that
the weighted sum `S` already exhausts the failure threshold.

A broader short-state scope test points to an even cleaner statement. Compute
`S` directly as

`S=sum_{i=1}^m (rho_i...rho_m)G_i+G_{m+1}`

rather than by the numerically unstable quotient `(K_m+T)/rho`. A `500,000`
sample run for each `m=2,...,10` found no failures among short equal-tail
states satisfying only the ordinary lower-branch conditions `c_0>rho_m`,
`K_m<=L`, and `M>=0`. A separate hypothesis probe found failures if
`c_0>rho_m` was removed, but no failures after it was restored, even without
the budget condition. Thus the likely proof target is not the full endpoint
budget statement, but the following branch invariant:

If the short state has final two slopes equal, lies in the lower branch, has
nonnegative ordinary margin `M`, and `M<G`, then

`G^2S>=(G-M)^2(T+L)`.

The ratio probe maximized
`((1-M/G)^2(T+L))/S` over random short states. It stayed below `1`, often
close to `1` in large-slope samples with ratios near `1`, so this invariant is
probably sharp and should be attacked directly.

The useful normalized notation is this. Put `p_i=rho_i...rho_m`,
`p_{m+1}=1`, and `p_0=0`. Then

`h=sum_{i=1}^{m+1}(p_i-p_{i-1})G_i`,

`S=sum_{i=1}^{m+1}p_iG_i`,

and `K_m=rho_m S-T`. For a fixed short state and a prospective next mass
`X`, the S-bound residual is

`F(X)=X^2S-(X-M)^2(T+L)`.

Thus `F(M)=M^2S>0`. If `S>=T+L`, then `F` is increasing for `X>=M`. If
`S<T+L`, then `F` is concave, so on any interval `X>=M` its minimum is at an
endpoint. Consequently, for a fixed state, checking all prospective next
slopes `0<=d<=alpha_{m+1}` reduces to checking the largest one
`d=alpha_{m+1}`.

There may be a sharper one-variable invariant behind the S-bound. Write

`u=M/G`, `q=S/(T+L)`.

The needed S-bound is just `q>=(1-u)^2` for `0<=u<1`. A one-ratio optimizer
instead points to the stronger curve

`q >= Phi(u)=(1-u^{2/3})/(1+u-u^{2/3})`.

This curve has a clean equality source: in the `m=1` limit
`rho_1->1` and `alpha_2=alpha_1=x`, one has
`u=(1+x)^{-3}` and `q=Phi(u)`. A separate boundary family with
`alpha_1` large and `rho_1->0` gives `q=1-u`, which is weaker than `Phi` for
most of the interval. A `1,200,000`-sample probe for each `m=1,...,10` found
no failures of `q>=Phi(u)`. Proving this power-curve invariant would
immediately imply the S-bound and hence the endpoint credit threshold.
This is now the main candidate invariant: the one-ratio equality family gives
the curve, and higher-dimensional random searches stay strictly above it
except in degenerate `u->1` limits.

An even cleaner companion target is

`q >= 1-u^{2/3}`.

It is weaker than the `Phi` curve, and for very small `u` it is also weaker
than the needed S-bound `q>=(1-u)^2`, so it does not close the endpoint
credit by itself. In original variables it is the polynomial-shaped inequality

`(T+L-S)^3 G^2 <= (T+L)^3 M^2`.

A matching `1,200,000`-sample probe for each `m=1,...,10` found no failures.
This cubic form looks more approachable because it resembles a Holder-type
estimate connecting the weighted deficit `T+L-S`, the endpoint mass `G`, and
the margin `M`. It is best viewed as a possible companion estimate to the
power curve, or as the large-`u` part of a proof of the S-bound.

The cubic target is now proved for `m=1`. In this case the lower branch gives
`rho_1<=1`; by continuity write

`rho_1=1/(1+s)`, `alpha_2=alpha_1/(1+z)`, with `s,z>=0`.

Let `A=alpha_1`. After substituting these parameters into

`M^2(T+L)^3-G^2(T+L-S)^3`,

and clearing the positive denominator, the numerator is a polynomial in
`A,s,z` with `276` monomials and no negative coefficients. This proves the
Holder-type cubic base case. The saved coefficient check is
`logs/993_holder_m1_coefficients.log`.

The same coefficient-positivity trick does not extend naively to `m=2`. With
the natural parametrization

`rho_1=1/((1+s)(1+v))`, `rho_2=(1+v)/(1+s)`,

and

`alpha_2=A/(1+y)`, `alpha_3=A/((1+y)(1+z))`,

the staged cleared numerator has `234151` monomials, including `31950`
negative coefficients. This does not disprove the cubic target, but it rules
out the most direct generalization of the base-case proof.

The direct S-bound polynomial has the same issue. Under the natural `m=1`
parametrization its cleared numerator already has negative coefficients, and
the analogous staged `m=2` numerator has `47292` monomials with `21042`
negative coefficients. Thus the sufficient S-bound itself probably needs a
structural argument, not raw coefficient positivity.

For `m=1`, however, the hard region has a useful numerical shape. Fixing
`alpha_1` and `rho_1` and scanning the terminal slope, the minimum of

`G^2S-(G-M)^2(T+L)`

over the region `0<=M<G` always occurred at the boundary where `M=G`. At that
boundary the residual is `G^2S>=0`. This suggests a direct one-ratio proof by
showing the terminal-slope polynomial has no interior negative minimum in the
hard region.

This one-ratio S-bound is now proved. Write

`a=alpha_1/(1+alpha_1)`, `w=a rho_1`, and `alpha_2=a c`.

Then `0<a<1`, `0<=w<=a`, and `0<=c<=1/(1-a)`. After multiplying the original
quantities by the same positive factor, the one-ratio variables become

`g=alpha_2(1+alpha_2)=ac(1+ac)`,

`s=w+ac`,

`u=1-a+a^2+ac`,

and

`y=g-M=a^2c^2+w^2-w+cw`.

Thus the hard region is exactly `H:=a^2c^2+w^2-w+cw>=0`, and the desired
S-bound is

`F:=g^2s-y^2u>=0`.

The key identity is the concavity certificate

`F_{ww}=-2u(2H+(c+2w-1)^2)`.

So on each hard interval in `w`, the residual is concave. Since `H` is a
convex quadratic in `w`, the hard set inside `0<=w<=a` is a union of endpoint
intervals. A concave function on each such interval takes its minimum at an
endpoint. The endpoints are either `H=0`, `w=0`, or `w=a`.

At a hard boundary `H=0`,

`F=a^2c^2(1+ac)^2(ac+w)>=0`.

At the left endpoint,

`F(0)=a^3c^3(1+ac(1+a-a^2))>=0`.

At the right endpoint, put `H_a=a c^2+c+a-1`. Then

`F(a)=a^2(1-a)H_a K+a^3(1-a)^2(c+1)`,

where

`K=a^2c^2+a^2-ac^2+3ac-c+1`.

In the right-endpoint hard region `H_a>=0`. Also `K` is concave as a function
of `c`, while

`K(0)=1+a^2>0`

and

`K(1/(1-a))=a(1+a-a^2)/(1-a)>0`.

Hence `K>=0` on the whole allowed interval `0<=c<=1/(1-a)`, and `F(a)>=0`.
This proves the sufficient S-bound for `m=1`. The exact symbolic certificate
is saved in `notes/verify_993_m1_s_bound.py`, with output in
`logs/993_m1_s_bound_certificate.log`.

The same concavity mechanism has a general first-product form. Normalize by
the same factor `1/(1+alpha_1)`, so the first scaled mass is
`a=alpha_1/(1+alpha_1)`. Fix every variable except `p=p_1`, and write
`q=p_2`, while `b` denotes the scaled second mass. The only dependence on `p`
is

`S=S_0+ap`

and

`Y:=G-M=Y_0-(a-b)p+a^2p^2/q`.

For the S-bound residual

`F=G^2S-Y^2U`,

one has the exact identity

`F_{pp}=-2U((2a^2p/q-(a-b))^2+2a^2Y/q)`.

Therefore `F` is concave on the hard region `Y>=0`, and `Y` itself is a
convex quadratic in `p`. On any admissible interval of first-product weights,
the hard set is a union of endpoint intervals, and a counterexample can only
come from a hard boundary `Y=0` or from an endpoint forced by the structural
constraints on `p_1`.

For `m=1`, these endpoints are exactly the three cases closed above. For
`m=2`, this reduces the next proof to the endpoint families `p_1=0`, adjacent
ratio equality `rho_1=rho_2`, and lower-branch equality. The symbolic check is
saved in `notes/verify_993_first_product_concavity.py`, with output in
`logs/993_first_product_concavity_certificate.log`.

The first of the `m=2` endpoint families, `p_1=0`, is also closed. Put
`x=alpha_2` after the same normalization and write `alpha_3=dx`, with
`0<=d<=1`. Let `p=p_2` and `K=1-a+a^2`. On this slice,

`G_3=dx(1+x)`,

`G=dx(1+x)(1+dx)`,

`S=px+G_3`,

`U=K+x+G_3`,

and

`M=px+(1-p)G_3`.

The residual is concave in `p`, since

`F_{pp}=-2x^2(d(1+x)-1)^2U`.

The valid set is cut out by `0<=Y=G-M<=G`, so every minimum occurs at
`Y=0`, `M=0`, or `p=0`. The boundary `Y=0` gives `F=G^2S>=0`. At `p=0`,

`F=d^3x^3(1+x)^2(1+x+dx(1+x)+a d x(1-a))>=0`.

On the boundary `M=0`, one has `p=d(1+x)/(d(1+x)-1)`, so

`F=G^2(S-U)`,

and

`S-U=(x+K-Kd(1+x))/(d(1+x)-1)`.

The denominator is positive on this boundary. Since `d<=1` and `K<=1`, the
numerator is at least `x+K-K(1+x)=x(1-K)>=0`. Hence the `p_1=0` endpoint is
proved. The exact check is saved in `notes/verify_993_m2_zero_first_endpoint.py`,
with output in `logs/993_m2_zero_first_endpoint_certificate.log`.

For the `m=2` lower-branch equality endpoint `p_1=1`, two boundary pieces are
now closed. Keep the same normalization and write `p=p_2`, `alpha_3=dx`, and

`H=G-a(1-a)`.

First take the boundary `p=1`. Then `M=a(1-a)`, so the hard condition is
`H>=0`. Dividing the residual by `H` as a polynomial in `d` gives

`F=H(1-a)P+a^2(1-a)^2(a+dx(1+x)+x)`.

The last term is positive. Also

`P_{dd}=2x^2(a-1)(1+x)<=0`,

so `P` is concave in `d` and its minimum on the hard interval occurs at either
`H=0` or `d=1`. At `H=0`,

`P=2a(a+dx(1+x)+x)>=0`.

At `d=1`, put `x=ta/(1-a)`, with `0<=t<=1`. After multiplying by the positive
denominator, the claim becomes `B(t)<=0`, where

`B_t=(1-a+at)(1-5a+3at)`,

`B(0)=-(1-a)^2(1+a^2)`,

and

`B(1)=-a(a^3-2a^2+2)`.

The first derivative has at most one zero in `[0,1]`, and that zero is a local
minimum, so the maximum of `B` is at an endpoint. Both endpoints are negative,
hence `P>=0` and the `p=1` boundary is closed.

Second take the boundary `M=0`. Then `F=G^2(S-U)`, and

`S-U=x(p-1)-(1-a)^2`.

Put `E=x(p-1)` and `L=d(1+x)-1`. The equation `M=0` gives

`EL=a(1-a/p)=a(E+(1-a)x)/(E+x)`,

while `d<=1` gives `L<=x`. If `E<=(1-a)^2`, these two facts imply

`Ex(E+x)>=a(E+(1-a)x)`.

But the difference

`R=a(E+(1-a)x)-Ex(E+x)`

is nonnegative on the rectangle `0<=E<=(1-a)^2`, `0<=x<=a/(1-a)`, and is
strictly positive in the `M=0` situation. As a function of `x` it is concave,
so its minimum is at an endpoint; at `x=0` it is `aE`, and at
`x=a/(1-a)` it is concave in `E`, with endpoint values `a^2` and
`a^2(1-a)^2`. This contradiction proves `E>(1-a)^2`, so `S-U>=0` and the
`M=0` boundary is closed. The symbolic check is saved in
`notes/verify_993_m2_lower_eq_boundaries.py`, with output in
`logs/993_m2_lower_eq_boundaries.log`.

The lower-branch-equality interior is now closed. The residual is concave in
`p=p_2` throughout the valid region. In exact form,

`F_{pp}=-2UQ/p^4`,

where

`Q=3a^4-2a^3p+2a^2d^2px^3+2a^2d^2px^2+2a^2px+p^4x^2(d(1+x)-1)^2`.

A focused `2,000,000`-sample probe over the lower-branch-equality endpoint
found no valid point with `Q<0`; the smallest sampled `Q` was about
`6.6e-7`, close to the already-closed `p=1` boundary. The proof explains this.

Put `L=d(1+x)-1`, so `-1<=L<=x`, and multiply `Q` by the positive factor
`1+x`. Also put

`D=2a^2+p^3(1+x)`.

After scaling `Y=G-M` by `p(1+x)`, polynomial division gives

`Y_scaled=Q/((1+x)D)+(1+x)U/D`,

where `U` is linear in `L`. Thus `Q<0` and `U<0` imply `Y<0`.

It remains to show `Q<0 => U<0`. Since `Q` is a quadratic in `L`, `Q<0`
implies its discriminant is positive. The discriminant is

`-4a^2px^2(1+x)^3 R`,

where

`R=6a^4-4a^3p+3a^2p^3(1+x)+4a^2px-2ap^4(1+x)+4p^4x^2+2p^4x`.

So `Q<0` implies `R<0`. Let

`C=(a^2(p+2)^2-4p^3(1+x))/8`.

If `C>0`, then `a>2p^{3/2}/(p+2)`. Since `a<1`, this forces
`2p^{3/2}<p+2`; for `p>=1` this gives `sqrt(p)<2`, hence
`2p^{3/2}/(p+2)>=2p/3`. Therefore `3a>2p`. But `R` is increasing in `x` and

`R(0)=a(3a-2p)(2a^2+p^3)>0`,

contradicting `R<0`. Hence `C<=0` whenever `R<0`.

At the vertex of the quadratic `Q`, the numerator of `-U` has the form

`CR + a^2((2a^2+p^3)D_0+p(p+2)D_1x)/8`.

Here `D_0,D_1>=0`: both are concave quadratics in `a`, and their endpoint
values at `a=0` and `a=1` are positive for `p>=1`. Thus `R<0` gives
`U(vertex)<0`. The root of the increasing linear function `U` lies to the
right of the vertex; at that root, `Q` is a positive square times a positive
factor. Hence the whole interval where `Q<0` lies in `U<0`, and therefore in
`Y<0`. This proves `Y>=0 => Q>=0`, so `F` is concave in `p` on the valid
region.

The valid `p`-interval endpoints are `p=1`, `M=0`, and `Y=0`. The first two
were closed above, while `Y=0` gives `F=G^2S>=0`. Therefore the `m=2`
lower-branch equality endpoint is proved. The exact symbolic certificate is
saved in `notes/verify_993_m2_lower_eq_interior.py`, with output in
`logs/993_m2_lower_eq_interior_certificate.log`. The earlier probe output is
saved in `logs/993_m2_lower_eq_interior_probe.log`.

Thus, in the `m=2` first-product reduction, only the adjacent-ratio equality
endpoint remains:

`rho_1=rho_2=p`, equivalently `p_1=p^2`, `p_2=p`, with `0<=p<=1`.

The endpoint values `p=0` and `p=1` are already covered by the `p_1=0` and
lower-branch-equality endpoint proofs. A dense probe over `200,000` random
states, with a `401`-point grid in `p` for each state, found no interior grid
minimum; every minimum occurred at `p=0` or `p=1`. The best point with positive
distance from `p=0`, `p=1`, `M=0`, and `Y=0` had scaled residual about
`1.2e-9`. This points to the next target: prove that this one-variable
degree-six residual has no interior local minimum in the valid region
`M>=0`, `Y>=0`. The probe output is saved in
`logs/993_m2_adjacent_equality_probe.log`.

A sharper selector probe makes this endpoint more structured. It is cleaner to
write

`r=d x`,

so the endpoint variables are `0<=r<=x<=a/(1-a)` and

`G=r(1+x)(1+r)`,

`S=ap^2+xp+r(1+x)`,

`M=ap^2(1-ap)+p(1-p)x+(1-p)r(1+x)`,

and

`Y=G-M=a^2p^3+(x-a)p^2+(r(1+x)-x)p+r^2(1+x)`.

Thus `M>=0` is automatic, and the hard condition is again just `Y>=0`. Put

`H=Y(1)=r(1+x)(1+r)-a(1-a)`

and

`E=F(1)-F(0)`.

A `1,000,000`-sample run found no failure of the following three stronger
branch inequalities on the hard set:

- if `H<=0`, then `F>=F(0)`;
- if `H>=0` and `E>=0`, then `F>=F(0)+p^2E`;
- if `H>=0` and `E<=0`, then `F>=F(1)+(1-p)(F(0)-F(1))`.

These three statements would close the adjacent-ratio endpoint, because the
already-proved endpoint cases give `F(0)>=0` and, when `H>=0`, `F(1)>=0`.
The same script records exact algebraic structure behind this selector:

`F-F(0)` has a factor `p`,

`F-F(0)-p^2E` has a factor `p(1-p)`,

and

`F-F(1)-(1-p)(F(0)-F(1))` has a factor `p(1-p)`.

Also, the critical equation for the ratio `Y^2/S`,

`2Y_pS-YS_p=0`,

is only quadratic in `r`, with leading coefficient

`(1+x)(x+2-2ap)>0`.

So an alternate proof route is to prove that every interior maximum of `Y^2/S`
lies below the endpoint threshold. The exact identities and probe output are
saved in `notes/probe_993_m2_adjacent_selector.py` and
`logs/993_m2_adjacent_selector_probe.log`.

The endpoint selector has a cleaner algebraic reduction. Continue with
`c=dx` and put

`D=x+2-a`, `E=F(1)-F(0)`.

Define `R` by

`D(F-F(0))=p((x+p(2-a))E+(1-p)R)`.

Then the companion identity is

`D(F-F(1))=(1-p)(-(x+2-a+p(2-a))E+pR)`.

Since all displayed prefactors except `E` are nonnegative, the single
implication

`Y>=0 => R>=0`

would close the whole `H=Y(1)>=0` side: if `E>=0` then `F>=F(0)`, and if
`E<=0` then `F>=F(1)`. Both endpoints are already proved when `H>=0`.

The same reduction exposes the remaining `H<0` side. There the numerical
evidence points to monotonicity in `c`:

`d(F-F(0))/dc >=0`

throughout the hard region `Y>=0`, `H<=0`. This would close the invalid-right
endpoint case because the left hard boundary is either `p=0` or `Y=0`; at
`Y=0`, one has `F=G^2S` and hence

`F-F(0)=G^2(ap^2+xp)+(G-G_3)^2U>=0`.

A `1,000,000`-sample probe found no failure of either `R>=0` on the `H>=0`
hard branch or this `c`-monotonicity on the `H<=0` hard branch. The exact
symbolic identities and the probe are saved in
`notes/verify_993_m2_adjacent_R_reduction.py`, with output in
`logs/993_m2_adjacent_R_reduction.log`.

The `H>=0` target also has a one-dimensional slice reduction. For fixed
`a,c,p`, the inequalities `H>=0`, `Y>=0`, and `c<=x<=a/(1-a)` again cut out
an explicit interval in `x`. On this interval, `R` is a quartic in `x`; its
derivative is cubic, so the exact slice minimum is obtained by checking the
two endpoints and the real derivative roots. A `200,000`-slice probe over the
full structural range `0<=c<=a/(1-a)` found no negative value and no interior
minimum. Every minimum occurred at the lower endpoint of the slice: `144,973`
at `x=c`, `1,975` at the `H=0` boundary, and `798` at the `Y=0` boundary.
Thus the experimental `H>=0` target is now to prove `R>=0` only on those
three lower-boundary families. The exact probe is saved in
`notes/probe_993_m2_adjacent_R_slice.py`, with output in
`logs/993_m2_adjacent_R_slice_probe.log`.

The lower-boundary families reduce further in one variable. On `x=c` and
`H=0`, the boundary value of `R` is a quartic in `p`, while the hard condition
`Y>=0` is cubic in `p`. On `Y=0`, the boundary value is rational in `p`; the
valid interval is cut out by the four polynomial inequalities `Y_x>0`,
`x>=c`, `x<=a/(1-a)`, and `H>=0`. A `100,000`-sample probe over the full
structural range minimized these one-variable problems exactly on every
nonempty sampled interval. On `x=c`, every minimum was at `p=0`. On `H=0`,
every minimum was at `p=0` or `p=1`. On `Y=0`, every minimum was already at
`p=1` or at the intersection with `x=c`. This suggests that the `H>=0` proof
of `R>=0` may now be reduced to endpoint certificates on `x=c,p=0` and on
`H=0,p=0,1`, plus the corresponding one-variable no-interior-minimum
statements. The exact probe is saved in
`notes/probe_993_m2_adjacent_R_boundaries.py`, with output in
`logs/993_m2_adjacent_R_boundaries_probe.log`.

There is also a derivative route to the same `x`-boundary reduction. Dividing
`R_x` by `Y` as a polynomial in `p` gives the exact identity

`R_x=QY+P`,

where `Q` is affine in `p` and `P` is quadratic in `p`. The structural
substitution

`a=(x+t)/(1+x+t)`, `c=x/(1+v)`

proves `Q>=0`: after substitution, the numerators of `Q(0)` and `Q(1)` each
have only nonnegative coefficients, and affine interpolation gives the result
for `0<=p<=1`. Thus the remaining derivative target is the smaller statement

`H>=0 => P>=0`,

with no `Y` assumption. A `500,000`-sample probe minimized this quadratic
exactly in `p` under only `H>=0` and the structural bounds. It found no
negative value; most minima occurred at `p=0`, with the rest at the quadratic
vertex. The exact identity and probe are saved in
`notes/verify_993_m2_adjacent_Rx_reduction.py`, with output in
`logs/993_m2_adjacent_Rx_reduction.log`.

The remaining `P>=0` statement has a useful shape. As a polynomial in `x`,
`P` is cubic, `P_x` is quadratic, `P_xx` is affine, and

`P_xxx=24c(1+c)(2c+p)>=0`.

A `200,000`-slice probe over the full `H>=0` structural domain minimized both
`P_x` and `P` exactly in `x`; every minimum occurred at the lower endpoint of
the `H>=0` interval, either `x=c` or `H=0`. On those two lower-boundary
families, exact minimization of the remaining quadratic in `p` found minima
only at `p=0` or at the quadratic vertex. Thus the current proof target is to
certify `P_x>=0`, then prove the two endpoint families `P(x=c)>=0` and
`P(H=0)>=0`. The exact probe is saved in
`notes/probe_993_m2_adjacent_P_shape.py`, with output in
`logs/993_m2_adjacent_P_shape_probe.log`.

The `P` target has an even sharper derivative tower. A second `200,000`-slice
probe minimized `P`, `P_x`, and `P_xx` exactly in `x` on the full `H>=0`
structural interval. In every case the minimum occurred at the lower endpoint,
again either `x=c` or `H=0`. On both lower-boundary families, exact
minimization in `p` found:

- `P_xx` is minimized at `p=0`;
- `P_x` is minimized at `p=0`;
- `P` is minimized either at `p=0` or at the quadratic vertex.

Thus a promising proof route is to certify `P_xx>=0` from the `p=0` lower
boundary checks, integrate to `P_x>=0`, and then handle the two remaining
quadratic boundary certificates for `P`. The exact probe is saved in
`notes/probe_993_m2_adjacent_P_derivative_tower.py`, with output in
`logs/993_m2_adjacent_P_derivative_tower_probe.log`.

The first step of this route is now certified. Since

`P_xxx=24c(1+c)(2c+p)>=0`,

`P_xx` is increasing in `x`, so it is enough to check the lower endpoint of
the `H>=0` interval. On both lower-boundary families, `P_xx` is a quadratic
in `p`; its value at `p=0` and its derivatives at `p=0` and `p=1` are
nonnegative, so the minimum is at `p=0`.

For `x=c`, the small-`c` case uses

`J=c(1+c)^2-a(1-a)>=0`.

Modulo `a^2-a+c(1+c)^2-J=0`, the three required quantities are linear in
`J` with nonnegative `J` coefficients; at `J=0`, the remaining inequalities
follow from `c<=1/5` and `0<=a<=1`. For `c>=1/5`, the structural substitution
`a=(c+s)/(1+c)`, `0<=s<=1`, gives Bernstein coefficients in `s` whose
coefficients are nonnegative after shifting `c=1/5+z`. For the `H=0`
endpoint, use instead `J=a(1-a)-c(1+c)^2>=0`; here `c<=1/5`, and the same
linear-in-`J` Bernstein checks apply. Therefore `P_xx>=0` throughout the
`H>=0` structural domain. The exact certificate is saved in
`notes/verify_993_m2_adjacent_Pxx_certificate.py`, with output in
`logs/993_m2_adjacent_Pxx_certificate.log`.

The next derivative step is partly closed. Since `P_xx>=0`, `P_x` is
increasing in `x`, so only the lower endpoint of the `H>=0` interval remains.
On the `x=c` lower endpoint with `c>=1/5`, the inequality `H>=0` is automatic:
`c(1+c)^2>1/4>=a(1-a)`. The structural constraint is encoded by

`a=(c+s)/(1+c)`, `0<=s<=1`.

For the quadratic `P_x(x=c)` in `p`, the value at `p=0` and the derivatives
at `p=0` and `p=1` have Bernstein expansions in `s` whose coefficients are
coefficient-positive after shifting `c=1/5+z`. Hence `P_x(x=c)>=0` on this
large-`c` branch. The exact certificate is saved in
`notes/verify_993_m2_adjacent_Px_large_c_certificate.py`, with output in
`logs/993_m2_adjacent_Px_large_c_certificate.log`.

The `H<0` derivative target has an additional one-dimensional reduction. If
`a,c,p` are fixed, then both hard inequalities are affine in `x`:

`Y=(c^2+cp+p^2-p)x+(c^2+cp+a^2p^3-ap^2)>=0`,

and

`H=(c^2+c)x+(c^2+c-a(1-a))<=0`.

The structural constraints add `c<=x<=a/(1-a)`. Therefore the hard `H<=0`
slice is an explicit interval in `x`. On this interval,

`d(F-F(0))/dc /(p(1+x))`

is only a quadratic polynomial in `x`. A `1,000,000`-slice probe minimized
this quadratic exactly on each nonempty interval; it found no negative value
and no case where the vertex was the minimizing point. Thus the next concrete
proof route for `H<0` is to prove the derivative inequality at the interval
endpoints `x=c`, `Y=0`, `H=0`, and `x=a/(1-a)` when those endpoints are active.
The exact slice probe is saved in `notes/probe_993_m2_adjacent_h_negative.py`,
with output in `logs/993_m2_adjacent_h_negative_probe.log`.

This slice picture sharpened further. The same probe now also minimizes the
`x`-derivative of the quadratic exactly on each hard interval. In another
`1,000,000`-slice run, the minimum of

`d/dx ( d(F-F(0))/dc /(p(1+x)) )`

was positive on every nonempty interval. Consequently the experimental
`H<0` target is stronger and simpler: the derivative in `c` is increasing in
`x`, so it should be enough to prove it only at the lower endpoint of the
hard interval. That lower endpoint is either `x=c` or the boundary `Y=0`.
In the same run, `108,844` valid slices had lower endpoint `x=c`, and `62`
had lower endpoint `Y=0`; the best lower-endpoint value was about
`1.8e-8`.

This `H<0` derivative target is now certified. Let

`W=d(F-F(0))/dc /(p(1+x))`.

First, the `Y=0` lower endpoint has a direct identity. With

`G_3=c(1+x)`, `G=G_3(1+c)`, `C=G-G_3`, and
`U=a+x+G_3+(1-a)^2`,

`F-F(0)=G^2p(ap+x)+(C^2-Y^2)U`.

Therefore, at `Y=0`,

`W=2c(1+c)(1+2c)(1+x)(ap+x)+(4c^3(1+x)U+c^4(1+x)^2)/p>=0`

for `p>0`; the degenerate `p=0` endpoint forces `c=0`.

Second, `W_x` is affine in `x`. Since `H<=0` bounds the hard interval above by
`x_H=a(1-a)/(c(1+c))-1`, it is enough to certify `W_x>=0` at `x=c` and
`x=x_H`. Both endpoints have Bernstein certificates after reducing by the
corresponding hard-boundary relation:

`a^2-a+c(1+c)(1+x)=0` on `H=0`,

and

`a^2-a+c(1+c)^2+K=0` on `x=c`, where
`K=a(1-a)-c(1+c)^2`.

In both cases, the Bernstein coefficients in `p` are increasing in `a`, and
substituting the lower bound for `a` leaves polynomials nonnegative on
`0<=c<=1/5`; this interval contains the branch because
`c(1+c)^2<=a(1-a)<=1/4`.

Finally, at the remaining lower endpoint `x=c`, the same `K` substitution gives
`[K^2]W(c)=-p^2(4c+p^3+2p)<=0`, so `W(c)` is concave in `K`. The feasible
conditions `K>=0` and `Y(c)>=0` form an interval in `K`; the `Y(c)=0` endpoint
is already covered by the `Y=0` identity, and the `K=0` endpoint has a
degree-five Bernstein certificate in `p`. Thus `W>=0` on the whole hard
`H<=0` slice, and consequently `F>=F(0)` on the `H<0` selector branch. The
exact certificate is saved in
`notes/verify_993_m2_adjacent_h_negative_certificate.py`, with output in
`logs/993_m2_adjacent_h_negative_certificate.log`.

The append-recurrence path also needs more than a one-line monotonicity
argument. Random tests that included the lower-branch cap `R^2 mu<=1` found no
real failures of the Holder-type residual after appending a final ratio, but
scans in `R` often had an interior minimum. Thus the induction cannot simply
reduce to either endpoint `R=rho_m` or `R=1/sqrt(mu)`.
The corresponding append test for the stronger `Phi` residual also found no
real failures; the smallest saved values are roundoff-level negatives at
degenerate `u` essentially equal to `1`. This supports trying to prove that
the actual append operation preserves the `Phi` feasible region, with the
lower-branch cap as an essential hypothesis.

Two stronger probes remove the equal-tail restriction. For a lower-branch
state with arbitrary terminal slope `alpha_{m+1}`, choose any prospective next
slope `d` with `0<=d<=alpha_{m+1}`, and put

`G(d)=d product_{i=1}^{m+1}(1+alpha_i)`.

Random searches for `m=1,...,10` found no failures of

`G(d)^2S >= (G(d)-M)^2(T+L)` whenever `0<=M<G(d)`.

This prospective form is better aligned with induction. If a new final ratio
`R` and a new final slope `d` are appended, then the short quantities update as

`M^+=R M-(R-1)G(d)`, `S^+=R S+G(d)`, and `T^++L=T+L+G(d)`.

The next proof attempt should be a one-step lemma showing that this update
preserves the prospective S-bound under the lower-branch restriction on `R`.
One tempting shortcut does not work: with earlier data fixed, the S-bound
residual is usually nonmonotone as the actual terminal slope varies. A scan for
`m=2,...,8` found the equal-terminal endpoint was not the worst point in most
valid samples. Thus this prospective invariant probably needs a direct
inductive argument, not another last-slope endpoint reduction.

For `t=5`, the lower-bound branch has a useful smaller form. Put

`A=alpha_1`, `B=alpha_2`, `C=alpha_3`, and `u=qrs`.

Then `q=u/(rs)`, the lower-branch condition is

`u^2<=r`,

and the target is equivalent to the unscaled inequality

`h>=A^2u^2/(rs(1+A))`.

The structural constraints also include `u<=rs` and `u<=r^2s`, coming from
`q<=1` and `q<=r`. Now package the last, harmful term as

`D=(s-1)G_4`.

For fixed `A,B,C,u,r,s`, the target decreases with `D` while the budget
increases with `D`, so the worst admissible value is

`D_* = min(D_s,L-K_0)`,

where

`L=1/(1+A)`,

`K_0=(us-1)A+(rs^2-1)B(1+A)+(s^2-1)C(1+A)(1+B)`,

and

`D_s=(s-1)C(1+A)(1+B)(1+C)`.

Equivalently, define

`K_s=K_0+D_s
     =(us-1)A+(rs^2-1)B(1+A)
       +C(1+A)(1+B)(s-1)(C+s+2)`.

If `K_s<=L`, the structural cap is active and the natural margin is

`S_s=uA+(rs-u)B(1+A)
     -C(1+A)(1+B)(C(s-1)+rs-1)
     -A^2u^2/(rs(1+A))`.

As a function of `C`, this margin is concave because

`d^2S_s/dC^2=-2(1+A)(1+B)(s-1)<0`.

Since `K_s` is increasing in `C`, the structural part reduces to endpoints:
`C=0`, `C=B`, or the boundary `K_s=L`. The endpoint `C=0` is immediate, as

`uA-A^2u^2/(rs(1+A))
 = uA(1-Aq/(1+A)) >= uA/(1+A)>0`

and `(rs-u)B(1+A)>=0`.

If `K_s>=L`, the budget cap is active and the natural margin is

`S_a=h_0-(L-K_0)-A^2u^2/(rs(1+A))`.

Here

`dS_a/dC=(1+A)(1+B)(s^2+s-1-rs)>0`,

because `r<=s` and `s>1`. Thus the active part is minimized at its left
endpoint, which is again the boundary `K_s=L`. Therefore the `t=5`
lower-bound branch is reduced to two endpoint targets:

1. `C=B` with `K_s<=L`;
2. the active boundary `K_s=L` with `0<=C<=B`.

The focused script `probe_t5_lower_branch.py` implements this last-slope
elimination. A `1,000,000`-sample run with seed `993` found no failures; the
smallest ordinary target margin was about `1.1e-10` in the degenerate
`q,r,s -> 1`, `A -> 0` limit. In the unscaled natural margin, the closest
sample was about `7.3e-16`, again with vanishing slopes. The best active-cap
sample had positive natural margin about `2.3e-2`, while a separate optimizer
pushed it down to about `2.1e-4` only near the boundary `K_s=L` with very small
slopes, matching the reduction above.

The same script now has an endpoint mode. It samples the `C=B` endpoint
directly and samples the boundary `K_s=L` by solving the boundary equation for
`u`. With seed `2400` and `1,000,000` trials it found no failures. The best
`C=B` natural margin was about `2.8e-13`, again from a tiny-slope degenerate
state. The best boundary natural margin was about `2.7e-4`. A separate
boundary optimizer pushed this down to about `3.7e-7`, also in a tiny-slope
state and with `C` essentially equal to `B`. This suggests that the endpoint
`C=B` is not just an artifact of the reduction; it is likely the algebraic
core of the remaining `t=5` lower branch.

The `C=B` endpoint has one more reduction. Put `x=rs`. Its natural margin is

`S_B=Au-A^2u^2/(x(1+A))
     +(1+A)B(1-u-B(x+s-2)-B^2(s-1))`.

For fixed `A,u,x,s`,

`dS_B/dB=-(1+A)(3B^2(s-1)+2B(s+x-2)+u-1)`.

At any interior stationary point this gives

`u=1-2B(s+x-2)-3B^2(s-1)`,

and consequently

`1-u-B(x+s-2)-B^2(s-1)
 =B(x+s-2)+2B^2(s-1)>=0`.

Thus every interior stationary point has positive margin, because the leading
part `Au-A^2u^2/(x(1+A))` is already positive. Therefore a counterexample on
the `C=B` endpoint can only occur at `B=0`, at `B=A`, or on the budget
boundary `K_s=L`. The endpoint `B=0` is immediate, so the remaining concrete
targets are the all-equal-slope corner `A=B=C` and the boundary `K_s=L`.
Optimizer probes of `A=B=C` again found only the tiny-slope zero limit.

The all-equal corner has a useful ratio endpoint reduction. Keeping
`A,u,s` fixed and writing `x=rs`, the all-equal natural margin is strictly
decreasing in `x`, since

`dS/dx=A^2u^2/(x^2(1+A))-A^2(1+A)<0`

from `u<=x`. Meanwhile the budget expression is increasing in `x`, with
derivative `A(1+A)s>0`. Hence this corner can only fail either on the budget
boundary `K_s=L`, already one of the remaining targets, or at the ratio
endpoint `x=s^2`, i.e. `r=s`. Direct optimization of this `r=s`,
`A=B=C` endpoint also found only the tiny-slope zero limit.

This last `r=s`, `A=B=C` endpoint is provable with the actual required target.
Let `S` denote its natural margin and `K` its structural budget. A direct
rearrangement gives

`S - A(1/(1+A)-K)/(1+A)
 = -A^2 P/(1+A)^2`,

where

`P=A^2s^2(q-s)
  +As^2(q-s)(q+2)
  +s^2(q-s)(q+1)-1`.

Since `q<s`, every displayed term in `P` is negative. Hence `P<0`, and

`S >= A(1/(1+A)-K)/(1+A)>=0`

whenever `K<=1/(1+A)`. Thus the all-equal endpoint is closed. The remaining
`t=5` lower-branch work is the active boundary `K_s=L`; the endpoint
reductions above show this is now the only unresolved place where the
last-slope-eliminated margin can be minimized.

The active boundary itself has a useful domination form. Write

`v=rs`, `w=(s-1)C`, and `delta=v+w-1`.

The boundary equation is

`(qvs-1)A+(vs-1)(1+A)B
 +(1+A)(1+B)w(C+s+2)=1/(1+A)`.

If `delta<=0`, the target is immediate. In the hard case `delta>0`, the
natural margin is

`S=v(qA+(1-q)(1+A)B-A^2q^2/(1+A))
  -C(1+A)(1+B)delta`.

Since `q<=1`, it is enough to prove the sharper domination

`C(1+A)(1+B)delta
 <= v(qA/(1+A)+(1-q)(1+A)B)`.

This domination has passed direct boundary sampling; no counterexample was
found in `2,000,000` random boundary samples. It is the cleanest single
inequality for the remaining active boundary, and the next paragraphs prove
it.

Two elementary facts help constrain it. First, on the active boundary one has
`w<1`. Indeed, if `w>=1`, then the positive tail term is greater than
`3(1+A)(1+B)`, while the two earlier terms are bounded below by
`-A-(1+A)B`; this would force `K_s>1`, contradicting
`K_s=1/(1+A)<=1`.

The domination inequality has no interior minimum in `C`. Fix `A,B,s` and
`v=rs`, and solve the active boundary for `q`. The domination margin

`D=v(qA/(1+A)+(1-q)(1+A)B)-C(1+A)(1+B)(v+C(s-1)-1)`

then becomes a quadratic polynomial in `C`. Its second derivative is

`D''=-2(1+B)(s-1)H/(As)`,

where

`H=A^2s+A(s+1)-B(1+A)^2`.

If `H>=0`, then `D` is concave in `C`, so its minimum on `0<=C<=B` is at an
endpoint. If `H<0`, then `D` is convex, but its derivative at `C=0` is

`D'(0)=(1+B)G/(As)`,

with

`G=B(1+A)^2(s-1)(s+2)+A^2s(1-v)+A(2-s^2-sv)`.

The inequality `H<0` gives `B(1+A)^2>A^2s+A(s+1)`, so

`G>A s(A+1)(s^2+s-1-v)`.

Since `v=rs<=s^2`, the last factor is at least `s-1>0`. Thus `D'(0)>0`.
In the convex case, `D` is increasing on the whole interval `C>=0`, and its
minimum is again at `C=0`. Therefore a counterexample to domination can only
occur on the endpoint `C=B`; the endpoint `C=0` is immediate.

It remains to prove domination on `C=B`, and this endpoint also collapses.
Put `P=(1+A)B`, `x=rs`, and `u=qx`. On `C=B`, the active boundary is

`A(us-1)+P(xs-1)+P(1+B)(s-1)(B+s+2)=1/(1+A)`,

and the domination margin is

`D=uA/(1+A)+(x-u)P-P(1+B)(x+B(s-1)-1)`.

Solving the boundary for `u` makes `D` an affine function of `x`. The feasible
`x` interval is contained between the relaxed crossing `q=r`, equivalently
`u=x^2/s`, and the relaxed crossing `q=0`, equivalently `u=0`; the constraints
`r<=s` and the lower branch only shrink this interval. Thus it is enough to
prove `D>0` at these two relaxed endpoints.

For the `q=0` endpoint, let

`F_0=-A+P(xs-1)+P(1+B)(s-1)(B+s+2)-1/(1+A)`.

Direct simplification gives

`(1+A)s(D+B F_0/s)
 =B(A+(s-1)(1+A)^2(1+B)^3)>0`.

On the active boundary `F_0=0`, so `D>0`.

For the `q=r` endpoint, write `r=q=x/s`. The boundary residual is

`F_r=A(x^2-1)+P(xs-1)+P(1+B)(s-1)(B+s+2)-1/(1+A)`.

A second direct simplification gives

`(1+A)s^2(D+B F_r/s)
 =B(1+A)^2(1+B)^3s(s-1)+s(x^2(A-B)-AB(x^2-1))`.

On the active boundary `F_r=0`. If `x<=1`, the right side is plainly
positive. If `x>1`, then the lower branch on this endpoint gives `x^3<=s`,
so `x^2-1<=s^{2/3}-1<=(2/3)(s-1)`. Since `(1+A)^2>=4A`,
the positive first term dominates the possible negative contribution
`sAB(x^2-1)`. Hence `D>0` at the `q=r` endpoint as well.

Therefore the domination inequality holds on the whole active boundary. This
closes the remaining active-boundary case in the `t=5` lower branch.
Combining this with the structural-cap reduction and the closed all-equal
endpoint proves the reduced `t=5` local slope lemma. Together with the
previous `t=3`, `t=4`, and terminal arguments, this now covers every hard
early-plateau first-positive index for `m<=6`.

Second, on the sub-boundary `C=B`, let `x=rs` and solve the boundary equation
for `u=qx`. The resulting margin is

`S_B=Au-A^2u^2/(x(1+A))
     +(1+A)B(1-u-B(x+s-2)-B^2(s-1))`.

A direct differentiation gives

`d^2S_B/dx^2
 = -2N^2/(s^2x^3(1+A)^3)<=0`,

where

`N=A^2B^3(s-1)+A^2B^2(s^2+2s-3)
  +A^2B(s^2+s-3)-A^2
  +2AB^3(s-1)+2AB^2(s^2+2s-3)
  +2AB(s^2+s-3)-A
  +B^3(s-1)+B^2(s^2+2s-3)+B(s^2+s-3)-1`.

Thus the `C=B` active-boundary slice is concave in `x`; any minimum occurs at
a feasible endpoint of the `x` interval. Direct endpoint optimization of the
ratio endpoint `x=s^2` found only positive margins, with the minimum moving
toward the large-`s`, tiny-slope limit. The remaining checks are therefore
endpoint checks for this concave slice plus the general domination inequality
above.

Endpoint-specific optimization of this `C=B` concave slice gives a clearer
picture of the remaining endpoint work. The `q=0` limit and the ratio endpoint
`x=s^2` appear to meet at the same worst limiting family, with natural margin
about `2.43e-7` at the current search scale. The `q=r` endpoint is less tight;
the best sampled margin was about `3.75e-5`. A lower-branch equality endpoint
was not found as an active minimizer in this parameterization. This suggests
that the next concrete algebraic target should be the combined `q=0`,
`x=s^2`, `C=B` endpoint family, followed by the `q=r` endpoint.

The combined `q=0`, `x=s^2`, `C=B` endpoint is also closed. In this limit the
margin is

`S=(1+A)B(1-B(s-1)(s+B+2))`.

The boundary equation is

`-A+(1+A)B(s-1)(s^2+s+1+(1+B)(s+B+2))=1/(1+A)`.

Since the bracket is larger than `(1+B)(s+B+2)`, it follows that

`(1+A)(1+B)B(s-1)(s+B+2) < A+1/(1+A)`.

Therefore

`B(s-1)(s+B+2)
 < (A^2+A+1)/((1+A)^2(1+B)) < 1`,

and hence `S>0`. Thus the tight endpoint family seen by the optimizer is
proved; the remaining explicit endpoint from the `C=B` concavity reduction is
the `q=r` endpoint.

For the `q=r` endpoint, it is cleaner to put

`x=qs`.

Then `r=q=x/s`, the lower-branch condition is `x^3<=s`, and the active
boundary becomes the quadratic equation

`A(x^2-1)+(1+A)B(xs-1)
 +(1+A)B(1+B)(s-1)(B+s+2)=1/(1+A)`.

The natural margin on this endpoint is

`S=Ax^2/s-A^2x^3/(s^2(1+A))
  +(1+A)B(1-x^2/s-B(x+s-2)-B^2(s-1))`.

The script `probe_t5_lower_branch.py` now has `qr-endpoint` and `qr-optimize`
modes which solve the quadratic exactly and test this endpoint. With seed
`5100` and `2,000,000` random samples, `102,489` admissible endpoint states
had no failure; the best natural margin was about `4.05e-5`. The optimizer
again found the same limiting family as before, with margin about `3.75e-5`
at the current search scale.

That optimizer lands at a more specific corner: `B=A` and lower-branch
equality `x^3=s`. This tight corner is provable. Write `s=p^3`, so
`x=p` and `q=r=p^{-2}`. With `B=A`, direct rearrangement gives

`S - A(1/(1+A)-K)/p^3
 = A(1+A)^4(p-1)(p^2+p+1)/p^3`.

Thus `S>0` on the boundary `K=1/(1+A)`. The apparent worst corner of the
`q=r` endpoint is closed, but the rest of the `q=r` endpoint still needs an
argument away from `B=A` or away from lower-branch equality.

This can be strengthened: the whole `B=A` face of the `q=r` endpoint is
closed, not only the lower-branch-equality corner. Let

`F=A(x^2-1)+(1+A)A(xs-1)
  +A(1+A)^2(s-1)(A+s+2)-1/(1+A)`.

This is the boundary residual on the `B=A` face. A direct simplification gives

`(1+A)s^2(S+A F/s)
 =A(s^2-s)(1+A)^5+A^2(s-x^3)`.

On the active boundary `F=0`, while `s>1` and the lower branch gives
`x^3<=s`. Hence `S>0` on the whole `B=A` face. The remaining `q=r` endpoint
work after this face is genuinely interior in the slope ratio `B/A`.

There is a complementary multiplier that closes the whole `q=r` endpoint. For
the general `B<=A` endpoint boundary residual `F`, direct
simplification gives

`(1+A)s^2(S+B F/s)
 =(1+A)^2B(1+B)^3s(s-1)+A^2x^2(s-x)
  +s(x^2(A-B)-AB(x^2-1))`.

On the active boundary `F=0`. The second term and `s x^2(A-B)` are
nonnegative, and the only possible negative contribution is
`-sAB(x^2-1)`. If `x<=1`, this contribution is also nonnegative. If `x>1`,
then the lower branch gives `x^2<=s^{2/3}`, so by concavity
`x^2-1<=s^{2/3}-1<=(2/3)(s-1)`. Meanwhile `(1+A)^2>=4A` and
`(1+B)^3>=1`, so

`(1+A)^2B(1+B)^3s(s-1)-sAB(x^2-1)
 >=sAB(4(s-1)-(x^2-1))>0`.

Thus `S>0` on the active boundary throughout the `q=r` endpoint.

An extended `qr-optimize` run with larger allowed `s` shows the other limiting
direction. When the upper search range for `s` is increased from about `159`
to about `10^3`, `10^4`, and `10^5`, the best margin keeps decreasing but the
optimizer moves toward `q=0` rather than toward the lower-branch equality
corner. For example, at `s` about `10^5`, the best point has
`q` about `7.9e-8` and `x^3/s` about `4.9e-12`. This is a distinct
small-`q`, large-`s` limiting direction inside the `q=r` endpoint, not the
previously closed `q=0`, `x=s^2`, `C=B` ratio endpoint. At this stage the
`q=r` endpoint appeared to have two controlling limiting families, but the
multiplier identity above now closes both families and all interpolating
states.

The limiting endpoint `x=0` of this second family is also closed. At `x=0`
the active boundary is

`-A-(1+A)B+(1+A)B(1+B)(s-1)(B+s+2)=1/(1+A)`,

and the margin factors as

`S=(1+A)B(1+B)(1-B(s-1))`.

It remains to show `B(s-1)<1`. If instead `y=B(s-1)>=1`, then the left side
tail term in the boundary is

`(1+A)(1+B)y(B+s+2)
 =(1+A)(1+B)y(y/B+B+3)`.

Since `y>=1`, this is at least

`(1+A)(1+B)(1/B+B+3)`,

which is strictly larger than

`A+(1+A)B+1/(1+A)`.

Indeed, the difference contains the positive term `(1+A)(1+B)/B` and the
remaining part is at least `3+2A-1/(1+A)>0`. This contradicts the boundary
equation. Hence `B(s-1)<1`, and the `x=0` small-`q` limiting endpoint has
`S>0`. This direct endpoint check is subsumed by the full multiplier proof
above, but it is a useful independent check on the large-`s` limiting family.

In fact the whole large-`s` part of the `q=r` endpoint is closed. Put
`y=B(s-1)` and

`M=1-y-x^2/s-B(x+y-1)`.

Then the margin is

`S=A x^2/s(1-Ax/(s(1+A)))+(1+A)BM`.

The first term is positive because `x^3<=s` implies `x<s`. It remains to
control `M`. The boundary equation gives

`(1+A)(1+B)y(B+s+2)
 =1/(1+A)+A(1-x^2)+(1+A)B(1-xs)`.

The right side is at most `1/(1+A)+A+(1+A)B`, hence

`y(B+s+2)
 <= (A/(1+A)+B+1/(1+A)^2)/(1+B)<1`.

Thus `y<1/(s+2)` and `B<1/((s+2)(s-1))`. Also `x<=s^{1/3}` and
`x+y-1<x`, so

`M>1-1/(s+2)-s^{-1/3}-s^{1/3}/((s+2)(s-1))`.

For `s>=4`, the last three terms are bounded by `1/6`, `2/3`, and `1/9`,
respectively, so `M>1/18`. This gives a separate proof of the `s>=4` part of
the `q=r` endpoint; the multiplier identity above is stronger and proves all
`s>1`.
The script now also has `qr-domination` and `qr-dom-optimize` modes for this
endpoint; a `1,000,000` sample run with seed `5205` found no failures in
`4,022` hard states, and the domination optimizer moved to the now-proved
large-`s` regime.

Together with the `q=0`, `x=s^2`, `C=B` endpoint proof, the multiplier
identity closes the explicit endpoints of the concave `C=B` active-boundary
slice. The affine endpoint argument for domination above then closes the
remaining interior active-boundary states.

One tempting shortcut is false, and this is a useful warning for the remaining
proof. The required target is

`h>=A^2q^2rs/(1+A)`,

while the stronger inequality

`h>=Aq^2rs`

would have implied it. Initial random sampling missed failures of this
stronger target, but a scale-free optimizer found a degenerate counterexample.
With

`q=0.9999999849999994`,

`r=1.0000000099999848`,

`s=1.0000000100000057`,

and `A=B=C=D=0.2247452646501279`, the eliminated last-slope candidate has

`strong_margin=-1.69e-15`,

while the actual required natural margin is still about `0.1835`. Thus the
linear target is too strong exactly near the equal-slope, equal-ratio boundary.

With `p=qrs` and `lambda=q^2rs`, the stronger margin after packaging
`E=(s-1)G_4` is

`S=p(1-q)A+(rs-p)(1+A)B+s(1-r)(1+A)(1+B)C-E`.

The same last-slope elimination applies: the worst value is

`E_*=min(E_s,L-K_0)`.

On the structural side this gives

`S_s=p(1-q)A+(rs-p)(1+A)B
     +(1+A)(1+B)C(1-rs-(s-1)C)`,

which is concave in `C`, while the active side is linear increasing in `C`
because the coefficient of `C` is

`(1+A)(1+B)(s^2+s-rs-1)>0`.

Thus the stronger `t=5` target would reduce to the same endpoint families
`C=0`, `C=B`, and `K_s=L`, but the equal-slope endpoint above shows this route
cannot close the problem. The focused lower-branch script still reports
`strong_margin`, because failures of that stronger margin identify where the
proof must use the weaker factor `A/(1+A)`.

The same false shortcut explains why the scale-free obstruction route fails.
Let

`x=G_2/G_1`, `y=G_3/G_2`, and `z=G_4/G_3`.

Then `K=AW`, where

`W=(qrs^2-1)+(rs^2-1)x+(s^2-1)xy+(s-1)xyz`.

Failure of the stronger target is exactly

`rs(1-q)(q+x)+s(1-r)xy < (s-1)xyz`.

The slope constraints imply `A>=U`, with

`U=max(0,x-1,(y-1)/(x+1-y),
       (z-1)/(xy-(z-1)(1+x)))`,

where the last two fractions are used only when their numerators are positive.
It would have been enough to prove

`U(1+U)W>=1`

for every failure shape, because the budget condition is
`A(1+A)W<1`. However, after reparameterizing the optimizer to search directly
on the failure surface, `probe_t5_ratio_obstruction.py` found a finite shape
with `U(1+U)W` about `2.8e-8`, again at the same nearly equal-ratio,
equal-slope boundary. So the next proof should return to the required margin,
not the stronger linear target.

There is a complementary ratio-of-jumps route for proving at least the
budgeted nonnegativity of `H`. Put

`rho=F_2/F_1`, `tau=F_3/F_2`,

and

`U=max(0,rho-1,(tau-1)/(rho+1-tau))`.

The slope constraints imply `F_1>=U(1+U)`. In the `y=1`, `s=r` reduction, if
`H<0`, then

`qr+r(1-q)rho < (r-1)rho tau`.

The normalized budget is

`F_1 W`,

where

`W=(qr^2-1)+(r^2-1)rho+(r-1)rho tau`.

So it would be enough to prove

`U(1+U)W>1`

under the displayed strict `H<0` inequality. A direct `5,000,000` sample probe
found no failure; the smallest sampled product was about `5.29`.

One important subcase already has a clean algebraic core. If `rho>1` and
`tau<=rho`, then `U=rho-1`. For fixed `r,rho,tau`, the budget coefficient `W`
is minimized on the boundary of the strict `H<0` inequality. In the branch
where this boundary has `q>0`, the resulting expression is linear in `tau`;
the endpoint `tau=0` gives a value greater than `rho`, while the endpoint
`tau=rho` gives

`U(1+U)W >= rho+rho^4(r-1)>1`.

If the boundary instead has `q=0`, then `tau>=r/(r-1)` and the endpoint
`tau=r/(r-1)` gives

`U(1+U)W-1 >= (rho^4+rho^2-2rho+1)/(rho-1)>0`.

Thus the `rho>1,tau<=rho` subcase cannot occur under budget `<1`. The
remaining cases are `rho<=1` and `rho>1,tau>rho`; both have the same flavor
but use the `(tau-1)/(rho+1-tau)` term in `U`.

There is also a useful degree-independent slope budget that proves the same
uncorrected bound whenever `t=m`, and suggests the next general sublemma. Put

`x_i=q_{m+1-i}`

for `0<=i<=m+1`, and, on the nonpositive block,

`B_i=x_{i+1}-x_i=-theta_i`.

Let

`h=B_0/x_0`.

Log-concavity of `Q` gives

`B_i/x_i<=B_{i-1}/x_{i-1}`

for `1<=i<t`. Hence every downward jump satisfies

`max(0,B_{i+1}-B_i)<=B_i^2/x_i<=h B_i`.

Therefore the bad variation `V` obeys

`V<=h N`,

where

`N=sum_{i=1}^{t-1}(p_i-1)B_i`

is the weighted negative budget in `D_m`. If `t=m`, then `D_m>0` says

`N<x_0-1<x_0`,

so

`V<hx_0=B_0=-theta_0`.

This recovers the terminal sign-change case and covers examples with several
bad jumps, such as

`P=(1,2,2,1,1)`, `Q=(1,30,24,19,15,11,1)`,

where

`theta=(-4,-4,-5,-6,29)`,

`V=2`, `B_0=4`, `D_4=1`, and `D_3=4`.

This terminal estimate is essentially sharp.  The previous example has ratio
`V/B_0=1/2`, but the same terminal mechanism can approach `1`.  For example,
with `P=(1,2,2,1,1)`,

- `Q=(1,94,72,55,42,32,1)` gives `V/B_0=9/10`;
- `Q=(1,208,158,120,91,69,1)` gives `V/B_0=21/22`;
- `Q=(1,944,714,540,408,308,1)` gives `V/B_0=49/50`.

The asymptotic reason is simple.  If the tail drops satisfy
`B_i approx lambda x_i` for `0<=i<=3`, then log-concavity is nearly sharp and,
for `P=(1,2,2,1,1)`,

`D_4>0` is governed by

`lambda(1+lambda)(2+lambda)<1`,

while

`V/B_0 approx lambda(1+lambda)(2+lambda)`.

Taking `lambda` up to the positive root of
`lambda(1+lambda)(2+lambda)=1` makes `V/B_0` approach `1` from below.  Thus the
terminal proof cannot be strengthened to `V<=cB_0` for any fixed `c<1`.

Added a terminal-drop frontier mode to `notes/profile_boundary_variation.py`
to test this slice directly.  For degree `(4,6)` it enumerates bounded drop
quadruples and degree-4 factor intervals, checks only the variation-maximizing
frontier factor in each interval, and validates the reported top states through
the canonical `variation_state` filter.  A logged run

```text
PYTHONPATH=notes uv run python notes/profile_boundary_variation.py 4 6 \
  --terminal-degree4-drop-search --terminal-n-cap 500 \
  --terminal-drop-cap 30 --terminal-a-cap 60 --terminal-b-cap 60 \
  --terminal-c-cap 4 --top 20
```

covered `299749` admissible drop intervals, `877181` valid factor intervals,
and `217817` frontier states, with no failures of `V<=B_0`.  The largest
capped state had

`P=(1,3,2,1,1)`,
`Q=(1,135,109,88,71,57,1)`,
`theta=(-14,-17,-21,-26,134)`,
and `V/B_0=13/14`.

Log:

- `logs/993_boundary_variation_terminal_drop_search_c4.log`.

For `t<m`, the same calculation gives only the coarse estimate

`V<=hN`, while `D_m>0` gives

`N<x_0+P_+`,

where

`P_+=sum_{i=t}^{m-1}(p_i-1)theta_i`.

This would prove the corrected bound if

`hP_+<=G_+`,

where

`G_+=sum_{i=t}^{m-1}(p_{i-1}-p_i)theta_i`.

A termwise sufficient condition is

`h<L-1`.

Indeed, every positive-block shifted ratio is at least `L`, so

`p_{i-1}-p_i>=p_i(L-1)>h(p_i-1)`.

However, this slope-budget route is too crude. The condition `hP_+<=G_+` can
fail even in safe positive-next states. For example,

`P=(1,11,5,2,1)`, `Q=(1,10202,10203,10101,10000,2000,1)`

gives

`theta=(-8000,-101,-102,1,10201)`,

with `D_4=582`, `D_3=19185`, `C=-1619`, and `L=11/5>2=y`. Here

`V=10`, `B_0+G_+=8003`,

so the corrected variation bound has enormous room, but

`hP_+=4>3=G_+`.

The reason is that `V<=hN` wastes almost all information: `N` counts the whole
negative budget, while `V` only counts the actual downward jumps.

The simpler tail-slope diagnostic is not necessary either. For example,

`P=(1,3,2,1,1)`, `Q=(1,44,45,38,32,21,1)`

gives

`theta=(-11,-6,-7,1,43)`, `D_4=1`, `D_3=19`,

and has a bad jump, but

`B_0/x_0=11/21 >= 1/2=L-1`.

It is still controlled because `V=2` and `B_0+G_+=12`.

The updated verifier therefore tracks the real target

`V<=B_0+G_+`

through the `early_plateau_corrected_variation_controlled` bucket, while the
tail-slope and slope-budget buckets remain diagnostics for failed proof
attempts. Proving `V<=B_0+G_+` directly, without passing through the full
negative budget `N`, is now the next local target.

Added `notes/profile_boundary_variation.py` to profile this exact target.  It
filters the same hard early-plateau states and records the ratio
`V/(B_0+G_+)`, along with examples where the older tail-slope and slope-budget
diagnostics succeed or fail.  Uniform random admissible-factor sampling mostly
misses this branch: for example, `(8,9)` with `50,000` random trials, first cap
`2000`, and seed `993` checked `2936` double-bad local states in
`verify_boundary_domination.py`, but none reached the positive-next
early-plateau variation target.

The profiler correctly detects the hand-written examples above:

- `P=(1,11,5,2,1)`, `Q=(1,10202,10203,10101,10000,2000,1)` has
  `V/(B_0+G_+)=10/8003`;
- `P=(1,3,2,1,1)`, `Q=(1,44,45,38,32,21,1)` has `V/(B_0+G_+)=1/6`;
- `P=(1,2,2,1,1)`, `Q=(1,30,24,19,15,11,1)` has `V/(B_0+G_+)=1/2`.

To get useful fresh data, the profiler now has a targeted `(4,6)` sampler for
the observed hard shape: degree-4 factors biased toward `C=1`, and degree-6
factors with one small rise or an all-decreasing head followed by a large tail
drop.  A logged run

```text
PYTHONPATH=notes uv run python notes/profile_boundary_variation.py 4 6 \
  --targeted-degree4-trials 1000000 --first-cap 20000 --seed 999 --top 16
```

found `3540` corrected-variation states among `24952` admissible generated
pairs, with no failures of `V<=B_0+G_+`.  The first-positive distribution was
`{3: 2842, 4: 698}`.  The tail-slope diagnostic failed on `895` of these
states, confirming it is not the right proof invariant; the slope-budget
diagnostic failed on only `3`, but is still not reliable in principle because
of the explicit example above.

Filtering the same targeted sampler to the nonterminal `t=3` branch with

```text
PYTHONPATH=notes uv run python notes/profile_boundary_variation.py 4 6 \
  --targeted-degree4-trials 1000000 --first-cap 20000 --seed 1001 \
  --only-first-positive 3 --top 16
```

found `2811` corrected-variation states, again with no failures.  The largest
sampled nonterminal ratio was

`P=(1,65,23,1,1)`,
`Q=(1,17390,17394,17258,17123,16959,1)`,
`theta=(-164,-135,-136,4,17389)`,
and `V/(B_0+G_+)=16/63`.

This random sampler still misses the true boundary.  There is a simple
nonterminal `t=3` family showing that the corrected variation target is
essentially sharp even away from the terminal case.  For every `b>=2`, put

`P_b=(1,b^2,b,1,1)`,

`M=b^2+b`,

`x=b^4+2b^3-b^2-b+1`,

and

`Q_b=(1,x+3M,x+3M+1,x+2M,x+M,x,1)`.

Then `P_b` and `Q_b` are admissible, the early-plateau state has

`theta=(-M,-M,-M-1,1,x+3M-1)`,

`D_4=1`, `t=3`, and

`V=(b^2-1)`, `B_0+G_+=M+b-1=b^2+2b-1`.

Thus

`V/(B_0+G_+)=(b^2-1)/(b^2+2b-1) -> 1`.

So neither the terminal nor the first nonterminal branch admits a uniform
improvement `V<=c(B_0+G_+)` with `c<1`; the proof has to preserve the exact
unit slack rather than seek a stronger constant-factor statement.

The same notation gives a direct proof of the corrected-variation target in
the first nonterminal case `m=4,t=3`.  Write

`P=(1,a,b,y,1)`,

`theta=(-E,-B,-A,s,r)`,

and assume `d=A-B>0`; otherwise `V=0`.  The target is

`E+(b-y)s >= (a-1)d`.

Let `x=q_5` and `u=q_4=x+E`.  The two tail log-concavity inequalities give

`d<=B^2/u`

and

`Eu>=xB`,

hence `E>=xd/B`.  The positive-next condition is

`D_4=x-1-(a-1)B-(b-1)A+(y-1)s>0`,

so, with `R=d/B` and `S=s/B`, it is enough to prove

`Phi=(b-1)(1+R)+S((b-y)/R-(y-1)) >= 0`.

If the coefficient of `S` is nonnegative, this is immediate.  Otherwise
`y>1` and `R>(b-y)/(y-1)`.  The middle negativity `C<0` gives

`S<(a+b+bR)/y`.

Since the coefficient of `S` is negative, it remains to prove

`(b-1)(1+R)+((a+b+bR)/y)((b-y)/R-(y-1)) >= 0`.

This expression is decreasing in `a`, and log-concavity of `P` gives
`a<=b^2/y`.  The hard condition `a/b>y` then implies `b>y^2`; put
`b=yz` with `z>y`.  At the worst endpoint `a=b^2/y=yz^2`, multiplying by
`R>0` reduces the inequality to

`G(R)=(z-1)R^2+(-yz+z^2+z-1)R+yz(z^2-1) >= 0`.

Let

`R_0=y(z-1)/(y-1)`.

Directly,

`(y-1)^2G(R_0)=y(z-1)(yz-1)^2>=0`,

and

`(y-1)G'(R_0)
 =(z-y)^2(3y-1)+(z-y)(y-1)(5y+1)+(y-1)^2(2y+1)>=0`.

Since `G` is a convex quadratic with leading coefficient `z-1>0`, it is
increasing for `R>=R_0`; the coefficient-negative branch has `R>R_0`, so
`G(R)>=0`.  This proves `V<=B_0+G_+` for the whole `m=4,t=3`
corrected-variation branch.

The same sharpness phenomenon already appears in the next nonterminal branch.
For every `t>=2`, put

`P_t=(1,t,t^2,t,1,1)`,

`M=t^2+2t+2`,

`x=(t^2+2t-3)M+t+1`,

and

`Q_t=(1,x+4M,x+4M+1,x+3M,x+2M,x+M,x,1)`.

Then the canonical profiler gives an early-plateau `m=5,t=4` state with

`theta=(-M,-M,-M,-M-1,1,x+4M-1)`,

`D_5=1`, and

`V=t^2-1`, `B_0+G_+=M+t-1=t^2+3t+1`.

Thus

`V/(B_0+G_+)=(t^2-1)/(t^2+3t+1) -> 1`.

This does not prove the full `m=5,t=4` corrected-variation branch, but it
shows that any proof of that branch must again use the exact inequality rather
than a strengthened constant-factor gap.

The profiler now has a targeted `(5,7)` sampler for this `t=4` branch.  It
generates degree-5 factors with `p_2/p_3>p_4`, constructs degree-7 tails
directly from `theta=(-E,-B,-A,-D,s,r)`, and validates every generated pair
through the canonical `variation_state` filter.  A logged run

```text
PYTHONPATH=notes uv run python notes/profile_boundary_variation.py 5 7 \
  --targeted-degree5-t4-trials 200000 --first-cap 20000 --seed 5004 \
  --only-first-positive 4 --top 16
```

checked `200000` corrected-variation states, all with first-positive index
`4`, and found no failures of `V<=B_0+G_+`.  The tail-slope diagnostic failed
on `18` states, but the slope-budget diagnostic held on all `200000`.

The largest sampled ratios were the sharp family above.  The top state was

`P=(1,80,6400,80,1,1)`,

`Q=(1,43053363,43053364,43046801,43040239,43033677,43027115,1)`,

with

`theta=(-6562,-6562,-6562,-6563,1,43053362)`,

and `V/(B_0+G_+)=6399/6641`.

The slope-budget shortcut is still not structural in this branch.  An
adversarial valid state

`P=(1,8,12,5,2,1)`,

`Q=(1,42090,43823,43545,43268,42956,4612,1)`

has

`theta=(-38344,-312,-277,-278,1733,42089)`.

Here `V/(B_0+G_+)=11/43543`, so the corrected target has huge slack, but

`(B_0/x_0)P_+=16612538/1153 > 5199=G_+`.

Thus the full `t=4` proof cannot simply reuse the terminal `V<=hN` estimate
plus `hP_+<=G_+`; it must use where the negative jumps actually occur.

The profiler also has a `--t4-jump-report` mode, which splits states according
to the two variation jumps

`A>B` and `D>A`

in `theta=(-E,-B,-A,-D,s,r)`.  On the same targeted sampler, with seed `5014`,
the split was:

- no variation jump: `73665` states;
- only `A>B`: `7520` states;
- only `D>A`: `109441` states;
- both jumps: `9374` states.

All `200000` states again satisfied `V<=B_0+G_+`.  The sharp family lives in
the `only D>A` bucket, where the largest ratio was again `6399/6641`.  In
this sampled run every `only A>B` state had `V<=B_0`, but that is not
structural.  The valid adversarial state

`P=(1,946,196,35,5,1)`,

`Q=(1,456394,556394,555755,554937,554120,553303,1)`

has

`theta=(-817,-817,-818,-639,100000,456393)`.

It lies in the `only A>B` bucket and has `V=945>B_0=817`, but
`G_+=3000000`, so the corrected target has slack `2999872`.  Thus each
active-jump bucket must allow positive-block gain; even the apparently easy
`only A>B` bucket is not a pure `B_0` estimate.

The `only A>B` bucket is nevertheless now controlled.  In this bucket

`V=(a-1)(A-B)`,

so write `d=A-B>0`, `R=d/B`, `T=D/B`, `S=s/B`, and let
`x=q_6`, `u=q_5=x+E`.  The same two tail log-concavity inequalities give

`d<=B^2/u`

and

`Eu>=xB`,

hence

`E>=(x/B)d`.

Thus it is enough to prove

`x/B+(c-y)S/R >= a-1`.

The positive-next condition gives

`x/B>(a-1)+(b-1)(1+R)+(c-1)T-(y-1)S`,

so the remaining target is

`Phi=(b-1)(1+R)+(c-1)T+((c-y)/R-(y-1))S >=0`.

If the coefficient of `S` is nonnegative, this is immediate.  Otherwise
`y>1` and

`R>R_0:=(c-y)/(y-1)`.

The middle negativity `ys<aB+bA+cD` gives

`S<(a+b(1+R)+cT)/y`.

Since the coefficient of `S` is negative, the worst case is this upper
endpoint for `S`.  The resulting expression is increasing in `T`, because

`d/dT = (c-y)(1+c/R)/y >=0`,

so it is enough to take `T=0`.  It is also decreasing in `a`; by
log-concavity of `P`, `a<=b^2/c`, so take the worst endpoint `a=b^2/c`.

Now put `b=cz`.  The hard condition gives `z>y`, and `c^2>=by` gives
`c>=yz`.  After multiplying the endpoint expression by `yR`, we get the
quadratic

`G(R)=(cz-y)R^2
 +(c^2z-cyz^2-cyz+cz^2+cz-y)R
 +cz(z+1)(c-y)`.

Its leading coefficient is positive.  At the left endpoint,

`(y-1)^2G(R_0)=y(c-y)(c-1)(cz-1)>=0`.

It remains only to check that the quadratic is already increasing at `R_0`.
Write `c=yz+w` and `z=y+eta`, with `w>=0` and `eta>0`.  A direct expansion
gives

`(y-1)G'(R_0)=z(y+1)w^2+wC_1+C_0`,

where

`C_1=eta^2(y^2+4y-1)+eta(2y^3+7y^2-2y-1)
     +y(y-1)(y+1)(y+3)>=0`

and

`C_0=y((3y-1)eta^3+(8y^2-3y-1)eta^2
       +eta y(y-1)(7y+4)+(y-1)^2(y+1)(2y+1))>=0`.

Thus `G'(R_0)>=0`; by convexity, `G(R)>=0` for all `R>=R_0`.  This proves
`Phi>=0`, and therefore

`(a-1)(A-B)<=E+(c-y)s`

throughout the `only A>B` branch.

The polynomial identities in this endpoint check are verified by
`notes/verify_boundary_variation_t4_only_a.py`.

The `only D>A` bucket is also controlled.  Here `A<=B`, `D>A`, and

`V=(b-1)(D-A)`.

Put `e=D-A>0`, `alpha=A/B`, `delta=e/B`, `X=x/B`, and keep
`x=q_6`, `u=q_5=x+E`.  The log-concavity inequality
`q_3^2>=q_2q_4` is

`(u+B+A)^2 >= (u+B+A+D)(u+B)`,

or

`e(u+B)<=A^2`.

Thus `delta<=alpha^2`, and together with `Eu>=xB` this gives

`E >= (X/alpha^2)e`.

If `y=1`, then the positive-next condition gives

`X>(a-1)+(b-1)alpha+(c-1)(alpha+delta)>=(b-1)alpha`.

Since `alpha<=1`, this already implies `E>=(b-1)e`, proving the bucket.

Now assume `y>1`, and set

`M=(a-1)+(b-1)alpha+(c-1)(alpha+delta)
  =a-1+(b+c-2)alpha+(c-1)delta`.

If `X>=M`, the same argument works because `M>=(b-1)alpha`.  Otherwise
positive-next gives

`S=s/B>(M-X)/(y-1)`.

The target margin is then bounded below by

`delta X/alpha^2+(c-y)(M-X)/(y-1)-(b-1)delta`.

As a function of `X` on `0<=X<=M`, this is linear.  If its slope is negative,
the minimum is at `X=M`, which is the already handled case.  If its slope is
nonnegative, the minimum is at `X=0`.  So it remains to prove

`H(delta):=(c-y)M/(y-1)-(b-1)delta >=0`.

Since `0<=delta<=alpha^2`, and `H` is linear in `delta`, it is enough to
check `delta=0` and `delta=alpha^2`.  The first endpoint is immediate.  At
the second endpoint put

`J(alpha)=(c-y)(a-1+(b+c-2)alpha+(c-1)alpha^2)/(y-1)
          -(b-1)alpha^2`.

The coefficient of `alpha` is nonnegative.  If the quadratic coefficient is
nonnegative, `J` is increasing from `J(0)>=0`; if the quadratic coefficient is
negative, `J` is concave, so its minimum on `[0,1]` is at an endpoint.  Thus
it only remains to check `alpha=1`.  Using `a>=1`,

`(y-1)J(1) >= (c-y)(b+2c-3)-(y-1)(b-1)`

`=b(c-2y+1)+(c-y)(2c-3)+(y-1)`.

Finally, the hard condition `b/c>y` and log-concavity `c^2>=by` imply
`c>y^2`.  Since the coefficients are integral and this branch has `y>1`, we
have `y>=2`; hence `c>y^2>=4`, `c-2y+1>0`, and `2c-3>0`.  Every term above
is therefore nonnegative.  This proves `J(1)>=0`, hence `H(delta)>=0`, and
therefore

`(b-1)(D-A)<=E+(c-y)s`

throughout the `only D>A` branch.

Together with the trivial `no variation jump` branch and the proved
`only A>B` branch, the sole remaining `m=5,t=4` corrected-variation bucket is
`both A>B, D>A`.  A `400000`-trial targeted split by `y` found that the
largest `only D>A` states are the sharp `y=1` family, while the sampled
`y>1` states have noticeably more room.

The final `both A>B, D>A` bucket also has a direct reduction.  Put

`R=(A-B)/B>0`, `H=(D-A)/B>0`, `S=s/B`, `X=x/B`, and `U=u/B`.

The two tail inequalities give

`RU<=1`

and

`H(U+1)<=(1+R)^2`.

Together with `Eu>=xB`, this gives

`E/B >= Lambda X`,

where

`Lambda=max(R, H/((1+R)^2-H))`.

Also `Lambda(1+R)>=H`: if `H<=R(1+R)` this follows from `Lambda>=R`; if
`H>R(1+R)` it follows from the second term in the maximum.

The normalized target is

`E/B+(c-y)S >= (a-1)R+(b-1)H`.

Positive-next gives

`X>K-(y-1)S`,

where

`K=(a-1)+(b-1)(1+R)+(c-1)(1+R+H)`.

Therefore the target follows if

`Lambda K-(a-1)R-(b-1)H + ((c-y)-Lambda(y-1))S >=0`.

If `y=1`, the coefficient of `S` is nonnegative.  If `y>1`, the coefficient
is still nonnegative in every valid state.  To see this, combine
positive-next with `C<0`, namely

`yS<a+b(1+R)+c(1+R+H)=N`.

Then

`X>K-(y-1)N/y=L/y`,

where

`L=(a-y)+(b-y)(1+R)+(c-y)(1+R+H)`.

Since `X<=U`, we have `U>L/y`.  The hard condition and log-concavity give
`b>cy`, `c^2>=by`, hence `c>y^2`; because `y>1` is integral, this implies
`c>=y^2+1`.

First, from `RU<=1` and `U>L/y`,

`R(1+R)<y/(b-y)<1/(c-1)<=1/y^2`,

so `R<1/y<(c-y)/(y-1)`.

Second, since `L>c-y` and `c-y>y(y-1)`, we have

`L/y>(y-1)/(c-y)`.

Using `H(U+1)<=(1+R)^2`, this gives

`H(c-1)/(c-y)<(1+R)^2`,

and hence

`H/((1+R)^2-H)<(c-y)/(y-1)`.

Thus `Lambda<(c-y)/(y-1)` when `y>1`, and so
`(c-y)-Lambda(y-1)>0`.

It remains only to check the zero-`S` part:

`Lambda K-(a-1)R-(b-1)H`

`=(a-1)(Lambda-R)+(b-1)(Lambda(1+R)-H)
  +Lambda(c-1)(1+R+H)>=0`.

This proves the `both A>B, D>A` bucket.  Consequently all four
`m=5,t=4` corrected-variation buckets satisfy

`V<=B_0+G_+`.

A `500000`-trial targeted diagnostic for the both-jump bucket found `23795`
both-jump states, including `159` with `y>1`; none had
`Lambda(y-1)>c-y`, matching the proof above.

The next nonterminal corrected-variation branch, `m=6,t=5`, again has no
constant-factor slack.  For every `t>=2`, put

`P_t=(1,t^2,t^4,t^6,t^3,1,1)`,

`M=t^6+t^4+t^3+t^2`,

`x=(M-4)M+t^3+1`,

and

`Q_t=(1,x+5M,x+5M+1,x+4M,x+3M,x+2M,x+M,x,1)`.

The canonical profiler gives an early-plateau `m=6,t=5` state with

`theta=(-M,-M,-M,-M,-M-1,1,x+5M-1)`,

`D_6=1`, and

`V=t^6-1`, `B_0+G_+=M+t^3-1=t^6+t^4+2t^3+t^2-1`.

Thus

`V/(B_0+G_+)=(t^6-1)/(t^6+t^4+2t^3+t^2-1) -> 1`.

So the newly completed `t=4` proof does not exhaust the sharp phenomenon:
the next branch also requires the exact corrected variation inequality.

The profiler now has a targeted `(6,8)` sampler for this `t=5` branch.  It
injects the sharp family above and otherwise generates degree-6 factors with
`p_3/p_4>p_5`, then constructs degree-8 tails directly from
`theta=(-E,-B,-A,-D,-F,s,r)`.  A logged run

```text
PYTHONPATH=notes uv run python notes/profile_boundary_variation.py 6 8 \
  --targeted-degree6-t5-trials 200000 --first-cap 1000000 --seed 7005 \
  --only-first-positive 5 --top 16
```

checked `199999` corrected-variation states, all with first-positive index
`5`, and found no failures of `V<=B_0+G_+`.  The tail-slope diagnostic failed
on only `1` state, while the slope-budget diagnostic held on every state.
The largest sampled ratio was the sharp-family `t=10` state

`P=(1,100,10000,1000000,1000,1,1)`,

with

`theta=(-1011100,-1011100,-1011100,-1011100,-1011101,1,1022324222100)`,

and `V/(B_0+G_+)=90909/92009`.

The profiler also has a `--t5-jump-report` mode, splitting states by the
three possible jumps

`A>B`, `D>A`, and `F>D`

inside `theta=(-E,-B,-A,-D,-F,s,r)`.  A second `200000`-trial targeted run
with seed `7015` again found no failures.  Its bucket counts were:

- no variation jump: `62192`;
- only `A>B`: `3092`;
- only `D>A`: `2802`;
- only `F>D`: `117246`;
- `A>B` and `D>A`: `3314`;
- `A>B` and `F>D`: `3265`;
- `D>A` and `F>D`: `3143`;
- all three jumps: `4944`.

The sharp family lives in the `F>D` bucket, whose top ratio was again
`90909/92009`.  The largest mixed-jump ratio in this run was `94/121` in the
all-three-jumps bucket.  As in the `t=4` branch, some active-jump buckets fail
the pure `V<=B_0` estimate, so the positive gain `(p_4-p_5)s` will be needed
in any full `t=5` proof.

The sharp subbucket `F>D` with `y=1` is already controlled.  In this subbucket
`A<=B`, `D<=A`, `F>D`, and

`V=(c-1)(F-D)`.

Put `e=F-D>0`, `X=x/B`, and `U=u/B`.  The tail log-concavity inequality
`q_3^2>=q_4q_2` gives

`e q_4<=D^2`.

Since `q_4>=u`, this implies `eu<=D^2`.  Together with `Eu>=xB`,

`E/e >= xB/D^2 = X/(D/B)^2`.

Positive-next, with `y=1`, gives

`X>(a-1)+(b-1)A/B+(c-1)D/B+(d-1)F/B >= (c-1)D/B`.

Since `D<=B`, we get `E/e>c-1`, and hence

`(c-1)(F-D)<E<=E+(d-1)s`.

For `y>1`, the same subbucket is still controlled.  Put

`alpha=A/B`, `beta=D/B`, `delta=e/B`, and

`M=(a-1)+(b-1)alpha+(c-1)beta+(d-1)(beta+delta)`.

Since `q_4>=B`, the inequality `e q_4<=D^2` gives

`0<delta<=beta^2<=beta<=1`.

As above, `E/e>=X/beta^2`.  If `X>=M`, then
`X>=(c-1)beta`, so `E/e>=c-1` and the target follows.  Otherwise
positive-next gives

`S=s/B>(M-X)/(y-1)`.

The normalized target margin is bounded below by

`delta X/beta^2+(d-y)(M-X)/(y-1)-(c-1)delta`.

This is linear in `X`.  If its slope is negative, the minimum occurs at
`X=M`, already handled.  If its slope is nonnegative, the minimum occurs at
`X=0`, so it remains to prove

`(d-y)M/(y-1)>=(c-1)delta`.

Let `C=(d-y)/(y-1)`.  Since

`M>=(c+d-2)beta+(d-1)delta`,

it is enough to prove

`C(c+d-2)beta+(C(d-1)-(c-1))delta>=0`.

If the coefficient of `delta` is nonnegative this is immediate.  Otherwise,
using `delta<=beta^2` and `beta<=1`, it is enough to check

`C(c+2d-3)>=(c-1)`.

After multiplying by `y-1`, this is

`(d-y)(c+2d-3)-(y-1)(c-1)`

`=c(d-2y+1)+(d-y)(2d-3)+(y-1)>=0`.

Indeed, the hard condition `c/d>y` and log-concavity `d^2>=cy` imply
`d>y^2`; since `y>1` is integral, `d-2y+1>0`, and every displayed term is
nonnegative.  Therefore the entire single-jump `F>D` bucket is proved.  The
remaining `t=5` work is now the mixed-jump buckets.

The other two single-jump buckets are also controlled.  First consider
`only A>B`.  Put

`R=(A-B)/B>0`, `T=D/B`, `W=F/B`, `S=s/B`, `X=x/B`, and `U=u/B`.

Here `D<=A` and `F<=D`, so `0<W<=T<=1+R`.  As before, tail log-concavity gives
`RU<=1`, and `Eu>=xB` gives

`E/B>=RX`.

Positive-next gives

`X>K-(y-1)S`,

where

`K=(a-1)+(b-1)(1+R)+(c-1)T+(d-1)W`.

The target follows if

`RK-(a-1)R+((d-y)-R(y-1))S>=0`.

For `y=1` this is immediate.  For `y>1`, combine positive-next with
`C<0`,

`yS<a+b(1+R)+cT+dW`,

to get

`X>L/y`,

where

`L=(a-y)+(b-y)(1+R)+(c-y)T+(d-y)W`.

Since `X<=U` and `RU<=1`, this gives `R<y/L`.  The hard condition
`c/d>y` and log-concavity imply `d>y^2`, `c>y^3`, `b>y^2`, and `a>y`;
hence, integrally, `L>y(y-1)`.  Therefore

`R<1/(y-1)<=(d-y)/(y-1)`,

so `(d-y)-R(y-1)>0`, and the displayed target inequality follows.

Now consider `only D>A`.  Put

`alpha=A/B`, `delta=(D-A)/B`, `T=F/B`, `S=s/B`, and `X=x/B`.

Here `0<alpha<=1`, `0<T<=alpha+delta`, and `F<=D`.  The tail inequality
`(D-A)(u+B)<=A^2` gives `0<delta<=alpha^2<=alpha`, while `Eu>=xB` gives

`E/((D-A))>=X/alpha^2`.

Let

`M=(a-1)+(b-1)alpha+(c-1)(alpha+delta)+(d-1)T`.

If `X>=M`, then `X>=(b-1)alpha`, so `E/(D-A)>=b-1` and the target follows.
Otherwise positive-next gives `S>(M-X)/(y-1)` when `y>1`; for `y=1` the
previous case already applies without the `S` term.  In the branch `y>1`,
the normalized target margin is bounded below by

`delta X/alpha^2+(d-y)(M-X)/(y-1)-(b-1)delta`.

This is linear in `X`.  If its slope is negative, the minimum occurs at
`X=M`, already handled.  If its slope is nonnegative, the minimum occurs at
`X=0`; it is enough to prove

`(d-y)M/(y-1)>=(b-1)delta`.

Since `M>=(b+c-2)alpha+(c-1)delta`, and `delta<=alpha^2<=alpha`, this reduces
to

`(d-y)(b+2c-3)>=(y-1)(b-1)`.

Equivalently,

`b(d-2y+1)+(d-y)(2c-3)+(y-1)>=0`,

which follows again from `d>y^2` and integrality.  This proves the `only D>A`
bucket.

A targeted `200000`-trial split with seed `7035` found that the `y>1` parts
of these two buckets are present but small: `57` states for `only A>B` and
`58` for `only D>A`; their largest sampled ratios were `25/86` and
`323/911`, respectively.

All mixed-jump buckets with `y=1` are controlled by a common effective-slope
argument.  Normalize by `B` and put

`alpha=A/B`, `beta=D/B`, `gamma=F/B`,

and

`r=max(0,alpha-1)`, `h=max(0,beta-alpha)`, `j=max(0,gamma-beta)`.

Thus

`V/B=(a-1)r+(b-1)h+(c-1)j`.

The relevant tail inequalities are

`rU<=1`,

`h(U+1)<=alpha^2`,

and

`j(U+1+alpha)<=beta^2`,

where `U=u/B`; each is used only when the corresponding jump is active.  Set
`Lambda` to be the maximum of the active quantities

`r`,

`h/(alpha^2-h)`,

and

`j/(beta^2-j(1+alpha))`.

Then `E/B>=Lambda X`, where `X=x/B`.  Moreover

`Lambda>=r`, `Lambda alpha>=h`, and `Lambda beta>=j`.

The first inequality is built into the definition.  For the second, either
`h<=r alpha`, in which case `Lambda>=r` suffices, or
`h>r alpha`, in which case `alpha^2-h<alpha` and the `h` term in `Lambda`
suffices.  For the third, either `j<=Lambda beta`, or
`j>Lambda beta`; in the latter case the already proved inequalities give
`Lambda(1+alpha)>=beta-1`, so
`j(1+alpha)>beta(beta-1)` and hence
`beta^2-j(1+alpha)<beta`, making the `j` term in `Lambda` sufficient.

When `y=1`, positive-next has no negative `S` term and gives

`X>K`,

where

`K=(a-1)+(b-1)alpha+(c-1)beta+(d-1)gamma`.

Therefore

`E/B>=Lambda X>Lambda K`

`>=(a-1)r+(b-1)h+(c-1)j=V/B`.

This proves every mixed-jump `t=5` bucket on the `y=1` face.

The same effective-slope argument also controls the `y>1` mixed buckets.  The
only extra point is to prove that the coefficient of `S` is nonnegative, i.e.

`Lambda(y-1)<d-y`.

Combining positive-next with `C<0`,

`yS<a+b alpha+c beta+d gamma`,

gives

`X>L/y`,

where

`L=(a-y)+(b-y)alpha+(c-y)beta+(d-y)gamma`.

The hard condition `c/d>y` and log-concavity imply `d>y^2`; since `y>1` is
integral, `d-y>y(y-1)`.  Also `a>y`, so `L>=a-y>=1`, and therefore

`y/L < (d-y)/(y-1)`.

Since `X<=U`, we have `U>L/y`.  Each active tail inequality now bounds its
corresponding Lambda component by `1/U`:

`r<=1/U`,

`h/(alpha^2-h)<=1/U`,

and

`j/(beta^2-j(1+alpha))<=1/U`.

Hence

`Lambda<y/L<(d-y)/(y-1)`.

Thus the target margin is at least its value at `S=0`, and the termwise
domination already proved above gives

`Lambda K>=V/B`.

This closes all `y>1` mixed-jump buckets.  Combining the no-variation bucket,
the three single-jump buckets, and the mixed-jump argument proves
`V<=B_0+G_+` for the full `m=6,t=5` corrected-variation branch.

A focused `500000`-trial residual diagnostic with seed `7075` found `196`
`y>1` mixed-jump states.  The controlling `Lambda` term varied across all
three active jumps, but the largest observed `Lambda/((d-y)/(y-1))` was only
about `0.0132`, matching the proof that this coefficient branch is safely
positive.

The next near-terminal frontier is `m=7,t=6`.  The profiler now has a
targeted `(7,9)` sampler, a four-jump report for

`theta=(-E,-B,-A,-D,-F,-H,s,r)`,

and a `y>1` Lambda diagnostic for the coefficient inequality

`Lambda(y-1)<e-y`.

The `y=1` part of the effective-slope proof appears degree-independent.  If
`z_i` are the negative tail drops normalized by the first drop and
`h_i=max(0,z_{i+1}-z_i)`, tail log-concavity gives

`h_i(U+z_1+...+z_{i-1})<=z_i^2`.

Thus each active jump contributes the Lambda term

`h_i/(z_i^2-h_i(z_1+...+z_{i-1}))`.

Taking the maximum of these terms gives `E/B>=Lambda X`.  The same induction
used in the `t=5` proof shows `h_i<=Lambda z_i` for every active jump, so the
`y=1` face follows from positive-next exactly as above.

The `y>1` step is the first place where higher degree is not a direct copy:
the old shortcut `L>=1` is no longer automatic from the `P` coefficients
alone.  In the `t=6` notation,

`L=(a-y)+(b-y)alpha+(c-y)beta+(d-y)gamma+(e-y)delta`.

A targeted `100000`-trial run with seed `8016` checked `99948` corrected
variation states, all with first-positive index `6`, and found no failures of
`V<=B_0+G_+`.  All `16` jump buckets occurred.  The plain `V<=B_0` estimate
already failed in the `H>F`, `F>D_H>F`, and all-four-jump buckets, so the
corrected gain is again necessary.

A second `100000`-trial run with seed `8026` focused on the `y>1` Lambda
coefficient.  It found `5913` `y>1` states and `1550` active-jump `y>1`
states.  There were no negative coefficient states and no states with `L<=0`;
in fact all `1550` active states satisfied the same `L` shortcut.  The
piecewise invariant below also had no failures in this run; the smallest
recorded margin was `35921/1335178`.
The largest observed ratio

`Lambda/((e-y)/(y-1))`

was only `9/449`, with the final jump controlling Lambda.

A separate proof-audit found that the coefficient inequality itself is false
in `m=7,t=6`; the random sampler above simply did not hit the obstruction.
The verifier `notes/verify_boundary_variation_t6_obstruction.py` checks an
infinite scaled family.  For every integer `n>=1`, take

`P=(1,3,9,27,81,18,4,1)`,

and

`Q_n=(1,1491410n,5808320n,5784210n,5760100n,5736000n,5712000n,912000n,96000n,1)`.

The `n=1` member gives

`theta=(-816000,-4800000,-24000,-24100,-24110,-24110,4316910,1491409)`,

with `V=1060`, corrected budget `61252740`, and huge slack.  However, after
normalizing by `B=4800000`, the active Lambda maximum is `Lambda=5`, while
`y=4` and `e-y=14`.  Hence

`(e-y)-Lambda(y-1)=-1`.

Also

`L=-193169/480000<0`.

So the exact `t=5` coefficient proof cannot prove the next branch.

The first attempted replacement was to keep the zero-`S` surplus.  Let

`N=a+b alpha+c beta+d gamma+e delta`

and

`K=(a-1)+(b-1)alpha+(c-1)beta+(d-1)gamma+(e-1)delta`.

Positive-next gives `X>K-(y-1)S`; the middle negativity gives `S<N/y`.
This suggested the linear endpoint invariant

`Lambda K - V/B + min(0,(e-y)-Lambda(y-1)) N/y >=0`.

In the negative-coefficient branch this is equivalently

`Lambda L+(e-y)N >= y V/B`.

The obstruction above has negative coefficient and negative `L`, but its
linear endpoint margin remains positive:

`23748757/1920000`.

However, a second explicit state shows that this linear endpoint invariant is
false.  With the same `P`, take

`Q=(1,4243,41208,41006,40804,40602,40401,201,1,1)`.

Then

`theta=(-200,-40200,-201,-202,-202,-202,36965,4242)`,

`Lambda=200`, `(e-y)-Lambda(y-1)=-586`, and

`L=-5389/13400<0`.

The linear endpoint margin is

`-581689/80400`.

The missing point is the floor `E/B>=0`.  The correct lower-bound target is
piecewise:

`Phi(S)=Lambda max(0,K-(y-1)S)+(e-y)S-V/B`,

for `0<=S<N/y`.  If the coefficient is negative and `L<0`, the minimum occurs
at `S=K/(y-1)`, not at `S=N/y`, and the needed inequality is only

`((e-y)/(y-1)) K >= V/B`.

For the linear-surplus obstruction above, this piecewise margin is positive:

`124661/10050`.

For the scaled coefficient-obstruction family, the piecewise margin is also
positive:

`892993/72000`.

The `L<0` branch of the piecewise statement is in fact directly controlled.
Let

`C=(e-y)/(y-1)`.

The hard condition `d/e>y` and log-concavity `e^2>=dy` give `e>y^2`, hence
`C>y>y-1`.  Also `d>y^3`, `c^2>=d`, and the first two log-concavity
inequalities imply `b^3>=c^2`; therefore

`b,c,d,e>y`.

If `L<0`, then necessarily `a<y`, and since all the other coefficients
`b-y,c-y,d-y,e-y` are positive integers,

`alpha+beta+gamma+delta<y-a<=y-1<C`.

Thus every normalized negative drop `1,alpha,beta,gamma,delta` is below `C`.
For any active jump `h_i=max(0,z_{i+1}-z_i)`, tail log-concavity gives

`h_i(U+z_0+...+z_{i-1})<=z_i^2`

for `i>=1`, while the `i=0` jump is bounded by `alpha<C`.  Hence in every
case

`h_i<=C z_i`.

Therefore

`V/B<=(a-1)C+(b-1)C alpha+(c-1)C beta+(d-1)C gamma<=C K`,

which is precisely the piecewise target in the `L<0` branch.  The remaining
`m=7,t=6` proof target is the negative-coefficient branch with `L>=0`; there
the minimum is still the linear endpoint

`Lambda K - V/B + ((e-y)-Lambda(y-1))N/y>=0`.

Added `notes/probe_boundary_variation_t6_surplus.py` to stress this
piecewise target in a relaxed negative-coefficient model.  The probe keeps
`P` admissible and hard, then directly generates normalized tail-drop shapes
with

`Lambda>(e-y)/(y-1)`

across all four possible Lambda controllers.  A `300000`-trial run with seed
`8056` produced `272718` negative-coefficient states and no failures of the
piecewise invariant.  The controller counts were

`[72977, 61101, 65714, 72926]`.

The smallest recorded piecewise margin was

`521233122676742397/19736522298667375`,

in controller `1`.  This is not a proof, but it suggests the piecewise
invariant may be robust even beyond the exact realizable `Q` tails.

The same relaxed run also tracked the simpler margin

`(e-y)N-yV/B`.

It found no failures; the smallest recorded value was

`2365994727235746/157892178389339`.

This suggests a cleaner way to finish the remaining `L>=0` branch: since
`Lambda L>=0`, it would be enough to prove the `N`-only sublemma

`(e-y)N>=yV/B`

in the actual small-`L` regime of the negative-coefficient branch.

That small-`L` regime follows from the same positive-next information used in
the lower-degree proofs.  If `L>0`, positive-next together with `C<0` gives
`X>L/y`; since `X<=U`, this implies `U>L/y`.  Every active Lambda component is
at most `1/U`.  Therefore

`Lambda<y/L`.

In the negative-coefficient branch `Lambda>(e-y)/(y-1)`, so

`0<=L<Y:=y(y-1)/(e-y)`.

The hard condition and log-concavity give `e>y^2`, hence `Y<1`.
Since

`L=(a-y)+(b-y)alpha+(c-y)beta+(d-y)gamma+(e-y)delta`,

and `b,c,d,e>y`, integrality forces `a<=y`; also `a>=2`, because
`b>y` and `b<=a^2`.  Put

`T=(b-y)alpha+(c-y)beta+(d-y)gamma+(e-y)delta`.

Then

`T=L+y-a<y-a+Y`.

In particular the three pre-final positive tail variables are small:

`alpha<y/(b-y)`, `beta<y/(c-y)`, and `gamma<y/(d-y)`.

Let `g=e-y` and

`M=gN-yV/B`.

The normalized tail log-concavity constraints give `h_i<=z_i^2` for
`i=1,2,3`, because the previous normalized tail sum contains `z_0=1`.  Also
`h_0=(alpha-1)_+<y`.  Decompose

`M=[ga-y(a-1)h_0]+[gb alpha-y(b-1)h_1]`

`+[gc beta-y(c-1)h_2]+[gd gamma-y(d-1)h_3]+ge delta`.

The first bracket is positive: since `a<=y`,

`y(a-1)h_0<y^2(a-1)<=y(y-1)a<ga`.

For the other three brackets use the following elementary coefficient lemma.
For every integer `x>y`,

`g x(x-y) >= y^2(x-1)`.

It is enough to take `g_0=y(y-1)+1<=g`.  Writing `x=y+r` with `r>=1`,

`g_0(y+r)r-y^2(y+r-1)`

`=1+(r-1)(g_0(r+1)+y(y-1)^2)>=0`.

Thus, for instance,

`y(b-1)h_1<=y(b-1)alpha^2`

`< y^2(b-1)alpha/(b-y)<=gb alpha`.

The same argument with `(x,z)=(c,beta)` and `(x,z)=(d,gamma)` controls the
`h_2` and `h_3` brackets.  Hence `M>0` throughout the remaining
`L>=0` negative-coefficient branch, i.e.

`(e-y)N>=yV/B`.
Hence

`Lambda L+(e-y)N>=yV/B`,

which closes the `m=7,t=6` corrected-variation branch.

Added `notes/probe_boundary_variation_t6_small_l.py` to stress the small-`L`
regime directly.  A `300000`-trial run with seed `8066` produced `435`
negative-coefficient candidates satisfying `0<=L` and `Lambda L<y`, with no
failures of the linear endpoint, threshold endpoint, or `N`-only margin.  The
tightest state had

`P=(1,2,4,8,12,5,2,1)`,

controller `3`, threshold `3`, and `L=397/15000`.

A longer `3000000`-trial run with seed `8067` produced `4088` such candidates
and again found no failures.  Its smallest threshold margin occurred at
`P=(1,2,4,7,11,5,2,1)`, while the smallest linear and `N`-only margins
occurred at `P=(1,2,4,8,12,5,2,1)`.

A separate broad feasibility-proxy check over random normalized drop shapes,
not requiring the small-`L` condition, had found no failures earlier; the
small-`L` proof above is the actual branch-closing argument.

With the `m=7,t=6` branch closed, the profiler was extended to the next
near-terminal frontier `m=8,t=7`.  The new targeted `(8,10)` sampler writes

`theta=(-E,-B,-A,-D,-F,-H,-J,s,r)`,

and the Lambda diagnostic was generalized from five normalized negative drops
to an arbitrary near-terminal negative block.  A `10000`-trial run with seed
`9017` checked `9870` first-positive-`7` states and found no failures of
`V<=B_0+G_+`.  All `32` jump buckets were represented.  On the `y>1` face it
found `408` states, `164` active-jump states, no negative-coefficient states,
and no piecewise-invariant failures; every active `y>1` state satisfied the
same `L` shortcut.  The largest observed

`Lambda/((f-y)/(y-1))`

was `11/1018`, with the final jump controlling Lambda.

The same piecewise proof also closes this `m=8,t=7` branch.  Write

`P=(1,a,b,c,d,e,f,y,1)`

and

`z=(1,alpha,beta,gamma,delta,epsilon)`.

The hard condition is `e/f>y`.  Together with `f^2>=ey`, it gives
`f>y^2` and `e>y^3`.  Log-concavity between the coefficients `p_0=1` and
`p_5=e` gives

`b^5>=e^2`, `c^5>=e^3`, and `d^5>=e^4`,

so `b,c,d,e,f>y`.

The `y=1` face and the positive-coefficient `y>1` branch are controlled by
the same effective-slope argument as before.  In the negative-coefficient
branch, put

`C=(f-y)/(y-1)`.

For `L<0`, the preceding `m=7,t=6` piecewise argument is unchanged: since all
tail coefficients after `a` exceed `y`, one gets `a<y` and every normalized
negative drop is below `C`; tail log-concavity then gives `h_i<=Cz_i`, hence
`V/B<=CK`.

For `L>=0`, the small-`L` proof is also unchanged with `g=f-y`.  The negative
coefficient and positive-next give

`0<=L<y(y-1)/(f-y)<1`.

Thus `a<=y`, and

`(b-y)alpha+(c-y)beta+(d-y)gamma+(e-y)delta+(f-y)epsilon<y`.

The coefficient lemma

`g x(x-y)>=y^2(x-1)` for every integer `x>y`

then controls the brackets for `x=b,c,d,e`, while the `a` bracket is absorbed
by `ga` exactly as in the `m=7,t=6` proof.  Therefore

`(f-y)N>=yV/B`,

and so the linear endpoint inequality follows.  This closes the full
`m=8,t=7` corrected-variation branch.

The same argument extends one more near-terminal step.  For `m=9,t=8`, write

`P=(1,a,b,c,d,e,f,g,y,1)`.

The hard condition is `f/g>y`, and `g^2>=fy` gives `g>y^2` and `f>y^3`.
Log-concavity between `p_0=1` and `p_6=f` gives

`b^6>=f^2`, `c^6>=f^3`, `d^6>=f^4`, and `e^6>=f^5`,

so again all coefficients `b,c,d,e,f,g` exceed `y`.  The `L<0` and
`L>=0` piecewise arguments above apply verbatim with `g-y` replacing `f-y`.
Thus the full `m=9,t=8` corrected-variation branch is also closed by the same
near-terminal certificate.

This coefficient argument is genuinely limited.  At `m=10,t=9`, the hard
condition is compatible with `b<=y`; for example

`P=(1,8,64,512,4096,32768,262144,2097152,15000,100,1)`

is admissible, satisfies `2097152/15000>100`, but has `b=64<=100=y`.
So the current small-`L` bracket proof should not be pushed past `m=9`
without a new idea.

Added `notes/probe_boundary_variation_t9_barrier.py` to stress this precise
barrier.  It generates admissible `m=10,t=9` hard factors with `b<=y`, then
directly samples normalized tail-drop shapes in the negative-coefficient
small-`L` branch.  A first `300000`-trial run with seed `9099` found only `5`
retained candidates but no failures.  After biasing the sampler toward the
large first jump that makes the negative coefficient possible, a second
`300000`-trial run with seed `9100` found `1216` retained candidates and again
no failures of the linear endpoint, threshold endpoint, or `N`-only margin.
The smallest margins all occurred at

`P=(1,3,9,27,81,243,729,2187,163,11,1)`,

with `b<y` and first-jump Lambda controller `0`.

This suggests the `m=10,t=9` obstruction is not a counterexample to the
endpoint inequality.  Under `b<=y`, log-concavity and the hard condition still
force

`a<b<c<d<e<f<g`

and `c,d,e,f,g,h>y`.  Indeed, write the adjacent coefficient ratios as
`r_i=p_i/p_{i-1}`.  Since `a^2>=b`, `r_2=b/a<=sqrt(b)<=sqrt(y)`, and
log-concavity makes the ratios nonincreasing.  Thus

`r_3r_4r_5r_6<=y^2`.

But

`r_3r_4r_5r_6r_7=g/b>=g/y>y^2`,

because the hard condition and `h^2>=gy` give `g>hy>y^3`.  Hence
`r_7>1`, and therefore all earlier ratios through `r_7` are also `>1`.

This controls the `L>=0` part of the barrier.  Put `G=h-y` and

`z=(1,alpha,beta,gamma,delta,epsilon,zeta,eta)`.

The negative coefficient and positive-next again give

`0<=L<Y:=y(y-1)/(h-y)<1`.

If `b>y`, the previous small-`L` proof applies directly, so assume `b<=y`.
For the first six jumps use only `h_i<=z_{i+1}`.  The coefficient-reserve
inequalities

`G p_{i+2}-y(p_{i+1}-1)`, for `0<=i<=5`,

are positive.  For `i<=4` this follows immediately from
`p_{i+2}>p_{i+1}` and `G>y(y-1)`.  For `i=5`, the ratio proof above gives

`f/g=1/r_7<y^3/g`,

so

`yf<y^4< Gg`.

Thus the first six jumps can be discarded with nonnegative reserve, leaving
only the final jump

`j=max(0,eta-zeta)`.

Let `S=1+alpha+beta+gamma+delta+epsilon`.  If `j>0`, tail log-concavity gives

`jS<=zeta^2`.

The small-`L` inequality and `b<=y` give

`(g-y)zeta <= L+y-a+(y-b)alpha <= y(1+alpha) <= yS`,

so

`j<=zeta^2/S <= y zeta/(g-y)`.

The remaining final-jump contribution is at least

`Gg zeta+Gh eta-y(g-1)j`

`>= G(g+h)zeta-y(g-1)j`

`>= zeta( G(g+h)-y^2(g-1)/(g-y) )`.

This is positive because `G>y(y-1)` and `g>hy>y^3`; indeed it is enough to
check

`(y-1)g(g-y)>y(g-1)`,

which is immediate for integers `y>=2` and `g>y^3`.  Hence

`(h-y)N>=yV/B`

throughout the `L>=0`, `b<=y` barrier.  This closes the linear-endpoint half
of the `m=10,t=9` negative-coefficient branch.

The `L<0` piecewise endpoint with `b<=y` is similar and slightly easier.
Here the target is

`CK>=V/B`, where `C=(h-y)/(y-1)`.

Use `h_i<=z_{i+1}` for the first six jumps.  Since `C>y>1` and
`p_{i+2}>p_{i+1}` for `0<=i<=5`, these jumps have nonnegative reserve in
`CK-V/B`.  For the final jump, again put `j=max(0,eta-zeta)` and
`S=1+alpha+beta+gamma+delta+epsilon`.  If `j>0`, tail log-concavity gives
`jS<=zeta^2`.  The condition `L<0` gives the same bound

`(g-y)zeta < y-a+(y-b)alpha <= y(1+alpha) <= yS`,

so `j<=y zeta/(g-y)`.  The remaining final contribution is

`C(g-1)zeta+C(h-1)eta-(g-1)j`

`>= C(g+h-2)zeta-(g-1)j`

`>= zeta(C(g+h-2)-y(g-1)/(g-y))`.

This is positive because `C>y` and `(g+h-2)(g-y)>g-1`.  Therefore
`CK>=V/B` in the `L<0`, `b<=y` barrier as well.

Combining the already proved `b>y` case, the `L>=0` barrier proof, and this
`L<0` piecewise endpoint closes the full `m=10,t=9` corrected-variation
branch.

A small standalone verifier in `notes/verify_boundary_variation_t9_barrier.py`
checks the ratio, reserve, and final scalar inequalities on the explicit
barrier pattern and random generated barrier factors.

First `m=11,t=10` diagnostic.  The profiler now has a generic
near-terminal sampler for degree pair `(m,m+2)`, targeting the same hard-tail
configuration `p_{m-3}>p_{m-2}y` and mostly flat negative drops before the
terminal rise.  A 50,000-trial run for `(11,13)` produced 7,473
`t=10` early-plateau states and no `V>B0+G+` failures.  The largest sampled
ratio was `825/1376<0.6`.  Among the `y>1` states, the generic Lambda
diagnostic found 139 candidates, 89 with active jumps, no negative
coefficient cases, and no piecewise invariant failures; all active cases used
the last pre-terminal jump as controller.

For the next `b<=y` barrier analysis, write

`P=(1,a,b,c,d,e,f,g,h,i,y,1)`.

The hard tail gives `i>y^2` and `h>y^3`.  If both `b<=y` and `c<=y`, then
with adjacent ratios `r_j=p_j/p_{j-1}` we have

`r_3=c/b<=r_2=b/a<=sqrt(b)` and also `r_3<=y/b`.

Hence `r_3<=min(sqrt(b),y/b)<=y^{1/3}`.  Since the ratios are nonincreasing,

`h/c=r_4 r_5 r_6 r_7 r_8<=y^{5/3}`,

so `h<=y^{8/3}<y^3`, a contradiction.  Thus the difficult `b<=y` branch still
has `c,d,e,f,g,h,i>y`.  Also `a<y`: otherwise `a>=y` would give
`ac>y^2>=b^2`, contradicting log-concavity.  The new issue is that the
reserve argument has two near-tail jumps to manage instead of one.

The relaxed `t=10` barrier probe in
`notes/probe_boundary_variation_t10_barrier.py` stress-tests this small-`L`
branch.  An unforced 50,000-trial run produced 46 negative-coefficient
small-`L` candidates, all controller `0`, with no linear, threshold, or
`N`-only margin failures.  A forced final-controller run produced 4
controller-`7` candidates, again with no failures.  The forced-controller
probe found no controller-`6` candidates in a 20,000-trial sample, suggesting
the penultimate jump may be inaccessible in the actual small-`L` branch.

The `L>=0` endpoint of this `b<=y` barrier can be closed.  Put `G=i-y`.
The hard tail gives `i>y^2`, so `G>y(y-1)`.
As in the previous barrier, the negative coefficient and positive-next
conditions give the small-`L` bracket

`0<=L<y(y-1)/(i-y)<1`.

First note that `c<d<e<f<g`.  We have `r_3<=sqrt(y)` and `c<=y^{3/2}`.
If `d<=c`, then all later ratios are at most `1`, forcing `h<=d<=c<y^3`,
contrary to the hard tail.  If `e<=d`, then `h<=e<=d<=y^2`; if `f<=e`,
then `h<=f<=e<=y^{5/2}`; and if `g<=f`, then `h<=g<=f<=y^3`.  Each is
impossible because `h>y^3`.

For the first six jumps this gives nonnegative reserve in
`GN-yV/B`: the `i=0` reserve follows from `a<y`, `b>=1`, and
`G>y(y-1)`, while the reserves through the jump before `g` follow from
`c<d<e<f<g` and `G>y`.

The branch has `y>=3`: if `y=2`, then `b<=2`, `a^2>=b`, and `b^2>=ac`
force `c<=2`, contradicting `c>y`.  The penultimate reserve is also
automatic.  Since

`g/h=1/r_8<=c r_3^4/h<=y^{7/2}/h<sqrt(y)`,

and `sqrt(y)<=y-1<i/y-1=G/y` for `y>=3`, we get

`G h>y g>y(g-1)`.

Thus all jumps except the last one are covered by the next coefficient.  For
the final jump `j=max(0,theta-eta)`, there is nothing left to prove if
`j=0`.  If `j>0`, then `theta=eta+j`, and tail log-concavity gives

`jS<=eta^2`, where `S=1+alpha+beta+gamma+delta+epsilon+zeta`.

Small `L` gives

`(h-y)eta<=L+y-a+(y-b)alpha<=y(1+alpha)<=yS`,

so `j<=y eta/(h-y)`.  The remaining final contribution in `GN-yV/B` is at
least

`eta(G(h+i)-y^2(h-1)/(h-y))`,

which is positive because `G>y(y-1)` and `h>y^3`.  Hence

`(i-y)N>=yV/B`

throughout the `L>=0`, `b<=y` barrier for `m=11,t=10`.

The `L<0` endpoint closes similarly.  Put `C=(i-y)/(y-1)`.  For the first
seven jumps, use `h_j<=z_{j+1}`.  The first reserve

`C(b-1)>=a-1`

holds because `b>=2`, `a<y`, and `C>y`.  The reserves through the jump before
`g` follow from `c<d<e<f<g` and `C>y`.  For the penultimate reserve, the ratio
bound above gives `g/h<sqrt(y)`, while `h>y^3` and `y>=3` imply

`g/(h-1)<y<C`,

so `C(h-1)>g-1`.

For the final jump, again there is nothing left to prove if `j=0`.  If
`j>0`, then `theta=eta+j`, and the same tail estimate from `L<0` gives

`j<=y eta/(h-y)`.

The remaining contribution in `CK-V/B` is at least

`eta(C(h+i-2)-y(h-1)/(h-y))`,

which is positive because `C>y` and `(h+i-2)(h-y)>h-1`.  Therefore
`CK>=V/B` in the `L<0`, `b<=y` endpoint as well.

Combining the already covered `b>y` branch, the `L>=0` barrier endpoint, and
this `L<0` endpoint closes the full `m=11,t=10` corrected-variation
near-terminal branch.

A standalone verifier in `notes/verify_boundary_variation_t10_barrier.py`
checks the ratio monotonicity, the `c>y` split, all linear and piecewise
reserve inequalities, and the final scalar inequalities on the explicit
barrier pattern and random generated barrier factors.

Next frontier diagnostic: `m=12,t=11`.  A 20,000-trial generic
near-terminal run for `(12,14)` produced 947 first-positive-`11` states and
no `V>B0+G+` failures.  The largest sampled ratio was `104/203`.  On the
`y>1` face it found 13 states, 11 active-jump states, no negative coefficient
states, and no piecewise-invariant failures; the active Lambda controller was
always the last pre-terminal jump.

The `m=11,t=10` barrier proof does not extend verbatim.  For

`P=(1,2,4,8,16,32,64,128,256,69,17,4,1)`,

the hard tail `69>17*4`, log-concavity, and `b<=y` all hold.  But if
`G=17-4`, the copied penultimate next-coefficient reserve would be

`G*69-4*(256-1)=-123<0`.

So the next branch needs either a sharper combined tail reserve or a new split;
the single-reserve argument from `t=10` is no longer enough.

Added `notes/probe_boundary_variation_t11_barrier.py` to stress this new
barrier.  The probe includes the explicit reserve-obstruction family

`(1,r,r^2,r^3,r^4,r^5,r^6,r^7,r^8,(r^4+1)r^2+1,r^4+1,r^2,1)`.

A 50,000-trial unforced run with seed `11100` produced 8 small-`L`
negative-coefficient candidates, all with controller `0`, and no linear,
threshold, or `N`-only failures.  Forced-controller runs on the failed local
reserve (`controller=7`, seed `11107`) and final jump (`controller=8`, seed
`11108`) produced 1 and 10 candidates respectively, again with no failures.
The smallest margins in all three runs occurred on the `r=2` obstruction
factor above.

The same probe now also tracks the candidate combined penultimate reserve after
paying the preceding jump from the `h z_7` term:

`(j-y)(h z_7+i z_8)-y(g-1)z_7-y(h-1)max(0,z_8-z_7)`.

A 20,000-trial forced-final-controller run with seed `11201` produced 2
small-`L` candidates and no failures of this combined reserve; a
forced-controller-`7` run with seed `11200` found no candidates.  This points
to the next proof step: replace the failed single next-coefficient reserve by
a two-term tail reserve using the small-`L` bound and tail log-concavity.
After correcting the accounting to subtract the preceding jump, 20,000-trial
runs with seeds `11300` and `11301` found 3 forced-controller-`7` candidates
and 4 forced-final-controller candidates respectively, again with no combined
reserve failures.

The algebraic replacement is simple.  Put

`G=j-y`, `u=max(0,theta-eta)`, and
`S=1+alpha+beta+gamma+delta+epsilon+zeta`.

If `u=0`, the penultimate jump contributes no variation.  If `u>0`, tail
log-concavity gives `uS<=eta^2`.  The small-`L` bracket gives

`(h-y)eta<=L+y-a+(y-b)alpha<=y(1+alpha)<=yS`,

and hence

`u<=y eta/(h-y)`.

After the ordinary reserve before this jump has been paid, the remaining
penultimate contribution is

`(G h-y(g-1))eta+G i theta-y(h-1)u`.

Therefore it is at least

`eta(G(h+i)-y(g-1)-y^2(h-1)/(h-y))`.

Thus the failed single reserve is replaced by the scalar inequality

`(G(h+i)-y(g-1))(h-y)>y^2(h-1)`.

The final jump can be treated the same way with
`v=max(0,kappa-theta)` and `(i-y)theta<=y(1+alpha)`, reducing it to

`G j(i-y)>y^2(i-1)`.

The verifier `notes/verify_boundary_variation_t11_barrier.py` checks this
corrected scalar inequality, the final scalar inequality, the corresponding
`L<0` piecewise scalar
inequalities, and the earlier reserve inequalities on the obstruction family
for bases `2..19` and on random generated hard-tail factors.  A 20,000-trial
run with seed `11120` found no failures.

This gives a proof of the remaining `m=12,t=11` barrier.  Write the adjacent
ratios as

`r_k=p_k/p_{k-1}` for `1<=k<=11`, and put `Y=log y`, `x_k=log r_k`.

The hard tail is `r_10 y<1`; hence `x_10+Y<0`.  Since `j>y^2`, the branch has
`y>=3`.  As before, `b<=y` and `c<=y` would give

`i/c=r_4 r_5 r_6 r_7 r_8 r_9<=r_3^6<=y^2`,

so `i<=y^3`, contradicting `i>jy>y^3`.  Thus `c>y`, and log-concavity gives
`a<y`.

The coefficients `c,d,e,f,g` are increasing.  If one of the adjacent
inequalities fails before `g`, all later ratios are at most `1`; using
`r_3<=sqrt(y)` gives respectively `i<=y^{3/2}`, `i<=y^2`, `i<=y^{5/2}`, or
`i<=y^3`, each contradicting `i>y^3`.

It remains to justify the reserve before `h`.  From `b<=y`,

`x_1+x_2<=Y`.

Hence each of `x_3,...,x_7` is at most `Y/2`.  Also `x_10<-Y` and
`x_11<=x_10<-Y`, while `x_9<=x_8`.  Therefore

`x_1+...+x_8=Y-(x_9+x_10+x_11)>3Y-x_8`.

Subtracting `x_1+x_2<=Y` gives

`x_3+...+x_8>2Y-x_8`.

But the first five terms on the left are at most `Y/2`, so

`2Y-x_8<5Y/2+x_8`,

and consequently

`x_8>-Y/4`, i.e. `h/g>y^{-1/4}`.

Since `G=j-y` satisfies `G/y>y-1`, this gives

`G h/(y g)>(y-1)y^{-1/4}>1`

for every integer `y>=3`.  Thus `G h>y(g-1)`, closing the last ordinary
next-coefficient reserve.

Also `h>y^2`: otherwise `r_9=i/h>y`, contradicting
`r_9<=r_3<=sqrt(y)`.  The combined penultimate reserve and the final reserve
are exactly the scalar inequalities displayed above.  They are positive
because `G h>y(g-1)`, `G>y(y-1)`, `h>y^2`, and `i>y^3`: after discarding the
positive `G h-y(g-1)` surplus, it is enough to check
`G i(h-y)>y^2(h-1)`, which follows from these three inequalities.  The same
argument with
`C=(j-y)/(y-1)>y` gives the `L<0` piecewise endpoint: the ordinary reserves
use `C>y`, the penultimate combined reserve reduces to

`(C(h+i-2)-(g-1))(h-y)>y(h-1)`,

and the final reserve reduces to

`C(j-1)(i-y)>y(i-1)`.

Therefore the `b<=y` barrier is closed for `m=12,t=11`; together with the
already covered `b>y` branch, this closes the full `m=12,t=11`
near-terminal corrected-variation branch.

Next frontier diagnostic: `m=13,t=12`.  A 15,000-trial generic
near-terminal run for `(13,15)` produced 229 first-positive-`12` states and
no `V>B0+G+` failures.  The largest sampled ratio was `251/617`.  On the
`y>1` face it found only 2 active-jump states, no negative coefficient states,
and no piecewise-invariant failures; both active states were controlled by the
last pre-terminal jump.  This suggests the combined-tail reserve pattern may
continue, but the next step is to formulate it once in general rather than
repeat another degree-specific barrier proof.

Added a first `m=13,t=12` barrier probe in
`notes/probe_boundary_variation_t12_barrier.py`.  The hard tail is now

`P=(1,a,b,c,d,e,f,g,h,i,j,k,y,1)`, `j>ky`, `G=k-y`.

The shifted obstruction family

`(1,r,r^2,r^3,r^4,r^5,r^6,r^7,r^8,r^8,(r^4+1)r^2+1,r^4+1,r^2,1)`

shows that the failed local reserve from `t=11` persists one slot later:
for `r=2`, `G j-y(i-1)=13*69-4*255<0`.  The corrected two-term reserve for
the penultimate jump is therefore

`G(i z_8+j z_9)-y(h-1)z_8-y(i-1)max(0,z_9-z_8)`.

A separate low-`c` family

`(1,r,r^2,r^3,r^4,r^5,r^6,r^7,r^8,r^9,r^10,r^7-1,r^3,1)`

has `b<=y` and `c=y`, so the `t=11` shortcut proving `c>y` cannot simply be
reused.  This branch must either be split off or handled by a ratio argument
that proves the needed reserves directly.

The direct ratio argument appears to be the right replacement.  First `y=2`
is impossible in the hard-tail `b<=y` branch: if `b<=2`, then
log-concavity at `a,b` forces the ratios through `c` to be at most `1`, so
the tail cannot later satisfy `j>2k`.

For `y>=3`, write the adjacent log-ratios as
`x_r=log(p_r/p_{r-1})` and `Y=log y`.  The hard tail gives
`x_11<-Y`; log-concavity at `k` and `j>ky` give `k>y^2`, hence
`x_12<-Y`.  Since `p_12=y`,

`x_1+...+x_10>3Y`.

The branch assumption `b<=y` gives `x_1+x_2<=Y`, and therefore
`x_3+...+x_10>2Y`.  Also `x_2<=Y/2`, so
`x_3,...,x_8<=Y/2`, while `x_10<=x_9`.  If `x_9<=-Y/2`, then the last
display would be at most `6Y/2+2(-Y/2)=2Y`, a contradiction.  Thus
`x_9>-Y/2`, so every early consecutive drop through `h/i` is smaller than
`sqrt(y)`.  Because `sqrt(y)<y-1<G/y`, all ordinary reserves through the
jump before `i` follow, including the low-`c` family.

The first stress run is encouraging.  An unforced 50,000-trial run with seed
`12100` found one negative-coefficient small-`L` candidate, on the shifted
`r=4` obstruction family with controller `0`.  A forced controller-`8`
80,000-trial run with seed `12118` found no candidates; a forced
controller-`9` 80,000-trial run with seed `12119` found two candidates, both
on the shifted `r=2` obstruction family.  None of these runs had linear,
threshold, `N`-only, combined-penultimate, or final reserve failures.  The
scalar verifier
`notes/verify_boundary_variation_t12_barrier.py` checks the obstruction
family, the low-`c` family, and 20,000 random generated hard-tail factors; it
found no failures with seed `12120`.

The two tail jumps now reduce exactly as in the previous branch.  For the
penultimate jump put `u=max(0,z_9-z_8)`.  Tail log-concavity gives
`uS<=z_8^2`, and the small-`L` bracket gives `(i-y)z_8<=yS`, hence
`u<=y z_8/(i-y)`.  After the ordinary jump before it has been paid, the
remaining contribution is at least

`z_8(G(i+j)-y(h-1)-y^2(i-1)/(i-y))`,

so the needed scalar is

`(G(i+j)-y(h-1))(i-y)>y^2(i-1)`.

This is positive because the ratio lemma gives `G i>y(h-1)`, while
`G j(i-y)>y^2(i-1)` follows from `G>y(y-1)`, `j>y^3`, and
`i^2>=j>y^3`.

For the final jump, the same argument with `v=max(0,z_10-z_9)` gives
`v<=y z_9/(j-y)` and reduces the reserve to

`G k(j-y)>y^2(j-1)`,

which follows from `G>y(y-1)`, `k>y^2`, and `j>y^3`.

The `L<0` endpoint has the cross-multiplied scalar checks

`(G(i+j-2)-(y-1)(h-1))(i-y)>y(y-1)(i-1)`

and

`G(k-1)(j-y)>y(y-1)(j-1)`.

The same inequalities are easier here: the ratio lemma gives
`G(i-1)>(y-1)(h-1)`, and the remaining final factors are smaller by one
power of `y`.  Thus the `b<=y` barrier for `m=13,t=12` is reduced to the
verified scalar inequalities above.

Next frontier diagnostic: `m=14,t=13`.  A 15,000-trial generic
near-terminal run for `(14,16)` with seed `13014` produced 91
first-positive-`13` states and no `V>B0+G+` failures; the largest sampled
ratio was `470/1299`.  A larger 50,000-trial run with seed `13015` produced
285 first-positive-`13` states and again no failures; the largest sampled
ratio rose to `425/754`.  Neither run found any `y>1` Lambda states.  Generic
sampling is therefore not reaching the hard barrier branch at this degree; the
next useful experiment is a dedicated `t=13` barrier sampler rather than more
untargeted near-terminal sampling.

Added the dedicated `m=14,t=13` barrier probe in
`notes/probe_boundary_variation_t13_barrier.py` and the matching scalar
verifier in `notes/verify_boundary_variation_t13_barrier.py`.  Write

`P=(1,a,b,c,d,e,f,g,h,i,j,k,l,y,1)`, `k>ly`, `G=l-y`.

The same shifted obstruction remains present:

`(1,r,r^2,r^3,r^4,r^5,r^6,r^7,r^8,r^8,r^8,(r^4+1)r^2+1,r^4+1,r^2,1)`.

For `r=2`, the local penultimate reserve is again negative:

`G k-y(j-1)=13*69-4*255<0`.

The corrected combined reserve is therefore

`G(j z_9+k z_10)-y(i-1)z_9-y(j-1)max(0,z_10-z_9)`.

The verifier checks this combined scalar, the final scalar, the corresponding
`L<0` piecewise scalars, and the ordinary reserve surrogate on the shifted
obstruction family, a shifted low-`c` family, and 20,000 generated hard-tail
factors.  It found no failures with seed `13120`.

The first small-`L` stress runs found the branch even thinner than at `t=12`.
An unforced 50,000-trial run with seed `13100` found no candidates, and
80,000-trial forced controller-`9` and controller-`10` random-family runs
with seeds `13119` and `13120` also found none.  A fixed-family obstruction
run at `r=2`, controller `9`, seed `13409`, and 100,000 trials found two
candidates, both with no linear, threshold, `N`-only, combined-penultimate, or
final reserve failures.  A fixed-family obstruction controller-`10` run with
seed `13210` found no candidates.

The ordinary-reserve ratio proof shifts with a slightly weaker exponent.
The cases `y=2` and `y=3` are impossible in the hard-tail `b<=y` branch.  For
`y=2`, log-concavity forces the early ratios to be at most `1`.  For `y=3`,
the only growing start is `(1,2,3,4,...)`; then integer log-concavity gives
successively `p_4<=5`, `p_5<=6`, and by induction `p_{11}<=12`, contradicting
`k>ly>27`.

For `y>=4`, write adjacent log-ratios as before.  The hard tail gives
`x_12<-Y`, while `l>y^2` gives `x_13<-Y`.  Since `p_13=y`,

`x_1+...+x_11>3Y`.

The assumption `b<=y` gives `x_1+x_2<=Y`, so
`x_3+...+x_11>2Y`.  The first seven terms `x_3,...,x_9` are at most `Y/2`,
and `x_11<=x_10`; hence `x_10>-3Y/4`.  Thus all ordinary adjacent ratios
through `j/i` are larger than `y^{-3/4}`.  For `y>=4`,
`y^{-3/4}>1/(y-1)`, while `G/y>y-1`; this gives every ordinary reserve
through the jump before `j`.

The two tail jumps again reduce to scalar inequalities.  The penultimate jump
uses

`(G(j+k)-y(i-1))(j-y)>y^2(j-1)`,

and the final jump uses

`G l(k-y)>y^2(k-1)`.

The ordinary reserve gives the positive surplus `G j-y(i-1)`.  The remaining
penultimate scalar and the final scalar follow from `G>y(y-1)`, `l>y^2`,
`k>ly>y^3`, and `j^2>=k`.  The `L<0` endpoint uses the checked piecewise
versions

`(G(j+k-2)-(y-1)(i-1))(j-y)>y(y-1)(j-1)`

and

`G(l-1)(k-y)>y(y-1)(k-1)`.

Next frontier diagnostic: `m=15,t=14`.  A 15,000-trial generic
near-terminal run for `(15,17)` with seed `14015` produced 34
first-positive-`14` states and no `V>B0+G+` failures.  The largest sampled
ratio was `488/1671`.  As for `t=13`, the generic sampler found no `y>1`
Lambda states, so the hard branch again appears too sparse for untargeted
near-terminal sampling.

Added `notes/probe_boundary_variation_t14_barrier.py` and
`notes/verify_boundary_variation_t14_barrier.py` for the next shifted barrier.
Write

`P=(1,a,b,c,d,e,f,g,h,i,j,k,l,m,y,1)`, `l>my`, `G=m-y`.

The shifted obstruction family is

`(1,r,r^2,r^3,r^4,r^5,r^6,r^7,r^8,r^8,r^8,r^8,(r^4+1)r^2+1,r^4+1,r^2,1)`.

For `r=2`, the copied local reserve again fails:

`G l-y(k-1)=13*69-4*255<0`.

The corrected two-term reserve tested by the probe is

`G(k z_10+l z_11)-y(j-1)z_10-y(k-1)max(0,z_11-z_10)`.

The scalar verifier checks the obstruction family, the shifted low-`c`
family, and 20,000 generated hard-tail factors; it found no failures with
seed `14120`.  The first small-`L` stress runs did not find actual candidates:
an unforced 50,000-trial run with seed `14100`, forced-controller-`10` and
forced-controller-`11` 80,000-trial random-family runs with seeds `14110` and
`14111`, and fixed `r=2` obstruction-family 150,000-trial runs with seeds
`14410` and `14411` all found zero small-`L` negative-coefficient candidates.
This suggests the barrier may become inaccessible at this shift, but the
current evidence is only diagnostic.

Added `notes/diagnose_boundary_variation_t14_rejections.py` to separate the
ways the `t=14` probe can fail before becoming a candidate.  On the fixed
`r=2` obstruction family with forced controller `10`, 100,000 trials with seed
`14510` all failed from a nonpositive Lambda denominator; the first bad
denominator was concentrated at indices `2` and `3` (`50,075` and `32,755`
times).  Forced controller `11` with seed `14511` behaved the same way
(`49,895` failures at index `2`, `33,021` at index `3`).  The random-family
50,000-trial run with seed `14500` also had only nonpositive-denominator
rejections.

This explains why the current probe sees no candidates, but it is not yet a
proof that the mathematical branch is empty: the random tail generator can
create invalid early jumps while trying to force a far-tail jump.  The next
step is therefore a denominator-aware tail sampler or an analytic lemma
showing that any far-tail small-`L` attempt necessarily causes an early
denominator failure.

The denominator-aware check resolves this in the other direction.  Added
`notes/probe_boundary_variation_t14_flat_tail.py`, which keeps the obstruction
tail flat through the chosen controller and then inserts a near-critical jump.
For the `r=2` obstruction family, `L_target=1/10`, `lambda_target=5`, and
`alpha=1/100`, it produces valid candidates for both controller `10` and
controller `11`.  The controller-`10` run has

`L=11745127/117292020`, `lambda=5`, `lambda L=11745127/23458404`,

with all reserve margins positive; the controller-`11` run similarly has

`L=11747717/117445320`, `lambda=5`, `lambda L=11747717/23489064`.

Thus the zero-candidate random probes were a sampler artifact, not evidence
that the `t=14` barrier branch is empty.  The right next step is to replace the
old random tail generator by a denominator-aware one before drawing more
experimental conclusions about higher shifts.

The same flat-tail construction also works in random-family mode.  With
20,000 generated hard-tail factors, seed `14610`, and controller `10`, it
produced 11,695 valid candidates; with seed `14611` and controller `11`, it
produced 11,746 valid candidates.  The smallest margins in both runs were the
explicit `r=2` obstruction candidates above, with no margin failures.

Next frontier diagnostic: `m=16,t=15`.  A 12,000-trial generic
near-terminal run for `(16,18)` with seed `15016` produced 11
first-positive-`15` states and no `V>B0+G+` failures.  The largest sampled
ratio was `371/1506`.  The generic sampler again found no `y>1` Lambda
states.

Added `notes/probe_boundary_variation_flat_tail.py` as a degree-parameterized
version of the denominator-aware flat-tail sampler.  It exactly reproduces the
two `t=14` obstruction margins above, and then reaches the next shifted
obstruction branch at `t=15`.  For the `r=2` family

`(1,2,4,8,16,32,64,128,256,256,256,256,256,69,17,4,1)`,

with `L_target=1/10`, `lambda_target=5`, and `alpha=1/100`, controller `11`
gives

`L=16665637/166497120`, `lambda=5`, `lambda L=16665637/33299424`,

and controller `12` gives

`L=16671167/166679820`, `lambda=5`, `lambda L=16671167/33335964`.

Both have positive linear, threshold, combined-penultimate, and final margins.
The same generic sampler on 20,000 generated hard-tail factors produced 6,688
valid candidates for controller `11` with seed `15110`, and 6,685 valid
candidates for controller `12` with seed `15111`, with zero margin failures.
Thus the denominator-aware branch also persists one shift beyond the dedicated
`t=14` probe.

The next shift behaves the same way.  For `m=17,t=16`, the `r=2` obstruction
family is

`(1,2,4,8,16,32,64,128,256,256,256,256,256,256,69,17,4,1)`.

With the same flat-tail parameters, controller `12` gives

`L=22445803/224298780`, `lambda=5`, `lambda L=22445803/44859756`,

and controller `13` gives

`L=22454273/224510880`, `lambda=5`, `lambda L=22454273/44902176`.

A 20,000-trial random-family check produced 5,965 valid candidates for
controller `12` with seed `16120`, and 5,985 valid candidates for controller
`13` with seed `16121`, again with zero margin failures.  This is now strong
evidence that the flat-tail construction is exposing a stable shifted
near-terminal branch rather than isolated `t=14`/`t=15` accidents.

Added `notes/verify_boundary_variation_generic_barrier.py` to test the scalar
reserve proof conditions in degree-parameterized form.  The generic verifier
passes the explicit obstruction families, the capped low-`c` families, and
5,000 generated hard-tail factors per degree for degrees `13` through `17`
with seed `17120`; it also passes 3,000 generated hard-tail factors per degree
for degrees `18` through `22` with seed `18122`.  A longer `18` through `24`
run with seed `18124` then fails in degree `23` at the last ordinary reserve
index `17` on

`(1,3,9,25,68,178,459,1105,2482,5457,11827,23962,45617,86584,135271,208745,321402,464263,525474,59323,6676,734,9,1)`.

The failed assertion is `(y-1)p_{19}>p_{18}-1`.  This is a proof-strategy
boundary rather than a product counterexample: the far-tail flat probes still
have positive margins, but the simple scalar proof cannot be applied unchanged
to all higher-degree hard tails.  The next split should isolate these
high-degree pre-tail ratio cases or replace the last ordinary reserve by a
second combined-reserve step.

To check that the degree-`23` scalar-verifier failure is not a hidden Lambda
failure, the flat-tail probe now has a threshold-relative mode:
`lambda_target=(6/5)threshold` and
`L_target<=y/(2 lambda_target)`.  In this mode the degree-`23` probe accepted
all 5,000 generated hard-tail factors for both controllers `18` and `19`
with seeds `23180` and `23181`, with zero margin failures.  A degree-`30`
smoke test likewise accepted all 2,000 generated hard-tail factors for both
controllers `25` and `26` with seeds `30250` and `30251`.  This reinforces
the current picture: the flat-tail Lambda branch remains robust at high
degree, while the attempted scalar proof needs a more refined high-degree
reserve split.

The generic scalar verifier now supports a combined-reserve depth.  Depth `2`
replaces the last two ordinary tail reserves by the two-term combined reserve.
It repairs the degree-`23` failure above: with seed `18124`, degrees `18`
through `24` pass 3,000 generated hard-tail factors per degree, and with seed
`25130`, degrees `25` through `30` pass 2,000 per degree.  A lighter
degree-`31` through `50` sweep with seed `31500` also passes 1,000 per degree
at coefficient cap `2,000,000`.

Raising the coefficient cap shows why this is not yet a final proof.  At cap
`10^12`, degree `30`, seed `93030`, and depth `2`, the verifier fails at the
new last ordinary reserve index `23` on a generated hard-tail factor.  Depth
`3` repairs that same high-cap degree-`30` run for 10,000 trials, and also
passes a high-cap degree-`50` run with 5,000 trials and seed `95050`.  This
suggests the proof should use a variable terminal combined block, or prove
that once the ordinary reserve fails, enlarging the combined block by one
step absorbs the failure.

Added `notes/diagnose_boundary_variation_combined_depth.py` to measure the
minimum combined depth needed by each generated factor.  At cap `10^12`,
degree `30`, and seed `99030`, the distribution over 2,000 generated factors
plus explicit families was `{1: 2001, 2: 21, 3: 2}`.  At degree `50`, seed
`99050`, the sampled distribution was `{1: 2024}`.  A broader high-cap sweep
over degrees `25` through `40`, seed `99250`, and 1,000 generated factors per
degree found maximum required depth `3`; depth-`3` cases occurred only in
degrees `27`, `31`, `32`, `36`, and `40` in that run.  So the adaptive
combined-block direction is promising, but the proof still needs a structural
bound on the required terminal depth.

Added `notes/probe_boundary_variation_combined_depth_family.py` to show that
no fixed combined depth can be enough in general.  For any requested depth
`s`, take `y=4`, a power-of-two rising prefix, then a terminal block dropping
by a factor `8` repeatedly before `(H,R,4,1)` with `H/R=8`.  The first eight
members are admissible, have `b<=y`, and require combined depths exactly
`1,2,...,8`.  Thus the scalar proof has to handle a variable terminal
combined block.  This is not bad news for the main problem: it tells us the
right invariant should sum over the whole terminal run of ordinary-reserve
failures, instead of trying to cap its length.

The generic verifier now has an adaptive terminal-block mode.  It uses the
ordinary reserve up to the first failed ordinary reserve, then applies the
combined reserve through the remaining terminal block.  This repairs both
high-cap fixed-depth failures: degree `30`, seed `93030`, cap `10^12`, and
10,000 generated factors pass, as does degree `50`, seed `95050`, cap
`10^12`, and 5,000 generated factors.  The broader high-cap degree `25`
through `40` sweep with seed `99250` also passes 1,000 generated factors per
degree.  On the forced-depth family, the adaptive start selects exactly the
required terminal block for depths `1` through `12`.  This made the pointwise
adaptive scalar target plausible at the time: prove that the combined reserve
holds from the first ordinary-reserve failure through the hard tail.  A
degree-`100` high-cap
smoke test with cap `10^18`, seed `99100`, and 2,000 generated hard-tail
factors also passes in adaptive mode.

Added `notes/diagnose_boundary_variation_adaptive_margins.py` to track the
tightest adaptive-block margins.  In a high-cap degree `25` through `40`
run with seed `99400`, the adaptive-depth distribution was
`{1: 16199, 2: 173, 3: 12}`.  The smallest combined, piecewise-combined,
final, and piecewise-final margins all came from the explicit `r=2`
obstruction family, not from the rare depth-`2` or depth-`3` random tails.
A degree-`100` high-cap run with seed `99500` showed the same tight states.
This suggested the adaptive combined block gains slack when it is genuinely
long; the sharp endpoint is still the small `r=2` obstruction tail.

Added `notes/adaptive-terminal-block-lemma.md` and
`notes/derive_boundary_variation_adaptive_lemma.py` to turn the adaptive
verifier into a proof target.  For a local triple
`A=p_i`, `B=p_{i+1}`, `C=p_{i+2}`, the combined reserve margin is

`A(-By+y^2)+B^2R-B^2y+BCR-BCy-BRy+By-CRy+Cy^2`.

At the local log-concavity frontier `A=Bs`, `C=B/s`, it becomes

`B^2(R+R/s-sy-y-y/s)+B(-Ry-Ry/s+s y^2+y+y^2/s)`.

This local relaxation is too weak by itself: the local data
`(y,R,A,B,C)=(2,5,24,11,5)` gives negative combined margin.  That false
alarm is blocked from the obvious linear-prefix extension by `p_2<=y`.

Added `notes/check_boundary_variation_prefix_z3.py` for bounded prefix
extension checks.  On the next local false-alarm tail
`(297,96,31,10,3,1)`, Z3 proves prefix lengths `3` through `10` unsatisfiable
under value cap `1000`; longer lengths time out as `unknown` with a
`500ms` per-length nonlinear timeout.  As a sanity check, the same encoding
finds the known forced-depth tail `(8192,1024,128,4,1)` at prefix length `14`
and verifies the resulting full factor.

Correction: the tail `(297,96,31,10,3,1)` does extend to a full admissible
monic factor; the missing prefix is simply long.  The factor

`(1,2,3,...,297,96,31,10,3,1)`

has degree `301`, satisfies `p_2<=y`, first fails the ordinary reserve at
index `295`, and then violates the non-piecewise scalar combined inequality
at index `296` with margin `-762`.  More generally,

`R=y^2+1`, `H=Ry+1`, `B=floor(H^2/R)`, `A=floor(B^2/H)`,

and `P_y=(1,2,3,...,A,B,H,R,y,1)` give the same scalar failure for the checked
range `y=3,...,8`.  This falsifies the pointwise adaptive scalar package, not
the Erdős 993 product statement: the flat-tail evaluator on the `y=3` factor
still has positive actual margins for controllers `295`, `296`, and `297`.
Running the same flat-tail smoke test on the full checked range gives positive
total linear and threshold margins for `y=3,...,8`, but for `y=4,...,8` the
actual combined-penultimate local reserve is slightly negative.  So the next
proof cannot just replace the false scalar with a sharper pointwise
`z`-dependent local reserve; it has to use a summed terminal-block margin.
Added `notes/probe_boundary_variation_terminal_sum_margin.py` to track this
directly.  On the frontier family it produced `18` valid flat-tail states, no
linear or threshold failures, and `15` local combined-penultimate failures;
the `N`-only margin remains large and grows from about `22.07` at `y=3` to
about `466.43` at `y=8`.

The same diagnostic now records the global jump-bound margin.  If
`h_k=max(0,z_{k+1}-z_k)` and `S_k=sum_{r<k}z_r`, then `lambda_k L<y` and the
Lambda denominator give `h_k(L+yS_k)<y z_k^2`.  Therefore

`G N-yV >= G N-sum_{k:h_k>0} y^2(p_{k+1}-1)z_k^2/(L+yS_k)`.

On the frontier flat-tail states this bound is positive and nearly equal to
the exact `N`-only margin.  The reduction and remaining target are isolated in
`notes/summed-jump-bound-lemma.md`.  The positive-jump restriction in that sum
is essential: an all-index subtraction is already false on the `r=2`
obstruction flat-tail states, with margin near `-105`.  A second split is also
necessary at the initial jump.  When the active jump is at index `0`, the
positive-jump lower bound can be negative because `S_0=0`; paying the `h_0`
term exactly restores the positive hybrid target on the same explicit states.
There is also a useful local cover: for every charged index `i>=1` with
`z_i<=S_i`, or with `p_{i+1}>y`, the term `G p_{i+1}z_i` pays the whole
summed-bound charge.  Thus the remaining hard subcase consists only of
low-coefficient record-large charged indices with `p_{i+1}<=y` and `z_i>S_i`.
The coarse denominator bound is false on exactly that subcase: a `y=4`
frontier-prefix construction has hybrid margin about `-228.5` while the exact
`N`-only margin remains about `3176.0`.  The current refined target therefore
pays those low-prefix record jumps exactly and uses the summed bound only on
the locally covered complement.
The refined target is now closed by a run-allocation argument: partition the
positive jumps of `z` into maximal increasing runs, then pay every exact
low-prefix record charge in a run from the unused reserve at that run's
uncharged endpoint.  Non-exception charged indices pay for themselves by the
local-cover inequalities.
For the `L<0` side, `notes/probe_boundary_variation_adaptive_piecewise.py`
checks the adaptive piecewise scalar margins directly.  It found no failures
on the frontier factors or a small random sweep, but it also shows that the
simpler shifted-adjacent reserve shortcut fails near the upper allowed `H`
boundary for `y=4`; the piecewise proof must use the full endpoint margin.

A high-cap random stress run with
`notes/probe_boundary_variation_terminal_sum_margin_random.py` checked degrees
`25` through `40`, `200` generated hard-tail factors per degree, and both
terminal controllers.  It produced `6,400` valid flat-tail states with no
linear, threshold, jump-bound, or local combined failures.  The smallest
linear and threshold margins came from the old `r=2` obstruction tail
`(...,256,256,69,17,4,1)`, while the smallest jump-bound margin was still
about `54.336`.

Added `notes/probe_boundary_variation_terminal_sum_margin_shapes.py` to test
less rigid low-`L` shapes.  It builds a low-`L` noisy nonincreasing tail,
inserts controlled near-terminal jumps, normalizes the active Lambda value to
`(6/5)threshold`, and then evaluates the same summed jump-bound.  A run over
degrees `25` through `40` attempted `8,000` shapes and produced `4,662` valid
Lambda-branch states, with no linear, threshold, jump-bound, or local combined
failures.  The smallest threshold margin was about `1.875`, again on the old
`r=2` obstruction tail, and the smallest jump-bound margin was about `7.443`.
The sampler now also supports fixed-family targeting.  On the `r=2`
obstruction family, a degree-`40` run produced `6,680` valid states and a
degree-`80` run produced `2,010` valid states, again with no failures.  The
local combined margin fell from about `0.080` to about `0.0209`, but the
summed jump-bound margin stayed near `7.44`, suggesting the global bound is
not controlled by the vanishing local reserve.

Widening the random-shape active-controller window to the last `8` possible
controllers produced `4,568` valid states over degrees `25` through `40`, with
no failures.  The tightest sampled case still came from the final controller
on the `r=2` obstruction tail, so the wider terminal window did not reveal a
new weaker configuration.

The shape sampler now has `--l-target` and `--l-safety` controls.  Pushing
toward the endpoint `lambda L<y`, with `l_safety=21/20`, did not produce a
tighter case.  A targeted degree-`40` obstruction run and a random
controller-window-`8` run both had no failures, and their smallest summed
jump-bound margins rose to about `8.57`.  This suggests the small-`L` limit is
the relevant hard regime for the summed bound.

A fixed low-`c` family run at degree `40`, base `2`, and controller window `8`
produced `1,598` valid states with no failures.  Its smallest jump-bound
margin was about `43.1`, so this family remains much less tight than the
`r=2` obstruction family for the summed-bound target.

The shape sampler now supports extra controlled jumps.  A multi-jump run over
degrees `25` through `40`, with controller window `8` and `3` extra jumps,
produced `7,071` valid states and no failures.  This was the tightest stress
test so far: the smallest threshold margin fell to about `0.555`, and the
smallest jump-bound margin to about `2.203`.  A smaller fixed obstruction run
with `6` extra jumps also found no failures.  A focused degree-`40` obstruction
run with positive-jump reporting pushed the sampled floor lower, to about
`1.953`, with active jumps at indices `(29,31,34)`.
Decomposing that tight state showed all three charged jumps are locally
covered, and the post-cover residual margin is still about `1.876`.

Added `notes/probe_boundary_variation_first_failure_bound.py` to isolate the
part that still seems right.  If the previous ordinary reserve succeeds, the
first failed ordinary-reserve index has strong enough bounds on `A`; a
`1,000,000`-sample run found no first-failure combined or piecewise failures.
The symbolic certificate in `notes/derive_boundary_variation_adaptive_lemma.py`
now proves that first-failure combined and piecewise margins are positive
after substituting `R=y^2+1+E` and `B=y+1+U`.  The next proof target is
therefore narrower: splice this first-failure certificate and the refined
summed terminal-block reserve back into the full adaptive factor proof.

The `L<0` piecewise branch is now closed separately in
`notes/piecewise-terminal-block-lemma.md`.  In this branch the reserve target
is

`CK>=V`, with `C=(R-y)/(y-1)`,
`K=sum_i(p_{i+1}-1)z_i`, and
`V=sum_i(p_{i+1}-1)max(0,z_{i+1}-z_i)`.

Every nonfinal jump is paid by the next shifted `K` term.  The needed adjacent
inequality

`(R-y)(p_{i+2}-1)>=(y-1)(p_{i+1}-1)`

holds for every pair before `H`: if the pair is not decreasing it is trivial,
while a decreasing pair has `p_{i+2}>=H` and ratio at most `H/R`; the remaining
endpoint check is a concave quadratic in `H` on `Ry<=H<=R^2/y`.  The final
`H -> R` shifted-adjacent inequality can fail, exactly as the frontier
diagnostic showed, but the full endpoint

`(R-y)(R-1)(H-y)>y(y-1)(H-1)`

and `L<0` give `max(0,z_R-z_H)<y z_H/(H-y)`, so the final `R` reserve pays
the final charge.  The algebra and a frontier classification are saved in
`logs/993_boundary_variation_piecewise_terminal_block_algebra.log`.

Thus the adaptive terminal-block package now has a proof route in both global
branches: the refined summed/run allocation for `L>=0`, and the shifted
piecewise allocation for `L<0`.  The remaining task is no longer to find a
terminal reserve, but to splice these branch lemmas cleanly into the full
factor verifier/proof skeleton.

Added `notes/adaptive-terminal-block-handoff.md` for that splice.  It states
the hard-branch theorem using the shared normalizations

`L=sum(p_{i+1}-y)z_i`, `N=sum p_{i+1}z_i`,
`K=sum(p_{i+1}-1)z_i`, and
`V=sum(p_{i+1}-1)max(0,z_{i+1}-z_i)`.

For `L>=0`, the linear/Lambda envelope is positive because the summed lemma
gives `GN-yV>0`.  For `L<0`, the threshold identity

`(G/(y-1))L+GN-yV=y(CK-V)`

reduces the proof to the piecewise lemma.  This handoff also clarifies that
the first-failure scalar certificate is now a compatibility check for the old
adaptive switch, not the main terminal reserve.

Added `notes/verify_boundary_variation_handoff_identities.py` to make the
normalization audit reproducible.  It checks

`N+L/(y-1)=yK/(y-1)`

and

`(G/(y-1))L+GN-yV=y(CK-V)`

on random hard-tail factors, forced `L<0` vectors, and the existing flat-tail
evaluator states.  The saved run covered `5,600` algebraic identities,
including `2,800` forced negative-`L` states, plus `8,400` flat-tail states;
see `logs/993_boundary_variation_handoff_identities.log`.

The handoff endpoint algebra was also tightened from `y>=3` to `y>=2`.
`notes/verify_boundary_variation_terminal_handoff.py` now checks the
coefficient-side conditions of the handoff: hard branch assumptions, all
nonfinal shifted-adjacent reserves, and the final piecewise endpoint.  The
saved run covered `6,326` frontier, obstruction-family, low-`c`, and generated
hard-tail factors; see
`logs/993_boundary_variation_terminal_handoff_coefficients.log`.

Added `notes/adaptive-terminal-block-proof-draft.md` as a cleaned proof
version of the hard near-terminal handoff.  It states the theorem directly:
for `L>=0`, the refined summed/run allocation gives `GN-yV>0`; for `L<0`,
the shifted allocation gives `CK>V`; the threshold identity connects this
piecewise target back to the original product lower envelope.

Marked `notes/verify_boundary_variation_generic_barrier.py` as a legacy
scalar-reserve verifier.  Its `--adaptive-terminal-block` mode intentionally
reproduces the falsified pointwise scalar target for diagnostics; the current
hard-branch proof should use
`notes/verify_boundary_variation_terminal_handoff.py` instead.

Added `notes/993-current-integration-audit.md` as the current state snapshot.
It separates the now-closed hard terminal handoff from the remaining upstream
monic product work.  The latest wide terminal-handoff verifier checked
`7,126` factors over degrees `13..80` with no coefficient-side failures; see
`logs/993_boundary_variation_terminal_handoff_coefficients_wide.log`.

Log:

- `logs/993_boundary_variation_degree4_targeted_seed999.log`.
- `logs/993_boundary_variation_degree4_targeted_t3_seed1001.log`.
- `logs/993_boundary_variation_t3_sharp_family.log`.
- `logs/993_boundary_variation_t4_sharp_family.log`.
- `logs/993_boundary_variation_degree5_t4_targeted_seed5004.log`.
- `logs/993_boundary_variation_t4_slope_budget_counterexample.log`.
- `logs/993_boundary_variation_degree5_t4_jump_report_seed5014.log`.
- `logs/993_boundary_variation_t4_only_A_b0_obstruction.log`.
- `logs/993_boundary_variation_t4_d_jump_y_split_seed6100.log`.
- `logs/993_boundary_variation_t4_both_lambda_seed6202.log`.
- `logs/993_boundary_variation_t5_sharp_family.log`.
- `logs/993_boundary_variation_degree6_t5_targeted_seed7005.log`.
- `logs/993_boundary_variation_degree6_t5_jump_report_seed7015.log`.
- `logs/993_boundary_variation_t5_single_nonfinal_y_split_seed7035.log`.
- `logs/993_boundary_variation_t5_mixed_ygt1_lambda_seed7075.log`.
- `logs/993_boundary_variation_degree7_t6_targeted_seed8016.log`.
- `logs/993_boundary_variation_t6_lambda_seed8026.log`.
- `logs/993_boundary_variation_t6_coefficient_obstruction.log`.
- `logs/993_boundary_variation_t6_relaxed_surplus_seed8056.log`.
- `logs/993_boundary_variation_t6_small_l_seed8066.log`.
- `logs/993_boundary_variation_t6_small_l_seed8067.log`.
- `logs/993_boundary_variation_degree8_t7_targeted_seed9017.log`.
- `logs/993_boundary_variation_t9_barrier_seed9099.log`.
- `logs/993_boundary_variation_t9_barrier_seed9100.log`.
- `logs/993_boundary_variation_degree11_t10_near_terminal_seed10011.log`.
- `logs/993_boundary_variation_t10_barrier_seed10100.log`.
- `logs/993_boundary_variation_t10_barrier_controller7_seed10107.log`.
- `logs/993_boundary_variation_degree12_t11_near_terminal_seed11012.log`.
- `logs/993_boundary_variation_t11_barrier_seed11100.log`.
- `logs/993_boundary_variation_t11_barrier_controller7_seed11107.log`.
- `logs/993_boundary_variation_t11_barrier_controller8_seed11108.log`.
- `logs/993_boundary_variation_t11_barrier_combined_controller7_seed11200.log`.
- `logs/993_boundary_variation_t11_barrier_combined_controller8_seed11201.log`.
- `logs/993_boundary_variation_t11_barrier_corrected_combined_controller7_seed11300.log`.
- `logs/993_boundary_variation_t11_barrier_corrected_combined_controller8_seed11301.log`.
- `logs/993_boundary_variation_t11_barrier_verifier_seed11120.log`.
- `logs/993_boundary_variation_degree13_t12_near_terminal_seed12013.log`.
- `logs/993_boundary_variation_t12_barrier_seed12100.log`.
- `logs/993_boundary_variation_t12_barrier_controller8_seed12118.log`.
- `logs/993_boundary_variation_t12_barrier_controller9_seed12119.log`.
- `logs/993_boundary_variation_t12_barrier_verifier_seed12120.log`.
- `logs/993_boundary_variation_degree14_t13_near_terminal_seed13014.log`.
- `logs/993_boundary_variation_degree14_t13_near_terminal_seed13015.log`.
- `logs/993_boundary_variation_t13_barrier_seed13100.log`.
- `logs/993_boundary_variation_t13_barrier_controller9_seed13119.log`.
- `logs/993_boundary_variation_t13_barrier_controller10_seed13120.log`.
- `logs/993_boundary_variation_t13_barrier_obstruction2_controller9_seed13409.log`.
- `logs/993_boundary_variation_t13_barrier_obstruction2_controller10_seed13210.log`.
- `logs/993_boundary_variation_t13_barrier_verifier_seed13120.log`.
- `logs/993_boundary_variation_degree15_t14_near_terminal_seed14015.log`.
- `logs/993_boundary_variation_t14_barrier_seed14100.log`.
- `logs/993_boundary_variation_t14_barrier_controller10_seed14110.log`.
- `logs/993_boundary_variation_t14_barrier_controller11_seed14111.log`.
- `logs/993_boundary_variation_t14_barrier_obstruction2_controller10_seed14410.log`.
- `logs/993_boundary_variation_t14_barrier_obstruction2_controller11_seed14411.log`.
- `logs/993_boundary_variation_t14_barrier_verifier_seed14120.log`.
- `logs/993_boundary_variation_t14_rejection_random_seed14500.log`.
- `logs/993_boundary_variation_t14_rejection_obstruction2_controller10_seed14510.log`.
- `logs/993_boundary_variation_t14_rejection_obstruction2_controller11_seed14511.log`.
- `logs/993_boundary_variation_t14_flat_obstruction2_controller10.log`.
- `logs/993_boundary_variation_t14_flat_obstruction2_controller11.log`.
- `logs/993_boundary_variation_t14_flat_random_controller10_seed14610.log`.
- `logs/993_boundary_variation_t14_flat_random_controller11_seed14611.log`.
- `logs/993_boundary_variation_degree16_t15_near_terminal_seed15016.log`.
- `logs/993_boundary_variation_t15_flat_random_controller11_seed15110.log`.
- `logs/993_boundary_variation_t15_flat_random_controller12_seed15111.log`.
- `logs/993_boundary_variation_t16_flat_random_controller12_seed16120.log`.
- `logs/993_boundary_variation_t16_flat_random_controller13_seed16121.log`.
- `logs/993_boundary_variation_generic_barrier_degree13_17_seed17120.log`.
- `logs/993_boundary_variation_generic_barrier_degree18_22_seed18122.log`.
- `logs/993_boundary_variation_generic_barrier_degree18_24_failure_seed18124.log`.
- `logs/993_boundary_variation_t22_flat_relative_controller18_seed23180.log`.
- `logs/993_boundary_variation_t22_flat_relative_controller19_seed23181.log`.
- `logs/993_boundary_variation_t29_flat_relative_controller25_seed30250.log`.
- `logs/993_boundary_variation_t29_flat_relative_controller26_seed30251.log`.
- `logs/993_boundary_variation_generic_barrier_depth2_degree18_24_seed18124.log`.
- `logs/993_boundary_variation_generic_barrier_depth2_degree25_30_seed25130.log`.
- `logs/993_boundary_variation_generic_barrier_depth2_degree31_50_seed31500.log`.
- `logs/993_boundary_variation_generic_barrier_depth2_degree30_highcap_seed93030.log`.
- `logs/993_boundary_variation_generic_barrier_depth3_degree30_highcap_seed93030.log`.
- `logs/993_boundary_variation_generic_barrier_depth3_degree50_highcap_seed95050.log`.
- `logs/993_boundary_variation_combined_depth_degree30_highcap_seed99030.log`.
- `logs/993_boundary_variation_combined_depth_degree50_highcap_seed99050.log`.
- `logs/993_boundary_variation_combined_depth_degree25_40_highcap_seed99250.log`.
- `logs/993_boundary_variation_forced_combined_depth_family.log`.
- `logs/993_boundary_variation_generic_barrier_adaptive_degree30_highcap_seed93030.log`.
- `logs/993_boundary_variation_generic_barrier_adaptive_degree50_highcap_seed95050.log`.
- `logs/993_boundary_variation_generic_barrier_adaptive_degree25_40_highcap_seed99250.log`.
- `logs/993_boundary_variation_forced_family_adaptive_depth.log`.
- `logs/993_boundary_variation_generic_barrier_adaptive_degree100_highcap_seed99100.log`.
- `logs/993_boundary_variation_adaptive_margins_degree25_40_highcap_seed99400.log`.
- `logs/993_boundary_variation_adaptive_margins_degree100_highcap_seed99500.log`.
- `logs/993_boundary_variation_adaptive_lemma_algebra.log`.
- `logs/993_boundary_variation_prefix_z3_tail_297_96_31_10_3_1.log`.
- `logs/993_boundary_variation_prefix_z3_forced_depth1_tail.log`.
- `logs/993_boundary_variation_first_failure_bound_seed99700.log`.
- `logs/993_boundary_variation_adaptive_failure_family_y3_8.log`.
- `logs/993_boundary_variation_adaptive_failure_family_flat_tail_y3_8.log`.
- `logs/993_boundary_variation_terminal_sum_margin_frontier_y3_8.log`.
- `logs/993_boundary_variation_terminal_sum_margin_random_degree25_40_seed99800.log`.
- `logs/993_boundary_variation_terminal_sum_margin_shapes_degree25_40_seed99900.log`.
- `logs/993_boundary_variation_terminal_sum_margin_shapes_obstruction2_degree40_seed99910.log`.
- `logs/993_boundary_variation_terminal_sum_margin_shapes_obstruction2_degree80_seed99911.log`.
- `logs/993_boundary_variation_terminal_sum_margin_shapes_window8_degree25_40_seed99920.log`.
- `logs/993_boundary_variation_terminal_sum_margin_shapes_obstruction2_degree40_lnear_seed99930.log`.
- `logs/993_boundary_variation_terminal_sum_margin_shapes_window8_lnear_degree25_40_seed99931.log`.
- `logs/993_boundary_variation_terminal_sum_margin_shapes_lowc2_degree40_seed99940.log`.
- `logs/993_boundary_variation_summed_bound_all_index_obstruction.log`.
- `logs/993_boundary_variation_terminal_sum_margin_shapes_multijump_degree25_40_seed99960.log`.
- `logs/993_boundary_variation_terminal_sum_margin_shapes_obstruction2_multijump_small_degree40_seed99962.log`.
- `logs/993_boundary_variation_terminal_sum_margin_shapes_obstruction2_multijump_degree40_seed99970.log`.
- `logs/993_boundary_variation_summed_bound_initial_jump_obstruction.log`.
- `logs/993_summed_bound_tight_state_decomposition_seed99970.log`.
- `logs/993_boundary_variation_low_prefix_record_jump.log`.
- `logs/993_boundary_variation_adaptive_piecewise_seed993123.log`.
- `logs/993_boundary_variation_piecewise_terminal_block_algebra.log`.
- `logs/993_boundary_variation_handoff_identities.log`.
- `logs/993_boundary_variation_terminal_handoff_coefficients.log`.
- `logs/993_boundary_variation_terminal_handoff_coefficients_wide.log`.
