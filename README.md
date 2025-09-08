# My-Job 프로젝트

## 📋 프로젝트 개요
Odoo 커스터마이징 프로젝트로, Kim's Asia 재고 관리 시스템을 개선하는 작업입니다.

## 🚀 주요 기능
- ✅ **재고 필터링**: Pricelist에서 재고 없는 제품 제외
- ✅ **사용자 권한 관리**: Account Journal 차단 기능
- 🔄 **페이징 기능**: 긴 제품 목록을 페이지별로 표시 (검토 중)

## 📁 프로젝트 구조
```
odoo/
├── custom/
│   └── 20240501-Kim-s-Asia/
│       └── ka_website_sale/
│           └── report/
│               └── product_pricelist_report.py
├── interzero/
│   └── iz_account/
│       └── models/
│           └── account_move.py
├── PROJECT_DOCS.md
├── IMPLEMENTATION_PLAN.md
└── README.md
```

## 🛠️ 기술 스택
- **Odoo**: 17.0
- **Python**: 3.8+
- **PostgreSQL**: 12+
- **JavaScript**: ES6+

## 📊 진행 상황
- [x] 재고 필터링 기능 구현
- [x] 로그 추가 및 테스트
- [x] 로그 제거 및 최종 정리
- [x] Account Journal 차단 기능
- [ ] 페이징 기능 (검토 중)

## 🔗 관련 링크
- [프로젝트 문서](./PROJECT_DOCS.md)
- [구현 계획서](./IMPLEMENTATION_PLAN.md)
- [GitHub 저장소](https://github.com/ggwnsghgg/My-Job)

## 📝 최근 업데이트
- **2025-01-08**: 재고 필터링 기능 구현 완료
- **2025-01-08**: Account Journal 차단 기능 구현 완료
- **2025-01-08**: 프로젝트 문서화 완료

---
*이 프로젝트는 Kim's Asia의 재고 관리 시스템 개선을 위한 Odoo 커스터마이징 작업입니다.*
