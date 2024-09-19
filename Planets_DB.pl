% Define the database of planets with their distance from the sun (in AU), mass (relative to Earth), and type (inner or outer)
planet(mercury, 0.39, 0.06, inner).
planet(venus, 0.72, 0.82, inner).
planet(earth, 1, 1, inner).
planet(mars, 1.52, 0.11, inner).
planet(jupiter, 5.2, 317.8, outer).
planet(saturn, 9.58, 95.2, outer).
planet(uranus, 19.18, 14.6, outer).
planet(neptune, 30.07, 17.2, outer).

% Rule to find the distance of a planet from the sun
distance_from_sun(Planet, Distance) :-
    planet(Planet, Distance, _, _).

% Rule to find the type of a planet (inner or outer)
planet_type(Planet, Type) :-
    planet(Planet, _, _, Type).

% Rule to check if a planet has moons (assuming any planet with mass > 0 has moons)
has_moon(Planet) :-
    planet(Planet, _, Mass, _),
    Mass > 0.
