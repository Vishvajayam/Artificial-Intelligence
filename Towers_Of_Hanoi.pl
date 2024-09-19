% Base case: Move a single disk from Source to Target
move(1, Source, Target, _) :-
    write('Move top disk from '), write(Source), write(' to '), write(Target), nl.

% Recursive case: Move N disks from Source to Target using Auxiliary as intermediate
move(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    move(M, Source, Auxiliary, Target),
    move(1, Source, Target, _),
    move(M, Auxiliary, Target, Source).
