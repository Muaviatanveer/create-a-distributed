import sqlite3
from typing import List, Tuple

class MemoryAgent:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = None

    def connect(self) -> None:
        try:
            self.connection = sqlite3.connect(self.db_path)
            print("Database connection established.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def close(self) -> None:
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def insert_data(self, table_name: str, data: List[Tuple]) -> None:
        """
        Insert multiple rows into a specified table using parameterized queries to prevent SQL injection.

        :param table_name: Name of the table to insert data into.
        :param data: A list of tuples, where each tuple represents a row of data to be inserted.
        """
        if not self.connection:
            raise Exception("Database connection is not established.")

        placeholders = ', '.join(['?' for _ in range(len(data[0]))])
        columns = ', '.join([f'\"{col}\"' for col in data[0].keys()])

        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        try:
            cursor = self.connection.cursor()
            cursor.executemany(query, [tuple(row.values()) for row in data])
            self.connection.commit()
            print(f"{len(data)} rows inserted into {table_name}.")
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")
            raise

    def fetch_data(self, table_name: str) -> List[Tuple]:
        """
        Fetch all rows from a specified table.

        :param table_name: Name of the table to fetch data from.
        :return: A list of tuples, where each tuple represents a row of data.
        """
        if not self.connection:
            raise Exception("Database connection is not established.")

        query = f"SELECT * FROM {table_name}"
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            raise

# Example usage
if __name__ == "__main__":
    db_path = 'example.db'
    agent = MemoryAgent(db_path)
    agent.connect()

    # Create a table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """
    cursor = agent.connection.cursor()
    cursor.execute(create_table_query)
    agent.connection.commit()

    # Insert data using parameterized queries
    user_data = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"}
    ]
    agent.insert_data("users", [tuple(row.values()) for row in user_data])

    # Fetch and print data
    users = agent.fetch_data("users")
    for user in users:
        print(user)

    agent.close()