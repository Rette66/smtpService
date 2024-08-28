import fastapi 
from mail_content import mail_html

from verification_code_poster import VerificationCodePoster


app = fastapi.FastAPI()

@app.get("/sendOne/{receiver}/{verification_code}")
def sendOne(receiver: str, verification_code: str):
    poster = VerificationCodePoster(verification_code)
    temp = mail_html
    temp = temp.replace('{code}', verification_code)
    poster.sendCode(receiver, temp)
    return "sent!"