import os
import git
import json
import pandas as pd
import mysql.connector
try:
    git.Repo.clone_from("https://github.com/PhonePe/pulse.git", 'PhonePe_Data')
except:
    pass

#agg_insurance
path1="C:/Users/91733/OneDrive/Desktop/PhonePe/pulse/data/aggregated/insurance/country/india/state/"
ins_state_list=os.listdir(path1)

cols={'State':[], 'Year':[], 'Quarter':[], 'Transaction_type':[],'Transaction_count':[], 'Transaction_amount':[]}
for state in ins_state_list:
    cur_year=path1+state+'/'
    ins_year_list=os.listdir(cur_year)

    for year in ins_year_list:
        cur_quarter=cur_year+year+'/'
        ins_quarter_list=os.listdir(cur_quarter)
        
        for file in ins_quarter_list:
            cur_file=cur_quarter+file
            data=open(cur_file,'r')

            File1=json.load(data)

            try:
                for i in File1['data']['transactionData']:
                    name=i['name']
                    count=i['paymentInstruments'][0]['count']
                    amt=i['paymentInstruments'][0]['amount']
                    cols['Transaction_type'].append(name)
                    cols['State'].append(state)
                    cols['Year'].append(year)
                    cols['Transaction_count'].append(count)
                    cols['Transaction_amount'].append(amt)
                    cols['Quarter'].append(int(file.strip('.json')))
            except:
                pass
                
agg_insurance=pd.DataFrame(cols)
agg_insurance['State'] = agg_insurance['State'].str.replace('-', ' ')  
agg_insurance['State'] = agg_insurance['State'].str.title()     
agg_insurance['State'] = agg_insurance['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu') 
agg_insurance['State'] = agg_insurance['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')    

#agg_transaction

path2="C:/Users/91733/OneDrive/Desktop/PhonePe/pulse/data/aggregated/transaction/country/india/state/"
trans_state_list=os.listdir(path2)

