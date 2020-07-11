django-raw-query
===

Django's ORM is excellent: use it. But there are times when raw database queries are preferable.

This tiny class helps you interact with your database. It saves a bit of typing, that's all. It doesn't hold your hand and it assumes your SQL is valid.

---

How to use it
===

### Installation
```
pip install django-raw-query
```


### Import the package
```
from rawquery import RawQuery
```

### Init the class
```
rq = RawQuery()
```

There are 5 functions you can call. They all have the same two parameters: an SQL string, and, optionally, a list of parameters. To protect against SQL injection, you must not include quotes around the %s placeholders in the SQL string.

### Fetch a single row: a dict
```
rq.single_row('SELECT * FROM my_table WHERE id = %s', [1])

# output:
# { 'id': 1, 'name': 'Thomas', 'class': 'G4R' }
```

### Fetch multiple rows: a list of dicts
```
rq.multiple_rows('SELECT * FROM my_table')

# output:
# [
#     { 'id': 1, 'name': 'Thomas', 'class': 'G4R' },
#     { 'id': 2, 'name': 'Charlotte', 'class': 'G1S' },
# ]
```

### Fetch a single value: e.g. an integer, string, etc.
```
rq.single_value('SELECT COUNT(*) FROM my_table')

# output:
# 2
```

### Fetch multiple values: a list of values
```
rq.multiple_values('SELECT name FROM my_table')

# output:
# ['Thomas', 'Charlotte']
```

### UPDATE or INSERT
```
rq.run("UPDATE my_table SET name = %s WHERE id = %s", ['Douglas', 1])

# output:
# 1  # cursor.rowcount
```

---
Final note: This class does not cater for multiple databases but it would be trivial to add. If anybody would like to add this, or any other feature, pull requests are welcome.