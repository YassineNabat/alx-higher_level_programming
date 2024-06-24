#!/usr/bin/env python3
"""
Lists all states with a name starting with N using SQLite
"""

import sqlite3

def main():
    
    conn = sqlite3.connect('path_to_your_database.db')
    cur = conn.cursor()

    cur.execute("""
                SELECT * FROM states
                WHERE name COLLATE nocase LIKE 'N%';
                """)                 

    states = cur.fetchall()

    for state in states:
        print(state)

    if __name__ == "__main__":
        main()
