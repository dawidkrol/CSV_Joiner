import sys
from Helpers.CSVJoiner import CSVJoiner, CSV_model, JoinType
from Helpers.CSVReader import CSVReader

if __name__ == '__main__':
    file_path = sys.argv[1]
    file_path2 = sys.argv[2]
    column_name = sys.argv[3]
    join_type = sys.argv[4]

    r = CSVReader()
    data = CSV_model([], [])
    data2 = CSV_model([], [])
    r.ReadFromFile(file_path, data)
    r.ReadFromFile(file_path2, data2)

    joiner = CSVJoiner()
    output = CSV_model([], [])
    match join_type:
        case 'left':
            output = joiner.join(column_name, data, data2, JoinType.left.value)
        case 'right':
            output = joiner.join(column_name, data, data2, JoinType.right.value)
        case 'inner':
            output = joiner.join(column_name, data, data2, JoinType.inner.value)

    print(output.header)
    print(output.data)