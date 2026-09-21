import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="방명록 API",
    description="클라우드컴퓨팅실습 개인과제 — 개인 소개 페이지의 방명록 Frontend(Vercel)에서 호출하는 Backend API",
    version="1.0.0",
    openapi_tags=[
        {"name": "안내", "description": "서비스 상태 확인"},
        {"name": "방명록", "description": "방명록 조회 · 작성 · 삭제"},
    ],
)

@app.get("/", tags=["안내"])
def root():
    return {
        "service": "방명록 API",
        "docs": "/docs",
        "frontend": "https://memo-frontend-sand.vercel.app/",
    }

# ── CORS: 허용 출처를 환경변수로 (배포 시 Vercel 주소로) ──
origins = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:5173"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청마다 DB 세션을 열고, 끝나면 반드시 닫는 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class MemoIn(BaseModel):
    content: str


class MemoOut(BaseModel):
    id: int
    content: str

    model_config = {"from_attributes": True}


@app.get(
    "/memos",
    response_model=list[MemoOut],
    tags=["방명록"],
    summary="방명록 목록 조회",
)
def list_memos(db: Session = Depends(get_db)):
    return db.query(models.Memo).all()


@app.post(
    "/memos",
    response_model=MemoOut,
    tags=["방명록"],
    summary="새 방명록 작성",
)
def create_memo(memo: MemoIn, db: Session = Depends(get_db)):
    new = models.Memo(content=memo.content)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


@app.delete(
    "/memos/{memo_id}",
    tags=["방명록"],
    summary="방명록 삭제",
)
def delete_memo(memo_id: int, db: Session = Depends(get_db)):
    obj = db.get(models.Memo, memo_id)

    if not obj:
        raise HTTPException(
            status_code=404,
            detail="Memo not found",
        )

    db.delete(obj)
    db.commit()

    return {"ok": True}