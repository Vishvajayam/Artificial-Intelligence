% Define the database of students, teachers, and subject codes
studies(john, csc101).
studies(susan, csc102).
studies(jim, csc101).
studies(alice, csc103).
studies(bob, csc102).

teaches(prof_smith, csc101).
teaches(prof_jones, csc102).
teaches(prof_clark, csc103).

% Rule to find which teacher teaches a student
teacher_of(Student, Teacher) :-
    studies(Student, Subject),
    teaches(Teacher, Subject).

% Rule to find which students are taught by a specific teacher
students_of(Teacher, Student) :-
    teaches(Teacher, Subject),
    studies(Student, Subject).
