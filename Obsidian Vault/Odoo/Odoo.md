 	1. 설치 방법
2. 개발 관련
	1. Multi Company 적용 방법
	2. Compute 적용한 필드는 store=True를 해야 xml 에서 도메인 기능이 제대로 작동한다
	3. res.config.settings 에 추가한 필드는 settings -> system parameters에서 볼 수 있다 만약 추가한 필드의 값이 보이지 않는다면 그 값을 어디에서 사용하고 있지 않기 때문에 생성이 되지 않은 것이기 때문에 추가한 필드가 사용될 수 있게 함수 라던지 작업을 하여 생성되게 해야 한다.
	4. data xml 의  noupdate 는 설치 할때는 업데이트 하고 추후에 모듈을 업데이트 할땐 data를 업데이트 하지 말라는 의미다
	5. def _search_get_detail(self, website, order, options):  
	    res = super(ProductTemplate, self)._search_get_detail(website, order, options)  
	    domains = res.get('base_domain', [])  
	    domains.append([('ka_customer_group_block_ids', '=', True)])  
	    res['base_domain'] = domains  
	    return res
		함수를 inherit 할때 get 을 사용하면 기존에 사용하던 함수의 값을 불러와서 정의할 수 있다.
		