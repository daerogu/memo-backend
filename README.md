# 방명록 Backend

전체 과제는 개인 소개 페이지 → 방명록 Frontend → FastAPI Backend → Supabase Database 구조로 구성되어 있습니다.

## 프로젝트 소개

클라우드컴퓨팅실습 개인 과제를 위해 제작한 방명록 Backend API입니다.

FastAPI를 이용하여 REST API를 구현하고, Frontend와 연동하여 방명록 데이터를 처리하도록 구성했습니다. 
작성된 방명록 데이터는 Supabase 데이터베이스에 저장되며, Backend는 Render를 통해 배포했습니다.

## 프로젝트 목적

FastAPI를 이용하여 REST API를 구현하고 Supabase 데이터베이스와 연결하는 Backend 개발 과정을 실습하는 것을 목표로 제작했습니다.

또한 Render에 Backend를 배포하고 Vercel에 배포된 React Frontend와 연결하여 실제 배포 환경에서 Frontend-Backend-Database 간 데이터 통신이 이루어지는 구조를 구현했습니다.

전체적인 데이터 흐름은 다음과 같습니다.

## 전체 데이터 흐름

- **React Frontend (Vercel)**
  - 사용자 입력 처리
  - FastAPI Backend에 `fetch` 요청

  ↓

- **FastAPI Backend (Render)**
  - REST API 요청 처리
  - SQLAlchemy를 통해 Database와 연결

  ↓

- **Supabase Database**
  - 방명록 데이터 저장 및 유지

## 주요 기능

- 방명록 목록 조회 API
- 새로운 방명록 작성 API
- 방명록 삭제 API
- Supabase 데이터베이스 연동
- Supabase를 통한 방명록 데이터 저장 및 유지
- CORS 설정을 통한 Frontend 연동
- FastAPI Swagger UI 제공
- Render를 통한 Backend 배포

주요 API는 다음과 같습니다.

- `GET /memos` : 방명록 목록 조회
- `POST /memos` : 새로운 방명록 작성
- `DELETE /memos/{id}` : 방명록 삭제

## 사용 기술

- Python
- FastAPI
- SQLAlchemy
- Supabase
- GitHub
- Render

## 파일 구성

- `main.py` : FastAPI 애플리케이션, API 및 CORS 설정
- `database.py` : Supabase 데이터베이스 연결 설정
- `models.py` : 데이터 모델 정의
- `requirements.txt` : Python 패키지 목록

## 배포 주소

| 구분 | 주소 |
| --- | --- |
| 개인 소개 페이지 | https://my-page-lake-gamma.vercel.app/ |
| 방명록 Frontend | https://memo-frontend-sand.vercel.app/ |
| 방명록 Swagger UI | https://memo-backend-yeu0.onrender.com/docs |

## GitHub 저장소

| 프로젝트 | 저장소 |
| --- | --- |
| 개인 소개 페이지 | https://github.com/daerogu/my-page |
| 방명록 Frontend | https://github.com/daerogu/memo-frontend |
| 방명록 Backend | https://github.com/daerogu/memo-backend |