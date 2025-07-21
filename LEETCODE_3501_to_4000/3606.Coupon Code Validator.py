def validateCoupons(code, businessLine, isActive):
    def isValid(record):
        return (record[0] in validBiz and record[2] and
                record[1].replace('_', 'a').isalnum())

    validBiz = {"electronics", "grocery", "restaurant", "pharmacy"}
    ans = sorted(filter(isValid, zip(businessLine, code, isActive)))
    return [coupId for _, coupId, _ in ans]  