# Odoo QWeb 스타일 조정 방법

## 1. 개요
Odoo QWeb 리포트에서 값이 잘리거나 정렬이 안 되는 문제를 해결하는 방법들을 정리합니다.

---

## 2. 주요 문제 상황

### 2.1 값이 잘리는 문제
- Customer No, Invoice No, Invoice Date 등의 값이 오른쪽에서 잘림
- PDF에서만 발생하는 문제
- Bootstrap 구조와 PDF 렌더링 충돌

### 2.2 정렬 문제
- 레이블과 값이 제대로 정렬되지 않음
- Bootstrap의 `row`, `col`, `d-flex` 등이 PDF에서 제대로 동작하지 않음

---

## 3. 해결 방법

### 3.1 Bootstrap 구조 개선

#### 3.1.1 기존 문제 코드
```xml
<div class="row">
    <div class="col-6 text-end pe-2"><strong>Customer No:</strong></div>
    <div class="col-6 text-start ps-2"><span t-field="o.partner_shipping_id.code"/></div>
</div>
```

#### 3.1.2 개선된 코드
```xml
<div class="row" t-if="o.partner_id.code">
    <div class="col text-end pe-2" style="width: 180px;">
        <strong>Customer No:</strong>
    </div>
    <div class="col text-start ps-2" style="word-break: break-all; overflow: visible;">
        <span t-field="o.partner_shipping_id.code"/>
    </div>
</div>
```

### 3.2 Table 구조로 변경 (권장)

#### 3.2.1 완전한 Table 구조
```xml
<div style="text-align: right; width: 100%;">
    <table style="width: 100%; border-collapse: collapse;">
        <tr t-if="o.partner_shipping_id.code">
            <td style="font-weight: bold; text-align: right; padding: 2px 5px; width: 45%;">Customer No:</td>
            <td style="text-align: left; padding: 2px 5px; width: 55%; word-break: break-all;">
                <span t-field="o.partner_shipping_id.code"/>
            </td>
        </tr>
        <!-- 추가 행들... -->
    </table>
</div>
```

---

## 4. 주요 스타일 속성

### 4.1 값이 잘리는 문제 해결
```css
style="word-break: break-all; overflow: visible;"
```

### 4.2 너비 고정
```css
style="width: 180px;"  /* 레이블용 */
style="width: 45%;"    /* 테이블 셀용 */
```

### 4.3 정렬 개선
```css
style="text-align: right;"  /* 레이블 */
style="text-align: left;"   /* 값 */
```

### 4.4 여백 조정
```css
style="padding: 2px 5px;"
```

---

## 5. Bootstrap vs Table 비교

| 구분 | Bootstrap | Table |
|------|-----------|-------|
| **PDF 호환성** | ❌ 문제 많음 | ✅ 안정적 |
| **정렬** | ❌ 예측 불가 | ✅ 정확 |
| **값 잘림** | ❌ 자주 발생 | ✅ 거의 없음 |
| **유지보수** | ❌ 복잡 | ✅ 간단 |
| **반응형** | ✅ 좋음 | ❌ 제한적 |

---

## 6. 실무 적용 예시

### 6.1 인보이스 정보 박스
```xml
<t t-set="address">
    <div class="row justify-content-end">
        <div class="col-auto">
            <div class="row" t-if="o.partner_id.code">
                <div class="col text-end pe-2" style="width: 180px;">
                    <strong>Customer No:</strong>
                </div>
                <div class="col text-start ps-2" style="word-break: break-all; overflow: visible;">
                    <span t-field="o.partner_shipping_id.code"/>
                </div>
            </div>
            <!-- 추가 행들... -->
        </div>
    </div>
</t>
```

### 6.2 테이블 구조 (최종 권장)
```xml
<t t-set="address">
    <div style="text-align: right; width: 100%;">
        <table style="width: 100%; border-collapse: collapse;">
            <tr t-if="o.partner_shipping_id.code">
                <td style="font-weight: bold; text-align: right; padding: 2px 5px; width: 45%;">Customer No:</td>
                <td style="text-align: left; padding: 2px 5px; width: 55%; word-break: break-all;">
                    <span t-field="o.partner_shipping_id.code"/>
                </td>
            </tr>
            <!-- 추가 행들... -->
        </table>
    </div>
</t>
```

---

## 7. PDF 렌더링 팁

### 7.1 PDF에서 안정적인 구조
- **Table**: 가장 안정적
- **Div + CSS**: 중간
- **Bootstrap**: 문제 많음

### 7.2 주의사항
- `overflow: hidden` 피하기
- `white-space: nowrap` 신중하게 사용
- `word-break: break-all` 적극 활용

### 7.3 테스트 방법
- 웹에서 확인 후 PDF 생성
- 다양한 데이터로 테스트
- 긴 텍스트, 특수문자 등 확인

---

## 8. CSS 클래스 vs 인라인 스타일

### 8.1 인라인 스타일 (권장)
```xml
<div style="word-break: break-all; overflow: visible;">
```

### 8.2 CSS 클래스
```xml
<div class="text-break overflow-visible">
```

### 8.3 선택 기준
- **PDF 전용**: 인라인 스타일
- **웹 + PDF**: CSS 클래스
- **복잡한 스타일**: CSS 클래스

---

## 9. 관련 파일
- `custom/soxnlox/sl_l10n_au/views/report_invoice.xml`
- 인보이스 정보 박스: 라인 40-77
- 테이블 헤더: 라인 95-115

---

## 10. 문제 해결 체크리스트

- [ ] Bootstrap 구조 확인
- [ ] `word-break: break-all` 추가
- [ ] `overflow: visible` 설정
- [ ] 너비 고정 (`width: 180px` 등)
- [ ] PDF 테스트
- [ ] 다양한 데이터로 검증

---

## 11. 참고 자료
- Odoo QWeb 문서
- Bootstrap PDF 호환성
- CSS word-break 속성
- Odoo PDF 렌더링 가이드 