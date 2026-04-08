radhika_kumari.
023-23-0115.

name(asgar_ali).
gender(asgar_ali, male).
height(asgar_ali, 5.4).
weight(asgar_ali, 65).
hobby(asgar_ali, reading).
hobby(asgar_ali, singing).
hobby(asgar_ali, game_playing).

name(sara).
gender(sara, female).
height(sara, 5.2).
weight(sara, 55).
hobby(sara, reading).

hobby(asgar_ali, reading).
hobby(asgar_ali, singing).
hobby(asgar_ali, game_playing).
hobby(radhika, reading).
hobby(radhika, series_watching).

get_height :-
    write('Enter name: '), read(X),
    height(X,H),
    write('Height is: '), write(H).

get_weight :-
    write('Enter name: '), read(X),
    weight(X,W),
    write('Weight is: '), write(W).

get_hobby :-
    write('Enter name: '), read(X),
    hobby(X,H),
    write('Hobby: '), write(H).