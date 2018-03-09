#coding:utf8
"""
fetch every hero's skill introduction and in every folder,it contains four pics and corresponding introductions
"""
import requests
import os
from bs4 import BeautifulSoup
hero_list_url = 'http://pvp.qq.com/web201605/js/herolist.json'
hero_skill_root_url = 'http://game.gtimg.cn/images/yxzj/img201606/heroimg/'
hero_skill_base_url = 'http://pvp.qq.com/web201605/herodetail/'
skill_base_dir = 'C:\\Users\\Zach\\Pictures\\Skill\\'
"""
skill-show...skill-list...skill-name/skill-desc/skill-tips
"""
#Read the hero num id
def get_ename(hero_json):
	"""
	Arguments:
		hero_json {[type]} -- [description]
	
	Returns:
		[dict] -- {'小乔':106,...}
	"""
	cname_ename = {}
	for hero in hero_json:
		cname_ename[hero['cname']] = hero['ename']
		return cname_ename
def hero_skill_urls(cname_ename,hero_skill_root_url):
	"""[summary]
	
	Get the urls corresponding to each hero
	
	Arguments:
		cname_ename {[dict]} -- {'小乔':109,...}
	Return:
		{'小乔':['url1','url2','url3'],...}
	"""
	hero_skill_urls = {}
	for item in cname_ename.items():
		hero_id = item[1]
		hero_skill_url1 = hero_skill_root_url + str(hero_id)+'/'+str(100*hero_id)+'.png'
		hero_skill_url2 = hero_skill_root_url + str(hero_id)+'/'+str(100*hero_id+10)+'.png'
		hero_skill_url3 = hero_skill_root_url + str(hero_id)+'/'+str(100*hero_id+20)+'.png'
		hero_skill_url4 = hero_skill_root_url + str(hero_id)+'/'+str(100*hero_id+30)+'.png'
		hero_skill_urls[item[0]] = [hero_skill_url1,hero_skill_url2,hero_skill_url3,hero_skill_url4]
	return hero_skill_urls
def get_cname_url(cname_ename,hero_skill_base_url):
	"""	
	Arguments:
	Return:
		{'小乔':url,...}
	"""
	cname_url = {}
	for item in cname_ename.items():
		num = item[1]
		cname_url[item[0]] = hero_skill_base_url + str(num) + '.shtml'
	return cname_url

def get_hero_skill_content(cname_url):
	"""
	Arguments:

	Return:
	{'小乔':['魅惑|大力|大大','魅惑描述','大力描述'],...}
	"""
	#fetch the url for every hero
	hero_skill = {}
	skill = []
	desc = []
	print("==========This is cname url ========")
	print(cname_url)
	for item in cname_url.items():
		url = item[1]
		#print("==========This is url in cname url========")
		print(url)
		res = requests.get(url)3
		soup = BeautifulSoup(res.text,'lxml')
		for skill in soup.select('.show-list'):
			skill.append(skill.select('.skill-name').b.string)
			desc.append(skill.select('.skill-desc').p)
			#skill = ['魅惑','大力']
			#desc = ['很厉害','不得了']
		desc.insert(0,"|".join(skill))
		hero_skill[item[0]] = desc
	return hero_skill
def write_skill_content(hero_skill,skill_base_dir):
	for name,desc in hero_skill.items():
		name_list = desc[0].split('|')
		if mkdir(skill_base_dir+name):
			os.chdir(skill_base_dir+name)
			for i in range(len(name_list)):
				file_name = name_list[i]
				with open(file_name,'wb') as f:
					f.write(desc[i+1])

def get_skillpng(hero_skill_urls):
	"""	
	[fetch the image from the net]
	
	Arguments:
		hero_skill_urls {[type]} -- {'小乔':['url1','url2','url3'],...}
	Return:
		None
	"""
	for name,urls in hero_skill_urls:
		if mkdir(skill_base_dir+name):
			os.chdir(skill_base_dir+name) #now we are in '小乔' folder,I want to create a folder contains four pngs
			for url in urls:
				i = 0
				file_name = name + str(i) +'.png'
				print("=====This is url I will get======")
				print(url[i])
				r = requests.get(url[i])
				i += 1
				with open(file_name,'wb'):
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
	hero_json = requests.get(hero_list_url).json()
	cname_ename = get_ename(hero_json)
	hero_skill_urls = hero_skill_urls(cname_ename,hero_skill_root_url)
	get_skillpng(hero_skill_urls)
	cname_url = get_cname_url(cname_ename,hero_skill_base_url)
	hero_skill = get_hero_skill_content(cname_url)
	write_skill_content(hero_skill,skill_base_dir)


