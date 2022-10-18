import sqlite3


class DbOperation():
    def __init__(self, db_name: str):
        self.dbname = db_name
        self.conn = sqlite3.connect(self.dbname, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table(self, operation: str):
        self.cur.execute(operation)

    def sqlite_operation(self, operation: str, data: list):
        # operationとdataの変数の数が違ったらエラー
        self.cur.execute(operation, data)
        self.commit_db()
        self.cur_close()
        self.conn_close

    def commit_db(self):
        self.conn.commit()

    def cur_close(self):
        self.cur.close()

    def conn_close(self):
        self.conn.close()

# tableを作るのは一回でいいから、それ用のクラスを作って継承させればいいかも。


class UserData():
    def __init__(self, db_name: str, table_name: str):
        self.db = DbOperation(db_name)
        create_table = f'CREATE TABLE IF NOT EXISTS {table_name}(email STRING PRIMARY KEY, username STRING, password INTEGER)'
        self.db.create_table(create_table)

    def add_user(self, email: str, username: str, password: int):
        insert_data = 'INSERT INTO userinfo (email, username, password) values(?, ?, ?)'
        user_info = [email, username, password]
        self.db.sqlite_operation(insert_data, user_info)


if __name__ == "__main__":
    user_data = UserData("user_info.db", "userinfo")
    email = "uiwtw3412o4@fsgdf.com"
    username = 'itoqhnvsr'
    password = 91298
    user_data.add_user(email, username, password)
