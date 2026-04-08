mortal(X) :-
human(X).
human(neuton).
human(radhika).

in(book, bag).
in(bag, room).
in(room, bedroom).
in(room, house).
in(house, street).
is_in(A,D):-
  in(A,B),
  in(B,C),
  in(C,D).

clever(mahek).
smart(rida).
intelligent(A):-
  clever(A);
  smart(A).

red(car1).
car(car1).
blue(bike1).
bike(bike1).

fun(X):- 
    red(X), car(X).
fun(X):- 
    blue(X), bike(X).
fun(ice_cream).
