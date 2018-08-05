#!/usr/bin python
# -*- coding: utf-8 -*-

import os

from datetime import datetime

import logging


FOLDER = './messages'
FILE_SKEL = 'aigua_messages_{}.csv'

FILE_PATH = os.path.join(FOLDER, FILE_SKEL)

if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)

def write_on_file(message, user):
    date = datetime.now().strftime('%Y%m%d')
    file_name = FILE_PATH.format(date)
    line = '"{HOUR}","{MESSAGE}","{USER}"\n'.format(
        HOUR=datetime.now(),
        MESSAGE=message,
        USER=user,
    )
    logging.info('Writing message of {}'.format(user))
    with open(file_name, 'a') as fd:
        fd.write(line)