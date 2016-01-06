#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yongjie'

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/table', methods=['GET', 'POST'])
def table():
    table_heads = ["head1", "head2"]
    table_rows = [
        ['aaa', 'bbb'], ['ccc', 'ddd'], ['eee', 'fff'],
        ['aaa', 'bbb'], ['ccc', 'ddd'], ['eee', 'fff'],
        ['aaa', 'bbb'], ['ccc', 'ddd'], ['eee', 'fff'],
        ['aaa', 'bbb'], ['ccc', 'ddd'], ['eee', 'fff'],
        ['aaa', 'bbb'], ['ccc', u'包鑫'], ['eee', 'fff'],
        ['aaa', 'bbb'], ['ccc', 'ddd'], ['eee', 'fff'],
        ['aaa', 'bbb'], ['ccc', 'ddd'], ['eee', u'李勇杰']
    ]
    return render_template('table.html', active_page='table', table_heads=table_heads, table_rows=table_rows)


@app.route('/chart', methods=['GET', 'POST'])
def chart():
    return render_template('chart.html', active_page='chart')


@app.route('/helpme', methods=['GET', 'POST'])
def helpme():
    return render_template('helpme.html', active_page='helpme')


@app.route('/chartdata', methods=['GET', 'POST'])
def chartData():
    print request.args.get('startDate'), request.args.get('endDate')
    return jsonify({'timeLine': ['周一', '周二', '周三', '周四', '周五', '周六', '周日']})


if __name__ == '__main__':
    app.run(debug=True)
