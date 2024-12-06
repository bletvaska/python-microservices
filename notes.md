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


## REST API

* nie je to protokol
* resource based

   /api/books
   /api/measurements

GET    /api/measurements       list     SELECT   [{},{},{}]
GET    /api/measurements/:id   detail   SELECT   {}
POST   /api/measurements                INSERT
DELETE /api/measurements/:id            DELETE
PATCH  /api/measurements/:id            UPDATE
PUT    /api/measurements/:id            UPDATE

http://namakany.web.sk:8080/api/books?author=foglar&published=1990
SELECT *
FROM books
WHERE
   author='foglar'
   AND published=1990
