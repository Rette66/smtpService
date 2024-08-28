mail_html = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>验证码邮件</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333333;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .header {
            text-align: center;
            border-bottom: 1px solid #eeeeee;
            padding-bottom: 20px;
            margin-bottom: 20px;
        }
        .header h1 {
            font-size: 24px;
            color: #333333;
        }
        .content {
            text-align: center;
            font-size: 18px;
            line-height: 1.6;
        }
        .code {
            font-size: 24px;
            font-weight: bold;
            color: #007bff;
            margin: 20px 0;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #777777;
            border-top: 1px solid #eeeeee;
            padding-top: 20px;
            margin-top: 20px;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #ffffff;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>验证码验证</h1>
        </div>
        <div class="content">
            <p>亲爱的用户，</p>
            <p>您正在进行账号安全验证，您的验证码如下：</p>
            <div class="code">{code}</div> <!-- 在这里替换成实际的验证码 -->
            <p>请在10分钟内使用该验证码完成验证。</p>
            <a href="#" class="button">立即验证</a> <!-- 如果有链接可用，替换href -->
        </div>
        <div class="footer">
            <p>如果您没有请求此操作，请忽略此邮件。</p>
            <p>感谢您的使用！</p>
        </div>
    </div>
</body>
</html>"""
