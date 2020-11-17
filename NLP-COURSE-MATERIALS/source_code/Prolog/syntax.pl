%%% Grammar (Lexicon & Phrase Structure Rules)
% Biggest phrase is sentence
%Lexicon
n --> [bones].
n --> [dogs].
d --> [some].
d --> [the].
v --> [eat].

%Phrase Structure Rules
s --> dp,vp.
s --> n,vp.
dp --> d,np.
vp --> v,dp.
vp --> v,n.
np --> n.

%s[dogs,eat,bones],[]). Ex