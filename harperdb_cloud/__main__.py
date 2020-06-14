#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import harperdb_cloud

if __name__ == "__main__":
    harper = harperdb_cloud.HarperDbCloud(sys.argv[1:], instance_url="https://sdktest-xonshiz.harperdbcloud.com/", username="test_user", password="GuessMe24!")
    # result = harper.create_dev_schema(instance_name="newOne")
    # result = harper.create_table(schema_name="newOne", table_name="doggo")
    # result = harper.insert_record(schema_name="newOne", table_name="doggo", records=[{
    #     "name": "Mark Senior Senior",
    #     "work": "BORK BORK!"
    # }])
    # result = harper.insert_via_csv(schema_name="newOne", table_name="doggo", file_path='/Users/xonshiz/Documents/Book1.csv')
    # result = harper.run_sql_command(sql_command="UPDATE newOne.doggo SET name = 'Mark Jr.' WHERE name = 'Mark'")
    # result = harper.update_record(schema_name="newOne", table_name="doggo", records=[{
    #     "id": "1f6c25f7-793b-4436-bd0c-5aa86ee86d22",
    #     "name": "Mark Senior Senior",
    #     "work": "BORK BORK BURK BURK BURK!"
    # }])
    # print(result)
