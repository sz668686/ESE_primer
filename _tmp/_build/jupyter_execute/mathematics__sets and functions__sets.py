# Sets

```{index} Sets (mathematics)
```

The notions of a *set* and an *element of a set* are some of the most primitive ones in mathematics so we normally do not even define them. However, intuitively, a set represents a collection of objects, which we call its elements. These objects can be anything: numbers, vectors, other sets... The reader might, understandably, be dissatisfied with this circular interpretation of a set as a collection, but hopefully this notebook will provide some intuition about the topic.

**Notation.**
- We denote a set by listing its elements, in any order we want, inside curly braces. For example, $A = \{ 1, 2, 3 \}$
- Let $A$ be a set. We write $a \in A$ to denote that $a$ is an element of $A$. We write $a \notin A$ to denote that $a$ is not an element of $A$. For example, $3 \in \{ 1, 2, 3 \}$.
- A set without any elements is called the **empty set** (or *null* set) and we denote it by $\emptyset$.
- Let $A$ and $B$ be sets. We say that $A$ is a **subset** of $B$, $A \subseteq B$, if every element of $A$ is also an element of $B$. For example, $\{ 1, 2 \} \subseteq \{ 1, 2, 3 \}$.

By convention, the empty set is a subset of every set and every set is a subset of itself:

- $\emptyset \subseteq A$
- $A \subseteq A$

## Set operations

```{sidebar} $\phantom{title}$
<img src="snfdata/setoperations.png" height="400">
```

We can extend the logic symbols explained in the {doc}`Logic <logic>` notebook to define set operations.

**Intersection** $\cap$. The intersection of sets $A$ and $B$ is denoted as $A \cap B$ and it corresponds to the logical $\land$ ("and"). Its result is a set which contains elements that are common in *both* $A$ and $B$. That is, $\forall x (x \in A \cap B) \iff ((x \in A) \land (x \in B))$. For example, \\( \{ 1, 2, 3 \} \cap \{ 1, 3, 5 \} = \{ 1, 3 \} \\).

**Union** $\cup$. The union of sets A and B is denoted as A $\cup$ B and it corresponds to the logical $\lor$ ("or"). Its result is a set which contains elements which are elements of A or elements of B, i.e. the two sets are "added" together. That is, $\forall x (x \in A \cup B) \iff ((x \in A) \lor (x \in B))$. For example, \\( \{ 1, 2, 3 \} \cup \{ 1, 3, 5 \} = \{ 1, 2, 3, 5 \} \\).

**Complement** $\backslash$ or $-$. Similarly to how we can "add" sets together, we can also "subtract" one set from another. We denote this as $A \backslash B$ and the result is a set which contains only elements that are in $A$ but not in $B$ (i.e. elements unique to $A$). We can write that as $\forall x (x \in A \backslash B) \iff ((x \in A) \land (x \notin B))$. For example, $\{ 1, 2, 3 \} \backslash \{ 1, 3, 5 \} = \{ 2 \}$ and \\( \{ 1, 2 \} \backslash \{ 1, 2 \} = \emptyset \\).

## Set of natural numbers

In the examples above we considered finite sets, but more often we will deal with infinite sets. We cannot define such sets by listing all its elements, so our understanding of them must derive from their definition. 

A set of **natural numbers** $\mathbb{N}$ is one such set whose elements are natural numbers \\(0, 1, 2, \dots \\), i.e. 

$$\mathbb{N} = \{0, 1, 2, \dots \}$$.

```{margin} Extra: [Peano axioms](https://en.wikipedia.org/wiki/Peano_axioms)
We have just described properties which form the Peano axioms of $\mathbb{N}$.
```

$\mathbb{N}$ is our natural choice for counting as we know the first (smallest) element and for every element we know what its successor is. Therefore, the set $\mathbb{N}$ has a natural ordering $<$ and we can easily define the binary operation of addition ($+$) on $\mathbb{N}$, since $n + m$ is simply the sum of the n-th and m-th successor of $0$.

## Set of integer numbers

