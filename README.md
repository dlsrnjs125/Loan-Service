# Loan Service

Django REST Framework 기반 대출 서비스 API

## 🚀 시작하기

### 필수 요구사항
- Python 3.11+
- PostgreSQL (선택사항, 개발 환경에서는 SQLite 사용)
- Make (선택사항, Makefile 사용 시)

### 빠른 시작 (Makefile 사용)

```bash
# 1. 의존성 설치
make install

# 2. 데이터베이스 마이그레이션
make migrate

# 3. 개발 서버 실행
make local          # 포그라운드 실행
make local bg       # 백그라운드 실행

# 4. 서버 종료
make stop           # 서버만 종료
make clean          # 서버 종료 + 정리
```

### 수동 설치 및 실행

1. **가상환경 생성 및 활성화**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **의존성 설치**
```bash
pip install -r requirements.txt
```

3. **환경 변수 설정 (선택사항)**
```bash
cp .env.example .env
# .env 파일을 편집하여 데이터베이스 설정 등을 구성하세요
# 개발 환경에서는 SQLite를 기본으로 사용합니다
```

4. **데이터베이스 마이그레이션**
```bash
python manage.py migrate
```

5. **슈퍼유저 생성 (선택사항)**
```bash
python manage.py createsuperuser
```

6. **개발 서버 실행**
```bash
python manage.py runserver
```

### Makefile 명령어

```bash
make help           # 도움말 표시
make install        # 의존성 설치
make local          # 개발 서버 실행 (포그라운드)
make local bg       # 개발 서버 실행 (백그라운드)
make migrate        # 마이그레이션 실행
make makemigrations # 마이그레이션 파일 생성
make check          # Django 시스템 체크
make shell          # Django shell 실행
make createsuperuser # 슈퍼유저 생성
make stop           # 서버 종료
make clean          # 서버 종료 및 정리
make test           # 테스트 실행
```

서버가 실행되면 다음 URL에서 접근할 수 있습니다:
- API 문서: http://localhost:8000/api/docs/
- Admin: http://localhost:8000/admin/
- ReDoc: http://localhost:8000/api/redoc/

## 📁 프로젝트 구조

```
Loan-Service/
├── api/                    # API 라우팅
│   └── v1/                 # API 버전 1
├── apps/                   # Django 앱
│   ├── core/               # 공통 모델 및 유틸리티
│   └── loans/              # 대출 도메인 앱 (구현 예정)
├── config/                 # 프로젝트 설정
│   ├── settings/           # 환경별 설정
│   │   ├── base.py        # 기본 설정
│   │   ├── development.py # 개발 환경 설정
│   │   └── production.py  # 프로덕션 환경 설정
│   ├── urls.py            # 메인 URL 설정
│   ├── wsgi.py            # WSGI 설정
│   └── asgi.py            # ASGI 설정
├── templates/              # Django 템플릿 (고객용/직원용)
│   ├── base.html
│   ├── customer/
│   └── staff/
├── static/                 # 정적 파일 (CSS, JS)
│   └── css/
├── manage.py              # Django 관리 스크립트
├── requirements.txt       # Python 의존성
└── README.md              # 프로젝트 문서
```

## 🏗️ 아키텍처

- **Framework**: Django 4.2 + Django REST Framework
- **Database**: SQLite (개발), PostgreSQL (프로덕션)
- **API Documentation**: drf-spectacular (Swagger/OpenAPI)

## 📝 현재 상태

### ✅ 완료된 초기 세팅
- Django 프로젝트 기본 구조
- Swagger/OpenAPI 문서화 설정
- 템플릿 폴더 구조 (고객용/직원용)
- 데이터베이스 연결 설정 (SQLite 기본)
- 기본 모델 구조 (BaseModel)

### 🔜 구현 예정
- 대출 도메인 모델 (대출상품, 고객, 신청, 심사, 계약, 상환 등)
- API 엔드포인트
- 서비스 레이어 (도메인 로직)
- 템플릿 뷰 (고객용/직원용 페이지)

## 🔧 개발

### 마이그레이션 생성
```bash
python manage.py makemigrations
python manage.py migrate
```

### 테스트 실행
```bash
python manage.py test
```

## 📚 API 문서

API 문서는 `/api/docs/`에서 확인할 수 있습니다.
현재는 초기 세팅 상태로, 대출 도메인 API는 구현 예정입니다.
