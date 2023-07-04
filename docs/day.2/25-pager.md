# Pager

Stránkovanie výsledkov

## V čom je problém

Nemôžeme vracať všetky záznamy

* príliš veľa
* s pribúdajúcim počtom bude aj ich spracovanie a vrátenie trvať dlhší a dlhší čas
* množstvo získaných dát bude rásť s pribúdajúcim počtom položiek
* veľmi jednoducho by sme vedeli zabezpečiť DOS útok


## Stránkovanie v rámci Django

```json
{
    "count": 4321,
    "next": "http://app.com/users/?page=2",
    "previous": null,
    "results": [
        ...
    ]
}
```

