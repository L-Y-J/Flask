#!usr/bin/env python
# -*- coding: utf-8 -*-

from query_generator import QueryCondition, QuerySql
import db_accessor

print db_accessor.exec_sql(QuerySql('').query_patch())
