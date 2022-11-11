# abacum


## Command line
You can load a csv file of transactions through a Django command:
```
pablobuenaposadasanchez@Pablos-MacBook-Pro abacum % make venv
python3.10 -m venv venv
venv/bin/pip install -r requirements.txt
Collecting Django==4.1
  Using cached Django-4.1-py3-none-any.whl (8.1 MB)
  ...
pablobuenaposadasanchez@Pablos-MacBook-Pro abacum % source venv/bin/activate
(venv) pablobuenaposadasanchez@Pablos-MacBook-Pro abacum % python src/manage.py loader sample-data.csv
accounts added 203, transactions added 79999
```

## Endpoints

### CSV loader - `POST http://localhost:8000/api/loader/`
you can also upload a csv of transactions through the API:
```
curl -F 'file=@/Users/pablobuenaposadasanchez/Desktop/abacum/sample-data.csv' http://localhost:8000/api/loader/
{"accounts":203,"transactions":79999}
```

### Full year balance by account - `GET http://localhost:8000/api/accounts/?year={year}`
```
curl "http://localhost:8000/api/accounts/?year=2020"
{
   "count":203,
   "next":"http://localhost:8000/api/accounts/?limit=100&offset=100&year=2020",
   "previous":null,
   "results":[
      {
         "id":68100000,
         "balance":19132576.59
      },
      {
         "id":52000012,
         "balance":18692301.35
      },
      {
         "id":62900403,
         "balance":17699648.72
      },
      {
         "id":20100000,
         "balance":18235456.37
      },
      {
         "id":46500000,
         "balance":19142308.52
      },
      {
         "id":10000000,
         "balance":22081760.43
      },
      {
         "id":52000007,
         "balance":20199728.68
      },
      {
         "id":47510001,
         "balance":22118295.68
      },
      {
         "id":12101800,
         "balance":17948767.43
      },
      {
         "id":52010001,
         "balance":20445328.2
      },
      {
         "id":62900990,
         "balance":20612213.27
      },
      {
         "id":62300100,
         "balance":22739354.6
      },
      {
         "id":62700801,
         "balance":19730434.21
      },
      {
         "id":11000000,
         "balance":22803759.55
      },
      {
         "id":70000100,
         "balance":20887731.44
      },
      {
         "id":47100000,
         "balance":19229326.41
      },
      {
         "id":62900100,
         "balance":19285558.49
      },
      {
         "id":57200002,
         "balance":17614054.34
      },
      {
         "id":52000100,
         "balance":19094637.23
      },
      {
         "id":26000000,
         "balance":22175037.18
      },
      {
         "id":62300900,
         "balance":16142842.94
      },
      {
         "id":57200102,
         "balance":23608890.56
      },
      {
         "id":56500001,
         "balance":20313284.31
      },
      {
         "id":57200005,
         "balance":20486520.39
      },
      {
         "id":52000004,
         "balance":20728205.35
      },
      {
         "id":70000001,
         "balance":18788352.56
      },
      {
         "id":48500000,
         "balance":22252475.39
      },
      {
         "id":62900390,
         "balance":19575335.55
      },
      {
         "id":62700900,
         "balance":20990064.31
      },
      {
         "id":11300000,
         "balance":19995684.96
      },
      {
         "id":21900000,
         "balance":19110258.61
      },
      {
         "id":62900991,
         "balance":21780189.96
      },
      {
         "id":70000012,
         "balance":19706297.38
      },
      {
         "id":40040100,
         "balance":21172163.97
      },
      {
         "id":63100000,
         "balance":21347852.69
      },
      {
         "id":74000000,
         "balance":20201707.63
      },
      {
         "id":47510000,
         "balance":20902769.86
      },
      {
         "id":62700903,
         "balance":21953415.18
      },
      {
         "id":47590000,
         "balance":20886055.46
      },
      {
         "id":62900402,
         "balance":18871208.02
      },
      {
         "id":10900000,
         "balance":22757065.71
      },
      {
         "id":43000000,
         "balance":18799416.54
      },
      {
         "id":62500000,
         "balance":20891935.07
      },
      {
         "id":57000000,
         "balance":19812110.15
      },
      {
         "id":62900340,
         "balance":18159004.16
      },
      {
         "id":64200000,
         "balance":18261440.51
      },
      {
         "id":52000006,
         "balance":18219931.61
      },
      {
         "id":52000011,
         "balance":13034846.24
      },
      {
         "id":62100100,
         "balance":19396786.37
      },
      {
         "id":52000201,
         "balance":22021213.65
      },
      {
         "id":28150000,
         "balance":20405551.58
      },
      {
         "id":41000200,
         "balance":23790962.49
      },
      {
         "id":28190000,
         "balance":23048743.73
      },
      {
         "id":57600000,
         "balance":19591517.81
      },
      {
         "id":28060000,
         "balance":19267107.18
      },
      {
         "id":62900330,
         "balance":21324526.15
      },
      {
         "id":52000200,
         "balance":20788246.89
      },
      {
         "id":21600000,
         "balance":18000188.38
      },
      {
         "id":12101400,
         "balance":22628682.77
      },
      {
         "id":12101700,
         "balance":18601568.57
      },
      {
         "id":62900400,
         "balance":21511476.34
      },
      {
         "id":52000014,
         "balance":22129533.97
      },
      {
         "id":28130000,
         "balance":19708671.56
      },
      {
         "id":52010000,
         "balance":20782818.61
      },
      {
         "id":67890000,
         "balance":24410161.71
      },
      {
         "id":67800000,
         "balance":21231349.23
      },
      {
         "id":12101600,
         "balance":22506416.94
      },
      {
         "id":11900000,
         "balance":17088936.45
      },
      {
         "id":55100000,
         "balance":18127974.16
      },
      {
         "id":62700902,
         "balance":23050745.84
      },
      {
         "id":67100000,
         "balance":21023317.22
      },
      {
         "id":62900450,
         "balance":21928713.97
      },
      {
         "id":68000000,
         "balance":18961155.94
      },
      {
         "id":57300001,
         "balance":17097359.03
      },
      {
         "id":69000000,
         "balance":19725743.87
      },
      {
         "id":47600010,
         "balance":17631343.17
      },
      {
         "id":62900300,
         "balance":19274241.17
      },
      {
         "id":62700100,
         "balance":20915699.83
      },
      {
         "id":57200004,
         "balance":20341414.12
      },
      {
         "id":46000000,
         "balance":16755602.88
      },
      {
         "id":52000009,
         "balance":18344108.36
      },
      {
         "id":14700000,
         "balance":18841814.88
      },
      {
         "id":64570000,
         "balance":21733443.7
      },
      {
         "id":43340000,
         "balance":23352038.38
      },
      {
         "id":41000100,
         "balance":21154090.34
      },
      {
         "id":47090000,
         "balance":19225852.28
      },
      {
         "id":12101200,
         "balance":19384592.3
      },
      {
         "id":62700901,
         "balance":22483304.57
      },
      {
         "id":52000017,
         "balance":19350572.1
      },
      {
         "id":54400000,
         "balance":18131300.32
      },
      {
         "id":26000001,
         "balance":20977032.68
      },
      {
         "id":43040000,
         "balance":20526855.24
      },
      {
         "id":62900404,
         "balance":20364458.97
      },
      {
         "id":12100000,
         "balance":18724258.38
      },
      {
         "id":62200100,
         "balance":19531483.82
      },
      {
         "id":41000000,
         "balance":18775712.46
      },
      {
         "id":20600000,
         "balance":19697875.1
      },
      {
         "id":52000002,
         "balance":21701275.59
      },
      {
         "id":62900003,
         "balance":20344881.46
      },
      {
         "id":62300200,
         "balance":20074020.54
      }
   ]
}
```

