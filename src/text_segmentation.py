# -*- coding: utf-8 -*-

import jieba

def text_seg(file_in_path='../tmp/book-utf-8.txt',
             file_out_path='../tmp/book-seg.txt',
             user_dict_path='../tmp/user_dict_path.txt')
    '''
        Use segmentation module to cut the word.
        You can find default user dict in '../tmp/userdict.txt'.
        Default_File_in: '../tmp/book-utf-8.txt'
        Default_File_out: '../tmp/book-seg.txt'
    '''
    jieba.load_userdict(user_dict_path)
    with file(file_in_path) as _f_in:
        while True:
            _line_in = _f_in.readline()
            if _line_in == '': break
            _seg_list = jieba.cut(_line_in, cut_all=False)
            # make cuted words separated with space
            _line_out = u' '.join(_seg_list)
            _line_out = _line_out.encode('utf-8')
            with file(file_out_path, 'a') as _f_out:
                _f_out.write(_line_out)

if __name__ == '__main__':
    text_seg()
