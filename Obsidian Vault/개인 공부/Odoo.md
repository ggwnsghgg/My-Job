**✅ Odoo 17 → 18 업그레이드 준비 요약**

  

📂 1. 서브모듈 브랜치 전환

• 모든 custom 서브모듈의 브랜치를 18.0으로 변경

• .gitmodules는 에 바라보고 있는 저장소 버전 변경 후 **서브모듈 참조 커밋만 업데이트**

  

**🧠 2. Odoo.sh 업그레이드 흐름 이해 및 적용**

* Odoo.sh에서 업그레이드 요청 후, **업그레이드된 DB가 제공됨**

* 이후 **custom 모듈 호환성 문제를 해결**한 후 **커밋 & 푸시**

* 커밋 메시지: git commit --allow-empty -m "Trigger update"

  

**⚠️ 3. 에러 대응 - <tree> → <list>

	Odoo 18부터는 list view에서 <tree> 사용 불가 → <list>로 수정
	
	이로 인해 lu_asp 모듈에서 XML view 에러 발생 → 수정 완료

  


✅ 4. 호환성 변경 커밋 진행

• tree → list 등 Odoo 18 호환성 수정 커밋 생성

• 변경된 커밋 ID를 .gitmodules와 연결된 경로 기준으로 반영됨

