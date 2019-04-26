import database

def auth(account, password):
    print(account)
    info = database.get_info('user', 'password', account)
    print(info)
    if password:
        if password == info:
            return database.get_info('user', 'id', account)
        else:
            return 'err2'
    else:
        return 'err1'
