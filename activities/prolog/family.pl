% CSMAXXXING AI Lab - Mission 6: The Family Detective (Symbolic AI)
% Use with SWISH (https://swish.swi-prolog.org) or the offline AI Lab (Prolog tab).
% Facts: parent(Parent, Child).
parent(tom, alice).
parent(alice, bob).
parent(alice, carol).
parent(bob, dave).

% Rules
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y)     :- parent(P, X), parent(P, Y), X \= Y.

% Step 3: add this rule yourself (remove the % at the start of the line)
% aunt_or_uncle(X, Y) :- sibling(X, P), parent(P, Y).

% Stretch: a rule can use itself (recursion)
% ancestor(X, Y) :- parent(X, Y).
% ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
