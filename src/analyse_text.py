# -*- coding: utf-8 -*-

import word2vec

def training():
    '''
        Training use file in '../tmp/book-seg.txt'.
        Make sure that you have ran the function 'text_seg' to do segmentation first.
    '''
    word2vec.word2vec('../tmp/book-seg.txt', '../tmp/book.bin', size=300, verbose=True)

def cosine_all():
    '''
        Use model to cosine all name in the book.
    '''
    _name_list = [u'何塞',
                  u'阿尔卡蒂奥', 
                  u'布恩迪亚', 
                  u'乌尔苏拉',
                  u'伊瓜兰',
                  u'奥雷里亚诺',
                  u'布恩迪亚',
                  u'阿玛兰妲',
                  u'丽贝卡',
                  u'蕾梅黛丝',
                  u'摩斯科特',
                  u'阿尔卡蒂奥',
                  u'奥雷里亚诺',
                  u'蕾梅黛丝',
                  u'费尔南达',
                  u'德尔',
                  u'卡皮奥',
                  u'佩特拉',
                  u'克特斯',
                  u'雷纳塔',
                  u'蕾梅黛丝',
                  u'阿玛兰妲',
                  u'奥雷里亚诺',
                  u'梅尔加德斯',
                  u'庇拉尔',
                  u'特尔内拉']
    map(lambda _: _.encode('utf-8'), _name_list)
    model = word2vec.load('../tmp/book.bin')
    return model.cosine(_name_list, n=10)


if __name__ == '__main__':
    training()
    model = word2vec.load('../tmp/book.bin')
    _l = model.cosine(u'何塞'.encode('utf-8'))
    for _ in _l[u'何塞'.encode('utf-8')]:
        print _[0].decode('utf-8'), _[1]
