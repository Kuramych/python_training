# -*- coding: utf-8 -*-
from model.contact import Contact



def test_contact(app):
    app.fixture_contact.contact.create_contact(Contact("adsad", "sfdsdf", "vxcxv", "hfghfgh", "xcvvx", "fjhfgjf", "cxzczcxzv", "chcnvc",
                               "dsfdsdf", "qewter", "jkghjgjg", "cbvbcncn", "fghfhfghf", "asdasad", "vbxcnbn", "1",
                               "April", "2000", "4", "February", "2010", "gfdgdg", "bvcbcbv", "gfdgdgdg"))

