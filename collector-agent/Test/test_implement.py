#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by eeliu at 11/7/19
import json
import time
from unittest import TestCase

import gevent

from CollectorAgent.CollectorAgentConf import CollectorAgentConf
from Common.Logger import TCLogger
from PinpointAgent.AppManagement import AppManagement
import os

# class FakeCollectorAgentConf:
#     def __init__(self):
#         self.CollectorSpanIp ='dev-pinpoint'
#         self.CollectorSpanPort =9996
#         self.CollectorStatIp ='dev-pinpoint'
#         self.CollectorStatPort =9995
#         self.CollectorAgentIp ='dev-pinpoint'
#         self.CollectorAgentPort =9994
#         self.max_pending_size =-1
#         self.collector_type = SUPPORT_THRIFT
#         self.collector_implement = ThriftAgentImplement
#         self.startTimestamp = int(time.time() * 1000)
#         self.version = '1.8.0-RC1'
#     def getWebPort(self):
#         return '8080'

class TestImplement(TestCase):
    def setUp(self) -> None:
        path = os.getcwd()
        self.grpc_config = path+'/conf/collector_grpc.conf'
        self.thrift_config = path+'/conf/collector_thrift.conf'

    def test_thrift(self):
        os.environ['COLLECTOR_CONFIG'] = self.thrift_config
        self.run_app_manager()

    def test_grpc(self):
        os.environ['COLLECTOR_CONFIG'] = self.grpc_config
        self.run_app_manager()

    def run_app_manager(self):
        from Common.Config import CAConfig
        collector_conf = CollectorAgentConf(CAConfig)
        app_management = AppManagement(collector_conf)
        while True:
            # stime =1573438683
            span = '{"name":"PHP Request","FT":1500,' \
                   '"server":"10.34.130.79:28081",' \
                   '"sid":"3345567788","psid":"3345567789","tid":"phpmyadmin^1560951035971^1",' \
                   '"S":1573438683,"E":20,' \
                   '"clues":["46:200"],' \
                   '"uri":"/index.html",' \
                   '"ERR":{"msg":"23456789op[xdcfvgbhnjmk"},' \
                   '"EC":1, "estr":"DIY",' \
                   '"calls":[{"name":"hello","S":1573438683,"E":8,"calls":[{"name":"hello2","1573438683":2,"E":2,"clues":["-1:null","14:2019/06/25"],"calls":[{"name":"hello3","S":1573438683,"E":4}]}]}],' \
                   '"client":"10.10.10.10"}'
            app_management.handle_front_agent_data(None, None, span.encode())
            time.sleep(3)
            # gevent.sleep(1)

# GRPC_TRACE=all;GRPC_VERBOSITY=DEBUG