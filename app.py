import sys
from config import DB_DETAILS

from util import get_tables

def main():
    """Program takes at least one argument"""
    env = sys.argv[1]
    db_details = DB_DETAILS[env]

    # Keeping both functionalities
    print(db_details)  # From the other branch
    tables = get_tables('tables_list')  # From HEAD branch
    for table in tables['table_name']:
        print(f"Processing table: {table}")

if __name__ == '__main__':
    main()
