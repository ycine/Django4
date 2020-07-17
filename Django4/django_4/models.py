from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

rodzaje1 = (
    ('Interpreted', 'Interpreted'),
    ('Functional', 'Functional'),
    ('Compiled', 'Compiled'),
    ('Procedural', 'Procedural'),
    ('Scripting', 'Scripting'),
    ('Markup', 'Markup'),
    ('Logic-Based', 'Logic-Based'),
    ('Concurrent', 'Concurrent'),
    ('Object-Oriented', 'Object-Oriented'),
)

jezyki1= [
('JS', 'Java Script'),
('Py', 'Python'),
('HTML', 'html'),
('C', 'c'),
('C++', 'c++'),
('C#', 'c#'),
('Java', 'java'),
('PHP', 'php'),
('RUBY', 'Ruby'),
('Julia', 'julia'),
('Go', 'go'),
('R', 'r'),
]

class Technologie(models.Model):
    jezyki= [
    ('JS', 'Java Script'),
    ('Py', 'Python'),
    ('HTML', 'html'),
    ('C', 'c'),
    ('C++', 'c++'),
    ('C#', 'c#'),
    ('Java', 'java'),
    ('PHP', 'php'),
    ('RUBY', 'Ruby'),
    ('Julia', 'julia'),
    ('Go', 'go'),
    ('R', 'r'),
    ]

    jezyk = models.CharField(max_length=15, null=False, choices=jezyki)
    biblioteka = models.CharField(max_length=30)
    rodzaje = (
        ('Interpreted', 'Interpreted'),
        ('Functional', 'Functional'),
        ('Compiled', 'Compiled'),
        ('Procedural', 'Procedural'),
        ('Scripting', 'Scripting'),
        ('Markup', 'Markup'),
        ('Logic-Based', 'Logic-Based'),
        ('Concurrent', 'Concurrent'),
        ('Object-Oriented', 'Object-Oriented'),
    )
    rodzaj = MultiSelectField(rodzaje)
    opis = models.CharField(max_length=300)
    data = models.DateTimeField(auto_now_add=True)