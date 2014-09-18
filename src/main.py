# -*- coding: utf-8 -*-

import analyse_text, draw, text_segmentation, os, SimpleHTTPServer, SocketServer

if __name__ == '__main__':
    text_segmentation.text_seg()
    analyse_text.training()
    _ = analyse_text.cosine_all()
    _ = analyse_text.get_relationship(_)
    draw.draw(_)
    os.chdir('../tmp')
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", 8000), Handler)
    print 'serving at port 8000'
    httpd.serve_forever()
