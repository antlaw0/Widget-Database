import sqlite3

sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name = 'widgets'	# name of the table to be created
id_column='id_column'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table 
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name, nf=id_column, ft='INTEGER'))

#add next column
new_column='name'
column_type='TEXT'
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column, ct=column_type))

#add next column
new_column='color'
column_type='TEXT'
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column, ct=column_type))

#add next column
new_column='size'
column_type='TEXT'
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column, ct=column_type))

#add next column
new_column='shape'
column_type='TEXT'
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column, ct=column_type))

		
#add next column
new_column='quantity'
column_type='INTEGER'
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column, ct=column_type))

		
		
print("Database and table created")

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()