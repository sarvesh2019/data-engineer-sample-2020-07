"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""

from src.some_storage_library import SomeStorageLibrary
if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    someStorageLibrary=SomeStorageLibrary()
    with open('data/SOURCE/SOURCECOLUMNS.txt') as sourcecol:
        cols = [col.rstrip().split('|') for col in sourcecol]
    with open('data/SOURCE/SOURCEDATA.txt') as datafile:
        data = [row.rstrip().replace('|',',') for row in datafile]
    cols = sorted(cols, key=lambda col: int(col[0]))
    data.insert(0, ','.join([col[1] for col in cols]))
    with open('RESULT.csv', 'w+') as f:     
        for row in data:
            f.write('%s\n' %row)
        f.close()
    someStorageLibrary.load_csv("RESULT.csv")
