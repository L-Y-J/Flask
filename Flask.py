#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, jsonify

import query_exec

app = Flask(__name__)


@app.route('/table', methods=['GET', 'POST'])
def table():
    res = query_exec.query_patch_list()
    table_heads = res.get('heads')
    table_rows = res.get('rows')
    return render_template('table.html', active_page='table', table_heads=table_heads, table_rows=table_rows)


@app.route('/chart', methods=['GET', 'POST'])
def chart():
    return render_template('chart.html', active_page='chart')


@app.route('/helpme', methods=['GET', 'POST'])
def helpme():
    return render_template('helpme.html', active_page='helpme')


@app.route('/chartdata', methods=['GET', 'POST'])
def chart_data():
    print request.args.get('startDate'), request.args.get('endDate')
    return jsonify({'timeLine': ['周一', '周二', '周三', '周四', '周五', '周六', '周日']})


if __name__ == '__main__':
    app.run(debug=True)
