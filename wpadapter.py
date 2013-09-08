# wpadapter.py inserts posts from a csv file to a wordpress blog

import datetime , xmlrpclib , csv

# STEP 1 create a wp insert function

def insert_wp_post(title="Title was not passed !",content="Content was not passed !"):
    wp_url = "http:// <INSERT YOUR WORDPRESS URL HERE >/xmlrpc.php"
    wp_username = "wordpress username"
    wp_password = "wordpress password"
    wp_blogid = ""
    postype=""
    status_draft = 0
    status_published = 1
    server = xmlrpclib.ServerProxy(wp_url)
    date_created = xmlrpclib.DateTime(datetime.datetime.strptime("2012-10-10 21:08", "%Y-%m-%d %H:%M"))
    categories = ["unsorted"]
    tags = ["sometag", "othertag"]
    data = {'post_type':postype ,'title': title, 'description': content,'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}
    post_id =server.wp.newPost(wp_blogid,wp_username,wp_password,data,status_published) 

# STEP 2 open csv file and row by row call insert function
reader=csv.reader(open("test.csv","rb"))
for row in reader:
    insert_wp_post(row[1],row[2])