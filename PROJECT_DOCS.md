# Odoo 프로젝트 문서

## 프로젝트 개요
- **프로젝트명**: Kim's Asia 재고 관리 시스템 개선
- **목표**: Pricelist에서 재고 없는 제품 제외 기능 구현
- **기간**: 2025년 1월
- **담당자**: 개발팀

## 구현 계획
- [x] 재고 필터링 기능 구현
- [x] 로그 추가 및 테스트
- [x] 로그 제거 및 최종 정리
- [ ] 페이징 기능 (검토 중)
- [ ] 사용자 권한 관리 (완료)

## 구현 내용

### 1. 재고 필터링 기능

#### 문제점
- Pricelist에서 재고가 없는 제품까지 표시됨
- 고객이 주문할 수 없는 제품이 목록에 포함됨

#### 해결 방안
- `qty_available > 0` 조건 추가
- 유통기한 체크 로직 유지

#### Before (변경 전)
```python
# product_pricelist_report.py
products = ProductClass.browse(active_ids).filtered(
    lambda p: any(
        not q.use_expiration_date or (q.use_expiration_date and q.removal_date and q.removal_date >= now)
        for q in p.product_variant_ids.stock_quant_ids
    )
)
```

#### After (변경 후)
```python
# product_pricelist_report.py
products = ProductClass.browse(active_ids).filtered(
    lambda p: p.qty_available > 0 and any(
        not q.use_expiration_date or (q.use_expiration_date and q.removal_date and q.removal_date >= now)
        for q in p.product_variant_ids.stock_quant_ids
    )
)
```

#### 변경 사항
1. **재고 수량 체크**: `p.qty_available > 0` 조건 추가
2. **검색 쿼리**: `('qty_available', '>', 0)` 조건 추가
3. **결과**: 재고가 없는 제품은 Pricelist에서 제외됨

### 2. 로그 추가 및 테스트

#### 추가된 로그
- 시작 로그: 모델과 ID 정보
- 총 제품 수: 체크할 전체 제품 수
- 재고 없는 제품: 제외된 제품 목록
- 유통기한 만료 제품: 제외된 제품 목록
- 최종 결과: 포함된 제품 수와 이름

#### 테스트 결과
- ✅ 재고 없는 제품 정상 제외
- ✅ 유통기한 만료 제품 정상 제외
- ✅ 재고 있는 제품만 Pricelist에 표시

### 3. 로그 제거 및 최종 정리

#### 제거된 내용
- 모든 `_logger.info()` 로그 출력문
- 디버깅용 임시 변수들

#### 유지된 기능
- 재고 필터링 로직
- 유통기한 체크 로직
- 제품 정렬 기능

## 기술적 세부사항

### 사용된 필드
- `qty_available`: 실제 사용 가능한 재고 수량
- `use_expiration_date`: 유통기한 사용 여부
- `removal_date`: 유통기한 날짜

### 성능 고려사항
- `qty_available`은 계산된 필드이므로 성능에 영향
- 대량 데이터 처리 시 인덱스 고려 필요

## 다음 단계
- [ ] 페이징 기능 구현 검토
- [ ] 성능 최적화
- [ ] 사용자 피드백 수집

## 참고 자료
- Odoo 공식 문서: Product Template
- Kim's Asia 모듈: ka_website_sale
- 파일 위치: `/custom/20240501-Kim-s-Asia/ka_website_sale/report/product_pricelist_report.py`
