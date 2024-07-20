from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes
from chain import ask_question
from threading import Lock

# API 서버 관련 셋팅
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# 결과를 저장할 딕셔너리
results = {}
lock = Lock()

@app.post("/stream_chat/")
async def stream_chat(request: Request):
    data = await request.json()

    # 'content' 키를 포함하는 딕셔너리 형태로 data를 전달
    input_data = {"question": data["content"], "type": data["type"]}
    print(input_data)
    answer = ask_question(input_data)
    print(answer)
    return {"answer": answer}

@app.get("/get_result/")
async def get_result(message: str):
    with lock:
        result = results.get(message)
    if result:
        return {"answer": result}
    else:
        return {"answer": None}

# api서버 띄우기 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
