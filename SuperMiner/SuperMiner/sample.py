# _*_ coding:gbk _*_
'''
download neuron data informatiom of chimapanzee from http://neuromorpho.org/

animations are stored in 'animations' file folder
data profile are stored in 'pages' file folder

based on my own SuperMiner frame

CopyRight (C) 2022, Airscker(Yufeng Wang)
'''

import SMiner as SM
import os
'''Initialize Engine'''
#web link of data
URL='http://neuromorpho.org/byspecies.jsp#top'
#Open browser and initialize the engine
sp1=SM.SuperMiner(url=URL,headless=False)

'''get the full list of objects'''
##Start the web miner engine
sp1.MineEngine()

#Click on the 'chimpanzee' button to get the data list of chimpanzee's neuron data
SM.Basic_Actions(engine=sp1.engine,Obj_list=sp1.Objects(Name='chimpanzee'),Obj_index=0,click=True)

#Get links of the neuron data
attr=SM.Attributes('href',sp1.Objects(Class='screenshot'))

#save data links into file

with open('chimpanzee_data_links.txt','w') as f:
    print('saving links...')
    for link in attr:
        f.write(link+'\n')
f.close()

#close browser
sp1.engine.quit()

#download data of neurons
for i in range(len(attr)):
    sp1=SM.SuperMiner(url=attr[i],headless=True)
    sp1.MineEngine()
    with open('Animation_links.txt','w+') as f:
        f.write(SM.Attributes('href',sp1.Objects(Xpath='/html/body/div/table/tbody/tr[3]/td/table[1]/tbody/tr/td[2]/table/tbody/tr/td/div/center/div/div/div/table[1]/tbody/tr/td[2]/a[6]'))[0])
    f.close()
    #download the animations and pages
    SM.Download(folder_name='animations',engine=sp1.engine,url_list=SM.Attributes('href',sp1.Objects(Xpath='/html/body/div/table/tbody/tr[3]/td/table[1]/tbody/tr/td[2]/table/tbody/tr/td/div/center/div/div/div/table[1]/tbody/tr/td[2]/a[6]')),data_type='page',file_type='.html')
    SM.Download(folder_name='pages',engine=sp1.engine,url_list=[attr[i]],data_type='page',file_type='.html')
    
    sp1.engine.quit()

os.system('pause')


