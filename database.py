import sqlite3

def addDataToDatabase(subscription, counter):
    conn = sqlite3.connect('D:\PythonTasks\instagram_get_groups\subscriptions.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO groups (subscription, counter) VALUES (?,?)", (subscription, counter))
    conn.commit()
    conn.close()
