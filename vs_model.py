import pickle
from math import log10, sqrt


def length(vector):
    length_v = float(0)
    for num in vector:
        length_v += num*num
    return sqrt(length_v)


# Compute the idf for each term
def get_idf(index):
    idf_dict = {}
    N = len(index)
    for word, doclist in index.items():
        temp = log10(N / len(doclist))  # idf = log_10(N/df)
        idf_dict[word] = temp*temp

    f = open('idf_dict.dat', 'wb')
    pickle.dump(idf_dict, f)
    f.close()
    return idf_dict


# Compute the doc vectors
def get_vectors(index, file_number, idf_dict):
    vectors = [[] for i in range(file_number)]
    for word, doc_list in index.items():
        idf = idf_dict[word]
        for doc, freq in doc_list.items():
            vectors[doc].append(len(freq)*idf)
    return vectors


# Compute the vectors' length
def get_vectorlength(vectors):
    vector_length = []
    for docv in vectors:
        vector_length.append(length(docv))

    f = open('vector_length.dat', 'wb')
    pickle.dump(vector_length, f)
    f.close()
    return vector_length


# load structure
def read_index():
    with open("posting_list.dat", 'rb') as f:
        index = pickle.load(f)
    return index


# Compute the values that a vs_model need
def vs_model_pre(file_num):
    index = read_index()
    idf_dict = get_idf(index)
    get_vectorlength(get_vectors(index, file_num, idf_dict))

