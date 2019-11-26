#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

import psutil

class Disks(Base):

    def info_dict(self, key_name, device_name, values_name, unit_name):
        """
        自定义磁盘信息格式
        :param key_name: 磁盘名称
        :param values_name: 分区名称
        :param unit_name: 磁盘信息单位
        :return:
        """

        info = {}
        info["name"] = key_name
        info["device"] = device_name
        info["value"] = values_name
        info["unit"] = unit_name
        return info

    @property
    def disk(self):
        """
        取磁盘详细信息
        :return:
        """
        disks = psutil.disk_partitions()
        return disks

    @property
    def dev_disk_all(self):
        """
        获取磁盘和挂载点对应关系
        :return:
        """
        mount_dev = {}
        disks = self.disk()

        for i in disks:
            d = {
                i.mountpoint: i.device,
            }
            mount_dev.update(d)
        return mount_dev

    @property
    def disk_mount_point(self):
        """
        获取挂载盘
        :return:
        """
        mount_point = []
        disks = self.disk()
        for i in disks:
            mount_point.append(i.mountpoint)
        return mount_point

    @property
    def usage(self):
        """
        获取所有挂载点磁盘信息，大小、已使用、剩余百分比
        :return:
        """
        point = self.disk_mount_point
        disk_info = {}
        for i in point:
            disk_total = psutil.disk_usage(i)
            disk_info[i] = disk_total
        return disk_info

if __name__ == '__main__':
    a = Disks()
    print a.usage