cols={'State':[], 'Year':[], 'Quarter':[], 'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for state in trans_state_list:
    cur_state=path2+state+"/"
    trans_year_list=os.listdir(cur_state)
    
    for year in trans_year_list:
        cur_year=cur_state+year+"/"
        trans_quarter_list=os.listdir(cur_year)
        
        for file in trans_quarter_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            File2=json.load(data)
            
            for i in File2['data']['transactionData']:
                name=i['name']
                count=i['paymentInstruments'][0]['count']
                amount=i['paymentInstruments'][0]['amount']
                cols['Transaction_type'].append(name)
                cols['Transaction_count'].append(count)
                cols['Transaction_amount'].append(amount)
                cols['State'].append(state)
                cols['Year'].append(year)
                cols['Quarter'].append(int(file.strip(".json")))
agg_transaction=pd.DataFrame(cols)
agg_transaction['State'] = agg_transaction['State'].str.replace('-', ' ')  
agg_transaction['State'] = agg_transaction['State'].str.title()     
agg_transaction['State'] = agg_transaction['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu') 
agg_transaction['State'] = agg_transaction['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')    

#agg_user
path3="C:/Users/91733/OneDrive/Desktop/PhonePe/pulse/data/aggregated/user/country/india/state/"
user_state_list=os.listdir(path3)

cols={'State':[], 'Year':[], 'Quarter':[], 'Brands':[], 'Transaction_count':[], 'Percentage':[]}
for state in user_state_list:
    cur_state=path3+state+"/"
    user_year_list=os.listdir(cur_state)
    
    for year in user_year_list:
        cur_year=cur_state+year+"/"
        user_file_list=os.listdir(cur_year)
        
        for file in user_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            File3=json.load(data)

            try:            
                for i in File3['data']['usersByDevice']:
                    brand=i['brand']
                    count=i['count']
                    percent=i['percentage']
                    cols['Brands'].append(brand)
                    cols['Transaction_count'].append(count)
                    cols['Percentage'].append(percent)
                    cols['State'].append(state)
                    cols['Year'].append(year)
                    cols['Quarter'].append(int(file.strip(".json")))
            except:
                pass

agg_user=pd.DataFrame(cols)  
agg_user['State'] = agg_user['State'].str.replace('-', ' ')  
agg_user['State'] = agg_user['State'].str.title()     
agg_user['State'] = agg_user['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu') 
agg_user['State'] = agg_user['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')

#map_insurance
path4="C:/Users/91733/OneDrive/Desktop/PhonePe/pulse/data/map/insurance/hover/country/india/state/"
map_ins_list=os.listdir(path4)

cols={'State':[], 'District':[], 'Year':[], 'Quarter':[], 'Transaction_count':[], 'Transaction_amount':[]}
for state in map_ins_list:
    cur_state=path4+state+"/"
    map_year_list=os.listdir(cur_state)
    
    for year in map_year_list:
        cur_year=cur_state+year+"/"
        map_file_list=os.listdir(cur_year)
        
        for file in map_file_list:
            cur_file=cur_year+file
            data=open(cur_file, 'r')

            File4=json.load(data) 

        
            for i in File4['data']['hoverDataList']:
                name=i['name']
                count=i['metric'][0]['count']
                amt=i['metric'][0]['amount']
                cols['District'].append(name)
                cols['Transaction_count'].append(count)
                cols['Transaction_amount'].append(amt)
                cols['State'].append(state)
                cols['Year'].append(year)
                cols['Quarter'].append(int(file.strip(".json")))
            
map_insurance=pd.DataFrame(cols)
map_insurance['State'] = map_insurance['State'].str.replace('-', ' ')  
map_insurance['State'] = map_insurance['State'].str.title()     
map_insurance['State'] = map_insurance['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu') 
map_insurance['State'] = map_insurance['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')

#map_transaction
path5="C:/Users/91733/OneDrive/Desktop/PhonePe/pulse/data/map/transaction/hover/country/india/state/"
map_trans_list=os.listdir(path5)

cols={'State':[], 'District':[], 'Year':[], 'Quarter':[], 'Transaction_count':[], 'Transaction_amount':[]}
for state in map_trans_list:
    cur_state=path5+state+"/"
    map_year_list=os.listdir(cur_state)
    
    for year in map_year_list:
        cur_year=cur_state+year+"/"
        map_file_list=os.listdir(cur_year)
        
        for file in map_file_list:
            cur_file=cur_year+file
            data=open(cur_file, 'r')

            File5=json.load(data) 

        
            for i in File5['data']['hoverDataList']:
                name=i['name']
                count=i['metric'][0]['count']
                amt=i['metric'][0]['amount']
                cols['District'].append(name)
                cols['Transaction_count'].append(count)
                cols['Transaction_amount'].append(amt)
                cols['State'].append(state)
                cols['Year'].append(year)
                cols['Quarter'].append(int(file.strip(".json")))
            
map_transaction=pd.DataFrame(cols)            
map_transaction['State'] = map_transaction['State'].str.replace('-', ' ')  
map_transaction['State'] = map_transaction['State'].str.title()     
map_transaction['State'] = map_transaction['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu') 
map_transaction['State'] = map_transaction['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')

# map_user
path6="C:/Users/91733/OneDrive/Desktop/PhonePe/pulse/data/map/user/hover/country/india/state/"
map_user_list=os.listdir(path6)

cols={'State':[], 'District':[], 'Year':[], 'Quarter':[], 'registeredUsers':[], 'appOpens':[]}
for state in map_user_list:
    cur_state=path6+state+"/"
    map_year_list=os.listdir(cur_state)
    
    for year in map_year_list:
        cur_year=cur_state+year+"/"
        map_file_list=os.listdir(cur_year)
        
        for file in map_file_list:
            cur_file=cur_year+file
            data=open(cur_file, 'r')

            File6=json.load(data) 
                
            for i in File6['data']['hoverData'].items():
                dist=i[0]
                reg_user=i[1]['registeredUsers']
                app_open=i[1]['appOpens']
                cols['District'].append(dist)
                cols['registeredUsers'].append(reg_user)
                cols['appOpens'].append(app_open)
                cols['State'].append(state)
                cols['Year'].append(year)
                cols['Quarter'].append(int(file.strip(".json")))
            
map_user=pd.DataFrame(cols) 
map_user['State'] = map_user['State'].str.replace('-', ' ')  
map_user['State'] = map_user['State'].str.title()     
map_user['State'] = map_user['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu') 
map_user['State'] = map_user['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')   

# top_insurance
path7="C:/Users/91733/OneDrive/Desktop/PhonePe/pulse/data/top/insurance/country/india/state/"
ins_state_list=os.listdir(path7)
cols={'State':[], 'Year':[], 'Quarter':[], 'Transaction_count':[], 'Transaction_amount':[], 'Pincode':[]}

for state in ins_state_list:
    cur_state=path7+state+'/'
    ins_year_list=os.listdir(cur_state)

    for year in ins_year_list:
        cur_year=cur_state+year+'/'
        ins_file_list=os.listdir(cur_year)

        for file in ins_file_list:
            cur_file=cur_year+file
            data=open(cur_file,'r')

            File7=json.load(data)
            for i in File7['data']['pincodes']:
                entityname=i['entityName']
                count=i['metric']['count']
                amount=i['metric']['amount']
                cols['Pincode'].append(entityname)
                cols['Transaction_count'].append(count)
                cols['Transaction_amount'].append(amount)
                cols['State'].append(state)
                cols['Year'].append(year)
                cols['Quarter'].append(int(file.strip('.json')))
top_insurance=pd.DataFrame(cols)
top_insurance['State'] = top_insurance['State'].str.replace('-', ' ')  
top_insurance['State'] = top_insurance['State'].str.title()     
top_insurance['State'] = top_insurance['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu') 
top_insurance['State'] = top_insurance['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')

# top_transaction
path8="C:/Users/91733/OneDrive/Desktop/PhonePe/pulse/data/top/transaction/country/india/state/"
trans_state_list=os.listdir(path8)

cols={'State':[], 'Year':[],'Quarter':[], 'Pincode':[], 'Transaction_amount':[], 'Transaction_count':[]}

for state in trans_state_list:
    cur_state=path8+state+"/"
    trans_year_list=os.listdir(cur_state)

    for year in trans_year_list:
        cur_year=cur_state+year+"/"
        trans_file_list=os.listdir(cur_year)

        for file in trans_file_list:
            cur_file=cur_year+file
            data=open(cur_file,'r')
            

            File8=json.load(data)
            for i in File8['data']['pincodes']:
                entityname=i['entityName']
                count=i['metric']['count']
                amount=i['metric']['amount']
                cols['Pincode'].append(entityname)
                cols['Transaction_count'].append(count)
                cols['Transaction_amount'].append(amount)
                cols['State'].append(state)
                cols['Year'].append(year)
                cols['Quarter'].append(int(file.strip('.json')))
top_transaction=pd.DataFrame(cols)
top_transaction['State'] = top_transaction['State'].str.replace('-', ' ')  
top_transaction['State'] = top_transaction['State'].str.title()     
top_transaction['State'] = top_transaction['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu') 
top_transaction['State'] = top_transaction['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')

# top_users
path9="C:/Users/91733/OneDrive/Desktop/PhonePe/pulse/data/top/user/country/india/state/"
user_state_list=os.listdir(path9)

cols={'State':[], 'Year':[],'Quarter':[], 'Pincode':[], 'registeredUsers':[]}

for state in user_state_list:
    cur_state=path9+state+"/"
    user_year_list=os.listdir(cur_state)

    for year in user_year_list:
        cur_year=cur_state+year+"/"
        user_file_list=os.listdir(cur_year)

        for file in user_file_list:
            cur_file=cur_year+file
            data=open(cur_file,'r')
            

            File8=json.load(data)
            for i in File8['data']['pincodes']:
                entityname=i['name']
                reg_user=i['registeredUsers']
                cols['Pincode'].append(entityname)
                cols['registeredUsers'].append(reg_user)
                cols['State'].append(state)
                cols['Year'].append(year)
                cols['Quarter'].append(int(file.strip('.json')))
top_user=pd.DataFrame(cols)
top_user['State'] = top_user['State'].str.replace('-', ' ')  
top_user['State'] = top_user['State'].str.title()     
top_user['State'] = top_user['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu') 
top_user['State'] = top_user['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')

#MySQL connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Kimch!811',
    database='PhonePe_Data'
)
cursor = connection.cursor()
#aggregated_insurance_table
create_table_1='''CREATE TABLE if not exists aggregated_insurance(State varchar(255),
                                                    Year int,
                                                    Quarter varchar(2),
                                                    Transaction_type varchar(255),
                                                    Transaction_count bigint,
                                                    Transaction_amount float
                                                    )'''
