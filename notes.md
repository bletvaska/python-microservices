# notes

## Zivot bez ORM

SELECT * FROM measurements;

[
(1, 5.12.2024, 09:00:00, kosice, sk, 4.2, 88, 1024),
(2, 5.12.2024, 08:45:00, kosice, sk, 4.1, 85, 1024),
(3, 5.12.2024, 08:30:00, kosice, sk, 4.0, 80, 1024),
]

[
{
'id': 1,
'dt': '5.12.2024 09:00:00',
'city': 'kosice',
'country': 'sk',
'temp': 4.2,
'hum': 88,
'pressure': 1024,
},
]

## Zivot s ORM

select(Measurement).all()  -- ORM --> SELECT * FROM measurement;

[
Measurement()
]

m = entries[0]
m.id, m.city, m.country
