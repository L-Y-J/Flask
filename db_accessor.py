#!usr/bin/env python
# -*- coding: utf-8 -*-

import pyodbc


def exec_sql(sql):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.16.50.151;DATABASE=SDP2_NC;UID=SDPforlipy;PWD=SDPforlipy2012')
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchone()
    conn.close()
    return rows


if __name__ == '__main__':
    print 'start test...'
    print exec_sql(u"SELECT cqmaster.t_supportwebquestion.id,cqmaster.t_editions.editionnum,cqmaster.t_supportwebquestion.submittime,cqmaster.statedef.name  AS status,cqmaster.t_groups.gname  AS dept,cqmaster.t_groups.gname AS currentdept,    cqmaster.t_groups.gname AS transferdept,    cqmaster.t_products.pname AS products,    cqmaster.t_supportwebquestion.questionid,    cqmaster.t_supportwebquestion.questiontype,    cqmaster.t_supportwebquestion.questiontypeaftervali,    cqmaster.t_supportwebquestion.questiontypeaftervali,    cqmaster.t_supportwebquestion.supportor,    cqmaster.t_supportwebquestion.supportadvice,    cqmaster.t_supportwebquestion.supportemail,    cqmaster.t_supportwebquestion.supportphone,    cqmaster.t_supportwebquestion.actualizer,    cqmaster.t_supportwebquestion.actualizeremail,    cqmaster.t_supportwebquestion.actualizerphone,    cqmaster.t_supportwebquestion.customname,    cqmaster.t_supportwebquestion.headline,    cqmaster.t_supportwebquestion.questionremark,    cqmaster.t_supportwebquestion.closedstyle,    cqmaster.t_supportwebquestion.supporturlattachment,    cqmaster.users.fullname,    cqmaster.users.email,    cqmaster.users.phone,    cqmaster.t_supportwebquestion.developoutremark,    cqmaster.t_supportwebquestion.devoloptoreqsremark,    cqmaster.t_supportwebquestion.reqtodevelopremark,    cqmaster.t_supportwebquestion.advicetotester,    cqmaster.t_supportwebquestion.devdealresultremark,    cqmaster.t_supportwebquestion.develpermodifyremak FROM    cqmaster.t_supportwebquestion INNER JOIN    cqmaster.statedef ON    cqmaster.t_supportwebquestion.state = cqmaster.statedef.id INNER JOIN    cqmaster.t_editions ON    cqmaster.t_supportwebquestion.cureentedition = cqmaster.t_editions.dbid INNER JOIN    cqmaster.t_products ON    cqmaster.t_supportwebquestion.currentpro = cqmaster.t_products.dbid INNER JOIN    cqmaster.t_groups ON    cqmaster.t_supportwebquestion.currentdept = cqmaster.t_groups.dbid     or cqmaster.t_supportwebquestion.dept = cqmaster.t_groups.dbid    or cqmaster.t_supportwebquestion.transferdept = cqmaster.t_groups.dbid INNER JOIN    cqmaster.users ON    cqmaster.t_supportwebquestion.prevcloseuser = cqmaster.users.dbid WHERE    ((cqmaster.t_groups.gname IN ('NC财务开发部'))    OR  (cqmaster.t_groups.gname IN ('NC财务开发部'))    OR  (cqmaster.t_groups.gname IN ('NC财务开发部'))) AND cqmaster.t_products.pname IN ('FI_ARAP_应收管理','FI_ARAP_应付管理') AND cqmaster.t_supportwebquestion.closedstyle LIKE '%补丁解决' AND cqmaster.t_supportwebquestion.submittime >= '2015-12-01 00:00:00'")