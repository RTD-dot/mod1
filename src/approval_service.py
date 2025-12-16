def approve(self, app_id, approver, comment):
    """优化：大额采购需二次审核"""
    for app in self.approval_records:
        if app["id"] == app_id and app["current_approver"] == approver:
            # 新增大额采购判断
            if app["amount"] > 50000 and current_idx == len(self.approval_flow)-1:
                app["status"] = "待二次审核"
                app["current_approver"] = "内控总监"
            else:
                app["status"] = "审批通过"
            # 其余逻辑不变...
