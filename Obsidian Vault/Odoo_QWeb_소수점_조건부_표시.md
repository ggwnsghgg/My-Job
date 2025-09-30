# Odoo QWeb 소수점 조건부 표시 방법

## 1. 개요
Odoo QWeb 템플릿에서 수량, 금액 등의 값을 표시할 때, 소수점이 있으면 소수점으로, 정수면 정수로 깔끔하게 표시하는 방법을 정리합니다.

---

## 2. 문제 상황
- 수량이 `7.67`, `4.50`인데 `7`, `4`로만 표시됨
- Total 계산이 잘못됨 (`7.67 + 4.50 = 12.17`이어야 하는데 `7 + 4 = 11`로 표시)
- 소수점이 있는 값과 정수 값을 구분해서 표시하고 싶음

---

## 3. 해결 방법

### 3.1 기본 원리
```xml
<span t-if="float(int(value)) == float(value)" t-esc="int(value)"></span>
<span t-else="" t-esc="value"></span>
```

### 3.2 동작 방식
- `float(int(value)) == float(value)`: 값이 정수인지 확인
- 정수면: `int(value)`로 정수 표시
- 소수점이 있으면: `value`로 원본 값 표시

---

## 4. 실제 적용 예시

### 4.1 개별 수량 표시
```xml
<td name="td_quantity" class="text-end">
    <span t-if="float(int(line.quantity)) == float(line.quantity)" t-esc="int(line.quantity)"></span>
    <span t-else="" t-esc="line.quantity"></span>
</td>
```

### 4.2 Total 수량 표시
```xml
<td name="tl_quantity" class="text-end">
    <span t-if="float(int(current_quantity)) == float(current_quantity)" t-out="int(current_quantity)"></span>
    <span t-else="" t-out="current_quantity"></span>
</td>
```

---

## 5. 다른 표시 방법들

### 5.1 항상 소수점 표시
```xml
<span t-esc="line.quantity"></span>
```

### 5.2 항상 정수 표시
```xml
<span t-esc="int(line.quantity)"></span>
```

### 5.3 소수점 자릿수 지정
```xml
<span t-esc="'%.2f' % line.quantity"></span>
```

### 5.4 조건부 소수점 자릿수
```xml
<span t-if="float(int(line.quantity)) == float(line.quantity)" t-esc="int(line.quantity)"></span>
<span t-else="" t-esc="'%.2f' % line.quantity"></span>
```

---

## 6. QWeb 옵션 비교

| 방법 | 정수 7.0 | 소수 7.67 | 설명 |
|------|----------|-----------|------|
| `t-esc="line.quantity"` | 7.0 | 7.67 | 원본 값 그대로 |
| `t-esc="int(line.quantity)"` | 7 | 7 | 정수만 |
| 조건부 표시 | 7 | 7.67 | **권장 방법** |
| `'%.2f' % line.quantity` | 7.00 | 7.67 | 소수점 2자리 |

---

## 7. 실무 팁

### 7.1 금액 필드에도 적용 가능
```xml
<span t-if="float(int(line.price_unit)) == float(line.price_unit)" t-esc="int(line.price_unit)"></span>
<span t-else="" t-esc="line.price_unit"></span>
```

### 7.2 통화 위젯과 함께 사용
```xml
<span t-if="float(int(line.price_unit)) == float(line.price_unit)" 
      t-esc="int(line.price_unit)"
      t-options='{"widget": "monetary", "display_currency": o.currency_id}'></span>
<span t-else="" 
      t-esc="line.price_unit"
      t-options='{"widget": "monetary", "display_currency": o.currency_id}'></span>
```

### 7.3 성능 고려사항
- 조건문은 간단하게 유지
- 복잡한 계산은 Python에서 미리 처리
- `t-esc` vs `t-out` 차이점 고려

---

## 8. 주의사항

### 8.1 float 비교의 한계
- 매우 작은 소수점 차이는 무시될 수 있음
- 정밀도가 중요한 경우 다른 방법 고려

### 8.2 PDF 렌더링
- PDF에서는 소수점 표시가 다를 수 있음
- 테스트 필수

### 8.3 다국어 지원
- 소수점 구분자가 다를 수 있음 (`.` vs `,`)
- 로케일 설정 확인

---

## 9. 관련 파일
- `custom/soxnlox/sl_l10n_au/views/report_invoice.xml`
- 수량 표시: 라인 135-138
- Total 표시: 라인 158-161

---

## 10. 참고 자료
- Odoo QWeb 문서
- Python float 비교 방법
- Odoo monetary 위젯 옵션 