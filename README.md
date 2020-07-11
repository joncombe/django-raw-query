django-raw-query
===

Django's ORM is excellent: use it. But there are times when raw database queries are preferable or unavoidable.

This tiny class helps you interact with your database. It saves a bit of typing, that's all. It doesn't hold your hand and it assumes your SQL is valid.

---

How to use it
===

### Import the package
```
from rawquery.rawquery import RawQuery
```

### Init the class
```
rq = RawQuery()
```

### Fetch multiple rows: a list of dicts
```
q.multiple_rows('SELECT * FROM my_table')

# output:
# [
#     { 'id': 1, 'name': 'Thomas', 'class': 'G4R' },
#     { 'id': 2, 'name': 'Charlotte', 'class': 'G1S' },
# ]
```

### Fetch a single row: a dict
```
q.single_row('SELECT * FROM my_table LIMIT 1')

# output:
# { 'id': 1, 'name': 'Thomas', 'class': 'G4R' }
```

### Fetch a single value: a single value, e.g. int, str, etc.
```
q.single_value('SELECT COUNT(*) FROM my_table')

# output:
2
```

### Fetch a flat list: a list of values
```
q.flat_list('SELECT name FROM my_table')

# output:
# ['Thomas', 'Charlotte']
```

### UPDATE or INSERT
```
q.run("UPDATE my_table SET name = 'Douglas' WHERE id = 1")

# output:
# 1  # cursor.rowcount
```