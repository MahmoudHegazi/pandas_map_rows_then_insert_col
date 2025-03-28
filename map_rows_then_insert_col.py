import pandas as pd


"""
it take 2 excel files add row for map and return excel file updated:
print(map_rows_then_insert_col(updater, mapper, ['saymbols', 'saymbols'], 'price'))
"""

# order_col



# this topest way to map and insert in performacne easy call (not change updater order get data for it)
def map_rows_then_insert_columns(updater, mapper, order_cols=[], target_cols=[]):
    updater = updater.copy()
    mapper = mapper.copy()
    np_nan = float('NaN')
    new_columns = {}
    mappers = {}

    if isinstance(updater, pd.DataFrame) and isinstance(mapper, pd.DataFrame) and isinstance(order_cols, list) and isinstance(target_cols, list) and len(order_cols) == 2 and order_cols[0] in updater.columns and order_cols[1] in mapper.columns and all([True if target_col in mapper.columns else False for target_col in target_cols]):
        
        for index, row in updater.iterrows():
            # here get update value by index
            col_val_in_updater = updater.loc[index, order_cols[0]]
            
            # based on goten value by index in the mapper will get the same value 
            target_row_in_mapper = mapper.query(f"{order_cols[1]} == @col_val_in_updater")

            map_index = mappers[order_cols[0]] if order_cols[0] in mappers else -1
            # mappers[order_cols[0]]
            
            if not target_row_in_mapper.empty:
                target_val = None
                if target_row_in_mapper.shape[0] > (map_index+1):
                    # dynamic if ex 3 or 1 abb and mapper 3 or more or 1 abb as updater it continue 0to0 , 1to1, 2to2,etc
                    mappers[order_cols[0]] = map_index+1
                elif target_row_in_mapper.shape[0] > (map_index):
                    # dynamic continue from last in map df ex update 3 abb and mapper 2 abb it map 0to0 1to1 2to1 duplicate 1
                    mappers[order_cols[0]] = map_index 
                else:
                    # this handle as i said map_index -1 so this handle the default 0 case first for any unique col
                    mappers[order_cols[0]] = 0
                
                
                for target_col in target_cols:
                    if target_col not in new_columns:
                        new_columns[target_col] = []
                    
                    target_val = target_row_in_mapper.iloc[mappers[order_cols[0]]][target_col]
                    new_columns[target_col].append(target_val)
                #print(mappers[order_col], 'hi', '-'*30)
            else:
                
                for target_col in target_cols:
                    if target_col not in new_columns:
                        new_columns[target_col] = []
                    new_columns[target_col].append(np_nan)
        # this can called in pandas the documentFragment invention and performance outsiden loop benfit and also (add lol typical as fragment the data to list not real excel or even real data frame so it hidden dataframe same as fragment but for python this part u need care all that for this
        
        for target_col, new_column in new_columns.items():
            updater[target_col] = new_column
        return updater
    return None


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

