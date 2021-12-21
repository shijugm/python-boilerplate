import myproj_tests.shared.myproj_test_settings as myproj_test_settings
import csv

"""
This file has all the utility functions for running tests
"""


# def create_test_db_connection():


def cleanup_db():
    """
    This function cleans up all the tables
    :return:
    """


def cast_db_column(table_name, column_name):
    """
    if there is a value in the myproj_test_config cast column key then use that
    in some cases the data needs to be formatted before comparison.
    :param table_name:
    :param column_name:
    :return:
    """
    try:
        cast_col = myproj_test_settings.cast_db_columns_dict[table_name][column_name]
    # should be a no key found exception
    except:
        cast_col = column_name

    return cast_col


def formatcolumn_string(col_val):
    trim_col_val = col_val.strip(' ')
    # if value has current date then replace it with date ,
    # if value = ~ then replace it with None ( which is null in the database)
    # return ret


"""
This method is called in the load data from csv method 
some values like current_date will be replaced with the actual value
"""


def replace_dynamic_values(row_tuple):
    row_list = list(row_tuple)
    updated_list = list(map(formatcolumn_string, row_list))
    return tuple(updated_list)


def load_table_from_csv(table_name, csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_cols = next(csv_reader)
        insert_sql = "insert into {0} values ({1})"
        insert_sql = insert_sql.format(table_name, ','.join('?' * len(csv_cols)))
        # prepare insert statement using the db connection
        # stmt = db.prepare(conn, insert_sql)
        for data in csv_reader:
            tuple_data = tuple(data)
            new_tuple = replace_dynamic_values(tuple_data)
            # db.execute(stmt, new_tuple)


# this function is useful when we have a static list to compare
# db outputs are a list of list so using this method a static list is converted to a list of list
# for comparison
def convert_list_to_listiflist(lst):
    return [[i] for i in lst]
