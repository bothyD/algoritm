import pandas as pd

def print_mas(matr):
    for el in matr:
        print(el)
    print()
def edit_table(table, row, column):
    for i in range(column-1):
        table.rename(columns={i: 'B'+str(i+1)}, inplace=True)
    table.rename(columns={column-1: 'Запасы'}, inplace=True)
    for i in range(row-1):
        table.rename(index={i:' A'+str(i+1)}, inplace=True)
    table.rename(index={row-1:' Потребности'}, inplace=True)
    print(table)

def main():
    with open('matrix_lab3.txt') as f:
        matrix = [list(map(str, row.split())) for row in f.readlines()]
    print_mas(matrix)
    row = len(matrix)
    column = len(matrix[0])
    df = pd.DataFrame.from_records(matrix)
    edit_table(df, row, column)

if __name__ == "__main__":
    main()