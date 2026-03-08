"""
경영진 대시보드 데이터 모듈
각 팀별 경영 현황 데이터를 제공합니다.

팀 구성:
- 사업수행팀 (Business Operations)
- 영업팀 (Sales)
- 전략기획실 (Strategic Planning)
- 인사팀 (HR)
- 재무팀 (Finance)
"""

import datetime
import random

# 현재 날짜 기준
TODAY = datetime.date.today()
CURRENT_YEAR = TODAY.year
CURRENT_MONTH = TODAY.month


def _monthly_series(base, variance=0.1):
    """월별 시계열 데이터 생성 (1월~현재월)"""
    result = []
    for m in range(1, CURRENT_MONTH + 1):
        factor = 1 + random.uniform(-variance, variance)
        result.append({"month": f"{m}월", "value": round(base * factor)})
    return result


def get_company_overview():
    """회사 전체 경영 현황 요약"""
    return {
        "company_name": "리스크제로(주)",
        "report_date": TODAY.isoformat(),
        "fiscal_year": CURRENT_YEAR,
        "total_employees": 87,
        "total_revenue": 4_850_000_000,
        "total_revenue_target": 6_000_000_000,
        "revenue_achievement_rate": 80.8,
        "operating_profit": 620_000_000,
        "operating_profit_margin": 12.8,
        "net_profit": 485_000_000,
        "yoy_revenue_growth": 15.2,
        "yoy_profit_growth": 8.7,
        "ongoing_projects": 23,
        "completed_projects": 14,
        "new_contracts_ytd": 18,
        "monthly_revenue": _monthly_series(400_000_000, 0.15),
        "department_headcount": {
            "사업수행팀": 28,
            "영업팀": 18,
            "전략기획실": 10,
            "인사팀": 12,
            "재무팀": 19,
        },
        "key_risks": [
            {"level": "high", "description": "주요 고객사 계약 갱신 협상 중 (3월 말 마감)"},
            {"level": "medium", "description": "신규 인력 충원 지연 (개발 직군)"},
            {"level": "low", "description": "사무실 임대 계약 갱신 (6월)"},
        ],
    }


def get_business_ops():
    """사업수행팀 경영 현황"""
    return {
        "department": "사업수행팀",
        "head": "김영수 팀장",
        "headcount": 28,
        "summary": {
            "ongoing_projects": 23,
            "completed_projects": 14,
            "delayed_projects": 3,
            "project_completion_rate": 82.4,
            "avg_project_duration_days": 95,
            "client_satisfaction_score": 4.3,
        },
        "projects": [
            {
                "name": "A사 안전보건 관리시스템 구축",
                "client": "A건설",
                "status": "진행중",
                "progress": 72,
                "budget": 350_000_000,
                "spent": 248_000_000,
                "deadline": "2026-05-15",
                "risk": "low",
            },
            {
                "name": "B사 스마트 안전 모니터링",
                "client": "B중공업",
                "status": "진행중",
                "progress": 45,
                "budget": 520_000_000,
                "spent": 210_000_000,
                "deadline": "2026-07-30",
                "risk": "medium",
            },
            {
                "name": "C사 AI 위험성 평가 플랫폼",
                "client": "C건설",
                "status": "진행중",
                "progress": 88,
                "budget": 280_000_000,
                "spent": 245_000_000,
                "deadline": "2026-03-31",
                "risk": "high",
            },
            {
                "name": "D사 산업안전 컨설팅",
                "client": "D제조",
                "status": "완료",
                "progress": 100,
                "budget": 150_000_000,
                "spent": 142_000_000,
                "deadline": "2026-02-28",
                "risk": "low",
            },
            {
                "name": "E사 건설현장 IoT 안전시스템",
                "client": "E건설",
                "status": "진행중",
                "progress": 30,
                "budget": 680_000_000,
                "spent": 185_000_000,
                "deadline": "2026-09-30",
                "risk": "low",
            },
        ],
        "monthly_delivery": _monthly_series(2, 0.3),
        "resource_utilization": 87.5,
    }


