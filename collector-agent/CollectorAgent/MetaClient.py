#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by eeliu at 11/5/19
import Service_pb2_grpc
from CollectorAgent.GrpcClient import GrpcClient
from Common.Logger import TCLogger
from Span_pb2 import PSqlMetaData, PApiMetaData, PStringMetaData


class MetaClient(GrpcClient):
    def __init__(self,address,meta=None):
        super().__init__(address, meta,-1)
        self.meta_stub=Service_pb2_grpc.MetadataStub(self.channel)
        self.is_ok = False
        self.id = 0
        self.sql_table = {}
        self.api_table = {}
        self.string_table={}

    def _send_sql_meta(self,meta):
        assert isinstance(meta,PSqlMetaData)
        future = self.meta_stub.RequestSqlMetaData.future(meta)
        future.add_done_callback(self._response)

    def _send_api_meta(self, meta):
        assert isinstance(meta, PApiMetaData)
        future = self.meta_stub.RequestApiMetaData.future(meta)
        future.add_done_callback(self._response)

    def _send_string_meta(self, meta):
        assert isinstance(meta, PStringMetaData)
        future = self.meta_stub.RequestStringMetaData.future(meta)
        future.add_done_callback(self._response)

    def update_api_meta(self, apiInfo, line, type):
        row_str = ("%s-%d-%d"%(apiInfo,line,type))
        if row_str in self.api_table:
            return self.api_table[row_str][0]
        else:
            id = self.id
            meta = PApiMetaData(apiId=id, apiInfo=apiInfo,line=line,type=type)
            self.api_table[row_str] = [id, meta]
            self._send_api_meta(meta)
            self.id += 1
            TCLogger.debug("register api meta id:%d -> api:[%s]", id, row_str)
            return id

    def update_string_meta(self, value):
        if value in self.string_table:
            return self.string_table[value][0]
        else:
            id = self.id
            meta = PStringMetaData(stringId=id,stringValue=value)
            self.string_table[value] = [id, meta]
            self._send_string_meta(meta)
            self.id += 1
            TCLogger.debug("register string meta id:%d -> value:[%s]",id,value)
            return id

    def update_sql_meta(self,sql):
        if sql in self.sql_table:
            return self.sql_table[sql][0]
        else:
            id = self.id
            meta = PSqlMetaData(sqlId=id,sql=sql)
            self.sql_table[sql] = [id,meta]
            self._send_sql_meta(meta)
            self.id+=1
            TCLogger.debug("register sql meta id:%d -> sql:[%s]", id, sql)
            return id

    def _response(self,future):
        if future.exception():
            TCLogger.warning("register meta failed %s",future.exception)
            return
        TCLogger.debug(future.result())

    def channel_set_ready(self):
        self.is_ok = True
        self._register_all_meta()

    def channel_set_idle(self):
        self.is_ok = True

    def channel_set_error(self):
        self.is_ok = False

    def _register_all_meta(self):
        # register sql
        for key,value in self.sql_table.items():
            self._send_sql_meta(value[1])
        # api
        for key,value in self.api_table.items():
            self._send_api_meta(value[1])
        # string
        for key,value in self.string_table.items():
            self._send_string_meta(value[1])