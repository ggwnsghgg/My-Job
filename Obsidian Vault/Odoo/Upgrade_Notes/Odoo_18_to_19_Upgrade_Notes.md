# Odoo 18에서 19 버전 업그레이드 변경사항

## 1. Python 버전 요구사항

- **최소 버전**: Python 3.10
- **최대 버전**: Python 3.13
- **현재 사용 중**: Python 3.11 ✅

## 2. 의존성 패키지 변경

### 새로 추가된 패키지
- **cbor2**: auth_passkey 모듈에서 사용
  - Python < 3.12: cbor2==5.4.2
  - Python >= 3.12: cbor2==5.6.2

### 누락된 패키지 (설치 필요)
- **asn1crypto**: auth_passkey 모듈의 webauthn 기능에서 사용
  - Python < 3.11: asn1crypto==1.4.0
  - Python >= 3.11: asn1crypto==1.5.1

### PostgreSQL 확장 (설치 완료)
- **pgvector**: AI 모듈에서 사용하는 벡터 데이터베이스 확장
  - AI 기능 (벡터 검색, 임베딩 등)에 필수
  - PostgreSQL 12+ 버전에서 지원
  - **해결 방법**: PostgreSQL 17용 파일을 PostgreSQL 14 디렉토리에 수동 복사
  - **추가 작업**: `/opt/homebrew/share/postgresql@14/extension/` 경로에 파일 복사 완료
  - **최종 해결**: PostgreSQL 14용 소스 컴파일 및 설치 완료

### 기존 패키지 버전 업데이트
- cryptography: 3.4.8 → 42.0.8 (Python >= 3.12)
- gevent: 21.8.0 → 24.11.1 (Python >= 3.13)
- greenlet: 1.1.2 → 3.1.1 (Python >= 3.13)
- Pillow: 9.0.1 → 11.1.0 (Python >= 3.13)
- psycopg2: 2.9.2 → 2.9.10 (Python >= 3.13)
- reportlab: 3.6.8 → 4.1.0 (Python >= 3.12)
- requests: 2.25.1 → 2.31.0 (Python >= 3.11)
- Werkzeug: 2.0.2 → 3.0.1 (Python >= 3.12)

## 3. 모듈 관련 변경사항

### auth_passkey 모듈
- WebAuthn 표준을 사용한 패스키 인증 기능 추가
- cbor2 의존성 필요
- webauthn 관련 기능 구현

### 모듈 로딩 이슈
- `lu_web` 모듈 로딩 실패
- 일부 모듈의 의존성이나 manifest 파일 누락 가능성

## 4. 에셋 번들링 변경
- bus.websocket_worker_assets.min.js 파일 생성 과정 변경
- 웹소켓 워커 관련 에셋 처리 방식 개선

## 5. 해결된 문제들
- ✅ cbor2 패키지 설치 완료
- ✅ asn1crypto 패키지 설치 완료
- ✅ PostgreSQL pgvector 확장 설치 완료 (PostgreSQL 14용 수동 복사)
- ⏳ lu_web 모듈 로딩 문제 해결 필요
- ⏳ 기타 모듈 의존성 문제 확인 필요

## 6. Odoo 19 Enterprise 모듈 활성화

### 핵심 Enterprise 모듈들 (데이터베이스에서 활성화 필요)
1. **base** - 기본 Enterprise 기능
2. **web** - 웹 인터페이스 개선
3. **web_enterprise** - Enterprise 웹 기능
4. **mail_enterprise** - 고급 메일 기능
5. **calendar** - 캘린더 기능
6. **contacts** - 연락처 관리
7. **crm** - CRM 기능
8. **sale** - 판매 관리
9. **purchase** - 구매 관리
10. **account** - 회계 기능
11. **stock** - 재고 관리
12. **hr** - 인사 관리
13. **project** - 프로젝트 관리
14. **helpdesk** - 헬프데스크
15. **knowledge** - 지식 관리
16. **documents** - 문서 관리
17. **spreadsheet** - 스프레드시트
18. **ai** - AI 기능
19. **auth_passkey** - 패스키 인증
20. **digest** - 요약 보고서

### 모듈 활성화 방법
1. Odoo 웹 인터페이스 접속
2. Apps 메뉴 → 업데이트 앱 목록
3. 위 모듈들을 검색하여 설치
4. 또는 데이터베이스 생성 시 자동 설치

## 7. 주의사항
- Python 버전에 따라 다른 패키지 버전 요구
- 기존 커스텀 모듈들의 호환성 확인 필요
- 데이터베이스 마이그레이션 시 주의 필요
- Enterprise 모듈들은 별도 라이선스 필요

---
*업데이트 날짜: 2025-09-30*
*Odoo 19 버전 업그레이드 진행 중*
