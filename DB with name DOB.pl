% Define the database of people with their names and dates of birth
person(john, date(15, march, 1980)).
person(susan, date(22, may, 1990)).
person(jim, date(12, january, 1975)).
person(alice, date(30, july, 1985)).
person(bob, date(10, october, 1992)).

% Rule to find a person's date of birth
born_on(Name, Day, Month, Year) :-
    person(Name, date(Day, Month, Year)).

% Rule to find all people born in a specific year
born_in(Name, Year) :-
    person(Name, date(_, _, Year)).
