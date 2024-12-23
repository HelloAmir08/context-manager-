import psycopg2


class DatabaseConnect:
    def __init__(self, host: str, database: str, port: int, user: str, password: str):
        self.host: str = host
        self.database: str = database
        self.port: int = port
        self.user: str = user
        self.password: str = password
        self.connection = None


    def __enter__(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                port=self.port,
                user=self.user,
                password=self.password
            )
            return self.connection
        except psycopg2.DatabaseError as e:
            print(f"Database error: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

