
디스플레이 이름을 변경할때 유용하게 사용됨


@api.depends('acc_number', 'bank_id')  
def _compute_display_name(self):  
    for acc in self:  
        acc.display_name = f"{acc.bank_id.name} - {acc.acc_number}" if acc.bank_id else acc.acc_number

 
 