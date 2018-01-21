# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:19:31 2017

@author: apple
"""

import os
import re
from bs4 import BeautifulSoup
import csv

""" 获取文件路径 """

f_dirs = []
for rt, dirs, files in os.walk("/Users/apple/Documents/The Economist Bilingual 2017 Vol.I/EPUB"):
    f_dir = []    
    f_dir.append(rt)
    f_dir.append(files)
    f_dirs.append(f_dir)
    
f_selected = []
b = re.compile(r".xhtml")


for r in f_dirs:
    for f in r[1]:
        if b.search(f):
            fs = []
            fs.append(r[0])
            fs.append(f)
            f_selected.append(fs)
            
""" 制作单词注释字典 """

gmat_word_list = {}
i=0
with open ('/Users/apple/Desktop/English/Tofel_Gmat.csv','r') as gmat_f:
    reader = csv.reader(gmat_f)
    for row in reader:
        footnote_list = []
        footnote_list.append(str(i+1))
        footnote_list.append('<aside epub:type="footnote" id="footnote-'+str(i+1)+'"><a epub:type="noteref" href="#noteref-'+str(i+1)+'">[i]</a>'+row[0]+'<br/>'+ row[1]+'</aside>')
        gmat_word_list[row[0]] = footnote_list
        i=i+1
    gmat_f.close()
'''soup = BeautifulSoup(gmat_word_list['liver'][1].decode('gbk'),'lxml')'''


def get_footnote_list(key):
    f_note = '<sup><a href="#footnote-'+file_word_list_selected[key][0]+'" epub:type="noteref" id = "noteref-'+file_word_list_selected[key][0]+'">[i]</a></sup><strong style = "color:#010030">'+ key + '</strong>'
    return f_note

    
"""编辑文件"""

for i in range(len(f_selected)):
    
    """获取每一篇文章的单词列表,unicode"""
    with open(f_selected[i][0]+"/"+f_selected[i][1],'r') as f:
        soup = BeautifulSoup(f)
        print f_selected[i][1]
        
        '''if not 'xmlns:epub' in soup.html.attrs:
            soup.html['xmlns:epub'] = "http://www.idpf.org/2007/ops"'''

        file_word_list_words = []
        file_word_list = {}
        
        for a in soup.findAll('a'):
            if a.p is not None:
                for p in a.findAll('p'):
                    a.insert_before(p)
                a.decompose()
        
        for p in soup.findAll('p'):
            if p.a is not None:
                p.a.decompose()
        
        pattern_a=re.compile(r'\w+')
        
        for p_tag in soup.findAll('p'):
            if p_tag.get_text() is not None:
                p_tag_text = p_tag.get_text()
                for match_a in pattern_a.finditer(p_tag_text):
                    file_word_list_words.append(match_a.group())
        
        """建立文章单词字典"""           
        for word in file_word_list_words:
            file_word_list[word.lower()] = ["N"]
                
        file_word_list_selected = {}
        for key in file_word_list.keys():
            for g_word in gmat_word_list.keys():
                pattern_b = re.compile(g_word)
                if re.match(pattern_b,key):
                    n_gmat = gmat_word_list[g_word]
                    n_gmat.append(g_word)
                    file_word_list_selected[key.encode('gbk')] = n_gmat
                    
        if len(file_word_list_selected.keys()) != 0:

            """            
            with open(dir_2,'wb') as com_f:
                writer2 = csv.writer(com_f)
                for key in file_word_list:
                    if file_word_list[key] !="N":
                        writer2.writerow([key, file_word_list[key]])
                    com_f.close()
                        
            with open (dir_2,'r') as com_f:
                reader = csv.reader(com_f)
                file_word_list_words_2=[]
                for item in reader:
                    file_word_list_words_2.append(item)
                    com_f.close()
            """
                    
            for p_tag in soup.findAll('p'):
                if p_tag.get_text() != "":
                    p_tag_text = p_tag.get_text().encode('utf-8')
                    for word in file_word_list_selected.keys()[0:len(file_word_list_selected.keys())]:
                        p_tag_text = p_tag_text.replace(word,get_footnote_list(word))
                        new_tag = u'<span>'+p_tag_text.decode("UTF-8") + u'</span>'
                        new_tag_soup = BeautifulSoup(new_tag)
                        p_tag.contents = [u'']
                        p_tag.contents.append(new_tag_soup.span)
        f_note_dict = {}
        for key in file_word_list_selected.keys():
            f_note_dict[file_word_list_selected[key][1]] = file_word_list_selected[key][0]
        
        for key in f_note_dict.keys():
            soup.body.append(BeautifulSoup(key.decode('gbk')).find_all('aside')[0])
        
        with open(f_selected[i][0]+"/"+f_selected[i][1],'w') as f:        
            f.write(soup.prettify('utf-8'))
            f.close()