### Full year balance for a specific account - `GET http://localhost:8000/api/accounts/{account_id}/?year={year}`
```
curl "http://localhost:8000/api/accounts/11300000/?year=2020"
{
   "id":11300000,
   "balance":19995684.96
}
```

### Monthly balance for a specific month by account - `GET http://localhost:8000/api/accounts/?year={year}&month={month}`
```
curl "http://localhost:8000/api/accounts/?year=2020&month=1"
{
   "count":203,
   "next":"http://localhost:8000/api/accounts/?limit=100&month=1&offset=100&year=2020",
   "previous":null,
   "results":[
      {
         "id":68100000,
         "balance":1574515.59
      },
      {
         "id":52000012,
         "balance":1256522.63
      },
      {
         "id":62900403,
         "balance":2568901.21
      },
      {
         "id":20100000,
         "balance":591933.29
      },
      {
         "id":46500000,
         "balance":356114.62
      },
      {
         "id":10000000,
         "balance":1364695.66
      },
      {
         "id":52000007,
         "balance":1870571.87
      },
      {
         "id":47510001,
         "balance":1963139.1
      },
      {
         "id":12101800,
         "balance":1269208.26
      },
      {
         "id":52010001,
         "balance":1987776.62
      },
      {
         "id":62900990,
         "balance":1545167.45
      },
      {
         "id":62300100,
         "balance":1538256.67
      },
      {
         "id":62700801,
         "balance":2253250.43
      },
      {
         "id":11000000,
         "balance":1586818.92
      },
      {
         "id":70000100,
         "balance":1057634.4
      },
      {
         "id":47100000,
         "balance":1581124.5
      },
      {
         "id":62900100,
         "balance":1410857.51
      },
      {
         "id":57200002,
         "balance":473952.55
      },
      {
         "id":52000100,
         "balance":983287.46
      },
      {
         "id":26000000,
         "balance":3001807.04
      },
      {
         "id":62300900,
         "balance":3148835.12
      },
      {
         "id":57200102,
         "balance":2092458.14
      },
      {
         "id":56500001,
         "balance":2173771.67
      },
      {
         "id":57200005,
         "balance":2716681.84
      },
      {
         "id":52000004,
         "balance":2174628.32
      },
      {
         "id":70000001,
         "balance":1930846.31
      },
      {
         "id":48500000,
         "balance":1713081.3
      },
      {
         "id":62900390,
         "balance":1571514.7
      },
      {
         "id":62700900,
         "balance":2039931.4
      },
      {
         "id":11300000,
         "balance":2123093.19
      },
      {
         "id":21900000,
         "balance":2827447.42
      },
      {
         "id":62900991,
         "balance":884649.95
      },
      {
         "id":70000012,
         "balance":2441850.71
      },
      {
         "id":40040100,
         "balance":1771737.92
      },
      {
         "id":63100000,
         "balance":3495510.92
      },
      {
         "id":74000000,
         "balance":2247623.71
      },
      {
         "id":47510000,
         "balance":1397918.44
      },
      {
         "id":62700903,
         "balance":1937980.58
      },
      {
         "id":47590000,
         "balance":1789656.85
      },
      {
         "id":62900402,
         "balance":1595787.96
      },
      {
         "id":10900000,
         "balance":1900336.43
      },
      {
         "id":43000000,
         "balance":2174115.15
      },
      {
         "id":62500000,
         "balance":2406515.65
      },
      {
         "id":57000000,
         "balance":2336218.57
      },
      {
         "id":62900340,
         "balance":1421408.89
      },
      {
         "id":64200000,
         "balance":1822191.87
      },
      {
         "id":52000006,
         "balance":605184.43
      },
      {
         "id":52000011,
         "balance":1006305.75
      },
      {
         "id":62100100,
         "balance":1790119.72
      },
      {
         "id":52000201,
         "balance":1633917.6
      },
      {
         "id":28150000,
         "balance":2409496.92
      },
      {
         "id":41000200,
         "balance":1299934.06
      },
      {
         "id":28190000,
         "balance":869705.0
      },
      {
         "id":57600000,
         "balance":698128.28
      },
      {
         "id":28060000,
         "balance":1240278.54
      },
      {
         "id":62900330,
         "balance":1869170.0
      },
      {
         "id":52000200,
         "balance":1914774.68
      },
      {
         "id":21600000,
         "balance":1924938.94
      },
      {
         "id":12101400,
         "balance":2364306.05
      },
      {
         "id":12101700,
         "balance":2385928.26
      },
      {
         "id":62900400,
         "balance":2448249.81
      },
      {
         "id":52000014,
         "balance":860597.12
      },
      {
         "id":28130000,
         "balance":1892418.41
      },
      {
         "id":52010000,
         "balance":1283231.17
      },
      {
         "id":67890000,
         "balance":2497079.83
      },
      {
         "id":67800000,
         "balance":1810011.42
      },
      {
         "id":12101600,
         "balance":2796871.55
      },
      {
         "id":11900000,
         "balance":1141389.27
      },
      {
         "id":55100000,
         "balance":1016219.24
      },
      {
         "id":62700902,
         "balance":2337889.7
      },
      {
         "id":67100000,
         "balance":1282547.88
      },
      {
         "id":62900450,
         "balance":1686364.28
      },
      {
         "id":68000000,
         "balance":1602650.18
      },
      {
         "id":57300001,
         "balance":1623528.2
      },
      {
         "id":69000000,
         "balance":1501896.46
      },
      {
         "id":47600010,
         "balance":1809732.77
      },
      {
         "id":62900300,
         "balance":1085451.1
      },
      {
         "id":62700100,
         "balance":2896730.66
      },
      {
         "id":57200004,
         "balance":1445126.05
      },
      {
         "id":46000000,
         "balance":1708156.33
      },
      {
         "id":52000009,
         "balance":2656016.88
      },
      {
         "id":14700000,
         "balance":913778.37
      },
      {
         "id":64570000,
         "balance":1952980.07
      },
      {
         "id":43340000,
         "balance":2321647.14
      },
      {
         "id":41000100,
         "balance":1466807.81
      },
      {
         "id":47090000,
         "balance":1704500.8
      },
      {
         "id":12101200,
         "balance":812398.54
      },
      {
         "id":62700901,
         "balance":3014109.57
      },
      {
         "id":52000017,
         "balance":1323139.98
      },
      {
         "id":54400000,
         "balance":1471320.64
      },
      {
         "id":26000001,
         "balance":1828206.62
      },
      {
         "id":43040000,
         "balance":2193316.19
      },
      {
         "id":62900404,
         "balance":1202239.06
      },
      {
         "id":12100000,
         "balance":1261981.4
      },
      {
         "id":62200100,
         "balance":1532914.44
      },
      {
         "id":41000000,
         "balance":1450632.55
      },
      {
         "id":20600000,
         "balance":2157860.06
      },
      {
         "id":52000002,
         "balance":2343219.03
      },
      {
         "id":62900003,
         "balance":1688811.41
      },
      {
         "id":62300200,
         "balance":1741849.25
      }
   ]
}
```