We very quickly find the limitations of the set $\mathbb{N}$. For example, the simple equation $n + x = 0$ has no solutions in $\mathbb{N}$ for $n \neq 0$. We call such numbers $x$ an *additive inverse* of $n$.

To solve such problems we therefore expand the set $\mathbb{N}$ by adding to it additive inverses of all elements of $\mathbb{N}$, noting that 0 is its own additive inverse ($0 + 0 = 0$). By doing this we reached the set of **integer numbers** $\mathbb{Z}$:

$$ \mathbb{Z} = \{ \dots, -2, -1, 0, 1, 2, \dots \} = - \mathbb{N} \cup \mathbb{N}. $$

```{index} Group
```

```{index} Commutative (Abelian) group
```

We will state without proof, but the reader can easily check this, that the set $\mathbb{Z}$ with the operation $+$ is an algebraic structure with properties:

1. **closure**: \\( \forall a,b \in \mathbb{Z}, a + b \in \mathbb{Z} \\)
2. **associativity**: \\( \forall a,b,c \in \mathbb{Z}, a + (b + c) = (a+b) + c\\)
3. **neutral element**: \\( \exists 0 \in \mathbb{Z} : \forall a \in \mathbb{Z}, 0 + a = a + 0 = a \\)
4. **inverse element**: \\( \forall a \in \mathbb{Z}, \exists -a \in \mathbb{Z} : a + -a = -a + a = 0 \\)
5. **commutativity**: \\( \forall a, b \in \mathbb{Z}, a + b = b + a \\)

We call a set equipped with a binary operation which satisfies properties 1-4 a **group**. If the 5th property is satisfied as well we call it a **commutative (Abelian) group**. For addition, it is the basic algebraic structure in which the equation $n + x = m$ can always be solved.

## Set of rational numbers

We can easily define another binary operation on the set $\mathbb{N}$: multiplication $\times$ or $\cdot$ by defining $n \times m = \underbrace{n + n + \dots + n}_m$. 

We can extend multiplication to the set $\mathbb{Z}$ as well. We will again state without proof, but the reader can easily check this, that multiplication on $\mathbb{N}$ and $\mathbb{Z}$ is associative, commutative, distributive over addition $(a (b +c) = ab + ac)$ and it has a neutral element 1 such that $n \times 1 = 1 \times n = n$.

Let us now consider the solution to the equation $n \times x = 1$ for $n \in \mathbb{Z}$. We find that the solution exists in $\mathbb{Z}$ only for $n = 1$. The number $x$ for which $nx = 1$ is called the *multiplicative inverse* or the *reciprocal* of $n$ and we denote it by $n^{-1} = \frac{1}{n}$.

To solve a general equation of the form $nx = m$ where $n, m \in \mathbb{Z}, n \neq 0$ we would therefore like to expand the set $\mathbb{Z}$ such that it includes all solutions of that equation. By doing this we have formed the set of **rational numbers** $\mathbb{Q}$:

$$ \mathbb{Q} = \{ \frac{m}{n}, \quad n, m \in \mathbb{Z}, n \neq 0 \}. $$

```{index} Field (mathematics)
```

What we have now achieved is very important. The set of rational numbers without zero equipped with multiplication $(\mathbb{Q}, \times)$ is also a commutative group, so we can always solve the equation of the form $nx = m$. Remember that zero does not have a reciprocal, so division by zero is impossible. Furthermore, multiplication distributes over addition and $(\mathbb{Q}, +)$ is also a commutative group. We call a set with these properties $(\mathbb{Q}, +, \times)$ a **field**.

## Set of real numbers

If we were to represent certain numbers on a number line we could find that not all numbers are in $\mathbb{Q}$. The simplest example would be the length of a diagonal of a unit square, i.e. $\sqrt{2}$. There are no $m, n \in \mathbb{Z}$ such that $\frac{m}{n} = \sqrt{2}$, i.e. we cannot construct it as a ratio of integers. We call such numbers *irrational numbers*.

We therefore expand our set $\mathbb{Q}$ to include irrational numbers. By doing that we form a set of **real numbers** and we denote it by $\mathbb{R}$. Now all points on the number line are elements of $\mathbb{R}$.

