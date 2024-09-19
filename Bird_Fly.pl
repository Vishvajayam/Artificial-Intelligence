% Define the database of birds and their ability to fly
bird(eagle, can_fly).
bird(penguin, cannot_fly).
bird(ostrich, cannot_fly).
bird(sparrow, can_fly).
bird(peacock, can_fly).

% Rule to check if a bird can fly
can_fly(Bird) :-
    bird(Bird, can_fly).

% Rule to check if a bird cannot fly
cannot_fly(Bird) :-
    bird(Bird, cannot_fly).
