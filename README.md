# PyPort

import modules via http, only supports `from "url" import *` currently.

Inspired by [Tsoding - Including C File over HTTPS.](https://www.youtube.com/watch?v=4vSyqK3SK-0)

it works!
```python
from "https://raw.githubusercontent.com/scaldings/math-library/main/math-lib.py" import *

print(are_amicable(1, 2))
```

and run it
```commandline
C:\Users\Something_IDK\pyport> pyport main.py
False
C:\Users\Something_IDK\pyport>
```
**Note:** Use `.\pyport` for Powershell because Microsoft :|


should get the point across
