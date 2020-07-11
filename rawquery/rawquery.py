from django.db import connection

class RawQuery:
    # return a list of dicts
    # e.g. SELECT * FROM my_table
    # [
    #    {'a': 1, 'b': 2, 'c': 3},
    #    {'a': 1, 'b': 2, 'c': 3},
    # ]
    def multiple_rows(self, sql):
        cursor = self._do_query(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    # return a single dict
    # e.g. SELECT COUNT(*) AS count, AVG(price) AS avg_price FROM my_table
    # { 'count': 12, 'avg_price': 95.2 }
    def single_row(self, sql):
        return self.multiple_rows(sql)[0]

    # return a single value
    # e.g. SELECT COUNT(*) FROM my_table
    # 134
    def single_value(self, sql):
        cursor = self._do_query(sql)
        return cursor.fetchone()[0]

    # return a list of single values
    # e.g. SELECT id FROM my_table
    # [1, 2, 3, 4, 5]
    def flat_list(self, sql):
        cursor = self._do_query(sql)
        return [row[0] for row in cursor.fetchall()]

    # UPDATE, INSERT, etc.
    def run(self, sql):
        cursor = self._do_query(sql)
        return cursor.rowcount

    def _do_query(self, sql):
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor
