import json
import os

# 获得词表
def get_words_dic():
    words_path = './data/news_1_gram.json'
    with open(words_path, 'r', encoding='utf-8') as f:
        words = json.load(f)
    return words

def FMM(sentence, words_dic):
    max_length = max(len(word) for word in words_dic)
    sentence = sentence.strip()
    words_length = len(sentence)
    cut_word_list = []

    while words_length > 0:
        max_cut_length = min(max_length, words_length)
        sub_sentence = sentence[0: max_cut_length]
        while max_cut_length > 0: # 最长匹配
            if sub_sentence in words_dic: # 在字典中
                cut_word_list.append(sub_sentence)
                break
            elif max_cut_length == 1: # 不在字典中
                cut_word_list.append(sub_sentence)
                break
            else: # 不在字典中，最大框长度-1
                max_cut_length = max_cut_length - 1
                sub_sentence = sub_sentence[0:max_cut_length]
        sentence = sentence[max_cut_length:]
        words_length = words_length - max_cut_length

    return cut_word_list


def BMM(sentence, words_dic):
    max_length = max(len(word) for word in words_dic) # 统计词典中词的最长长度
    sentence = sentence.strip()
    words_length = len(sentence)
    cut_word_list = []

    while words_length > 0:
        max_cut_length = min(max_length, words_length)
        sub_sentence = sentence[-max_cut_length:] # 与FMM不同之处
        while max_cut_length > 0:
            if sub_sentence in words_dic:
                cut_word_list.append(sub_sentence)
                break
            elif max_cut_length == 1:
                cut_word_list.append(sub_sentence)
                break
            else:
                max_cut_length = max_cut_length -1
                sub_sentence = sub_sentence[-max_cut_length:]  # 与FMM不同之处
        sentence = sentence[0:-max_cut_length] # 与FMM不同之处
        words_length = words_length - max_cut_length
    cut_word_list.reverse()

    return cut_word_list

# 实现双向匹配算法中的切词方法
def Bi_MM(sentence, words_dic):
    bmm_word_list = BMM(sentence, words_dic)
    fmm_word_list = FMM(sentence, words_dic)
    if bmm_word_list == fmm_word_list:
        return bmm_word_list
    else:
        bmm_word_list_size = len(bmm_word_list)
        fmm_word_list_size = len(fmm_word_list)
        if bmm_word_list_size != fmm_word_list_size:
            return bmm_word_list if bmm_word_list_size < fmm_word_list_size else fmm_word_list
        else:
            FMM_one_word_count = sum([1 for word in fmm_word_list if len(word) == 1])
            BMM_one_word_count = sum([1 for word in bmm_word_list if len(word) == 1])
            return fmm_word_list if BMM_one_word_count > FMM_one_word_count else bmm_word_list