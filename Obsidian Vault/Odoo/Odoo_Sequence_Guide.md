# Odoo 18.0 채번(시퀀스) 변경 가이드

## 개요
Odoo에서 문서 번호를 자동으로 생성하는 채번 시스템을 커스터마이징하는 방법을 설명합니다.

---

## 기본 채번 변경 함수

### 1. 기본 구조
```python
@api.model
def create(self, vals):
    if vals.get('name', '/') == '/':
        # 채번 로직 구현
        vals['name'] = '새로운_번호_형식'
    return super().create(vals)
```

### 2. 실제 예시 (제공된 코드)
```python
@api.model
def create(self, vals):
    if vals.get('name', '/') == '/':
        year_suffix = datetime.today().strftime('%y')  # 두 자리 연도
        seq = self.env['ir.sequence'].next_by_code('iz.sale.order') or '000'
        vals['name'] = f'S{year_suffix}{seq[-3:]}'
    return super().create(vals)
```

---

## 코드 분석

### 각 부분 설명

| 부분 | 설명 | 예시 |
|------|------|------|
| `@api.model` | 모델 레벨 데코레이터 | 클래스 메서드로 정의 |
| `vals.get('name', '/')` | name 필드 값 확인 | 기본값 '/' |
| `datetime.today().strftime('%y')` | 현재 연도 (2자리) | '24' (2024년) |
| `self.env['ir.sequence'].next_by_code()` | 시퀀스에서 다음 번호 가져오기 | '0001', '0002' 등 |
| `seq[-3:]` | 시퀀스의 마지막 3자리 | '001', '002' 등 |
| `f'S{year_suffix}{seq[-3:]}'` | 최종 번호 형식 | 'S24001', 'S24002' 등 |

### 생성되는 번호 예시
- **2024년**: S24001, S24002, S24003, ...
- **2025년**: S25001, S25002, S25003, ...

---

## 다양한 채번 패턴

### 1. 연도 + 월 + 시퀀스
```python
@api.model
def create(self, vals):
    if vals.get('name', '/') == '/':
        year_month = datetime.today().strftime('%y%m')  # YYMM
        seq = self.env['ir.sequence'].next_by_code('my.sequence') or '000'
        vals['name'] = f'SO{year_month}{seq[-3:]}'
    return super().create(vals)
```
**결과**: SO2401001, SO2401002, SO2402001, ...

### 2. 접두사 + 연도 + 시퀀스
```python
@api.model
def create(self, vals):
    if vals.get('name', '/') == '/':
        year = datetime.today().strftime('%Y')  # 4자리 연도
        seq = self.env['ir.sequence'].next_by_code('my.sequence') or '000'
        vals['name'] = f'INV-{year}-{seq[-4:]}'
    return super().create(vals)
```
**결과**: INV-2024-0001, INV-2024-0002, ...

### 3. 회사별 채번
```python
@api.model
def create(self, vals):
    if vals.get('name', '/') == '/':
        company_code = self.env.company.code or 'MAIN'
        year = datetime.today().strftime('%y')
        seq = self.env['ir.sequence'].next_by_code('my.sequence') or '000'
        vals['name'] = f'{company_code}{year}{seq[-3:]}'
    return super().create(vals)
```
**결과**: MAIN24001, MAIN24002, ...

---

## 시퀀스 설정

### 1. XML에서 시퀀스 정의
```xml
<record id="seq_my_sequence" model="ir.sequence">
    <field name="name">My Custom Sequence</field>
    <field name="code">my.sequence</field>
    <field name="prefix"></field>
    <field name="padding">3</field>
    <field name="number_increment">1</field>
    <field name="number_next">1</field>
</record>
```

### 2. 시퀀스 필드 설명

| 필드 | 설명 | 예시 |
|------|------|------|
| `name` | 시퀀스 표시 이름 | "My Custom Sequence" |
| `code` | 시퀀스 코드 | "my.sequence" |
| `prefix` | 접두사 | "SO" |
| `padding` | 자릿수 | 3 (001, 002, ...) |
| `number_increment` | 증가값 | 1 |
| `number_next` | 다음 번호 | 1 |

---

## 고급 채번 기능

### 1. 연도별 시퀀스 리셋
```python
@api.model
def create(self, vals):
    if vals.get('name', '/') == '/':
        current_year = datetime.today().year
        sequence = self.env['ir.sequence'].search([('code', '=', 'my.sequence')])
        
        # 연도가 바뀌면 시퀀스 리셋
        if sequence.date_range_ids:
            last_range = sequence.date_range_ids.sorted('date_from')[-1]
            if last_range.date_from.year != current_year:
                # 새 연도 시퀀스 생성
                sequence._create_date_range_seq(current_year)
        
        year_suffix = datetime.today().strftime('%y')
        seq = sequence.next_by_code('my.sequence') or '000'
        vals['name'] = f'S{year_suffix}{seq[-3:]}'
    return super().create(vals)
```

### 2. 조건부 채번
```python
@api.model
def create(self, vals):
    if vals.get('name', '/') == '/':
        # 조건에 따른 다른 시퀀스 사용
        if vals.get('type') == 'sale':
            seq_code = 'sale.sequence'
        elif vals.get('type') == 'purchase':
            seq_code = 'purchase.sequence'
        else:
            seq_code = 'default.sequence'
        
        year = datetime.today().strftime('%y')
        seq = self.env['ir.sequence'].next_by_code(seq_code) or '000'
        vals['name'] = f'{vals.get("type", "DOC").upper()}{year}{seq[-3:]}'
    return super().create(vals)
```

---

## 주의사항

### 1. 성능 고려사항
- **시퀀스 조회 최적화**: 자주 사용되는 시퀀스는 캐싱 고려
- **데이터베이스 락**: 동시 생성 시 데드락 방지

### 2. 데이터 무결성
- **중복 방지**: 시퀀스 번호의 유일성 보장
- **롤백 처리**: 생성 실패 시 시퀀스 롤백 고려

### 3. 마이그레이션 고려사항
- **기존 데이터**: 기존 번호와의 충돌 방지
- **시퀀스 초기화**: 새 채번 규칙 적용 시 시퀀스 초기화

---

## 실제 사용 예시

### 1. 판매 주문 채번
```python
# models/sale_order.py
from datetime import datetime
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            year_suffix = datetime.today().strftime('%y')
            seq = self.env['ir.sequence'].next_by_code('iz.sale.order') or '000'
            vals['name'] = f'S{year_suffix}{seq[-3:]}'
        return super().create(vals)
```

### 2. 인보이스 채번
```python
# models/account_move.py
class AccountMove(models.Model):
    _inherit = 'account.move'
    
    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            year = datetime.today().strftime('%Y')
            month = datetime.today().strftime('%m')
            seq = self.env['ir.sequence'].next_by_code('iz.invoice') or '000'
            vals['name'] = f'INV-{year}-{month}-{seq[-3:]}'
        return super().create(vals)
```

---

## 요약

Odoo 18.0에서 채번을 변경하는 핵심 포인트:

1. **`@api.model` 데코레이터** 사용
2. **`vals.get('name', '/')`** 로 기본값 확인
3. **`ir.sequence`** 모델로 시퀀스 관리
4. **`datetime`** 모듈로 날짜 정보 활용
5. **f-string** 으로 번호 형식 구성

이 방법을 통해 비즈니스 요구사항에 맞는 맞춤형 문서 번호를 생성할 수 있습니다. 