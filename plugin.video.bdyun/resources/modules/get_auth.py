#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcaddon, xbmcvfs
import os, sys, re, json 
from resources.modules import auth

dialog = xbmcgui.Dialog()


class VcodeWindow(xbmcgui.WindowDialog):
    def __init__(self, cookie, tokens, vcodetype, codeString, vcode_path):
        self.cookie = cookie
        self.tokens = tokens
        self.vcodetype = vcodetype
        self.codeString = codeString
        self.vcode_path = vcode_path

        # windowItems
        self.image = xbmcgui.ControlImage(80, 100, 500, 200, self.vcode_path)
        self.buttonInput = xbmcgui.ControlButton(
            100, 330, 220, 50, label=u'输入验证码', alignment=6, font='font13', textColor='0xFFFFFFFF'
        )
        self.buttonRefresh = xbmcgui.ControlButton(
            290, 330, 220, 50, label=u'刷新验证码', alignment=6, font='font13', textColor='0xFFFFFFFF'
        )
        self.addControls([self.image, self.buttonInput, self.buttonRefresh])
        self.buttonInput.controlRight(self.buttonRefresh)
        self.buttonRefresh.controlLeft(self.buttonInput)
        self.setFocus(self.buttonInput)


    def onControl(self, event):
        if event == self.buttonInput:
            self.close()
        elif event == self.buttonRefresh:
            (self.codeString, self.vcode_path) = auth.refresh_vcode(self.cookie, self.tokens, self.vcodetype)
            if self.codeString and self.vcode_path:
                self.removeControl(self.image)
                self.image = xbmcgui.ControlImage(80, 100, 500, 200, self.vcode_path)
                self.addControl(self.image)
            else:
                dialog.ok('Error', u'无法刷新验证码，请重试')



# Authorisation Process
def run(username,password):
    token='f2c614657279c3c6ea2da481c17e3344ab4ad299b3172c7ae52ad5da0fa4236b'
    tokens = {'token': token}
    tokens['bdstoken'] = 'f2c614657279c3c6ea2da481c17e3344ab4ad299b3172c7ae52ad5da0fa4236b'
    cookie='BIDUPSID=69D036750DA4F55B9234BDF0015D8DD3; PSTM=1573048057; BAIDUID=69D036750DA4F55B38E3700F13BB23FE:FG=1; PANWEB=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pan_login_way=1; BDSFRCVID=-VLsJeCCxG3D-H6uW6P13FCIaQGYn6HlFT1q3J; H_BDCLCKID_SF=tR3j3Ru8KJjEe-Kk-PnVep81jhbZKxJmMgkeKT6dJtK5qKjgyxJvBPCSQnrXtfvQ3HPDQCOFfD_MMK8lDTtaen-W5gTBKR3a-D60Wt88Kb7VbpRb0MnkbfJBD4bHXP5NJjTULnR9-f5oqnjaj-7VD5L7yajKBlOGX5T9Xt-5Lp35HUPmMPopQT8rQMDOK5OibCru-Jvxab3vOIJNXpO154PzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-Ftqj_s-I6XsJoq2RbhKROvhj4V3xAyyxom3bvxt2PLaIQaQKQmhDODLUrH0f-4hGj72U5nt6CeaDcJ-J8XMKL9j6bP; H_PS_PSSID=1453_21115_30211_30494_30284_30191_22157; delPer=0; PSINO=5; BDUSS=k1UTRETERFZ2g5ZThNM3pGZk9pZHo2ajcxTnRhOXBYSHp2TEpvUVZJb21vVEplSVFBQUFBJCQAAAAAAAAAAAEAAADoPCnGYmluYXJ5QQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACYUC14mFAteNz; STOKEN=f2c614657279c3c6ea2da481c17e3344ab4ad299b3172c7ae52ad5da0fa4236b; SCRC=0e3d89fdc3fd17bbe60eb828b7ca4419; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1577519604,1577547206,1577719362,1577784363; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1577784363; cflag=13%3A3; PANPSC=4771948124322857221%3A7%2FdjZ%2BYU7V3mGU8YTSFORFcS2d9ns3O5g0mIZdLHpdQGbqupDlB1gmTH3eOEOzbc%2FFD%2F%2FL47AHviLaLUl0KD5De4ZdaW7CoOlL98c8Ccr9ch6uZoP3DwQ9YfJggg9xZJx9weu44rnxOmKs46Hp4FtUxxFjP7z0UnUfCieuM2tEsE7lWkT%2FAWsFDj1C1x5%2F3H'
    cookie = parse_cookies(cookie)
    return cookie,tokens

def parse_cookies(cookie):
    cookies = {}
    for c in cookie.split('; '):
        k, v = c.split('=', 1)
        cookies[k] = v
    return cookies