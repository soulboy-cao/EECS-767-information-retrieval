import pickle
import urllib.request
import chardet

def download_html(memutxt, target_dir):
    # memutxt = "./crawled.txt"

    count = 0
    url_dic = {}
    url_title = {}
    with open(memutxt, 'r') as datafile:
        for i in range(1100):
            try:
                link = datafile.readline()
                print(str(link))
                response = urllib.request.urlopen(str(link))
                html = response.read()
                title = str(html).split('<title>')[1].split('</title>')[0]
                chardit1 = chardet.detect(html)
                fp = open(target_dir+str(count) + ".htm", "wb")
                strhtm = html.decode(chardit1['encoding']).encode('utf-8')
                fp.write(strhtm)
                fp.close()
                print("OK")
                url_dic[count] = str(link)
                url_title[count] = title
                count = count + 1
            except:
                print("fail")
                continue
    datafile.close()

    f = open('url_dic.dat', 'wb')
    pickle.dump(url_dic, f)
    f.close()
    f = open('url_title.dat', 'wb')
    pickle.dump(url_title, f)
    f.close()

