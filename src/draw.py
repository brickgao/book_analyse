# -*- coding: utf-8 -*-

def draw(_dict):
    '''
        Draw the relationship graph.
    '''
    with file('../tmp/index.html', 'w') as _file_out:
        _html = '''
                <html xmlns="http://www.w3.org/1999/xhtml" lang="zh-CN">
                  <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                    <title>Example</title>
                    <script type="text/javascript" src="http://datavlab.org/datavjs/libs/jquery.js"></script>
                    <!--<script type="text/javascript" src="http://datavlab.org/datavjs/libs/jquery.pngFix.js"></script>-->
                    <script type="text/javascript" src="http://datavlab.org/datavjs/deps/compatible.js"> </script>
                    <script type="text/javascript" src="http://datavlab.org/datavjs/deps/d3.min.js"></script>
                    <script type="text/javascript" src="http://datavlab.org/datavjs/deps/d3.csv.js"></script>
                    <script type="text/javascript" src="http://datavlab.org/datavjs/deps/d3.layout.min.js"></script>
                    <script type="text/javascript" src="http://datavlab.org/datavjs/deps/d3.geom.min.js"></script>
                    <script type="text/javascript" src="http://datavlab.org/datavjs/deps/raphael.min.js"></script>
                    <script type="text/javascript" src="http://datavlab.org/datavjs/deps/eventproxy.js"></script>
                    <script type="text/javascript" src="http://datavlab.org/datavjs/deps/seajs/sea.js"></script>
                    <script type="text/javascript">
                        seajs.config({
                        alias: {
                            'datav': 'http://datavlab.org/datavjs/deps/datav.js',
                            'tree': 'http://datavlab.org/datavjs/deps/libs/tree.js',
                            'treemap': 'http://datavlab.org/datavjs/deps/libs/treemap.js',
                            'stream': 'http://datavlab.org/datavjs/deps/libs/stream.js',
                            'scatterplotMatrix': 'http://datavlab.org/datavjs/deps/libs/scatterplotMatrix.js',
                            'force': 'http://datavlab.org/datavjs/deps/libs/force.js',
                            'matrix': 'http://datavlab.org/datavjs/deps/libs/matrix.js',
                            'bubble': 'http://datavlab.org/datavjs/deps/libs/bubble.js',
                            'chord': 'http://datavlab.org/datavjs/deps/libs/chord.js'
                            }
                        });
                    </script>
                  </head>
                  <body>
                    <div id="chart"></div>
                  </body>
                  <script>
                    seajs.use(["force", "datav"], function (Force, DataV) {
                      var net = new Force("chart", {
                        width: 800,
                        height: 600,
                        tag: true
                      });
                      DataV.csv("data.csv", function (source) {
                        net.setSource(source, {id: 0, name: 1, nValue: 2, source: 3, target: 4, lValue: 5});
                        net.render();
                      });
                    });
                  </script>
                </html>
                  '''
        _file_out.write(_html)
    with file('../tmp/data.csv', 'w') as _file_out:
        _file_out.write('Id, Name, Value\n')
        _cnt = 0
        for _ in _dict.keys():
            _file_out.write("%d, %s, %d\n" % (_cnt, _.encode('utf-8'), 1))
            _cnt += 1
        _file_out.write('Source, Target, Value\n')
        _cnt = 0
        for _i in _dict.keys():
            for _j in _dict[_i]:
                _file_out.write("%d, %d, %d\n" % (_cnt, list(_dict.keys()).index(_j), 1))
            _cnt += 1
