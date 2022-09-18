import os
import pytest


def test_get_size_file():
    picture_size = os.path.getsize('../resouces/my_picture.jpg')
    picture_time = os.path.getmtime('../resouces/my_picture.jpg')
    picture_ctime = os.path.getctime('../resouces/my_picture.jpg')
    print(picture_time)
    print(picture_ctime)
    assert picture_size == 40401

def test_get_all_type_path():
    print(os.path.abspath('../resouces/book.csv'))
    print(os.path.dirname(os.path.abspath('../resouces/book.csv')))
    current_file_process = os.path.abspath(__file__) # where start process
    current_dir_where_start_process = os.path.dirname(os.path.abspath(__file__)) # this is direcory where start process
    print(current_file_process)
    print(current_dir_where_start_process)
    join_dir = os.path.join(current_dir_where_start_process, 'resouces', 'TMP') # glue path
    print(join_dir)