# -*- coding: utf-8 -*-
import requests
import os
hero_list_url = 'http://pvp.qq.com/web201605/js/herolist.json'
hero_skin_root_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'
skin_base_dir = 'C:\\Users\\Zach\\Pictures\\image\\heroskin\\'


def get_ename(hero_json):
    '''{小乔:106,...}'''
    cname_ename = {}
    for hero in hero_json:
        cname_ename[hero['cname']] = hero['ename']
    return cname_ename

def get_skin_name(hero_json): 
    '''{'小乔':[恋之微风|万圣前夜|天鹅之梦|纯白花嫁|缤纷独角兽],...}'''
    cname_skin_name = {}
    for hero in hero_json:
        cname_skin_name[hero['cname']] = hero['skin_name']
        #print(cname_skin_name)
    return cname_skin_name

def get_hero_skin_count(cname_skin_name): 
    '''{'小乔':5,...}'''
    cname_skin_count = {} 
    for item in cname_skin_name.items():
        cname_skin_count[item[0]] = len(item[1].split('|'))
        #print(cname_skin_count)
    return cname_skin_count

def get_skin_name_url(skin_base_rul,cname_skin_count,cname_ename):
    '''{小乔:[skin_url1,skin_url2],...}'''
    cname_url_list = {}
    for cname,count in cname_skin_count.items():
        base_url = skin_base_rul+str(cname_ename[cname])+'/'+str(cname_ename[cname])+'-bigskin-'
        skin_url_list = [str(base_url)+str(num)+'.jpg' for num in range(1,count+1)]
        cname_url_list[cname] = skin_url_list
    return cname_url_list

def get_cname_skin_name(cname_skin_name):
	"""		
	Arguments:
		cname_skin_name {[list]} -- [it looks like {"小乔":[水晶之恋|大力出奇迹],...}]	
	Returns:
		[dict] -- {"小乔":[水晶之恋,大力出奇迹],...}
		"""
	cname_skin_name_dict = {}         
	for cname,skin_name_list in cname_skin_name.items():
		#print(cname)
		#print(skin_name_list)
		skin_list = [name for name in skin_name_list.split('|')]
		cname_skin_name_dict[cname] = skin_list
	return cname_skin_name_dict

def get_hero_skin(cname_url_list,cname_skin_name):
	for cname,skin_url in cname_url_list.items():
		if mkdir(skin_base_dir+cname):
			os.chdir(skin_base_dir+cname)  
			for i in range(len(skin_url)):
				file_name = cname_skin_name[cname][i]+'.jpg'
				r = requests.get(skin_url[i])
				with open(file_name,'wb') as f:
					f.write(r.content)

def mkdir(path):
    import os
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path+' 创建成功')
        return True
    else:
        print(path+' 目录已存在')
        return False
    return 

if __name__ == '__main__':
    hero_list_body = requests.get(hero_list_url)
    hero_list_json = hero_list_body.json()
    cname_ename = {}  
    cname_skin_name = {}
    cname_skin_count = {}
    cname_skin_name_str_list = get_skin_name(hero_list_json)
    #{'小乔':'恋之微风|万圣前夜|天鹅之梦|纯白花嫁|缤纷独角兽',...}
    #print("======this is  skin  name  str list ======")
    #print(cname_skin_name_str_list)
    cname_skin_name_list = get_cname_skin_name(cname_skin_name_str_list)
    cname_skin_count = get_hero_skin_count(cname_skin_name_str_list)
    #{'小乔':2,...}
    cname_ename = get_ename(hero_list_json)
    cnam_skin_url_list = get_skin_name_url(hero_skin_root_url,cname_skin_count,cname_ename)
    #print("======this is skin url list =========")
    #print(cnam_skin_url_list)
    #print("=====this is skin name list======")
    #print(cname_skin_name_list)
    get_hero_skin(cnam_skin_url_list,cname_skin_name_list)