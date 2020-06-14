import harperdb_cloud

harper = harperdb_cloud.HarperDbCloud(instance_url="https://sdktest-xonshiz.harperdbcloud.com/", username="test_user",
                                      password="GuessMe24!")

schema_result = harper.create_dev_schema(instance_name="PythonDevSchema")

create_table_result = harper.create_table(schema_name="PythonDevSchema", table_name="doggo")

insert_record_result = harper.insert_record(schema_name="PythonDevSchema", table_name="doggo", records=[{
    "name": "Mark",
    "work": "BORK BORK!"
}])

update_result_result = harper.update_record(schema_name="PythonDevSchema", table_name="doggo", records=[{
    "id": "",
    "name": "Mark Senior Senior",
    "work": "BORK BORK BURK BURK BURK!"
}])

run_sql_command_result = harper.run_sql_command(sql_command="SELECT * FROM PythonDevSchema.doggo")

insert_via_csv_result = harper.insert_via_csv(schema_name="PythonDevSchema", table_name="doggo",
                                              file_path='/Users/xonshiz/Documents/Book1.csv')
