# !/usr/bin/env python3  Line 1
# -*- coding: Windows-1252 -*- Line 2

import unittest
import aos_methods as methods

class AosAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.topmenu()
        methods.contact_us()
        methods.adduser()
        methods.logout()
        methods.login()
        methods.shoppingcart()
        methods.orders()
        methods.delete_user()
        methods.tearDown()
        print('''             /\.../\          
            (  •.•  )           
             ..=*=..            
       **~~( .\.||./ )  ©Have a kitty day! ''')
