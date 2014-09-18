# -*- coding: utf-8 -*-

import jieba

def text_seg():
    '''
        Use segmentation module to cut the word.
        You can find user dict in '../tmp/userdict.txt'
        File_in: '../tmp/book-utf-8.txt'
        File_out: '../tmp/book-seg.txt'
    '''
    jieba.load_userdict("../tmp/userdict.txt")
    with file('../tmp/book-utf-8.txt') as _f_in:
        while True:
            _line_in = _f_in.readline()
            if _line_in == '': break
            _seg_list = jieba.cut(_line_in, cut_all=False)
            # make cuted words separated with space
            _line_out = u' '.join(_seg_list)
            _line_out = _line_out.encode('utf-8')
            with file('../tmp/book-seg.txt', 'a') as _f_out:
                _f_out.write(_line_out)

if __name__ == '__main__':
    text_seg()
