1. 7월1일에 go live
2. 개발진행
	* sl_sale 모듈 개발완료 
3. 금일 기준으로 Go Live 진행
	1. 이번주 기준으로 데이터 정리

2024 / 8 / 5
1. 추가 개발건 Review 예정

2024 / 8 / 26
1. B2B 관련 개발 대기중


2025 / 6 / 30

report_invoice_document.xml 에서


<xpath expr="//div[@id='right-elements']" position="inside">
            <div id="receivable" class="border p-2">
            // 이쪽 부분 t-if 조건부 삭제
                <div class="m-2 fw-bold">
                    Balance as of <span t-out="datetime.date.today()" t-options="{'widget': 'date'}"/>
                    <span class="text-nowrap ms-2" t-field="o.partner_id.credit" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.currency_id}"/>
                </div>
                <ul class="m-0">
                    <li class="fw-normal">Balance includes your last balance and the amount of this invoice.</li>
                    <li class="fw-normal">Balance may not reflect recent payments.</li>
                </ul>
            </div>
        </xpath>