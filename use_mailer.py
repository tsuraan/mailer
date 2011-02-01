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

msg3 = Message(From="translation@ginstrom.com",
                  To=["translation@ginstrom.com", "software@ginstrom.com"],
                  charset="utf-8")
msg3.Subject = "HTML with Attachment"
msg3.Html = """Hello, <b>日本語</b>"""
msg3.attach("picture.png")
mailer.send(msg3)

# now try specifying the MIME type
msg4 = Message(From="translation@ginstrom.com",
                  To=["translation@ginstrom.com", "software@ginstrom.com"],
                  charset="utf-8")
msg4.Subject = "HTML with Attachment (MIME type specified)"
msg4.Html = """Hello, please have a look at this image."""
msg4.attach("picture.png", mimetype="image/png")
mailer.send(msg4)
