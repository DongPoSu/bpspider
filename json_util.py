import daode
import jisuan
from constant import TEST_TYPE_REAL
from dao.DaoBean import TestBean
from dao.dao import insert_test
from kuaijijichu import jichu


def save_test(tests, catagory_id, type):
    data_list = list()
    count = 0
    temp_data = list(tests.get("list"))
    for data in temp_data:
        count += 1
        data_list.append(
            TestBean(test_id=data.get("testId"), test_name=data.get("name"), catagory_id=catagory_id, type=type,
                     sort_index=count))
    insert_test(data_list)


# save_test(jichu, "3ab2de9cf68bc537920ebfcd09e35d82", TEST_TYPE_REAL)
# save_test(daode.daode, "d295c8be0e105d9205bf84be8df52a1c", TEST_TYPE_REAL)
# save_test(jisuan.diansuan, "294a6e41976877340815767d5aac6686", TEST_TYPE_REAL)
