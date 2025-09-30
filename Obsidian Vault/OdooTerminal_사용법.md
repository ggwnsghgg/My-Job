# OdooTerminal 사용법 정리

## 1. OdooTerminal이란?
OdooTerminal은 Odoo ERP의 데이터베이스와 모델을 명령어로 직접 다루는 커맨드라인(CLI) 도구입니다. 개발자, 운영자, 컨설턴트가 데이터 조회, 수정, 디버깅, 대량 작업 등에 활용합니다.

---

## 2. 주요 명령어

| 명령어 예시                         | 설명                                                                              |
| ------------------------------ | ------------------------------------------------------------------------------- |
| `search <모델명> [조건]`            | 모델의 레코드 목록 조회<br>예: `search account.move`, `search res.partner is_company=True` |
| `show <모델명> <id>`              | 특정 레코드 상세 조회<br>예: `show account.move 47`                                       |
| `create <모델명> <필드=값 ...>`      | 새 레코드 생성<br>예: `create res.partner name="테스트" is_company=True`                  |
| `write <모델명> <id> <필드=값 ...>`  | 특정 레코드 수정<br>예: `write account.move 47 state="posted"`                          |
| `delete <모델명> <id>`            | 특정 레코드 삭제                                                                       |
| `call <모델명> <id> <메서드> [파라미터]` | 모델의 메서드 직접 호출<br>예: `call account.move 47 action_post`                          |
| `fields <모델명>`                 | 모델의 필드 목록과 타입 확인                                                                |
| `help <명령어>`                   | 명령어별 사용법 안내                                                                     |

---

## 3. 활용 예시
- 대량 데이터 점검 및 수정
- 테스트 데이터 생성/삭제
- 특정 조건의 레코드 빠른 검색
- 워크플로우(예: 인보이스 승인) 직접 실행
- 개발 중 ORM 동작 확인 및 디버깅

---

## 4. 주의사항 및 한계
- 실시간 DB에 직접 접근하므로, 실수로 데이터 손상 가능 → 운영 환경에서는 주의 필요
- 복잡한 트랜잭션/관계형 데이터는 GUI보다 CLI가 더 어려울 수 있음
- 일부 명령어/옵션은 Odoo 버전, Terminal Addon 버전에 따라 다를 수 있음

---

## 5. 기타
- Odoo 공식 shell(odoo shell, odoo-bin shell)과 유사하지만, OdooTerminal은 좀 더 직관적이고 명령어 기반입니다.
- 커스텀 명령어, 스크립트 실행 등도 지원할 수 있습니다.

---

## 6. 참고
- 더 궁금한 점이나 실무 예시가 필요하면 언제든 문의하세요! 