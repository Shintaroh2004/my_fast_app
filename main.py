from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel  # リクエストbodyを定義するために必要
from typing import List  # ネストされたBodyを定義するために必要
import uvicorn

app = FastAPI()


# リクエストbodyを定義
class User(BaseModel):
    user_id: int
    name: str


# シンプルなJSON Bodyの受け取り
@app.post("/user")
# 上で定義したUserモデルのリクエストbodyをuserで受け取る
# user = {"user_id": 1, "name": "太郎"}
def create_user(user: User):
    # レスポンスbody
    return {"res": "ok", "ID": user.user_id, "name": user.name}

app.mount("/", StaticFiles(directory="static",html=True), name="static")

#コード上でuvicornの起動
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)