from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from smtplib import SMTP_SSL

from fastapi import FastAPI


from mail_pool import Mails
from tools import get_time_stamp

app = FastAPI()



class VerificationCodePoster():
    def __init__(self, verification_code: str) -> None:
        self.smtp_service = None
        self.pdf_apart = None
        # self.pdf_path = pdf_path
        self.verification_code = verification_code
        self.mail_content = "验证码是\n" + verification_code
        self.mail_title = "输入" + self.verification_code +  "以注册"


    def load_smtp(self):
        """选择smtp服务商"""
        self.smtp_service = random.choice(Mails)
        if self.smtp_service['counts'] > 2:
            Mails.remove(self.smtp_service)
        print("发件邮箱>>>:", self.smtp_service['mail'])

    def sendCode(self, receiver: str, html_content: str):
        self.load_smtp()
        # 发件邮箱
        smtp_server = self.smtp_service['smtp']
        sender_mail = self.smtp_service['mail']
        sender_authentication = self.smtp_service['auth']

        # 邮件内容
        msg = MIMEMultipart('related')
        msg["Subject"] = Header(self.mail_title, 'utf-8')
        print(f"ColumbusK <{sender_mail}>".encode('utf-8'))
        msg["From"] = Header(f"zkz <{sender_mail}>")
        msg["To"] = receiver
        msg["date"] = get_time_stamp()
        # 添加pdf附件
        # msg.attach(self.pdf_apart)
        # HTML部分
        msgAlternative = MIMEMultipart('alternative')
        msgAlternative.attach(MIMEText(html_content, 'html', 'utf-8'))
        msg.attach(msgAlternative)
        # HTML插图
        # fp = open(r'./resource/TheEco_logo.png', 'rb')
        # msgImage1 = MIMEImage(fp.read())
        # fp.close()
        # fp = open(r'./resource/Bilibili_Logo.png', 'rb')
        # msgImage2 = MIMEImage(fp.read())
        # fp.close()
        # 定义图片 ID，在 HTML 文本中引用
        # msgImage1.add_header('Content-ID', '<image1>')
        # msgImage2.add_header('Content-ID', '<image2>')
        # msg.attach(msgImage1)
        # msg.attach(msgImage2)
        # 送信状态标志位
        flag = True
        # 送信主流程
        try:
            with SMTP_SSL(host=smtp_server, port=465) as smtp:
                # 登录发邮件服务器
                smtp.login(user=sender_mail, password=sender_authentication)
                # 实际发送、接收邮件配置
                smtp.sendmail(from_addr=sender_mail,
                              to_addrs=receiver, msg=msg.as_string())
                smtp.quit()
        except Exception as e:
            print(e)
            flag = False
        if flag:
            print(receiver, "邮件发送成功 √")
        else:
            # 失败SMTP计数
            self.smtp_service['counts'] += 1
            print(receiver, "邮件发送失败 ×")
        return flag





# @app.post("/send/email")
# def batch_send(receivers: list, subject: str, contents: list, attachment_path: str):
#     # 1. 配置SMTP服务
#     mail_163 = "columbusknight@163.com"
#     pwd_163 = 'IMZSDHKHDACEZDSY'
#     smtp_163 = 'smtp.163.com'

#     # 2. 邮件内容
#     mail_contents = contents

#     # 3. 实例化SMTP对象
#     mail = yagmail.SMTP(user=Mails[0], password=pwd_163, host=smtp_163)

#     # 4. send方法发送
#     res = mail.send(to=receivers, subject=subject,
#                     contents=mail_contents, attachments=attachment_path)
#     print(res)
#     print(">>>>>> 批量发送完成! <<<<<<")


# sendOne("845265098@qq.com")
