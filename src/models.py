#!/usr/bin/python
# -*- coding: utf-8 -*-
# System imports
import json
import os
# Third party imports
from sqlalchemy import (create_engine,
                        MetaData,
                        Table,
                        Column,
                        String,
                        DateTime,
                       )
# Local imports


class DataInfoDB(object):
    def __init__(self):
        user = os.getenv('USER')
        if not user:
            raise ValueError('Database username required')

        password = os.getenv('PASSWORD')

        if not password:
            raise ValueError('Database password name required')
        host = os.getenv('HOST', 'localhost')
        port = os.getenv('PORT', 5432)
        db = os.getenv('DB')
        if not db:
            raise ValueError('Database name is required')

        self.url = 'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'.format(
            USER=user,
            PASSWORD=password,
            HOST=host,
            PORT=port,
            DB=db
        )
        self.conn = None
        self.meta = None

    def connect(self):
        self.conn = create_engine(
            name_or_url=self.url,
            client_encoding='utf-8',
        )

        self.meta = MetaData(
            bind=self.conn,
            reflect=True
        )
        return self.conn, self.meta


    def initialize_models(self,):

        user_info = Table(
            'user_info', self.meta,
            Column('user_name', String),
            Column('inserted', DateTime),
            Column('url', String)
        )

        self.meta.create_all(self.conn)

    def insert_user_info(self, user_name, date, url):
        clause = self.meta.tables['user_info'].insert().values(
            user_name=user_name,
            inserted=date,
            url=url,
        )
        self.conn.execute(clause)

    def get_info(self):
        table = self.meta.tables['user_info']
        result = []
        for row in self.conn.execute(table.select()):
            result.append(
            {'user': row.user_name,
             'date': row.inserted.strftime('%Y/%m/%d %H:%m:%S'),
             'message': row.url }
            )
        return json.dumps(result)
