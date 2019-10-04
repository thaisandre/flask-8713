
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='1234',
        database='banco'
    )

if __name__ == '__main__':
    conn = get_connection()
    print(conn)
    print('conexão aberta!')

    conn.close()
    print('conexão fechada!')
