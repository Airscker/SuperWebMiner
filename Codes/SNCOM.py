# _*_ coding:gbk _*_
import SuperMiner as SP
import os
import click


'''Initialize Engine'''
URL='http://www.nhc.gov.cn/cms-search/xxgk/searchList.htm?type=search'

sp1=SP.SuperMiner(url=URL,headless=False)
'''get the full list of objects'''
#Start miner engine
sp1.MineEngine()

#scroll the page to get the full items
SP.Basic_Actions(engine=sp1.engine,Obj_list=sp1.Objects(Id='keyword'),Obj_index=0,send_keys=True,message='接种情况')
#Get properties
attr=SP.Attributes('href',sp1.Objects(Class='wgblist'))
print(sp1.Objects(Class='wgblist'))
print(attr)
#download files
SP.Download(engine=sp1.engine,url_list=attr,data_type='page',file_type='.html')
#Close engine
os.system('pause')
sp1.engine.quit()
#/html/body/div[2]/div[2]/ul


@click.command()
@click.option("--url",help="Hide or display browser GUI",default="https://www.bing.com")
@click.option("--NOGUI/--GUI",help="Dsiplay the browser GUI",default=True)
@click.option("--key",help="The key of the element you want to find\nId,Name,Class,Link,Partial_link,Tag,Xpath,CSS are available.",default="Class")
@click.option("--scroll",default=10,help="Scroll the page to get more info")
@click.option("--com",help="commands you want to take action",default="")
@click.option("")
def  Superminer(url="https://www.bing.com",NOGUI=True,key="Class",scroll=10):
    SPE=SP.SuperMiner(url=url,headless=NOGUI)
    SPE.MineEngine()
    if scroll>0:
        SP.Basic_Actions(engine=SPE.engine,Obj_index=-2,send_keys=False,rollpage=True,roll_times=scroll,time_sleep=1)


    return 0

