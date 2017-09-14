import sqlite3

def create_database():
	sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
	table_name = 'widgets'	# name of the table to be created
	id_column='id_column'

	# Connecting to the database file
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	# Creating a new SQLite table 
	c.execute('CREATE TABLE {tn} ({nf} {ft})'\
			.format(tn=table_name, nf=id_column, ft='INTEGER PRIMARY KEY AUTOINCREMENT'))

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


id_index=1
def insert(name, color, size, shape, quantity):
	global id_index
	sqlite_file = 'my_first_db.sqlite'
	table_name = 'widgets'
	id = id_index
	id_index+=1 #advance id counter
	name=name
	color=color
	size=size
	shape=shape
	quantity=quantity
		
	# Connecting to the database file
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	#adding record
	#c.execute("INSERT INTO {tn} ({cn}, {cn}, {cn}, {cn}, {cn}, {cn}) VALUES (id, name, color, size, shape, quantity)".\
	#format(tn=table_name, cn='id_column', cn='name_column', cn='color_column', cn='size_column', cn='shape_column', cn='quantity_column'))

	#take six supplied values and make new entry
	c.execute("INSERT INTO widgets VALUES (?, ?, ?, ?, ?, ?);", (id, name, color, size, shape, quantity))
	
	#commit the addition
	conn.commit()
	conn.close()




"""
Total rows: 1

Column Info:
ID, Name, Type, NotNull, DefaultVal, PrimaryKey
(0, 'id', 'TEXT', 0, None, 1)
(1, 'date', '', 0, None, 0)
(2, 'time', '', 0, None, 0)
(3, 'date_time', '', 0, None, 0)

Number of entries per column:
date: 1
date_time: 1
id: 1
time: 1
"""


def connect(sqlite_file):
    """ Make connection to an SQLite database file """
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return conn, c

def close(conn):
    """ Commit changes and close connection to the database """
    #conn.commit()
    conn.close()

def total_rows(cursor, table_name, print_out=False):
	""" Returns the total number of rows in the database """
	c.execute('SELECT COUNT(*) FROM {}'.format(table_name))
	count = c.fetchall()
	if print_out:
		print('\nTotal rows: {}'.format(count[0][0]))
	return count[0][0]

def table_col_info(cursor, table_name, print_out=False):
    """ 
       Returns a list of tuples with column informations:
      (id, name, type, notnull, default_value, primary_key)
    
    """
    c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = c.fetchall()
    
    if print_out:
        print("\nColumn Info:\nID, Name, Type, NotNull, DefaultVal, PrimaryKey")
        for col in info:
            print(col)
    return info

def values_in_col(cursor, table_name, print_out=True):
    """ Returns a dictionary with columns as keys and the number of not-null 
        entries as associated values.
    """
    c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = c.fetchall()
    col_dict = dict()
    for col in info:
        col_dict[col[1]] = 0
    for col in col_dict:
        c.execute('SELECT ({0}) FROM {1} WHERE {0} IS NOT NULL'.format(col, table_name))
        # In my case this approach resulted in a better performance than using COUNT
        number_rows = len(c.fetchall())
        col_dict[col] = number_rows
    if print_out:
        print("\nNumber of entries per column:")
        for i in col_dict.items():
            print('{}: {}'.format(i[0], i[1]))
    return col_dict


if __name__ == '__main__':

    sqlite_file = 'my_first_db.sqlite'
    table_name = 'widgets'

    conn, c = connect(sqlite_file)
    total_rows(c, table_name, print_out=True)
    table_col_info(c, table_name, print_out=True)
    values_in_col(c, table_name, print_out=True) # slow on large data bases
    
    close(conn)

	
	
def show_entries():
	conn = sqlite3.connect('my_first_db.sqlite')
	c = conn.cursor()

	c.execute("SELECT * FROM widgets")
	print(c.fetchall())

def show_query():
	name=input("Enter name of widget to search for: ")
	
	conn = sqlite3.connect('my_first_db.sqlite')
	c = conn.cursor()

	#c.execute('SELECT * FROM widgets WHERE {cn}={f}'.\
        #format(cn=column_name, f=query_value))
	print("\n Query result: ")
	c.execute("SELECT * FROM widgets WHERE name = ?;", (name,)) 
	print(c.fetchall())
	print("\n")
	
	
def add():
	name=input("Enter name of widget: ")
	color=input("Enter color of widget: ")
	size=input("Enter size of widget: ")
	shape=input("Enter shape of widget: ")
	quantity=input("Enter quantity of widget: ")
	insert(name, color, size, shape, quantity)
	
	
def delete():
	name=input("Enter name of widget to delete: ")
	sqlite_file = 'my_first_db.sqlite'
	table_name = 'widgets'
		
	# Connecting to the database file
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	c.execute("DELETE FROM widgets WHERE Name=?", (name,))
	print("Record with name "+name+" has been deleted.")
	
	#commit the addition
	conn.commit()
	
def update():
	thisLoop=True
	canContinue=False
	f=""
	while(thisLoop==True):
		name=input("Enter name of widget to update: ")
		print("Type the name of this widget's field you wish to update or exit to abort: ")
		print("name")
		print("color")
		print("size")
		print("shape")
		print("quantity")
		f=input("Enter your selection: ")
		if f=="color" or f=="name" or f=="size" or f=="shape" or f=="quantity":
			new_value=input("Enter new value for this field: ")
			canContinue=True
			break
		elif f=="exit":
			break
		else:
			print("Invallid selection.")
	
	if canContinue == True:
		sqlite_file = 'my_first_db.sqlite'
		table_name = 'widgets'
		
		# Connecting to the database file
		conn = sqlite3.connect(sqlite_file)
		c = conn.cursor()

		if f=="color":
			c.execute("UPDATE widgets SET color = ? WHERE name = ?", (new_value, name))
		elif f=="name":
			c.execute("UPDATE widgets SET name = ? WHERE name = ?", (new_value, name))
		elif f=="size":
			c.execute("UPDATE widgets SET size = ? WHERE name = ?", (new_value, name))
		elif f=="shape":
			c.execute("UPDATE widgets SET shape = ? WHERE name = ?", (new_value, name))
			print("F = "+f)
		else:
			c.execute("UPDATE widgets SET quantity = ? WHERE name = ?", (new_value, name))
	
	
	
	
	#commit the addition
	conn.commit()
	
	
loop=True
opt=0
while(loop==True):	
	print("Choose from the following list of commands: ")
	print("create")
	print("add")
	print("show")
	print("delete")
	print("update")
	print("query")
	print("exit")
	opt=input("Type a command: ")
	if opt == "exit":
		print("Goodbye")
		loop=False
	elif opt == "query":
		show_query()
	elif opt == "create":
		create_database()
	elif opt == "add":
		add()
	elif opt == "delete":
		delete()
	elif opt == "show":
		show_entries()
	elif opt == "update":
		update()
	else:
		print("Command not recognized.")
	
	
	
	