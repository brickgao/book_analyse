# -*- coding: utf-8 -*-

import analyse_text, draw, text_segmentation

if __name__ == '__main__':
    text_segmentation.text_seg()
    analyse_text.training()
    _ = analyse_text.cosine_all()
    _ = analyse_text.get_relationship(_)
    draw.draw(_)
