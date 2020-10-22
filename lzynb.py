def read_file(file_name):
    bibs = []
    with open(file_name, 'r', encoding='utf-8') as f:
        temp_dict = {}
        try:
            for lid, line in enumerate(f):
                line = line.strip()
                if line.startswith('@'):
                    if line.endswith(','):
                        if temp_dict:
                            bibs.append(temp_dict)

                        temp_dict = {}
                        temp_dict['name'] = line.split('{')[-1][:-1]
                    else:
                        print('error in name')
                elif not line or line.startswith('}'):
                    pass
                else:
                    a = line.split('=')
                    if len(a) > 2:
                        print('inner error')
                    key = a[0].strip()
                    value = a[1].strip()
                    if value[-1] == ',':
                        value = value[:-1]
                    if value[0] in ['"', '{']:
                        value = value[1:-1]
                    temp_dict[key] = value
        except:
            print("\033[31m"+ "解析 bib 文件出错，出错行：" + str(lid) + "，内容：" + line +"\033[0m")
            import traceback
            traceback.print_exc()
            exit()
        bibs.append(temp_dict)
        return bibs

conference_abbr = {
    'AAAI': 'the Association for the Advancement of Artificial Intelligence',
    'NAACL': 'North American chapter of the Association for Computational Linguistics',
    'ACL': 'Annual Meeting of the Association for Computational Linguistics',
    'AFNLP': 'Asian Federation of Natural Language Processing',
    'COLING': 'International Conference on Computational Linguistics',
    'EMNLP': 'Conference on Empirical Methods in Natural Language Processing',
    'CONLL': 'Conference on Computational Natural Language Learning',
    'SemEval': 'International Workshop on Semantic Evaluation',
    'LREC': 'International Conference on Language Resources and Evaluation',
    'ACM': 'Association for Computing Machinery',
    'SIGIR': 'Special Interest Group on Information Retrieval',
    'IJCAI': 'International Joint Conferences on Artificial Intelligence',
    'ICML': 'International Conference on Machine Learning',
    'NIPS': 'Conference on Neural Information Processing Systems',
    'UAI': 'Conference on Uncertainty in Artificial Intelligence',
    'AISTATS': 'International Conference on Artificial Intelligence and Statistics',
    'NLPCC': 'International Conference on Natural Language Processing and Chinese Computing',
    'EACL': 'European Association of Computational Linguistics',
    'WWW': 'International World Wide Web Conference',
    'ICLR': 'International Conference on Learning Representations'
}

def gen_author(bib_author):
    author_str = ""
    authors = bib_author.split("and")

    gt3 = False
    if len(authors) > 3:
        authors = authors[:3]
        gt3 = True

    sb_authors = []
    for aid, author in enumerate(authors):
        author = author.strip()
        if "," in author:
            names = author.split(",")
            family_first = True
        else:
            names = author.split(" ")
            family_first = False
        names = list(map(lambda x: x.strip(), names))
        if family_first:
            tmp = names[0]
            for name in names[1:]:
                tmp += " " + name[0] if name[0] != '{' else name[1]
        else:
            tmp = names[-1]
            for name in names[:-1]:
                tmp += " " + name[0] if name[0] != '{' else name[1]
        sb_authors.append(tmp)

    if gt3:
        sb_authors.append("et al")

    return ", ".join(sb_authors)

def gen_bib(bib):
    ret = ""

    # idx
    idx = "\\bibitem{" + bib["name"] + "}"
    ret += idx + ' '

    # author
    ret += gen_author(bib['author']) + '. '

    # title
    ret += bib["title"] + '. '

    # source
    if "booktitle" in bib:
        src = bib['booktitle'] 
    elif "journal" in bib:
        src = bib['journal']
    else:
        print("\n% \033[31m"+ ">>>>>> 下面这个会议可能有问题：没有 booktitle 或者 journal "+ bib['name'] +"\033[0m")
        src = ""
    if src.upper() in conference_abbr:
        src = 'In: Proceedings of ' + conference_abbr[src.upper()]
    else:
        if len(src) < 20:
            print("\n% \033[31m"+ ">>>>>> 下面这个会议可能有问题："+ bib['name'] +"\033[0m")

    if src != "":
        ret += src + ', '

    # year
    if 'year' in bib:
        ret += bib['year'] + '.'

    
    return ret

bibs = read_file("test.bib")
text = ""
for line in open("test.tex", encoding='utf8'):
    if line.strip() and line.strip()[0] != '%':
        text += line

num = 0
# print(bibs)
for bib in bibs:
    if bib['name'] + ',' in text or bib['name'] + '}' in text:
        try:
            print(gen_bib(bib))
        except:
            print("\n% \033[31m"+ '这个bib有问题' +bib['name'] +"\033[0m")
        num += 1

print('\n\nFound' + str(num) + 'bibs')
