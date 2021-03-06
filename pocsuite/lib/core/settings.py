#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014-2015 pocsuite developers (http://sebug.net)
See the file 'docs/COPYING' for copying permission
"""

import os
import subprocess
import time
import sys

from lib.core.revision import getRevisionNumber

VERSION = "0.1"
REVISION = getRevisionNumber()
SITE = "http://sebug.net"
VERSION_STRING = "pocsuite/%s%s" % (VERSION, "-%s" % REVISION if REVISION else "-nongit-%s" % time.strftime("%Y%m%d", time.gmtime(os.path.getctime(__file__))))

IS_WIN = subprocess.mswindows

PLATFORM = os.name
PYVERSION = sys.version.split()[0]

ISSUES_PAGE = "https://github.com/knownsec/Pocsuite/issues"
GIT_REPOSITORY = "git@github.com:knownsec/Pocsuite.git"
GIT_PAGE = "https://github.com/knownsec/Pocsuite"

LEGAL_DISCLAIMER = "Usage of pocsuite for attacking targets without prior mutual consent is illegal."


BANNER = """\033[01;33m 
                              ,--. ,--.         
 ,---. ,---. ,---.,---.,--.,--`--,-'  '-.,---.  \033[01;37m{\033[01;%dm%s\033[01;37m}\033[01;33m
| .-. | .-. | .--(  .-'|  ||  ,--'-.  .-| .-. : 
| '-' ' '-' \ `--.-'  `'  ''  |  | |  | \   --. 
|  |-' `---' `---`----' `----'`--' `--'  `----'  
`--'                                            \033[0m\033[4;37m%s\033[0m

""" % ((31 + hash(REVISION) % 6) if REVISION else 30, VERSION_STRING.split('/')[-1], SITE)

# Encoding used for Unicode data
UNICODE_ENCODING = "utf-8"
# Format used for representing invalid unicode characters
INVALID_UNICODE_CHAR_FORMAT = r"\?%02x"

USAGE = "python pocsuite.py [options]"

INDENT = " " * 2

POC_ATTRS = ("vulID", "version", "author", "vulDate", "name", "appVersion", "samples", "desc", "createDate", "updateDate", "references", "appPowerLink", "vulType", "appName")

POC_IMPORTDICT = {
    "from pocsuite.net import": "from lib.request.basic import",
    "from pocsuite.poc import": "from lib.core.poc import",
    "from pocsuite.utils import register": "from lib.core.register import registerPoc as register",
    "from pocsuite.lib": "from lib"
}

OLD_VERSION_CHARACTER = ("from comm import cmdline", "from comm import generic")

HTTP_DEFAULT_HEADER = {
    "Accept": "*/*",
    "Accept-Charset": "GBK,utf-8;q=0.7,*;q=0.3",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Referer": "http://www.baidu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0"
}


PCS_OPTIONS = {
    'threads': 1,
    'url': None,
    'urlFile': None,
    'agent': None,
    'pocFile': None,
    'referer': None,
    'Mode': 'verify',
    'cookie': None,
    'randomAgent': False,
    'report': None,
    'proxy': None,
    'proxyCred': None,
    'timeout': 5
}

REPORT_TABLEBASE = """\
    <tbody>
    %s
    </tbody>
    """

REPORT_HTMLBASE = """\
    <!DOCTYPE html>
    <html lang="zh-cn">
        <head>
            <meta charset="utf-8">
            <title></title>
            <style type="text/css">
            caption{padding-top:8px;padding-bottom:8px;color:#777;text-align:left}th{text-align:left}.table{width:100%%;max-width:100%%;margin-bottom:20px}.table>thead>tr>th,.table>tbody>tr>th,.table>tfoot>tr>th,.table>thead>tr>td,.table>tbody>tr>td,.table>tfoot>tr>td{padding:8px;line-height:1.42857143;vertical-align:top;border-top:1px solid #ddd}.table>thead>tr>th{vertical-align:bottom;border-bottom:2px solid #ddd}
            </style>
        </head>
        <body>
            <div class="container">
                <table class="table">
                    <thead>
    %s
                    </thead>
    %s
                </table>
            </div>
        </body>
    </html>
    """
