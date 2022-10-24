from playwright.sync_api import Playwright, sync_playwright
import sqlite3
from sqlite3 import Error
# from sqlite_python import create_connection, create_table 
#顯示學生成績表



import sqlite3

sqliteConnection = sqlite3.connect('house.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")




def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to file:///C:/Users/Polun/_/tasker%202022/%E5%9C%B0%E6%94%BF%E8%B3%87%E6%96%99220925/%E7%9B%B8%E9%97%9C%E6%AA%94%E6%A1%88/0925/%E5%8D%81%E6%B3%89%E5%8D%81%E7%BE%8E%E8%B6%85%E5%80%BC%E9%A6%96%E9%81%B8-%E6%89%80%E6%9C%89%E6%AC%8A%E9%83%A8.html
    # page.goto("file:///Users/polunlin/workspace/tasker_0925_%E5%9C%B0%E6%94%BF%E8%B3%87%E6%96%99/%E5%9C%B0%E6%94%BF%E8%B3%87%E6%96%99220925/0925/%E5%8D%81%E6%B3%89%E5%8D%81%E7%BE%8E%E8%B6%85%E5%80%BC%E9%A6%96%E9%81%B8-%E6%89%80%E6%9C%89%E6%AC%8A%E9%83%A8.html")
    # page.goto("file:///Users/polunlin/workspace/tasker_0925_%E5%9C%B0%E6%94%BF%E8%B3%87%E6%96%99/%E6%96%B0%E6%8E%A5%E5%BA%B7%E8%8E%8A%E7%A4%BE%E5%8D%80%E5%9B%9B%E6%88%BF4.html")
    page.goto("file:///Users/polunlin/workspace/tasker_0925_%E5%9C%B0%E6%94%BF%E8%B3%87%E6%96%99/%E8%80%81%E8%8E%8A%E5%A4%A7%E5%BB%881.html")
    
    # file:///Users/polunlin/workspace/tasker_0925_%E5%9C%B0%E6%94%BF%E8%B3%87%E6%96%99/%E6%96%B0%E6%8E%A5%E5%BA%B7%E8%8E%8A%E7%A4%BE%E5%8D%80%E5%9B%9B%E6%88%BF4.html
    table_label = page.locator("#content > table") ## locator of tables
    ##  table_label.count() ## number of tables
    #content > table:nth-child(4)
    #content > table:nth-child(4)
    #content > table:nth-child(5)
    # print(house_label_count)
    house_list= []
    tmp_dict = {}
    type = ""
    tmp_dict2 = {}
    tmp_dict1={}
    for table_idx in range(table_label.count()): ## for loop of tables table_idx(0,1,2,3) 
        tr = table_label.nth(table_idx).locator("tr") ## locator of trs in table_idx(th) table  

        for tr_idx in range(tr.count()): ## for loop of tr tr_idx(0,1,2,3) 
            td = tr.nth(tr_idx).locator("td")
            th = tr.nth(tr_idx).locator("th")

            if th.count()==1 :
                # print(th.nth(0).text_content().strip())
                type = th.nth(0).text_content().strip()
                tmp_dict[type] =[]
                tmp_dict1 = {}
            if td.count()==1 :
                type = td.nth(0).text_content().strip()
                tmp_dict[type] =[]
                tmp_dict1 = {}
                # print(td.nth(0).text_content().strip())
                # if td.nth(0).text_content().strip() == ' 物坐落地號':
                    
                # 建物坐落地號
                # 附屬建物
                # 共有部分
                    # print(td.nth(td_idx).text_content().strip())
                   
            if td.count()>1:
                for td_idx in range(td.count()):
                    # print(td.nth(td_idx).text_content().strip())
                    if td_idx %2== 0:
                        if "建物坐落土地所有權登記次序" in td.nth(0).text_content().strip():
                            break
                        else:
                            # tmp_dict1 = tmp_dict2
                            if type =='建物坐落地號' and td.nth(td_idx).text_content().strip() =='':
                                col = '建物坐落地號'
                            else :
                                col = td.nth(td_idx).text_content().strip()
                            tmp_dict1[col] = ""
                    tmp_dict2 = {}
                    if td_idx %2 == 1:
                        if col =='地段':
                            id1 = td.nth(td_idx).text_content().strip().split(" ")[0]
                            col2 = td.nth(td_idx).text_content().strip().split(" ")[1]
                            tmp_dict1['地段1'] = id1
                            tmp_dict1['地段2'] = col2
                            del tmp_dict1['地段']
                        elif col =='建號':   
                            id2 = td.nth(td_idx).text_content().strip().split(" ")[0]
                            tmp_dict1['建號'] =id2
                        else:
                            if type !='建物標示部':
                                tmp_dict1['建號'] =id2
                                tmp_dict1['地段1'] = id1
                            tmp_dict1[col] = td.nth(td_idx).text_content().strip()
        # print(tmp_dict1)      
        tmp_dict[type].append(tmp_dict1)
        print(tmp_dict)
                        # tmp_dict[type].append(td.nth(td_idx).text_content().strip())
            # house_list.append(tmp_dict)
    # if tmp_dict != {}:
    #     house_list.append(tmp_dict)
    # if '建物標示部' in tmp_dict:
    #     keys = ','.join(tmp_dict['建物標示部'].keys())
    #     for keys,values in tmp_dict['建物標示部']:

    #     user1 = {"id":100, "name": "Rumpelstiltskin", "dob": "12/12/12"}
    #     cursor.execute("INSERT INTO users VALUES (:id, :name, :dob)", user1) 
    # tmp_dict['建物標示部']


    
       
            # if len(td.nth(td_idx).text_content().strip()) >0:
                    
            #     if hi ==0:
            #         if '資料來源' in  td.nth(tt).text_content().strip():
            #             break                                
            #     if hi==1 :
            #         # if td.nth(0).text_content().strip() =='成交物件':
            #         # if exists("house1.xlsx"):
            #         #     break
            #         house_label_list.append(td.nth(tt).text_content().strip())    
            #         if tt ==0:
            #             house_label_list.append("類型")
            #     elif tt==0:
            #         for key,value in using_type_map.items():                                        
            #                 if  value in td.nth(tt).text_content().strip():
            #                     house_label_list.append(td.nth(tt).text_content().strip().replace(value,""))
            #                     house_label_list.append(value)
            #                     break
            #     elif  tt ==9:
            #         house_label_list.append(td.nth(tt).text_content().strip().split()[0])  
            #     else:
            #         house_label_list.append(td.nth(tt).text_content().strip())
                # print(td.nth(tt).text_content().strip())
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
