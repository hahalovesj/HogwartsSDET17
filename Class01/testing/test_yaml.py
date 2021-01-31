#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml


def test_yaml():
    with open("datas/calc.yml") as f:
        data = yaml.safe_load(f)
        print(data)
        print(data['add']['datas'])