cursor.execute(create_table_1)
connection.commit()
insert_table_1 = '''
        INSERT INTO aggregated_insurance (State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

data=agg_insurance.values.tolist()
cursor.executemany(insert_table_1, data)
connection.commit()

#aggregated_transaction_table
create_table_2='''CREATE TABLE if not exists aggregated_transaction(State varchar(255),
                                                    Year int,
                                                    Quarter varchar(2),
                                                    Transaction_type varchar(255),
                                                    Transaction_count bigint,
                                                    Transaction_amount float
                                                    )'''
cursor.execute(create_table_2)
connection.commit()
insert_table_2 = '''
    INSERT INTO aggregated_transaction (State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount)
    VALUES (%s, %s, %s, %s, %s, %s)
'''

data=agg_transaction.values.tolist()
cursor.executemany(insert_table_2, data)
connection.commit()

#aggregated_user_table
create_table_3='''CREATE TABLE if not exists aggregated_user(State varchar(255),
                                                    Year int,
                                                    Quarter varchar(2),
                                                    Brands varchar(255),
                                                    User_count bigint,
                                                    User_Percentage float
                                                    )'''
cursor.execute(create_table_3)
connection.commit()
insert_table_3 = '''
        INSERT INTO aggregated_user (State, Year, Quarter, Brands, User_count, User_Percentage)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

