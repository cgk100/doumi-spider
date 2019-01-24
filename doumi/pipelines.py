# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql 

def db_handle():
        conn=pymysql.connect(
            host='127.0.0.1',
            db='spider',
            user='root',
            passwd='168168',
            charset='utf8',
            use_unicode=False
        )
        return conn

class DoumiPipeline(object):

    def process_item(self, item, spider):
        dbobject=db_handle()
        cursor=dbobject.cursor()
        sql="insert into doumi(title,price,cpy_name,url,cate_tag,description,request_num,jiesuan,cpy_type,address,tag_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        try:
            cursor.execute(sql,
            (item['title'],item['price'],item['cpy_name'],item['url'],item['cate_tag'],
            item['description'],item['request_num'],item['jiesuan'],item['cpy_type'],item['address'],item['tag_type'])
            )
            dbobject.commit()
        except Exception,e:
            print e
            dbobject.rollback()

        return item