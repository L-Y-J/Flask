#!usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta


class QueryCondition(object):
    def __init__(self, start_date, end_date):
        self.start_date = start_date if start_date is not None and len(start_date) == 10 else (
            date.today() - timedelta(days=30)).isoformat()
        self.end_date = end_date if end_date is not None and len(end_date) else date.today().isoformat()
        self.condition_list = []


class QuerySql(object):
    def __init__(self, condition):
        self.condition = condition

    def query_patch_forlist(self):
        sql = (
            "SELECT T1.id,T16.editionnum,T1.submittime,T8.name as status,T6.gname as dept,T17.gname as currentdept,"
            "T47.gname as transferdept,T18.pname as products,T1.questionid,T1.questiontype,T1.questiontypeaftervali,"
            "T1.questiontypeaftervali,T1.supportor,T1.supportadvice,T1.supportemail,T1.supportphone,T1.actualizer,"
            "T1.actualizeremail,T1.actualizerphone, T1.customname, T1.headline, T1.questionremark, T1.closedstyle,"
            "T1.supporturlattachment, T9.fullname, T9.email, T9.phone, T1.developoutremark, T1.devoloptoreqsremark,"
            "T1.reqtodevelopremark, T1.advicetotester, T1.devdealresultremark, T1.develpermodifyremak "
            "FROM cqmaster.t_supportwebquestion T1 "
            "INNER JOIN cqmaster.statedef T8 ON T1.state = T8.id "
            "INNER JOIN cqmaster.t_editions T16 ON T1.cureentedition = T16.dbid "
            "INNER JOIN cqmaster.t_products T18 ON T1.currentpro = T18.dbid "
            "INNER JOIN cqmaster.t_groups T17 ON T1.currentdept = T17.dbid "
            "INNER JOIN cqmaster.t_groups T6 ON T1.dept = T6.dbid "
            "INNER JOIN cqmaster.t_groups T47 ON T1.transferdept = T47.dbid "
            "INNER JOIN cqmaster.users T9 ON T1.prevcloseuser = T9.dbid "
            "WHERE "
            "((T17.gname IN ('NC财务开发部')) OR (T47.gname IN ('NC财务开发部')) OR (T6.gname IN ('NC财务开发部'))) "
            "AND T18.pname IN ('FI_ARAP_应收管理','FI_ARAP_应付管理') "
            "AND T1.closedstyle LIKE '%补丁解决' "
            "AND T1.submittime >= ? "
            "AND T1.submittime <= ?"
        )
        self.condition.condition_list.append(self.condition.start_date)
        self.condition.condition_list.append(self.condition.end_date)
        return sql.decode('utf-8')

    def query_patch_forchart(self):
        sql = (
            "SELECT COUNT (T1.id)"
            "FROM cqmaster.t_supportwebquestion T1 "
            "INNER JOIN cqmaster.statedef T8 ON T1.state = T8.id "
            "INNER JOIN cqmaster.t_editions T16 ON T1.cureentedition = T16.dbid "
            "INNER JOIN cqmaster.t_products T18 ON T1.currentpro = T18.dbid "
            "INNER JOIN cqmaster.t_groups T17 ON T1.currentdept = T17.dbid "
            "INNER JOIN cqmaster.t_groups T6 ON T1.dept = T6.dbid "
            "INNER JOIN cqmaster.t_groups T47 ON T1.transferdept = T47.dbid "
            "INNER JOIN cqmaster.users T9 ON T1.prevcloseuser = T9.dbid "
            "WHERE "
            "((T17.gname IN ('NC财务开发部')) OR (T47.gname IN ('NC财务开发部')) OR (T6.gname IN ('NC财务开发部'))) "
            "AND T18.pname IN ('FI_ARAP_应收管理','FI_ARAP_应付管理') "
            "AND T1.closedstyle LIKE '%补丁解决' "
            "AND T1.submittime >= ? "
            "AND T1.submittime <= ?"
        )
        self.condition.condition_list = self.auto_set_period()
        return sql.decode('utf-8')

    def auto_set_period(self):
        period = []
        s = datetime.strptime(self.condition.start_date, '%Y-%m-%d')
        e = datetime.strptime(self.condition.end_date, '%Y-%m-%d')
        d = s - e
        if (d.days < 7):
            period.append()
        return period


if __name__ == '__main__':
    condition = QueryCondition("2016:01:01", "2016:01:13")
    query_sql = QuerySql(condition)
    query_sql.query_patch_forlist()
    print query_sql.condition.condition_list