data=agg_user.values.tolist()
cursor.executemany(insert_table_3, data)
connection.commit()

#map_insurance_table
create_table_4='''CREATE TABLE if not exists map_insurance(State varchar(255),
                                                    Year int,
                                                    Quarter varchar(2),
                                                    District varchar(255),
                                                    Transaction_count bigint,
                                                    Transaction_amount float
                                                    )'''
cursor.execute(create_table_4)
connection.commit()
insert_table_4 = '''
        INSERT INTO map_insurance (State, District, Year, Quarter,  Transaction_count, Transaction_amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

data=map_insurance.values.tolist()
cursor.executemany(insert_table_4, data)
connection.commit()

#map_transaction_table
create_table_5='''CREATE TABLE if not exists map_transaction(State varchar(255),
                                                    Year int,
                                                    Quarter varchar(2),
                                                    District varchar(255),
                                                    Transaction_count bigint,
                                                    Transaction_amount float
                                                    )'''
cursor.execute(create_table_5)
connection.commit()
insert_table_5 = '''
        INSERT INTO map_transaction (State, District, Year, Quarter,  Transaction_count, Transaction_amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

data=map_transaction.values.tolist()
cursor.executemany(insert_table_5, data)
connection.commit()

#map_user_table
create_table_6='''CREATE TABLE if not exists map_user(State varchar(255),
                                                    Year int,
                                                    Quarter varchar(2),
                                                    District varchar(255),
                                                    registeredUsers bigint,
                                                    appOpens bigint
                                                    )'''
cursor.execute(create_table_6)
connection.commit()
insert_table_6 = '''
        INSERT INTO map_user (State, District, Year, Quarter,  registeredUsers, appOpens)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

data=map_user.values.tolist()
cursor.executemany(insert_table_6, data)
connection.commit()
#top_insurance_table
create_table_7='''CREATE TABLE if not exists top_insurance(State varchar(255),
                                                    Year int,
                                                    Quarter varchar(2),
                                                    Transaction_count bigint,
                                                    Transaction_amount float,
                                                    Pincode varchar(255)
                                                    )'''
cursor.execute(create_table_7)
connection.commit()
insert_table_7 = '''
        INSERT INTO top_insurance (State, Year, Quarter,  Transaction_count, Transaction_amount, Pincode)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

data=top_insurance.values.tolist()
cursor.executemany(insert_table_7, data)
connection.commit()

#top_transaction_table
create_table_8='''CREATE TABLE if not exists top_transaction(State varchar(255),
                                                    Year int,
                                                    Quarter varchar(2),
                                                    Transaction_count bigint,
                                                    Transaction_amount float,
                                                    Pincode varchar(255)
                                                    )'''
cursor.execute(create_table_8)
connection.commit()
insert_table_8 = '''
        INSERT INTO top_transaction (State, Year, Quarter, Pincode, Transaction_count, Transaction_amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

data=top_transaction.values.tolist()
cursor.executemany(insert_table_8, data)
connection.commit()

#top_user_table
create_table_9='''CREATE TABLE if not exists top_user(State varchar(255),
                                                    Year int,
                                                    Quarter varchar(2),
                                                    Pincode varchar(255),
                                                    registeredUsers bigint
                                                    )'''
cursor.execute(create_table_9)
connection.commit()
insert_table_9 = '''
        INSERT INTO top_user (State, Year, Quarter, Pincode, registeredUsers)
        VALUES (%s, %s, %s, %s, %s)
    '''

data=top_user.values.tolist()
cursor.executemany(insert_table_9, data)
connection.commit()

  