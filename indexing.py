import pickle


def indexing(url_dic, inputpath):
    term_dict = {}
    origin_files = list(url_dic.keys())

    # Construct the invert index
    for filename in origin_files:
        # print(filecount)
        file = open(inputpath + str(filename) + ".htm.txt", 'r', encoding='UTF-8')
        text = file.read().split()
        file.close()
        location = 0
        for word in text:
            if word in term_dict:
                item = term_dict[word]
                if filename in item:
                    item[filename].append(location)
                else:
                    item[filename] = [location]

            else:
                term_dict[word] = {filename: [location]}
            location += 1



    # f = open('file_list.dat', 'wb')
    # pickle.dump(origin_files, f)
    # f.close()

    f = open('posting_list.dat', 'wb')
    pickle.dump(term_dict, f)
    f.close()
