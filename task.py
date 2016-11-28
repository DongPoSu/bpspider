# coding=utf8

# 单选：
from bs4 import BeautifulSoup

import constant
from myHttp.http import HttpLib
from myHttp.httpBean import Bean
from service import get_detail_id, get_all_test, get_test_list, save_data

headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "scrolls=4.0; Hm_lvt_6494b281632e05d6a9ea89627613055e=1479260095,1479691627,1479796756,1479867373; Hm_lpvt_6494b281632e05d6a9ea89627613055e=1479867373; JSESSIONID=850E07D18AE11D24162869C986052CEB.node8028_tk3; Hm_lvt_c97145c1d82787f6f2157fdacf2128cf=1479725389,1479796760,1479796763,1479867374; Hm_lpvt_c97145c1d82787f6f2157fdacf2128cf=1479867421",
    "Referer": "http://tiku.bp668.com/accCert.html?index",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
}

test_ids = [
           "9a65df9c71a0b1019e8732f83a9b91f2"
            ]

baset_kaodian_url="http://tiku.bp668.com/accCert.html?buildKonwTest&type=knowtest_right_retry&testType=1&knowId={test_id}"
base_testid_url = "http://tiku.bp668.com/accCert.html?submitTest&testId={test_id}&testType=2"

base_test_url = "http://tiku.bp668.com/accCert.html?loadQues&questype={questType}&quesId={quesId}&" \
                "type=error_analyze&testId=3dbaaee53e125bb0b3c3d0ef54a706e4&testType=1&stuId=0fc1215bc374991d21cbced8df56fca2"
for test_id in test_ids:
    ques_dict = get_detail_id(headers=headers, base_url=baset_kaodian_url, test_id=test_id)
    print("MULTI_QUEST_TYPE: %s " % ques_dict.get(constant.MULTI_QUEST_TYPE, ""))
    data_list = get_test_list(headers=headers, base_url=base_test_url, test_id=test_id,
                  quest_ids=ques_dict.get(constant.MULTI_QUEST_TYPE),
                  questType=constant.MULTI_QUEST_TYPE)
    save_data(data_list, constant.MULTI_QUEST_TYPE)

    print("JUDGE_QUEST_TYPE: %s " % ques_dict.get(constant.MULTI_QUEST_TYPE, ""))
    data_list = get_test_list(headers=headers, base_url=base_test_url, test_id=test_id,
                              quest_ids=ques_dict.get(constant.JUDGE_QUEST_TYPE),
                              questType=constant.JUDGE_QUEST_TYPE)
    save_data(data_list, constant.JUDGE_QUEST_TYPE)
