import sqlite3
class Row(object):
	#keep track of unique ids
	id_index=1
	def insert(name, color, size, shape, quantity):
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
		c.execute("INSERT INTO {tn} ({cn}, {cn}, {cn}, {cn}, {cn}, {cn}) VALUES (id, name, color, size, shape, quantity)".\
		format(tn=table_name, cn='id_column', cn='name_column', cn='color_column', cn='size_column', cn='shape_column', cn='quantity_column'))
	
	
		conn.commit()
		conn.close()