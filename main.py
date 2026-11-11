# S0 闸门 T1 · hello-api —— 本文件由 Loomy 于 2026-11-11 代写（S0 assisted，用户选择 B 案）
# 依据: https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "ok"}
