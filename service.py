# coding=utf-8

from bs4 import BeautifulSoup

import constant
from constant import JUDGE_QUEST_TYPE, METHOD_GET
from dao.DaoBean import TestSubject
from dao.dao import insert_single_test, insert_multi_test, insert_judge_test, insert_calc_test, insert_practice_test
from myHttp.http import HttpLib
from myHttp.httpBean import Bean
from string_util import parser_ques_id


# 获取题目id
def get_detail_id(headers, base_url, test_id):
    d = dict()
    bean = Bean()
    url = base_url.format(test_id=test_id)
    bean.set_attr(headers=headers, url=url, method=METHOD_GET)
    soup = BeautifulSoup(HttpLib(bean).request())
    single_str = soup.find(id="nopaperAnsSingleChoiceStr")['value']
    multi_str = soup.find(id="nopaperAnsMultChoiceStr")['value']
    judge_str = soup.find(id="nopaperAnsJudgmentStr")['value']
    calc_str = soup.find(id="nopaperAnsCalcparentStr")['value']
    practice_str = soup.find(id="nopaperAnsPracticalStr")['value']
    d.setdefault(constant.SINGLE_QUEST_TYPE, parser_ques_id(single_str))
    d.setdefault(constant.MULTI_QUEST_TYPE, parser_ques_id(multi_str))
    d.setdefault(constant.JUDGE_QUEST_TYPE, parser_ques_id(judge_str))
    d.setdefault(constant.CALC_QUEST_TYPE, parser_ques_id(calc_str))
    d.setdefault(constant.PRACTICE_QUEST_TYPE, parser_ques_id(practice_str))
    return d


def get_all_test(headers, test_id, ques_dict, base_url):
    single_list = get_test_list(headers=headers, base_url=base_url, test_id=test_id,
                               quest_ids=ques_dict.get(constant.SINGLE_QUEST_TYPE),
                               questType=constant.SINGLE_QUEST_TYPE)
    multi_list = get_test_list(headers=headers, base_url=base_url, test_id=test_id,
                              quest_ids=ques_dict.get(constant.MULTI_QUEST_TYPE),
                              questType=constant.MULTI_QUEST_TYPE)
    judge_list = get_test_list(headers=headers, base_url=base_url, test_id=test_id,
                              quest_ids=ques_dict.get(constant.JUDGE_QUEST_TYPE),
                              questType=constant.JUDGE_QUEST_TYPE)
    calc_list = get_test_list(headers=headers, base_url=base_url, test_id=test_id,
                             quest_ids=ques_dict.get(constant.CALC_QUEST_TYPE),
                             questType=constant.CALC_QUEST_TYPE)
    practice_list = get_test_list(headers=headers, base_url=base_url, test_id=test_id,
                                 quest_ids=ques_dict.get(constant.PRACTICE_QUEST_TYPE),
                                 questType=constant.PRACTICE_QUEST_TYPE)
    result_list = list()
    result_list.extend(single_list)
    result_list.extend(multi_list)
    result_list.extend(judge_list)
    result_list.extend(calc_list)
    result_list.extend(practice_list)


# 获取题目信息
def get_test_list(headers, base_url, quest_ids, questType, test_id):
    bean = Bean()
    index = 0
    data_list = list()
    for quesId in quest_ids:
        url = base_url.format(questType=questType, quesId=quesId)
        bean.set_attr(headers=headers, url=url, method=METHOD_GET)
        soup = BeautifulSoup(HttpLib(bean).request())
        index += 1
        try:
            data_list.append(
                TestSubject(test_id=test_id, content=get_test_content(soup, questType),
                            right_answer=get_answer(headers,soup, questType), sort_index=index))
        except:
            print(
                "test_id:%s questType:%s  quesId:%s count:%s" % (str(test_id), str(questType), str(quesId), str(index)))

    return data_list


