import sys
from config import DB_DETAILS
from util import get_tables
def main():
    """"program takes at least one argument"""
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    tables = get_tables('tables_list')
    for table in tables['table_name']:
        print(db_details)


if __name__ == '__main__':
    main()