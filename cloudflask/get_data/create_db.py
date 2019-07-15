import sqlite3

DB_FILE = '/data/posture.db'

def create_db(db_file):
    '''Creates or connects to an SQLite database and creates tables specified
    in the config.yaml file.'''
    try:
        #Connect to SQLite
        c = sqlite3.connect(db_file)
        print('\nConnected to %s using SQLite Version %s...\n'%(db_file,
            sqlite3.version))
    except sqlite3.Error as e:
        print("Connection to %s failed:"%db_file)
        print(e)
        quit()
    with open('config.yaml', 'rt') as f:
        config = yaml.load(f)
    for table in config.keys():
        try:
            #Create schema
            sql = "CREATE TABLE %s("%table
            sql += ', '.join(config[keys])
            sql += " PRIMARY KEY (image_id);")
            c.execute(sql)
        except sqlite3.Error as e:
            #If data tables already exist and throw error, ends process.
            print("\nTable %s already populated."%table)
            c.close()

create_db(DB_FILE)
