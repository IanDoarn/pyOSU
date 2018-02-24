# pyOSU

Simple wrapper for osu! api written in python 3.6

### Example
Example of call api get_user

```python
from pyOSU.call import Call

key = "YOUR_API_KEY_HERE"
user = "sakudan"

api_call = Call(key)
data = api_call.get_user(user)

print(data)
```

Returned data
```json
[  
    {  
        "user_id":"2949928",
        "username":"Sakudan",
        "count300":"9059840",
        "count100":"555727",
        "count50":"63309",
        "playcount":"77133",
        "ranked_score":"11271704218",
        "total_score":"74651422546",
        "pp_rank":"2943",
        "level":"100.477",
        "pp_raw":"6676.88",
        "accuracy":"98.95134735107422",
        "count_rank_ss":"58",
        "count_rank_ssh":"37",
        "count_rank_s":"843",
        "count_rank_sh":"58",
        "count_rank_a":"328",
        "country":"US",
        "pp_country_rank":"463",
        "events":[  
        ]
    }
]
```