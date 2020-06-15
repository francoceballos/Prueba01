import sqlite3

class ClassDBMetod(object):

    def __init__(self, path):
        self.path = path
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback):
        if exc_class != None:
            print(f"ERROR Data base {exc}")
        self.conn.commit()
        self.conn.close()