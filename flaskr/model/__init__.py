import pymysql
def getConnection():
    return pymysql.connect(host='dgo.ojudge.in.th', user='dbsec33', password='123456', db='Hospital', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)