# 获取题目
def get_test_content(soup, questType):
    if constant.JUDGE_QUEST_TYPE == questType:
        return JudgeMentTestService.get_judge_content(soup)
    elif constant.CALC_QUEST_TYPE == questType:
        return CalcTestService.get_calc_content(soup)
    elif constant.PRACTICE_QUEST_TYPE == questType:
        return PracticeTestService.get_practice_content(soup)
    else:
        return SelectTestService.get_select_content(soup)


# 获取答案
def get_answer(headers, soup, questType):
    if constant.JUDGE_QUEST_TYPE == questType:
        return JudgeMentTestService.get_judge_answer(soup)
    elif constant.CALC_QUEST_TYPE == questType:
        return CalcTestService.get_calc_answer(soup)
    elif constant.PRACTICE_QUEST_TYPE == questType:
        return PracticeTestService.get_practice_answer(headers, soup=soup)
    else:
        return SelectTestService.get_select_answer(soup)


def save_data(data_list, questType):
    if constant.JUDGE_QUEST_TYPE == questType:
        insert_judge_test(data_list)
    elif constant.MULTI_QUEST_TYPE == questType:
        insert_multi_test(data_list)
    elif constant.SINGLE_QUEST_TYPE == questType:
        insert_single_test(data_list)
    elif constant.CALC_QUEST_TYPE == questType:
        insert_calc_test(data_list)
    elif constant.PRACTICE_QUEST_TYPE == questType:
        insert_practice_test(data_list)


def concat(title, content, type):
    if JUDGE_QUEST_TYPE == type:
        return title
    else:
        return title + "&" + content


def clear_str(data):
    return str(data).replace("\\n", "") \
        .replace("\\t", "") \
        .replace("\\r", "") \
        .replace("\\", "") \
        .replace("['", "") \
        .replace("']", "").replace("\t", "").replace("疑义提交", "")


class PracticeTestService:
    @staticmethod
    def get_practice_content(soup):
        tag = soup.select("#quescontent")
        return tag[0]

    @staticmethod
    def get_practice_answer(headers, soup):
        url = "http://tiku.bp668.com/"+soup.select("a[target|_blank]")[0]["href"]
        bean = Bean()
        bean.set_attr(url=url,headers=headers)
        soup = BeautifulSoup(HttpLib(bean).request())
        return soup.select("embed")[0]['src']


class SelectTestService:
    # 获取选择题题目
    @staticmethod
    def get_select_content(soup):
        tag = soup.div
        tag['class'] = ['quescontent']
        i = 0
        content = ""
        title = ""
        for child in tag.children:
            if i == 1:
                for t in child.ul.find_all("li"):
                    content += clear_str(t.contents)
                    content += "@"
                content = content[0:len(content) - 1]
                break
            else:
                title += clear_str(child)
            i += 1
        return title + "&" + content

    # 获取选择题答案
    @staticmethod
    def get_select_answer(soup):
        tag_answer = soup.div.div.div
        tag_answer['class'] = ['explain']
        t1 = str(tag_answer.ul.li.get_text())
        t2 = str(tag_answer.p.get_text())
        t = clear_str(str(t1) + str(t2))
        return t


class JudgeMentTestService:
    # 获取判断题题目
    @staticmethod
    def get_judge_content(soup):
        tag = soup.div
        tag['class'] = ['quescontent']
        for child in tag.children:
            return clear_str(child)

    # 获取判断题答案
    @staticmethod
    def get_judge_answer(soup):
        tag_answer = soup.div.div.div
        tag_answer['class'] = ['explain']
        t1 = str(tag_answer.ul.li.get_text())
        t2 = str(tag_answer.p.get_text())
        t = clear_str(str(t1) + str(t2))
        return t


class CalcTestService:
    @staticmethod
    def get_calc_content(soup):
        tag = soup.select("#quescontent")
        return tag[0]

    @staticmethod
    def get_calc_answer(soup):
        tag1 = soup.find_all("a")
        for t in tag1:
            soup.a.decompose()
        tag = soup.select("#quesoperate")
        return tag[0]
