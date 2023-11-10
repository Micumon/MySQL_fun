class QueryWriter:

    def __init__(self, query=""):
        self.query = query

    def __str__(self):
        return self.query

    def select(self, column_name="*"):
        return QueryWriter(self.query + f"SELECT {column_name}")

    def from_st(self, table_name):
        return QueryWriter(self.query + f" FROM {table_name}")

    def where(self, where_st):
        return QueryWriter(self.query + f" WHERE {where_st}")


