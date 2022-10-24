import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"/Users/polunlin/workspace/tasker_0925_地政資料/地政資料220925/house.db"
    sql_create_table1 = """CREATE TABLE IF NOT EXISTS 主表格 (
                                    id integer PRIMARY KEY,
                                    縣市 text ,
                                    鄉鎮市區 text ,
                                    地段1 text NOT NULL,
                                    地段2 text,
                                    建號 text NOT NULL,
                                    主要用途  text,
                                    主要建材 text,
                                    層數 text,
                                    總面積 text,
                                    登記日期 text ,
                                    登記原因 text
                                );"""
    sql_create_table2 = """CREATE TABLE IF NOT EXISTS 建物坐落地號 (
                                    id integer PRIMARY KEY,
                                    地段1 text NOT NULL,
                                    建號 text NOT NULL,
                                    建物坐落地號 text NOT NULL,
                                    主要用途  text,
                                    CONSTRAINT fk_column
                                    FOREIGN KEY (地段1, 建號)
                                    REFERENCES 主表格 (地段1, 建號)
                                );"""
    sql_create_table3 = """CREATE TABLE IF NOT EXISTS 主建物層次 (
                                id integer PRIMARY KEY,
                                地段1 text NOT NULL,
                                建號 text NOT NULL,
                                瞭望室 text,
                                瞭望台 text,
                                騎樓 text,
                                避難室兼停車場 text,
                                停車場 text,
                                車庫 text,
                                夾層 text,
                                電梯樓梯間 text,
                                走廊 text,
                                倉庫 text,
                                雨遮 text,
                                管理員室（警衛室） text,
                                陽台 text,
                                花台 text,
                                防空避難室 text,
                                機械房 text,
                                儲藏室 text,
                                門廳 text,
                                水箱 text,
                                屋頂突出物 text,
                                通道 text,
                                平台 text,
                                見其他登記事項 text,
                                地下層 text,
                                地下1層 text,
                                地下2層 text,
                                地下3層 text,
                                地下4層 text,
                                地下5層 text,
                                地下6層 text,
                                地下7層 text,
                                地下8層 text,
                                地下9層 text,
                                地下10層 text,
                                '1層' text,
                                '2層' text,
                                '3層' text,
                                '4層' text,
                                '5層' text,
                                '6層' text,
                                '7層' text,
                                '8層' text,
                                '9層' text,
                                '10層' text,
                                '11層' text,
                                '12層' text,
                                '13層' text,
                                '14層' text,
                                '15層' text,
                                '16層' text,
                                '17層' text,
                                '18層' text,
                                '19層' text,
                                '20層' text,
                                '21層' text,
                                '22層' text,
                                '23層' text,
                                '24層' text,
                                '25層' text,
                                '26層' text,
                                '27層' text,
                                '28層' text,
                                '29層' text,
                                '30層' text,
                                '31層' text,
                                '32層' text,
                                '33層' text,
                                '34層' text,
                                '35層' text,
                                '36層' text,
                                '37層' text,
                                '38層' text,
                                '39層' text,
                                '40層' text,
                                '41層' text,
                                '42層' text,
                                '43層' text,
                                '44層' text,
                                '45層' text,
                                '46層' text,
                                '47層' text,
                                '48層' text,
                                '49層' text,
                                '50層' text,
                                '51層' text,
                                '52層' text,
                                '53層' text,
                                '54層' text,
                                '55層' text,
                                '56層' text,
                                '57層' text,
                                '58層' text,
                                '59層' text,
                                '60層' text,
                                '61層' text,
                                '62層' text,
                                '63層' text,
                                '64層' text,
                                '65層' text,
                                '66層' text,
                                '67層' text,
                                '68層' text,
                                '69層' text,
                                '70層' text,
                                '71層' text,
                                '72層' text,
                                '73層' text,
                                '74層' text,
                                '75層' text,
                                '76層' text,
                                '77層' text,
                                '78層' text,
                                '79層' text,
                                '80層' text,
                                '81層' text,
                                '82層' text,
                                '83層' text,
                                '84層' text,
                                '85層' text,
                                '86層' text,
                                '87層' text,
                                '88層' text,
                                '89層' text,
                                '90層' text,
                                '91層' text,
                                '92層' text,
                                '93層' text,
                                '94層' text,
                                '95層' text,
                                '96層' text,
                                '97層' text,
                                '98層' text,
                                '99層' text,
                                '100層' text,
                                '101層' text,
                                '102層' text,
                                '103層' text,
                                '104層' text,
                                '105層' text,
                                '106層' text,
                                '107層' text,
                                '108層' text,
                                '109層' text,
                                '110層' text,
                                '111層' text,
                                CONSTRAINT fk_column
                                FOREIGN KEY (地段1, 建號)
                                REFERENCES 主表格 (地段1, 建號)
                            );"""
    sql_create_table4 = """CREATE TABLE IF NOT EXISTS 附屬建物表格 (
                                    id integer PRIMARY KEY,
                                    地段1 text NOT NULL,
                                    建號 text NOT NULL,
                                    附屬建物用途 text,
                                    平台 text,
                                    儲藏室 text,
                                    花台 text,
                                    陽台 text,
                                    露台 text,
                                    雨遮 text,
                                    夾層 text,
                                    地下一層 text,
                                    地下二層 text,
                                    防空避難室 text,
                                    屋頂突出物 text,
                                    水箱 text,
                                    見使用執照 text,
                                    瞭望室 text,
                                    電梯樓梯間 text,
                                    機械房 text,
                                    車庫 text,
                                    停車場 text,
                                    見其他登記事項 text,
                                    走廊 text,
                                    騎樓 text,
                                    管理員室（警衛室） text,
                                    瞭望台 text,
                                    避難室兼停車場 text,
                                    倉庫 text,
                                    通道 text,
                                    見使用執照1 text,
                                    地下層 text,
                                    廚房 text,
                                    浴廁 text,
                                    CONSTRAINT fk_column
                                    FOREIGN KEY (地段1, 建號)
                                    REFERENCES 主表格 (地段1, 建號)
                                );"""
    sql_create_table5 = """CREATE TABLE IF NOT EXISTS 共有部分 (
                                    id integer PRIMARY KEY,
                                    地段1 text NOT NULL,
                                    建號 text NOT NULL,
                                    共有部分 text,
                                    權利範圍 text,
                                    面積 text,
                                    CONSTRAINT fk_column
                                    FOREIGN KEY (地段1, 建號)
                                    REFERENCES 主表格 (地段1, 建號)
                                );"""
    sql_create_table6 = """CREATE TABLE IF NOT EXISTS 建物坐落地號 (
                                    id integer PRIMARY KEY,
                                    地段1 text NOT NULL,
                                    建號 text NOT NULL,
                                    車位建號 text,
                                    含停車位 text,
                                    編號 text,
                                    權利範圍 text,
                                    CONSTRAINT fk_column
                                    FOREIGN KEY (地段1, 建號)
                                    REFERENCES 主表格 (地段1, 建號)
                                );"""
    sql_create_table7 = """CREATE TABLE IF NOT EXISTS 所有權部 (
                                    id integer PRIMARY KEY,
                                    地段1 text NOT NULL,
                                    建號 text NOT NULL,
                                    登記次序 text,
                                    登記日期 text,
                                    登記原因 text,
                                    所有權人姓名 text,
                                    統一編號 text,
                                    住址 text,
                                    權利範圍 text,
                                    其他登記事項 text,
                                    CONSTRAINT fk_column
                                    FOREIGN KEY (地段1, 建號)
                                    REFERENCES 主表格 (地段1, 建號)
                                );"""
    sql_create_table8 = """CREATE TABLE IF NOT EXISTS 他項權利部 (
                                    id integer PRIMARY KEY,
                                    地段1 text NOT NULL,
                                    建號 text NOT NULL,
                                    登記日期 text,
                                    登記原因 text,
                                    權利人姓名 text,
                                    擔保債權總金額 text,
                                    共同擔保地號1 text,
                                    共同擔保地號2 text,
                                    共同擔保地號3 text,
                                    共同擔保地號4 text,
                                    共同擔保地號5 text,
                                    共同擔保地號6 text,
                                    共同擔保地號7 text,
                                    共同擔保地號8 text,
                                    共同擔保地號9 text,
                                    共同擔保地號10 text,
                                    共同擔保地號11 text,
                                    共同擔保地號12 text,
                                    共同擔保地號13 text,
                                    共同擔保地號14 text,
                                    共同擔保地號15 text,
                                    共同擔保地號16 text,
                                    共同擔保地號17 text,
                                    共同擔保地號18 text,
                                    共同擔保地號19 text,
                                    共同擔保地號20 text,
                                    共同擔保地號21 text,
                                    共同擔保地號22 text,
                                    共同擔保地號23 text,
                                    共同擔保地號24 text,
                                    共同擔保地號25 text,
                                    共同擔保地號26 text,
                                    共同擔保地號27 text,
                                    共同擔保地號28 text,
                                    共同擔保地號29 text,
                                    共同擔保地號30 text,
                                    共同擔保建號1 text,
                                    共同擔保建號2 text,
                                    共同擔保建號3 text,
                                    共同擔保建號4 text,
                                    共同擔保建號5 text,
                                    共同擔保建號6 text,
                                    共同擔保建號7 text,
                                    共同擔保建號8 text,
                                    共同擔保建號9 text,
                                    共同擔保建號10 text,
                                    共同擔保建號11 text,
                                    共同擔保建號12 text,
                                    共同擔保建號13 text,
                                    共同擔保建號14 text,
                                    共同擔保建號15 text,
                                    共同擔保建號16 text,
                                    共同擔保建號17 text,
                                    共同擔保建號18 text,
                                    共同擔保建號19 text,
                                    共同擔保建號20 text,
                                    共同擔保建號21 text,
                                    共同擔保建號22 text,
                                    共同擔保建號23 text,
                                    共同擔保建號24 text,
                                    共同擔保建號25 text,
                                    共同擔保建號26 text,
                                    共同擔保建號27 text,
                                    共同擔保建號28 text,
                                    共同擔保建號29 text,
                                    共同擔保建號30 text,
                                    CONSTRAINT fk_column
                                    FOREIGN KEY (地段1, 建號)
                                    REFERENCES 主表格 (地段1, 建號)
                                );"""
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_table1)
        create_table(conn, sql_create_table2)
        create_table(conn, sql_create_table3)
        create_table(conn, sql_create_table4)
        create_table(conn, sql_create_table5)
        create_table(conn, sql_create_table6)
        create_table(conn, sql_create_table7)
        create_table(conn, sql_create_table8)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()