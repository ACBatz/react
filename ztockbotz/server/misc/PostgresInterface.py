import psycopg2
from psycopg2._psycopg import AsIs

from stockbot.Stock import Stock


class PostgresInterface:
    class __PostgresInterface:
        def __init__(self, arg):
            self.val = arg

    instance = None

    def __init__(self, arg):
        if not PostgresInterface.instance:
            PostgresInterface.instance = PostgresInterface.__PostgresInterface(arg)
        else:
            PostgresInterface.instance.val = arg
        self.__createTableIfNotExists(arg)

    def __createTableIfNotExists(self, arg):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("select exists(select * from information_schema.tables where table_name=%s)", [arg])
        if not cur.fetchone()[0]:
            sql = (
                """
                CREATE TABLE %(table)s (
                    TIME    BIGINT      NOT NULL,
                    PRICE   NUMERIC     NOT NULL,
                    VOL     BIGINT      NOT NULL,
                    CAP     NUMERIC     NOT NULL,
                    UNIQUE(TIME)
                );
                """
            )
            cur.execute(sql, {'table': AsIs(arg)})
            conn.commit()
            conn.close()

    def get_connection(self):
        try:
            return psycopg2.connect(dbname='stockbotDB', user='postgres', password='andrew', host='127.0.0.1',
                                    port='5432')
        except:
            print('Error connecting to database')
            raise ConnectionError

    def insert(self, stock: Stock):
        conn = self.get_connection()
        cur = conn.cursor()
        sql = (
            """
            INSERT INTO %(table)s (TIME, PRICE, VOL, CAP) VALUES (%(datetime)s, %(price)s, %(volume)s, %(cap)s);
            """
        )
        cur.execute(sql, {'table': AsIs(stock.ticker), 'datetime': stock.datetime, 'price': stock.price, 'volume': stock.volume, 'cap': stock.cap})
        conn.commit()
        conn.close()

    def select(self, ticker):
        conn = self.get_connection()
        cur = conn.cursor()
        sql = (
            """
            SELECT * FROM %(table)s
            """
        )
        cur.execute(sql, {'table': AsIs(ticker)})
        records = cur.fetchall()
        conn.close()
        return {'code': AsIs(ticker), 'records': records}
