# pandas_map_rows_then_insert_col

it's dynamic based on your argment will detect your need and process excat same target and handle diffrent mode only the chaing arguments which is two dataframes df or two excel files so if  u have 2 fiels with relation id in both you can get any value and update the original file updater with this value by adding new columng this provide best performance for this task and way like documentFragment in html it handle large data with dummy hidden list not df or Series so it only make 1 dataframe update to insert full column even if it mapped 1kk rows so very good for this reuasble google

## update v2
will provide callback so you can control even new added value ex calcaute by other cols or other args while mapping or just return exact matched 1 col



![image](https://github.com/user-attachments/assets/50886713-be55-4185-88e5-86215c66054f)

![image](https://github.com/user-attachments/assets/bf7503b1-2587-4885-83cc-6115ae315966)

![image](https://github.com/user-attachments/assets/956df466-f982-41f2-9db1-3f3e87b59fd7)

![image](https://github.com/user-attachments/assets/29024ec4-0135-41cb-b6a2-25f5ab48da21)

![image](https://github.com/user-attachments/assets/b3024e6c-f88c-48aa-8b99-22e6317db20a)

### notice the relation key needed for mapping and it dynamic name ex in excel file name id and in excel 2 called product_id
![image](https://github.com/user-attachments/assets/bc60f490-4306-4148-832f-2ff447910cfe)


calls

```python

file_to_update = {
  "saymbols": ['ABB', 'ABB', 'ABB'],
  "duration": [50, 40, 45]
}

# this the file have the new columns need to mapped to updater file rows or df (use list not process serios within loop or full df repaint +reflow, update df with df[]) 
file_to_map = {
  "saymbols": ['ABB', 'ABB', 'ABB'],
  "price": [12.25, 1, 2],
  "ok":['dynamic', 'true', 'add_row']
}

#load data into a DataFrame object:
updater = pd.DataFrame(file_to_update)

# add as many as needed and even make later callback
mapper = pd.DataFrame(file_to_map)
print(map_rows_then_insert_columns(updater, mapper, ['saymbols', 'saymbols'], ['price', 'ok']))

print(updater)
print(mapper)

```


```
file_to_update = {
  "saymbols": ['ABB', 'ABB', 'ABB'],
  "duration": [50, 40, 45]
}

# this the file have the new columns need to mapped to updater file rows or df (use list not process serios within loop or full df repaint +reflow, update df with df[]) 
file_to_map = {
  "saymbols_2": ['ABB', 'CDD', 'c'],
  "price": [12.25, 1, 2]
}

#load data into a DataFrame object:
updater = pd.DataFrame(file_to_update)

mapper = pd.DataFrame(file_to_map)
print(map_rows_then_insert_col(updater, mapper, ['saymbols', 'saymbols_2'], ['price']))
```
