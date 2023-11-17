import imaplib

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("baolong22.aws@gmail.com", "mnxt arel ztvd yvjg")
mail.select("inbox")
print(mail)