### Monthly balance for a specific month and a specific account - `GET http://localhost:8000/api/accounts/{account_id}/?year={year}&month={month}`
```
curl "http://localhost:8000/api/accounts/11300000/?year=2020&month=1"
{
   "id":11300000,
   "balance":2123093.19
}
```

### Monthly balances by account - `GET http://localhost:8000/api/accounts/monthly/`
```
curl "http://localhost:8000/api/accounts/monthly/"
[
    {
        "id":68100000,
        "balance":1574515.59,
        "date":"2020-01"
    },
    {
        "id":68100000,
        "balance":3427955.17,
        "date":"2020-02"
    }, ...
]
```

### Monthly balance for a specific account - `GET http://localhost:8000/api/accounts/monthly/{account_id}/`
```
curl "http://localhost:8000/api/accounts/monthly/68100000/"
[
   {
      "id":68100000,
      "balance":1574515.59,
      "date":"2020-01"
   },
   {
      "id":68100000,
      "balance":3427955.17,
      "date":"2020-02"
   },
   {
      "id":68100000,
      "balance":5169206.49,
      "date":"2020-03"
   },
   {
      "id":68100000,
      "balance":6167774.3,
      "date":"2020-04"
   },
   {
      "id":68100000,
      "balance":8483263.47,
      "date":"2020-05"
   },
   {
      "id":68100000,
      "balance":9821448.63,
      "date":"2020-06"
   },
   {
      "id":68100000,
      "balance":10698144.77,
      "date":"2020-07"
   },
   {
      "id":68100000,
      "balance":12090567.69,
      "date":"2020-08"
   },
   {
      "id":68100000,
      "balance":13112213.49,
      "date":"2020-09"
   },
   {
      "id":68100000,
      "balance":14541562.73,
      "date":"2020-10"
   },
   {
      "id":68100000,
      "balance":16923656.13,
      "date":"2020-11"
   },
   {
      "id":68100000,
      "balance":19132576.59,
      "date":"2020-12"
   }
]
```
