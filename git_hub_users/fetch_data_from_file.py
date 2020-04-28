import requests # to get the data from site/web
import json
#response = requests.get('https://api.github.com/repos/git/git/contributors')
#print(response.json())
from git_hub_users.read_github_users import UserInfo


'''
 create table userinfo (
    -> id int,
    -> login varchar(255),
    -> node_id varchar(255),
    -> avatar_url varchar(255),
    -> gravatar_id varchar(255),
    -> url varchar(255),
    -> html_url varchar(255),
    -> followers_url varchar(255),
    -> following_url varchar(255),
    -> gists_url varchar(255),
    -> starred_url varchar(255),
    -> subscriptions_url varchar(255),
    -> organizations_url varchar(255),
    -> repos_url varchar(255),
    -> events_url varchar(255),
    -> received_events_url varchar(255),
    -> type varchar(255),
    -> site_admin varchar(255),
    -> contributions int,
    -> primary key(id)
    -> );

'''

users  = [UserInfo(**user) for user in json.load(open('C:\\Users\\Yogesh\\Desktop\\github.json'))]

for user in users:
    #print(user.__dict__)

    for user in users:
        #print(str(user.__dict__).replace('\'','\"'))
        print(str(user.__dict__).replace('\'','\"'))




#def mylogic(user):   #
#    return user.id


#users.sort(key=mylogic)
users.sort(key=lambda user : user.login)

#print(users)

import sys
sys.exit(0)
#print(users)
'''
def get_github_users_list():
    with open('C:\\Users\\Yogesh\\Desktop\\github.json') as file:
        #lines = file.read()
        #lines = file.readlines()
        userjson = json.load(file)
        print(len(userjson))
        listOfUsers = []
        for user in userjson:
            listOfUsers.append(UserInfo(**user))

        return listOfUsers


users  = get_github_users_list()
'''


#users.sort(key=mylogic,reverse=False)

#print(users)


INSERT_QUERY = '''insert into userinfo values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{})'''


import pymysql



def insert_users_into_db():
    conn = pymysql.connect('localhost', 'root', 'root', 'scpdb')
    for user in users:
        FINAL_INSERT_QUERY = INSERT_QUERY.format(user.id, user.login, user.node_id, user.avatar_url, user.gravatar_id,
                                           user.url, user.html_url, user.followers_url, user.following_url,
                                           user.gists_url, user.starred_url, user.subscriptions_url,
                                           user.organizations_url, user.repos_url, user.events_url,
                                           user.received_events_url, user.type, user.site_admin, user.contributions)
        channel = conn.cursor()
        channel.execute(FINAL_INSERT_QUERY)
    conn.commit()

def get_list_of_users_from_db():
    FETCH_INFO= 'select * from userinfo where id>=25000'
    conn = pymysql.connect('localhost', 'root', 'root', 'scpdb')
    channel = conn.cursor()
    channel.execute(FETCH_INFO)
    print('--here is the data from database -- ')
    records = channel.fetchall()
    return records

#insert_users_into_db()
import openpyxl
def insert_into_excel():
    workbook = openpyxl.Workbook()
    sheet = workbook.create_sheet('userdata')
    headers = list(users[0].__dict__.keys())
    headers[0],headers[1] = headers[1],headers[0]

    for index,item in enumerate(headers):
        sheet[chr(index+65)+'1']=item.upper()

    records = get_list_of_users_from_db()

    for row,record in enumerate(records):
        row+=2
        for index in range(0,19):
            sheet[chr(index+65)+str(row)]=record[index]

    workbook.save('E:\\temp\\DUMP\\gituser.xlsx')
    print('Headers Created as per records...!')

#insert_into_excel()
print('last tested.....')
print('last tested.....')
