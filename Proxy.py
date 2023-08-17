#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rab_models/Proxy.py
# @DATE: 2023/05/17 Wed
# @TIME: 14:58:53
#
# @DESCRIPTION: 代理模型


import uuid
from sqlalchemy import Column, String, Text, Boolean, DateTime, Integer

from external.rab_common import orm as external_rab_common_orm


# ORM 基类 Base
ORM_BASE = external_rab_common_orm.Base


class Proxy(ORM_BASE):
    """
    @description: 代理模型
    """

    # === 表名 ===
    __tablename__ = "pp_proxy"
    # === 表结构 ===
    id = Column(String(32), nullable=True, comment="ID")
    # === 代理基础信息 ===
    host = Column(String(255), primary_key=True, comment="【主键】代理 Host")
    port = Column(Integer, primary_key=True, comment="【主键】代理 Port")
    # 是否支持 HTTP
    is_http_available = Column(Boolean, nullable=True, comment="是否支持 HTTP")
    # 是否支持 SOLCKS5
    is_socks5_available = Column(Boolean, nullable=True, comment="是否支持 SOLCKS5")
    # 用户名和密码
    username = Column(String(255), primary_key=True, comment="【主键】用户名")
    password = Column(String(255), nullable=True, comment="密码")
    # 是否中国可用
    is_china_available = Column(Boolean, nullable=True, comment="是否中国可用")
    # 备注
    remark = Column(Text, nullable=True, comment="备注")
    # === 供应商信息 ===
    # 代理供应商 ID
    provider_id = Column(String(255), nullable=True, comment="代理供应商 ID")
    # 代理供应商类型
    provider_type = Column(String(255), nullable=True, comment="代理供应商类型")
    # === 订阅相关信息 ===
    # 订阅 ID
    subscription_id = Column(String(32), nullable=True, comment="订阅 ID（如果有的话）")
    # === 节点相关信息 ===
    # 节点 ID
    node_id = Column(String(255), nullable=True, comment="节点 ID（如果有的话）")
    # === 代理实际信息 ===
    # 出口 IP
    exit_ip = Column(String(255), nullable=True, comment="出口 IP")
    # 是否支持 IPv4
    is_ipv4_available = Column(Boolean, nullable=True, comment="是否支持 IPv4")
    # 是否支持 IPv6
    is_ipv6_available = Column(Boolean, nullable=True, comment="是否支持 IPv6")
    # 国家代码
    country_code = Column(String(255), nullable=True, comment="国家代码")
    # 地区
    region = Column(String(255), nullable=True, comment="地区")
    # 城市
    city = Column(String(255), nullable=True, comment="城市")
    # 经度
    longitude = Column(String(255), nullable=True, comment="经度")
    # 纬度
    latitude = Column(String(255), nullable=True, comment="纬度")
    # 时区
    timezone = Column(String(255), nullable=True, comment="时区")
    # ASN
    asn = Column(String(255), nullable=True, comment="ASN")
    # 组织
    organization = Column(String(255), nullable=True, comment="组织")
    # ASN 名称
    asn_name = Column(String(255), nullable=True, comment="ASN 名称")
    # ASN 类型
    asn_type = Column(String(255), nullable=True, comment="ASN 类型")
    # ASN 域名
    asn_domain = Column(String(255), nullable=True, comment="ASN 域名")
    # ASN 路由
    asn_route = Column(String(255), nullable=True, comment="ASN 路由")
    # === 代理匿名信息 ===
    # 是否是 VPN
    is_privacy_vpn = Column(Boolean, nullable=True, comment="是否是 VPN")
    # 是否是代理
    is_privacy_proxy = Column(Boolean, nullable=True, comment="是否是代理")
    # 是否是 TOR
    is_privacy_tor = Column(Boolean, nullable=True, comment="是否是 TOR")
    # 是否是中继
    is_privacy_relay = Column(Boolean, nullable=True, comment="是否是中继")
    # 是否是机房托管
    is_privacy_hosting = Column(Boolean, nullable=True, comment="是否是机房托管")
    # === 更新相关 ===
    # 基础测试时间间隔（秒）
    base_test_interval = Column(Integer, nullable=True, comment="基础测试时间间隔（秒）")
    # 上次基础测试时间
    last_base_test_at = Column(DateTime, nullable=True, comment="上次基础测试时间")
    # 下次基础测试时间
    next_base_test_at = Column(DateTime, nullable=True, comment="下次基础测试时间")
    # === 创建者和更新者信息 ===
    created_by = Column(String(255), nullable=True, comment="创建者 ID")
    created_by_name = Column(String(255), nullable=True, comment="创建者名称")
    created_at = Column(DateTime, nullable=True, comment="创建时间")
    updated_by = Column(String(255), nullable=True, comment="更新者 ID")
    updated_by_name = Column(String(255), nullable=True, comment="更新者名称")
    updated_at = Column(DateTime, nullable=True, comment="更新时间")

    def __init__(self, host, port, is_http_available, is_socks5_available, username, password, is_china_available, remark, provider_id, provider_type, subscription_id, node_id, base_test_interval):
        """
        @description: 初始化
        @param {str} host 代理 Host
        @param {int} port 代理 Port
        @param {bool} is_http_available 是否支持 HTTP
        @param {bool} is_socks5_available 是否支持 SOLCKS5
        @param {str} username 用户名
        @param {str} password 密码
        @param {bool} is_china_available 是否中国可用
        @param {str} provider_id 代理供应商 ID
        @param {str} provider_type 代理供应商类型
        @param {str} subscription_id 订阅 ID
        @param {str} node_id 节点 ID
        """
        self.id = uuid.uuid4().hex
        self.host = host
        self.port = port
        self.is_http_available = is_http_available
        self.is_socks5_available = is_socks5_available
        self.username = username
        self.password = password
        self.is_china_available = is_china_available
        self.remark = remark
        self.provider_id = provider_id
        self.provider_type = provider_type
        self.subscription_id = subscription_id
        self.node_id = node_id
        self.base_test_interval = base_test_interval
    
    def clear_test_base_result(self):
        """
        @description: 清除测试相关结果
        """
        self.exit_ip = None
        self.is_ipv4_available = None
        self.is_ipv6_available = None
        self.country_code = None
        self.region = None
        self.city = None
        self.longitude = None
        self.latitude = None
        self.timezone = None
        self.asn = None
        self.organization = None
        self.asn_name = None
        self.asn_type = None
        self.asn_domain = None
        self.asn_route = None
        self.is_privacy_vpn = None
        self.is_privacy_proxy = None
        self.is_privacy_tor = None
        self.is_privacy_relay = None
        self.is_privacy_hosting = None

    def to_dict(self):
        """
        @description: 转换为字典
        """
        return {
            "id": self.id,
            "host": self.host,
            "port": self.port,
            "is_http_available": self.is_http_available,
            "is_socks5_available": self.is_socks5_available,
            "username": self.username,
            "password": self.password,
            "is_china_available": self.is_china_available,
            "remark": self.remark,
            "provider_id": self.provider_id,
            "provider_type": self.provider_type,
            "subscription_id": self.subscription_id,
            "node_id": self.node_id,
            "exit_ip": self.exit_ip,
            "is_ipv4_available": self.is_ipv4_available,
            "is_ipv6_available": self.is_ipv6_available,
            "country_code": self.country_code,
            "region": self.region,
            "city": self.city,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "timezone": self.timezone,
            "asn": self.asn,
            "organization": self.organization,
            "asn_name": self.asn_name,
            "asn_type": self.asn_type,
            "asn_domain": self.asn_domain,
            "asn_route": self.asn_route,
            "is_privacy_vpn": self.is_privacy_vpn,
            "is_privacy_proxy": self.is_privacy_proxy,
            "is_privacy_tor": self.is_privacy_tor,
            "is_privacy_relay": self.is_privacy_relay,
            "is_privacy_hosting": self.is_privacy_hosting,
            "base_test_interval": self.base_test_interval,
            "last_base_test_at": self.last_base_test_at,
            "next_base_test_at": self.next_base_test_at,
            "created_by": self.created_by,
            "created_by_name": self.created_by_name,
            "created_at": self.created_at,
            "updated_by": self.updated_by,
            "updated_by_name": self.updated_by_name,
            "updated_at": self.updated_at
        }