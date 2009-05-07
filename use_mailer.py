#coding: UTF8
"""
Design Patterns in Python
listing 1 for Chapter 3

"""

from mailer import Mailer
from mailer import Message
import urllib

msg1 = Message(From="translation@ginstrom.com",
                  To=["translation@ginstrom.com", "software@ginstrom.com"],
                  charset="utf-8")
msg1.Subject = "日本語のHTMLメール"
msg1.Html = """Hello, <b>日本語</b>"""

mailer = Mailer('smtp01.odn.ne.jp')

msg2 = Message(Body="ナイスボディー!", attachments=["picture.png"])
msg2.From = "translation@ginstrom.com"
msg2.To = "translation@ginstrom.com"
msg2.Subject = "日本語の添付ファイルメール"
msg2.charset = "utf-8"

mailer.send([msg1, msg2])

msg = Message()
msg.From = "translation@ginstrom.com"
msg.To = "translation@ginstrom.com"
msg.Subject = "テキストメール"
msg.Body = "これは日本語のキストメールでございます。"
msg.charset = "utf-8"
mailer.send(msg)