def get_sales():
    """영업팀 경영 현황"""
    return {
        "department": "영업팀",
        "head": "이지현 팀장",
        "headcount": 18,
        "summary": {
            "annual_target": 6_000_000_000,
            "ytd_actual": 4_850_000_000,
            "achievement_rate": 80.8,
            "pipeline_value": 3_200_000_000,
            "new_leads_month": 15,
            "conversion_rate": 32.5,
            "avg_deal_size": 285_000_000,
        },
        "pipeline": [
            {
                "client": "F그룹",
                "deal_name": "통합 안전관리 플랫폼",
                "value": 850_000_000,
                "stage": "제안서 제출",
                "probability": 60,
                "expected_close": "2026-04-15",
            },
            {
                "client": "G공사",
                "deal_name": "스마트 건설안전 시스템",
                "value": 1_200_000_000,
                "stage": "기술검토",
                "probability": 40,
                "expected_close": "2026-06-30",
            },
            {
                "client": "H제조",
                "deal_name": "산업안전 AI 솔루션",
                "value": 450_000_000,
                "stage": "협상중",
                "probability": 75,
                "expected_close": "2026-03-25",
            },
            {
                "client": "I건설",
                "deal_name": "현장 모니터링 시스템",
                "value": 320_000_000,
                "stage": "초기접촉",
                "probability": 20,
                "expected_close": "2026-08-30",
            },
            {
                "client": "J에너지",
                "deal_name": "위험성 평가 컨설팅",
                "value": 380_000_000,
                "stage": "제안서 제출",
                "probability": 55,
                "expected_close": "2026-05-15",
            },
        ],
        "monthly_sales": _monthly_series(550_000_000, 0.2),
        "top_clients_revenue": [
            {"client": "A건설", "revenue": 850_000_000},
            {"client": "B중공업", "revenue": 720_000_000},
            {"client": "C건설", "revenue": 580_000_000},
            {"client": "D제조", "revenue": 450_000_000},
            {"client": "E건설", "revenue": 380_000_000},
        ],
    }


def get_strategic_planning():
    """전략기획실 경영 현황"""
    return {
        "department": "전략기획실",
        "head": "박민준 실장",
        "headcount": 10,
        "summary": {
            "strategic_initiatives": 8,
            "completed_initiatives": 3,
            "on_track": 4,
            "at_risk": 1,
            "market_share": 12.5,
            "market_growth_rate": 18.3,
        },
        "initiatives": [
            {
                "name": "AI 기반 안전관리 솔루션 고도화",
                "status": "진행중",
                "progress": 65,
                "priority": "최상",
                "owner": "박민준",
                "deadline": "2026-12-31",
            },
            {
                "name": "동남아 시장 진출 전략",
                "status": "진행중",
                "progress": 40,
                "priority": "상",
                "owner": "최서연",
                "deadline": "2026-09-30",
            },
            {
                "name": "ESG 경영 체계 구축",
                "status": "진행중",
                "progress": 55,
                "priority": "상",
                "owner": "정하늘",
                "deadline": "2026-06-30",
            },
            {
                "name": "데이터 기반 의사결정 체계 수립",
                "status": "완료",
                "progress": 100,
                "priority": "중",
                "owner": "박민준",
                "deadline": "2026-02-28",
            },
        ],
        "market_analysis": {
            "total_market_size": 38_800_000_000,
            "company_position": "상위 5위",
            "growth_areas": ["AI 안전관리", "스마트 건설", "ESG 컨설팅"],
            "threats": ["대기업 진출 확대", "규제 변화"],
        },
        "kpi_tracking": [
            {"kpi": "신규 시장 진출", "target": 2, "actual": 1, "unit": "개국"},
            {"kpi": "신제품 출시", "target": 3, "actual": 2, "unit": "개"},
            {"kpi": "전략 파트너십", "target": 5, "actual": 4, "unit": "건"},
            {"kpi": "시장 점유율", "target": 15.0, "actual": 12.5, "unit": "%"},
        ],
    }


