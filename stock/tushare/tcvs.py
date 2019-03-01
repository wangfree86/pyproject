import csv
with open('159928.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    aList = [123, 'xyz', 'zara', 'abc'];

    for row in f_csv:
        row1 = row[7:8]
        aList.append(row[7:8]);
        print(row1)
    print(aList)