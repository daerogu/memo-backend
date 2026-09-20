# Guestbook Backend

## 프로젝트 소개

전체적인 흐름은 소개페이지 -> 방명록남기기 입니다.

클라우드컴퓨팅실습 개인 과제를 위해 제작한 방명록 Backend API입니다.

FastAPI를 이용하여 REST API를 구현하고, Frontend와 연동하여 방명록 데이터를 처리하도록 구성했습니다. Backend는 Render를 통해 배포했습니다.

## 프로젝트 목적

FastAPI를 이용하여 REST API를 구현하고 데이터베이스와 연결하는 Backend 개발 과정을 실습하는 것을 목표로 제작했습니다.

또한 Render에 Backend를 배포하고 Vercel에 배포된 React Frontend와 연결하여 실제 배포 환경에서 Frontend-Backend 간 API 통신이 이루어지는 구조를 구현했습니다.

## 주요 기능

- 방명록 목록 조회 API
- 새로운 방명록 작성 API
- 방명록 삭제 API
- 데이터베이스 연동
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
- GitHub
- Render

## 파일 구성

- `main.py` : FastAPI 애플리케이션, API 및 CORS 설정
- `database.py` : 데이터베이스 연결 설정
- `models.py` : 데이터 모델 정의
- `requirements.txt` : Python 패키지 목록

## 배포 주소

Render

https://memo-backend-yeu0.onrender.com/

FastAPI Swagger UI

https://memo-backend-yeu0.onrender.com/docs

## 관련 프로젝트

- Personal Page  
  https://github.com/daerogu/my-page

- Guestbook Frontend  
  https://github.com/daerogu/memo-frontend

