// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    today_year, today_month, today_day = map(int, today.split('.'))
    terms_dict = {}
    for term in terms:
        t, month = term.split()
        terms_dict[t] = int(month)
    
    def calculate_expire_date(year, month, day, term):
        expire_month = month + term
        expire_year = year + (expire_month - 1) // 12
        expire_month = (expire_month - 1) % 12 + 1
        if day > 28:
            day = 28
        return (expire_year, expire_month, day)
    
    def date_is_expired(expire_date, today_date):
        return expire_date <= today_date
    
    result = []
    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        year, month, day = map(int, date.split('.'))
        expire_date = calculate_expire_date(year, month, day, terms_dict[term])
        
        if date_is_expired(expire_date, (today_year, today_month, today_day)):
            result.append(i + 1)
    
    return result
