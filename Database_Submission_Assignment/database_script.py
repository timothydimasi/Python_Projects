import sqlite3

# creates the database file in this directory - if it doesn't exist already -
# and establishes a connection 
conn = sqlite3.connect('database.db')

# while connection is open, create cursor object and execute the SQL code
# SQL code creates a table with two columns - if it hasn't already been done
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT \
        )")
    conn.commit()
conn.close()

# the tuple that was provided to us in the instructions
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


# opening the connection to the db file again
conn = sqlite3.connect('database.db')
with conn:
    cur = conn.cursor()
    # now we are creating the for loop and conditional statement to iterate through the tuple
    for file in fileList:
        if file.endswith(".txt"):
            print(file)
            # file is the variable with local scope that contains the .txt file names
            cur.execute("INSERT INTO tbl_files(col_name) VALUES (?)", (file,))
    conn.commit()
conn.close()

    
    
        

