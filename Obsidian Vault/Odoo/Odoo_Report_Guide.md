# Odoo 18.0 리포트 시스템 완전 가이드

## 목차
1. [리포트 시스템 개요](#리포트-시스템-개요)
2. [Odoo 18.0의 새로운 기능](#odoo-180의-새로운-기능)
3. [리포트 구성 요소](#리포트-구성-요소)
4. [리포트 URL 구조](#리포트-url-구조)
5. [리포트 생성 방법](#리포트-생성-방법)
6. [QWeb 템플릿 작성](#qweb-템플릿-작성)
7. [리포트 액션 설정](#리포트-액션-설정)
8. [용지 형식 설정](#용지-형식-설정)
9. [실제 사용 예시](#실제-사용-예시)
10. [고급 기능](#고급-기능)
11. [문제 해결](#문제-해결)

---

## 리포트 시스템 개요

Odoo 18.0의 리포트 시스템은 QWeb 템플릿 엔진을 기반으로 하며, HTML을 PDF로 변환하여 문서를 생성합니다.

### 주요 특징
- **QWeb 템플릿 기반**: HTML과 XML을 조합한 템플릿 언어 사용
- **다양한 출력 형식**: HTML, PDF, 텍스트 지원
- **동적 데이터 바인딩**: 모델 데이터를 템플릿에 자동 연결
- **반응형 디자인**: 웹과 인쇄 모두에 최적화
- **향상된 성능**: Odoo 18.0에서 개선된 렌더링 엔진
- **개선된 보안**: 강화된 XSS 방지 및 보안 기능

---

## Odoo 18.0의 새로운 기능

### 1. 개선된 리포트 에디터
- **드래그 앤 드롭 인터페이스**: 직관적인 리포트 디자인
- **실시간 미리보기**: 변경사항을 즉시 확인 가능
- **향상된 템플릿 라이브러리**: 더 많은 기본 템플릿 제공

### 2. 성능 최적화
- **캐싱 시스템 개선**: 리포트 렌더링 속도 향상
- **메모리 사용량 최적화**: 대용량 리포트 처리 개선
- **비동기 렌더링**: 백그라운드에서 리포트 생성

### 3. 새로운 QWeb 기능
```xml
<!-- Odoo 18.0에서 추가된 새로운 QWeb 문법 -->
<t t-set="dynamic_content" t-value="doc._compute_dynamic_data()"/>
<t t-if="dynamic_content.get('show_section')">
    <div class="dynamic-section">
        <span t-esc="dynamic_content['value']"/>
    </div>
</t>
```

### 4. 향상된 다국어 지원
- **동적 언어 전환**: 리포트 내에서 언어 변경 가능
- **개선된 번역 시스템**: 더 정확한 번역 지원
- **로컬라이제이션 강화**: 지역별 형식 자동 적용

### 5. 보안 강화
- **XSS 방지 개선**: 더 강력한 보안 필터링
- **권한 기반 접근**: 세밀한 리포트 접근 제어
- **감사 로그**: 리포트 생성 및 접근 기록

### 6. 새로운 리포트 타입
- **인터랙티브 리포트**: 사용자 상호작용 가능한 리포트
- **대시보드 리포트**: 실시간 데이터 시각화
- **스케줄링 리포트**: 자동 리포트 생성 및 배포

### 7. 개선된 개발자 도구
- **리포트 디버거**: 실시간 디버깅 및 오류 추적
- **성능 프로파일러**: 리포트 렌더링 성능 분석
- **템플릿 검증기**: QWeb 템플릿 문법 검증

---

## 리포트 구성 요소

리포트는 다음 3가지 핵심 파일로 구성됩니다:

### 1. QWeb 템플릿 (report_template.xml)
```xml
<!-- 리포트의 HTML 구조와 스타일 정의 -->
<template id="my_report_template">
    <t t-call="web.basic_layout">
        <div class="page">
            <!-- 리포트 내용 -->
        </div>
    </t>
</template>
```

### 2. 리포트 액션 (reports/report_name.xml)
```xml
<!-- 리포트의 메타데이터와 설정 -->
<record id="my_report_action" model="ir.actions.report">
    <field name="name">My Report</field>
    <field name="model">my.model</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">my_module.my_report_template</field>
    <field name="report_file">my_module.my_report_template</field>
</record>
```

### 3. 용지 형식 (report.paperformat)
```xml
<!-- 페이지 설정 -->
<record id="my_paperformat" model="report.paperformat">
    <field name="name">A4 Portrait</field>
    <field name="format">A4</field>
    <field name="orientation">Portrait</field>
    <field name="margin_top">20</field>
    <field name="margin_bottom">25</field>
    <field name="margin_left">5</field>
    <field name="margin_right">0</field>
</record>
```

---

## 리포트 URL 구조

### 기본 URL 패턴
```
http://localhost:8069/report/{converter}/{report_external_id}/{docids}
```

### URL 구성 요소 분석

| 구성 요소 | 설명 | 예시 |
|-----------|------|------|
| `converter` | 출력 형식 | `html`, `pdf`, `text` |
| `report_external_id` | 리포트 외부 ID | `account.report_invoice` |
| `docids` | 문서 ID (선택사항) | `1`, `1,2,3` |

### 실제 URL 예시

#### HTML 리포트 보기
```
http://localhost:8069/report/html/account.report_invoice/1
```

#### PDF 리포트 다운로드
```
http://localhost:8069/report/pdf/account.report_invoice/1
```

#### 여러 문서 리포트
```
http://localhost:8069/report/html/account.report_invoice/1,2,3
```

#### 옵션과 컨텍스트 포함
```
http://localhost:8069/report/html/account.report_invoice/1?options={"key":"value"}&context={"lang":"ko_KR"}
```

### 컨트롤러 처리 과정

```python
@http.route([
    '/report/<converter>/<reportname>',
    '/report/<converter>/<reportname>/<docids>',
], type='http', auth='user', website=True, readonly=True)
def report_routes(self, reportname, docids=None, converter=None, **data):
    report = request.env['ir.actions.report']
    
    if converter == 'html':
        html = report._render_qweb_html(reportname, docids, data=data)[0]
        return request.make_response(html)
    elif converter == 'pdf':
        pdf = report._render_qweb_pdf(reportname, docids, data=data)[0]
        return request.make_response(pdf, headers=[('Content-Type', 'application/pdf')])
```

---

## 리포트 생성 방법

### 1. 모듈 구조
```
my_module/
├── __manifest__.py
├── views/
│   └── report_template.xml
├── reports/
│   └── report_actions.xml
└── static/
    └── src/
        └── css/
            └── report_styles.css
```

### 2. 매니페스트 파일 설정
```python
{
    'name': 'My Report Module',
    'version': '18.0.1.0.0',
    'depends': ['base', 'web'],
    'data': [
        'views/report_template.xml',
        'reports/report_actions.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'my_module/static/src/css/report_styles.css',
        ],
        'web.report_assets_pdf': [
            'my_module/static/src/css/report_pdf_styles.css',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
```

---

## QWeb 템플릿 작성

### 기본 템플릿 구조
```xml
<template id="my_report_template">
    <!-- 기본 레이아웃 호출 -->
    <t t-call="web.basic_layout">
        <div class="page">
            <!-- 헤더 -->
            <div class="oe_structure"/>
            
            <!-- 제목 -->
            <h1 class="text-center">
                <span t-field="doc.name"/>
            </h1>
            
            <!-- 내용 -->
            <div class="row">
                <div class="col-12">
                    <!-- 리포트 내용 -->
                </div>
            </div>
        </div>
    </t>
</template>
```

### 데이터 바인딩

#### 기본 필드 출력
```xml
<!-- 단순 필드 출력 -->
<span t-field="doc.name"/>

<!-- 날짜 형식 지정 -->
<span t-field="doc.create_date" t-options="{'widget': 'date'}"/>

<!-- 통화 형식 지정 -->
<span t-field="doc.amount" t-options="{'widget': 'monetary'}"/>
```

#### 조건문 사용
```xml
<!-- 조건부 출력 -->
<t t-if="doc.state == 'confirmed'">
    <span class="badge badge-success">확인됨</span>
</t>
<t t-else="">
    <span class="badge badge-warning">대기중</span>
</t>
```

#### 반복문 사용
```xml
<!-- 리스트 반복 -->
<t t-foreach="doc.line_ids" t-as="line">
    <tr>
        <td><span t-field="line.product_id.name"/></td>
        <td><span t-field="line.quantity"/></td>
        <td><span t-field="line.price_unit"/></td>
    </tr>
</t>
```

#### 테이블 구조
```xml
<table class="table table-bordered">
    <thead>
        <tr>
            <th>제품명</th>
            <th>수량</th>
            <th>단가</th>
            <th>금액</th>
        </tr>
    </thead>
    <tbody>
        <t t-foreach="doc.order_line" t-as="line">
            <tr>
                <td><span t-field="line.product_id.name"/></td>
                <td class="text-right"><span t-field="line.product_uom_qty"/></td>
                <td class="text-right"><span t-field="line.price_unit"/></td>
                <td class="text-right"><span t-field="line.price_subtotal"/></td>
            </tr>
        </t>
    </tbody>
</table>
```

### 스타일링

#### CSS 클래스 사용
```xml
<div class="row">
    <div class="col-6">
        <div class="card">
            <div class="card-header">
                <h5>고객 정보</h5>
            </div>
            <div class="card-body">
                <p><strong>이름:</strong> <span t-field="doc.partner_id.name"/></p>
                <p><strong>이메일:</strong> <span t-field="doc.partner_id.email"/></p>
            </div>
        </div>
    </div>
</div>
```

#### 인라인 스타일
```xml
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px;">
    <h3 style="color: #007bff; margin-bottom: 10px;">요약 정보</h3>
    <p style="font-size: 14px; line-height: 1.6;">
        <span t-field="doc.name"/>
    </p>
</div>
```

---

## 리포트 액션 설정

### 기본 리포트 액션
```xml
<record id="my_report_action" model="ir.actions.report">
    <field name="name">My Custom Report</field>
    <field name="model">sale.order</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">my_module.my_report_template</field>
    <field name="report_file">my_module.my_report_template</field>
    <field name="binding_model_id" ref="sale.model_sale_order"/>
    <field name="binding_type">report</field>
    <field name="paperformat_id" ref="my_module.my_paperformat"/>
</record>
```

### 필드 설명

| 필드명 | 설명 | 예시 |
|--------|------|------|
| `name` | 리포트 표시 이름 | "My Custom Report" |
| `model` | 대상 모델 | "sale.order" |
| `report_type` | 리포트 타입 | "qweb-pdf", "qweb-html" |
| `report_name` | QWeb 템플릿 ID | "my_module.my_template" |
| `report_file` | 템플릿 파일 경로 | "my_module.my_template" |
| `binding_model_id` | 연결할 모델 | ref="sale.model_sale_order" |
| `binding_type` | 바인딩 타입 | "report" |
| `paperformat_id` | 용지 형식 | ref="my_module.my_paperformat" |

### 고급 설정

#### 조건부 리포트
```xml
<record id="conditional_report" model="ir.actions.report">
    <field name="name">Conditional Report</field>
    <field name="model">sale.order</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">my_module.conditional_template</field>
    <field name="report_file">my_module.conditional_template</field>
    <field name="print_report_name">'Order_%s' % (object.name)</field>
    <field name="binding_model_id" ref="sale.model_sale_order"/>
    <field name="binding_type">report</field>
</record>
```

#### 다중 언어 지원
```xml
<record id="multilingual_report" model="ir.actions.report">
    <field name="name">Multilingual Report</field>
    <field name="model">sale.order</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">my_module.multilingual_template</field>
    <field name="report_file">my_module.multilingual_template</field>
    <field name="binding_model_id" ref="sale.model_sale_order"/>
    <field name="binding_type">report</field>
</record>
```

---

## 용지 형식 설정

### 기본 A4 설정
```xml
<record id="a4_paperformat" model="report.paperformat">
    <field name="name">A4 Portrait</field>
    <field name="default" eval="True"/>
    <field name="format">A4</field>
    <field name="page_height">0</field>
    <field name="page_width">0</field>
    <field name="orientation">Portrait</field>
    <field name="margin_top">20</field>
    <field name="margin_bottom">25</field>
    <field name="margin_left">5</field>
    <field name="margin_right">0</field>
    <field name="header_line" eval="False"/>
    <field name="header_spacing">10</field>
    <field name="dpi">100</field>
</record>
```

### 필드 설명

| 필드명 | 설명 | 기본값 |
|--------|------|--------|
| `name` | 용지 형식 이름 | - |
| `default` | 기본 형식 여부 | False |
| `format` | 용지 크기 | A4, A3, Letter 등 |
| `page_height` | 페이지 높이 (mm) | 0 (자동) |
| `page_width` | 페이지 너비 (mm) | 0 (자동) |
| `orientation` | 방향 | Portrait, Landscape |
| `margin_top` | 상단 여백 (mm) | 20 |
| `margin_bottom` | 하단 여백 (mm) | 25 |
| `margin_left` | 좌측 여백 (mm) | 5 |
| `margin_right` | 우측 여백 (mm) | 0 |
| `header_line` | 헤더 라인 표시 | False |
| `header_spacing` | 헤더 간격 (mm) | 10 |
| `dpi` | 해상도 | 100 |

### 커스텀 용지 형식
```xml
<record id="custom_paperformat" model="report.paperformat">
    <field name="name">Custom Business Card</field>
    <field name="format">custom</field>
    <field name="page_height">55</field>
    <field name="page_width">85</field>
    <field name="orientation">Portrait</field>
    <field name="margin_top">5</field>
    <field name="margin_bottom">5</field>
    <field name="margin_left">5</field>
    <field name="margin_right">5</field>
    <field name="header_line" eval="False"/>
    <field name="header_spacing">0</field>
    <field name="dpi">300</field>
</record>
```

---

## 실제 사용 예시

### 1. 간단한 인보이스 리포트

#### 템플릿 (invoice_template.xml)
```xml
<template id="simple_invoice_template">
    <t t-call="web.basic_layout">
        <div class="page">
            <div class="oe_structure"/>
            
            <!-- 헤더 -->
            <div class="row">
                <div class="col-6">
                    <h2>인보이스</h2>
                    <p><strong>번호:</strong> <span t-field="doc.name"/></p>
                    <p><strong>날짜:</strong> <span t-field="doc.invoice_date" t-options="{'widget': 'date'}"/></p>
                </div>
                <div class="col-6 text-right">
                    <h3>고객 정보</h3>
                    <p><span t-field="doc.partner_id.name"/></p>
                    <p><span t-field="doc.partner_id.street"/></p>
                    <p><span t-field="doc.partner_id.city"/></p>
                </div>
            </div>
            
            <!-- 상품 목록 -->
            <div class="row mt-4">
                <div class="col-12">
                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <th>제품</th>
                                <th class="text-right">수량</th>
                                <th class="text-right">단가</th>
                                <th class="text-right">금액</th>
                            </tr>
                        </thead>
                        <tbody>
                            <t t-foreach="doc.invoice_line_ids" t-as="line">
                                <tr>
                                    <td><span t-field="line.product_id.name"/></td>
                                    <td class="text-right"><span t-field="line.quantity"/></td>
                                    <td class="text-right"><span t-field="line.price_unit"/></td>
                                    <td class="text-right"><span t-field="line.price_subtotal"/></td>
                                </tr>
                            </t>
                        </tbody>
                        <tfoot>
                            <tr>
                                <td colspan="3" class="text-right"><strong>총액:</strong></td>
                                <td class="text-right"><strong><span t-field="doc.amount_total"/></strong></td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
            </div>
        </div>
    </t>
</template>
```

#### 리포트 액션 (invoice_report.xml)
```xml
<record id="simple_invoice_paperformat" model="report.paperformat">
    <field name="name">Simple Invoice A4</field>
    <field name="format">A4</field>
    <field name="orientation">Portrait</field>
    <field name="margin_top">20</field>
    <field name="margin_bottom">25</field>
    <field name="margin_left">10</field>
    <field name="margin_right">10</field>
    <field name="header_line" eval="False"/>
    <field name="dpi">100</field>
</record>

<record id="simple_invoice_report" model="ir.actions.report">
    <field name="name">Simple Invoice</field>
    <field name="model">account.move</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">my_module.simple_invoice_template</field>
    <field name="report_file">my_module.simple_invoice_template</field>
    <field name="binding_model_id" ref="account.model_account_move"/>
    <field name="binding_type">report</field>
    <field name="paperformat_id" ref="my_module.simple_invoice_paperformat"/>
</record>
```

### 2. 복잡한 다중 페이지 리포트

#### 템플릿 (complex_report_template.xml)
```xml
<template id="complex_report_template">
    <t t-call="web.basic_layout">
        <!-- 첫 번째 페이지 -->
        <div class="page">
            <div class="oe_structure"/>
            
            <!-- 표지 -->
            <div class="text-center" style="margin-top: 100px;">
                <h1 style="font-size: 32px; margin-bottom: 30px;">월간 매출 리포트</h1>
                <h3 style="color: #666;">2024년 1월</h3>
                <p style="margin-top: 50px;">생성일: <span t-esc="context_timestamp(datetime.datetime.now()).strftime('%Y-%m-%d')"/></p>
            </div>
        </div>
        
        <!-- 두 번째 페이지 -->
        <div class="page">
            <div class="oe_structure"/>
            
            <!-- 목차 -->
            <h2>목차</h2>
            <ul>
                <li>매출 요약</li>
                <li>제품별 매출</li>
                <li>지역별 매출</li>
                <li>고객별 매출</li>
            </ul>
        </div>
        
        <!-- 세 번째 페이지 -->
        <div class="page">
            <div class="oe_structure"/>
            
            <!-- 매출 요약 -->
            <h2>매출 요약</h2>
            <div class="row">
                <div class="col-6">
                    <div class="card">
                        <div class="card-body">
                            <h5>총 매출</h5>
                            <h3 class="text-success">₩<span t-esc="sum(docs.mapped('amount_total'))"/></h3>
                        </div>
                    </div>
                </div>
                <div class="col-6">
                    <div class="card">
                        <div class="card-body">
                            <h5>주문 수</h5>
                            <h3 class="text-info"><span t-esc="len(docs)"/></h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </t>
</template>
```

---

## 고급 기능

### 1. 조건부 템플릿

#### 다중 템플릿 선택
```xml
<template id="conditional_report_template">
    <t t-if="doc.state == 'draft'">
        <t t-call="my_module.draft_template"/>
    </t>
    <t t-elif="doc.state == 'confirmed'">
        <t t-call="my_module.confirmed_template"/>
    </t>
    <t t-else="">
        <t t-call="my_module.default_template"/>
    </t>
</template>
```

### 2. 동적 데이터 처리

#### Python 함수 호출
```xml
<template id="dynamic_report_template">
    <t t-call="web.basic_layout">
        <div class="page">
            <t t-set="calculated_data" t-value="doc._calculate_report_data()"/>
            
            <h2>계산된 데이터</h2>
            <p>총합: <span t-esc="calculated_data['total']"/></p>
            <p>평균: <span t-esc="calculated_data['average']"/></p>
        </div>
    </t>
</template>
```

### 3. 다국어 지원

#### 언어별 템플릿
```xml
<template id="multilingual_template">
    <t t-call="web.basic_layout">
        <div class="page">
            <t t-set="lang" t-value="doc.partner_id.lang or 'ko_KR'"/>
            
            <h1 t-lang="lang">인보이스</h1>
            <p t-lang="lang">고객명: <span t-field="doc.partner_id.name"/></p>
            <p t-lang="lang">금액: <span t-field="doc.amount_total"/></p>
        </div>
    </t>
</template>
```

### 4. 차트 및 그래프

#### Chart.js 사용 (Odoo 18.0 개선)
```xml
<template id="chart_report_template">
    <t t-call="web.basic_layout">
        <div class="page">
            <canvas id="salesChart" width="400" height="200"></canvas>
            
            <script type="text/javascript">
                // Odoo 18.0에서 개선된 차트 렌더링
                var ctx = document.getElementById('salesChart').getContext('2d');
                var chart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: ['1월', '2월', '3월', '4월', '5월', '6월'],
                        datasets: [{
                            label: '매출',
                            data: [12, 19, 3, 5, 2, 3],
                            backgroundColor: 'rgba(54, 162, 235, 0.2)',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                display: true,
                                position: 'top'
                            }
                        }
                    }
                });
            </script>
        </div>
    </t>
</template>
```

#### Odoo 18.0 새로운 차트 기능
```xml
<!-- 인터랙티브 차트 지원 -->
<template id="interactive_chart_template">
    <t t-call="web.basic_layout">
        <div class="page">
            <div class="chart-container" style="position: relative; height:400px;">
                <canvas id="interactiveChart"></canvas>
            </div>
            
            <script type="text/javascript">
                // Odoo 18.0 인터랙티브 차트
                var ctx = document.getElementById('interactiveChart').getContext('2d');
                var interactiveChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: ['1월', '2월', '3월', '4월', '5월', '6월'],
                        datasets: [{
                            label: '매출',
                            data: [12, 19, 3, 5, 2, 3],
                            borderColor: 'rgb(75, 192, 192)',
                            tension: 0.1
                        }]
                    },
                    options: {
                        interaction: {
                            intersect: false,
                            mode: 'index'
                        },
                        plugins: {
                            tooltip: {
                                enabled: true
                            }
                        }
                    }
                });
            </script>
        </div>
    </t>
</template>
```

---

## 문제 해결

### 1. 일반적인 오류

#### 템플릿을 찾을 수 없음
```
Error: Template 'my_module.my_template' not found
```
**해결방법:**
- 템플릿 ID가 정확한지 확인
- 모듈이 올바르게 설치되었는지 확인
- 매니페스트 파일에 템플릿이 포함되었는지 확인

#### 모델을 찾을 수 없음
```
Error: Model 'my.model' not found
```
**해결방법:**
- 모델명이 정확한지 확인
- 모델이 정의된 모듈이 의존성에 포함되었는지 확인

#### 권한 오류
```
Error: Access denied
```
**해결방법:**
- 사용자에게 해당 모델에 대한 읽기 권한이 있는지 확인
- 리포트 액션의 `auth` 설정 확인

### 2. 디버깅 방법

#### 로그 확인
```bash
# Odoo 서버 로그에서 오류 확인
tail -f /var/log/odoo/odoo-server.log
```

#### 템플릿 테스트
```python
# Python 콘솔에서 템플릿 테스트
env['ir.actions.report']._render_qweb_html('my_module.my_template', [1])
```

#### 브라우저 개발자 도구
- F12를 눌러 개발자 도구 열기
- Network 탭에서 리포트 요청 확인
- Console 탭에서 JavaScript 오류 확인

### 3. 성능 최적화

#### 대용량 데이터 처리 (Odoo 18.0 개선)
```xml
<!-- 페이지네이션 사용 -->
<t t-foreach="doc.line_ids[:100]" t-as="line">
    <!-- 최대 100개 항목만 표시 -->
</t>

<!-- Odoo 18.0 새로운 지연 로딩 -->
<t t-set="lazy_data" t-value="doc._get_lazy_data()"/>
<t t-if="lazy_data">
    <t t-foreach="lazy_data" t-as="item">
        <div class="lazy-item">
            <span t-esc="item.name"/>
        </div>
    </t>
</t>
```

#### 이미지 최적화
```xml
<!-- 이미지 크기 제한 -->
<img t-att-src="image_data_uri(doc.image)" style="max-width: 300px; max-height: 200px;"/>

<!-- Odoo 18.0 WebP 지원 -->
<img t-att-src="image_data_uri(doc.image, format='webp')" style="max-width: 300px; max-height: 200px;"/>
```

#### 캐싱 활용 (Odoo 18.0 개선)
```xml
<!-- 정적 데이터 캐싱 -->
<t t-set="cached_data" t-value="doc._get_cached_data()"/>

<!-- Odoo 18.0 새로운 캐싱 시스템 -->
<t t-set="smart_cache" t-value="doc._get_smart_cached_data()"/>
<t t-if="smart_cache.get('is_valid')">
    <div class="cached-content">
        <span t-esc="smart_cache['data']"/>
    </div>
</t>
```

#### Odoo 18.0 성능 모니터링
```python
# 성능 프로파일링 활성화
import time
import logging

_logger = logging.getLogger(__name__)

def _render_with_profiling(self, report_name, docids, data=None):
    start_time = time.time()
    result = self._render_qweb_html(report_name, docids, data=data)
    end_time = time.time()
    
    _logger.info(f"Report {report_name} rendered in {end_time - start_time:.2f} seconds")
    return result
```

---

## 참고 자료

### 공식 문서
- [Odoo 18.0 QWeb Documentation](https://www.odoo.com/documentation/18.0/developer/reference/addons/web/qweb.html)
- [Odoo 18.0 Report Documentation](https://www.odoo.com/documentation/18.0/developer/reference/addons/web/reporting.html)
- [Odoo 18.0 Migration Guide](https://www.odoo.com/documentation/18.0/developer/misc/other/migration.html)

### 유용한 링크
- [Odoo Community Association](https://odoo-community.org/)
- [Odoo GitHub Repository](https://github.com/odoo/odoo)

### 개발 도구
- [Odoo Studio](https://www.odoo.com/app/studio)
- [Odoo Apps Store](https://apps.odoo.com/)

---

## 마무리

이 가이드를 통해 Odoo 리포트 시스템의 모든 측면을 이해하고 활용할 수 있습니다. 실제 프로젝트에서 이 지식을 바탕으로 효과적인 리포트를 개발하시기 바랍니다.

### 추가 학습 포인트
1. **Odoo 18.0 새로운 QWeb 기능** 학습
2. **향상된 CSS 스타일링** 심화
3. **인터랙티브 JavaScript** 통합 방법
4. **성능 최적화 및 모니터링** 기법
5. **보안 강화 기능** 이해
6. **리포트 에디터 활용** 방법
7. **대시보드 리포트** 개발 기법

### 연락처
문의사항이나 추가 도움이 필요하시면 언제든 연락주세요. 