def get_hr():
    """인사팀 경영 현황"""
    return {
        "department": "인사팀",
        "head": "한소희 팀장",
        "headcount": 12,
        "summary": {
            "total_employees": 87,
            "new_hires_ytd": 12,
            "turnover_rate": 8.5,
            "avg_tenure_years": 3.2,
            "training_hours_per_person": 24,
            "employee_satisfaction": 78.5,
            "open_positions": 5,
        },
        "department_breakdown": [
            {"dept": "사업수행팀", "count": 28, "new_hires": 4, "turnover": 2},
            {"dept": "영업팀", "count": 18, "new_hires": 3, "turnover": 1},
            {"dept": "전략기획실", "count": 10, "new_hires": 1, "turnover": 0},
            {"dept": "인사팀", "count": 12, "new_hires": 2, "turnover": 1},
            {"dept": "재무팀", "count": 19, "new_hires": 2, "turnover": 1},
        ],
        "recruitment": [
            {"position": "AI 개발자", "dept": "사업수행팀", "status": "면접진행", "applicants": 35},
            {"position": "안전관리 컨설턴트", "dept": "사업수행팀", "status": "공고중", "applicants": 18},
            {"position": "영업 매니저", "dept": "영업팀", "status": "서류검토", "applicants": 22},
            {"position": "재무분석가", "dept": "재무팀", "status": "공고중", "applicants": 12},
            {"position": "기획 담당자", "dept": "전략기획실", "status": "최종면접", "applicants": 8},
        ],
        "training_programs": [
            {"name": "AI/ML 기초 교육", "participants": 25, "completion_rate": 80},
            {"name": "안전관리 전문가 과정", "participants": 15, "completion_rate": 93},
            {"name": "리더십 워크숍", "participants": 12, "completion_rate": 100},
            {"name": "ESG 교육", "participants": 45, "completion_rate": 67},
        ],
        "monthly_headcount": _monthly_series(85, 0.03),
    }


def get_finance():
    """재무팀 경영 현황"""
    return {
        "department": "재무팀",
        "head": "정태호 팀장",
        "headcount": 19,
        "summary": {
            "total_revenue": 4_850_000_000,
            "operating_profit": 620_000_000,
            "operating_margin": 12.8,
            "net_profit": 485_000_000,
            "total_assets": 8_200_000_000,
            "total_liabilities": 2_800_000_000,
            "equity": 5_400_000_000,
            "debt_ratio": 34.1,
            "current_ratio": 2.15,
            "cash_reserves": 1_850_000_000,
        },
        "income_statement": [
            {"item": "매출액", "current": 4_850_000_000, "previous": 4_210_000_000, "change": 15.2},
            {"item": "매출원가", "current": 3_100_000_000, "previous": 2_750_000_000, "change": 12.7},
            {"item": "매출총이익", "current": 1_750_000_000, "previous": 1_460_000_000, "change": 19.9},
            {"item": "판관비", "current": 1_130_000_000, "previous": 980_000_000, "change": 15.3},
            {"item": "영업이익", "current": 620_000_000, "previous": 480_000_000, "change": 29.2},
            {"item": "당기순이익", "current": 485_000_000, "previous": 370_000_000, "change": 31.1},
        ],
        "expense_breakdown": [
            {"category": "인건비", "amount": 2_100_000_000, "ratio": 43.3},
            {"category": "외주비", "amount": 980_000_000, "ratio": 20.2},
            {"category": "기술개발비", "amount": 620_000_000, "ratio": 12.8},
            {"category": "마케팅비", "amount": 350_000_000, "ratio": 7.2},
            {"category": "임차료", "amount": 280_000_000, "ratio": 5.8},
            {"category": "기타", "amount": 520_000_000, "ratio": 10.7},
        ],
        "monthly_revenue": _monthly_series(400_000_000, 0.15),
        "monthly_profit": _monthly_series(50_000_000, 0.25),
        "budget_vs_actual": [
            {"dept": "사업수행팀", "budget": 1_800_000_000, "actual": 1_720_000_000, "variance": -4.4},
            {"dept": "영업팀", "budget": 950_000_000, "actual": 980_000_000, "variance": 3.2},
            {"dept": "전략기획실", "budget": 450_000_000, "actual": 420_000_000, "variance": -6.7},
            {"dept": "인사팀", "budget": 380_000_000, "actual": 365_000_000, "variance": -3.9},
            {"dept": "재무팀", "budget": 620_000_000, "actual": 595_000_000, "variance": -4.0},
        ],
    }


def get_all_dashboard_data():
    """전체 대시보드 데이터"""
    return {
        "overview": get_company_overview(),
        "business_ops": get_business_ops(),
        "sales": get_sales(),
        "strategic_planning": get_strategic_planning(),
        "hr": get_hr(),
        "finance": get_finance(),
    }
