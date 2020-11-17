
% Fact - Rule


parent(tom,bob).
parent(pam,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).

female(pam).
female(liz).
female(pat).
female(ann).
male(jim).
male(tom).
male(bob).

happy(X) :- hasachild(X).
hasachild(X) :- parent(X,_).
mother(X,Y) :- parent(X,Y),female(X).

grandparent(X,Z) :- parent(X,Y),parent(Y,Z).

sister(X,Y) :- parent(Z,X),parent(Z,Y),female(X),X\=Y.

grandchild(X,Y) :- parent(Y,Z),parent(Z,X).
% x is grandchild of y

hastwochildren(X) :- hasachild(X),parent(X,Y),sister(Y,_).



ancestor(X,Z) :- parent(X,Z).

%recursive
ancestor(X,Z) :- parent(X,Y),ancestor(Y,Z).





