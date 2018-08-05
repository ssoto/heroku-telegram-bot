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

def build_file_name():
    date = datetime.now().strftime('%Y%m%d')
    return FILE_PATH.format(date)


def write_on_file(message, user):
    file_name = build_file_name()
    line = '{HOUR},{MESSAGE},{USER}\n'.format(
        HOUR=datetime.now(),
        MESSAGE=message,
        USER=user,
    )
    logging.info('Writing message of {} in {}'.format(user, file_name))
    with open(file_name, 'a') as fd:
        fd.write(line)

def read_from_file():
    file_name = build_file_name()
    result = []
    with open(file_name, 'r') as fd:
        for line in fd.readlines():
            splitted = line.split(',')
            [hour, message, user] = splitted
            result.append(
                '{} ({}) - {}'.format(
                    hour,
                    user,
                    message,
                )
            )
    return '\n'.join([r for r in result])
