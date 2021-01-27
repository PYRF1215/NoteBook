import requests
from bs4 import BeautifulSoup
import pymysql


class S_():
    def __init__(self, *stock_):
        self.stock_ = stock_
        

    def crawler(self):

        list_ = []

        for i in self.stock_:

            fd = requests.get("https://tw.stock.yahoo.com/q/q?s=" + i)
            
            sp = BeautifulSoup(fd.text.replace("加到投資組合", ""), "html5lib")

            date = sp.find("font", "tt").text.strip()[-9:]

            table_ = sp.find_all("table")[2]
            td_ = table_.find_all("td")[0:11]

            list_.append((date,) + tuple(j.text.strip() for j in td_))
        return list_

    def sql_(self, stocks):

        db_para = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "mysql123",
            "db": "stock",
            "charset": "utf8"
        }

        try:
            conn = pymysql.connect(**db_para)

            with conn.cursor() as cursor:
                sql = """INSERT INTO stock(
                                資料日期,
                                股票代號,
                                時間,
                                成交,
                                買進,
                                賣出,
                                漲跌,
                                張數,
                                昨收,
                                開盤,
                                最高,
                                最低)
                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                for insert_sql in stocks:
                    cursor.execute(sql,insert_sql )
                conn.commit()



        except Exception as ex:
            print("Exception:", ex)


    
            
def disp_menu():
    print("股票資料庫操作頁面")
    print("-----------")
    print("1.從網路上新增擷取股票資料")
    print("2.股票清單查詢顯示")
    print("0.離開")
    print("-----------")
    
    
    
    
    
    
def add_stock():
    print("新增股票代碼 (回首頁請輸入exit) : ")
    while 1:
        x = input(str())
        if x == 'exit' :break
        
        else:
            insert_sql = S_('%4s'%x)
            print(insert_sql.crawler())
            insert_sql.sql_(insert_sql.crawler())

def disp_all_stock():
    conn  =  pymysql.connect ( host = '127.0.0.1' ,  user = 'root' ,  passwd = "mysql123" ,  db = 'stock' ) 
    cur  =  conn.cursor () 
    cur.execute( "SELECT 資料日期,股票代號,時間,成交,買進,賣出,漲跌,張數,昨收,開盤,最高,最低 FROM stock" ) 
    for  r  in  cur:
        print ( r ) 
    cur.close () 
    conn.close()

def gui():
    import StockFinder
    

    

while True:
    disp_menu()
    
    choice = int(input("請輸入您的選擇："))
    if choice == 0:break
    if choice == 1:
        add_stock()
    elif choice == 2:
        disp_all_stock()
    else:break
    x=input("請按Enter鍵回主選單")
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    