# run_q(q, args, fetch=False): run query
# q: query, args:usually None, fetch: whether to get result
# return query result in json format

# get_similar(table, id): get similar item/user for CF
# table: 'user_sim' or 'item_sim', id: int
# return a list of similar idea

# get_info(table, column, idx): get item/user info given name/id
# table: 'user' or 'item', column: 'name', 'id' or 'password', idx: str of name or int id
# return str of name/password or int id

# get_similar_item(name): get similar item for content-based
# name: str of item name
# return a list of similar itme name

database_address = '35.245.49.151'

import pymysql
import json

cnx = pymysql.connect(host= database_address,
                              user='ha',
                              password='password',
                              db='pipeline',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)

def run_q(q, args, fetch=False):
    cursor = cnx.cursor()
    cursor.execute(q, args)
    if fetch:
        result = cursor.fetchall()
    else:
        result = None
    cnx.commit()
    return result

def get_similar(id):
    q = "select * from user_sim where sim0=" + str(id)
    r = run_q(q, None, True)
    if r:
        return list(r[0].values())[:-1]

def get_best(id):
    q = "select * from favorit where id=" + str(id)
    r = run_q(q, None, True)
    res = [k for k in list(r[0].values())[:-1] if k!=0]
    return res

def get_info(table, column, idx):
    if column == 'name':
        index = 'id'
    else:
        index = 'name'
    q = "select * from " + table + " where " + index + "='" + str(idx) + "'"
    result = run_q(q, None, True)
    if result:
        return result[0][column]

def get_similar_item(name):
    id = get_info('item', 'id', name)
    q = "select * from `content-based` where id0=" + str(id)
    r = run_q(q, None, True)
    print(r)
    res = []
    for i in list(r[0].values())[:-1]:
        res.append(get_info('item', 'name', i))

    print(res)
    return res
