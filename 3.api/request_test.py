from langserve import RemoteRunnable


# langserve식 stream api request입니다.
chain = RemoteRunnable("http://172.207.35.30:8004/prompt/")

for token in chain.stream({"question":"파주시 관광 명소 추천해줘"}):
    print(token)    