consonant(b).
consonant(c).
consonant(ç).
consonant(d).
consonant(f).
consonant(g).
consonant(ğ).
consonant(h).
consonant(j).
consonant(k).
consonant(l).
consonant(m).
consonant(n).
consonant(p).
consonant(r).
consonant(s).
consonant(ş).
consonant(t).
consonant(v).
consonant(y).
consonant(z).

initial(q0).
final(q0).
final(q1).
final(q2).
final(q3).
final(q4).
final(q5).
final(q6).
final(q7).
final(q8).


t(q0,a,q1).
t(q0,e,q2).
t(q0,ı,q3).
t(q0,i,q4).
t(q0,o,q5).
t(q0,ö,q6).
t(q0,u,q7).
t(q0,ü,q8).
t(q1,a,q1).
t(q1,ı,q3).
t(q3,ı,q3).
t(q3,a,q1).
t(q5,a,q1).
t(q5,u,q7).
t(q7,u,q7).
t(q7,a,q1).
t(q2,e,q2).
t(q2,i,q4).
t(q4,i,q4).
t(q4,e,q2).
t(q6,e,q2).
t(q6,ü,q8).
t(q8,ü,q8).
t(q8,e,q2).
t(X,A,X) :- consonant(A).

% start
                    #kedi       #state : q0 kedi,q0
check_vowel_harmony(String) :- initial(State),check_vowel_harmony(String,State).


% end

check_vowel_harmony('',State) :- final(State).

% in-between

check_vowel_harmony(String,State) :- 
            i       [ked] 
    concat(First,Rest,String),

    t(State,First,NextState),
    check_vowel_harmony(Rest,NextState).

