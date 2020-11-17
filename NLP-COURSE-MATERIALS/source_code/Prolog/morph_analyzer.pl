initial(q0).
final(q0).
final(q1).
final(q2).
final(q3).
final(q4a).
final(q4b).


t(q0,noun,q1).
t(q1,plur,q2).
t(q1,poss,q3).
t(q1,acc,q4a).
t(q1,dat,q4a).
t(q1,abl,q4a).
t(q1,inst,q4a).
t(q1,loc,q4b).
t(q1,gen,q4b).
t(q2,poss,q3).
t(q2,acc,q4a).
t(q2,dat,q4a).
t(q2,abl,q4a).
t(q2,inst,q4a).
t(q2,loc,q4b).
t(q2,gen,q4b).
t(q3,acc,q4a).
t(q3,dat,q4a).
t(q3,loc,q4b).
t(q3,abl,q4a).
t(q3,inst,q4a).
t(q3,gen,q4b).
t(q4b,rel,q1).

morpheme(noun,kedi).
morpheme(noun,kiler).
morpheme(noun,kopek).
morpheme(noun,kitap).
morpheme(noun,ceket).
morpheme(plur,ler).
morpheme(plur,lar).
morpheme(poss,i).
morpheme(poss,imiz).
%morpheme(poss,ımız).
morpheme(acc,i).
morpheme(acc,ni).
%morpheme(acc,nı).
morpheme(dat,e).
morpheme(dat,a).
morpheme(dat,ye).
morpheme(dat,ya).
morpheme(dat,ne).
morpheme(dat,na).
morpheme(abl,ten).
morpheme(abl,tan).
morpheme(abl,nden).
morpheme(abl,ndan).
morpheme(inst,le).
morpheme(inst,la).
morpheme(inst,yle).
morpheme(inst,yla).
morpheme(loc,de).
morpheme(loc,da).
morpheme(loc,te).
morpheme(loc,ta).
morpheme(loc,nde).
morpheme(loc,nda).
morpheme(gen,in).
morpheme(gen,un).
morpheme(gen,nin).
morpheme(gen,nun).

morpheme(gen,nin).
morpheme(rel,ki).

% nominal isim soylu
% verbal fiil soylu

word_inflection(String,Morphemes):-
       initial(State),
       %% State --> q0 oluyor
       word_inflection(String,State,Morphemes).
       %% word_inflection(kediler,q0,X)


word_inflection('',State,[]):- final(State).
       %% Bitiş durumu
       %% Kelimen boş + State'in final


word_inflection(String,State,[Morpheme|Rest]):-
    concat(Value,Rest_Str,String),
    %% Kelimeyi parçalıyoruz k - ediler , ke - diler 
    morpheme(Morpheme,Value),
    %% Morpheme'i buluyoruz morpheme(X,kedi) X -> noun
    t(State,Morpheme,Next),
    %% t(q0,noun,X)
    %% X -> q1
    word_inflection(Rest_Str,Next,Rest).
    %% word_inflection(ler,q1,[noun])
