#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib as plt
import CleanDataFun as clean


def allParcableCountryData():
    us = clean.cleanData('../Data/Youtube/USvideos.csv', '../Data/Youtube/US_category_id.json', "latin_1")
    mx= clean.cleanData('../Data/Youtube/MXvideos.csv', '../Data/Youtube/MX_category_id.json', "latin_1")
    ca=clean.cleanData('../Data/Youtube/CAvideos.csv', '../Data/Youtube/CA_category_id.json', "latin_1")
    de=clean.cleanData('../Data/Youtube/DEvideos.csv', '../Data/Youtube/DE_category_id.json', "latin_1")
    gb=clean.cleanData('../Data/Youtube/GBvideos.csv', '../Data/Youtube/GB_category_id.json', "latin_1")
    ind=clean.cleanData('../Data/Youtube/INvideos.csv', '../Data/Youtube/IN_category_id.json', "latin_1")
    fr=clean.cleanData('../Data/Youtube/FRvideos.csv', '../Data/Youtube/FR_category_id.json', "latin_1")
    us["country"] = "us"
    mx["country"] = "mx"
    ca["country"] = "ca"
    de["country"] = "de"
    gb["country"] = "gb"
    ind["country"] = "in"
    fr["country"] = "fr"
    data = us.append([mx,ca,de,gb,ind,fr])
    return data




