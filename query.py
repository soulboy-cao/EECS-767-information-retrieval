import pickle
from processing import implStopwordStemmer


# Get candidates docs (union)
def combine_doclist(doc_lists):
    if len(doc_lists):
        sum_list = list(doc_lists[0])
        for num in range(1, len(doc_lists)):
            sum_list = sum_list + list(doc_lists[num])
        result = list(set(sum_list))
        return result
    else:
        return []


# load structure
def get_index():
    with open("posting_list.dat", 'rb') as f:
        index = pickle.load(f)
    return index


def get_idf_dict():
    with open("idf_dict.dat", 'rb') as f:
        idf_dict = pickle.load(f)
    return idf_dict


def get_docv_length():
    with open("vector_length.dat", 'rb') as f:
        docv_length = pickle.load(f)
    return docv_length


# Transform dict to list
def dict2list(dic:dict):
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst


# Processing query
def processing_query(index, idf_dict, docv_length, query_str):
    # Pre-process the query with the stop list and stemmer
    stem_query = implStopwordStemmer(query_str).split()
    print("stem_query",stem_query)
    query = {}
    for term in stem_query:
        if term in query:
            query[term] += 1
        else:
            query[term] = 1
    # Get docs
    doclists = []
    for term in query.keys():
        if term in index:
            doclists.append(index[term].keys())
    # print("doclists",doclists)
    # Candidates:candidate documents that contain at least one query term
    candidates = combine_doclist(doclists)
    # Candidates:candidate documents that contain at least one query term

    # Compute the TF-IDF similarity score between the query and each candidate document
    result = {}
    for doc in candidates:
        result[doc] = float(0)

    for term in query.keys():
        idf = idf_dict[term]
        index_item = index[term]
        for doc in candidates:
            if doc in index_item:
                result[doc] += index_item[doc]*query[term]*idf*idf

    return result


def get_url_dic():
    with open("url_dic.dat", 'rb') as f:
        url_dic = pickle.load(f)
    return url_dic


# Query main
index = get_index()
idf_dict = get_idf_dict()
docv_length = get_docv_length()
url_dic = get_url_dic()
result_num = 10

flag = True
while flag:
    query_str = input("Please input the query:")
    if query_str == "out":
        flag = False
    else:
        result = processing_query(index, idf_dict, docv_length, query_str)
        result_list = sorted(dict2list(result), key=lambda x: x[1], reverse=True)
        show_list = []
        for item in result_list[0:result_num]:
            show_list.append((url_dic[item[0]], item[1]))
        print(show_list)


