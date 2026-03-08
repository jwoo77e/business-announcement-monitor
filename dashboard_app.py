"""
경영진 대시보드 웹 애플리케이션
Flask 기반의 경영 현황 대시보드를 제공합니다.
"""

from flask import Flask, render_template, jsonify
from dashboard_data import (
    get_all_dashboard_data,
    get_company_overview,
    get_business_ops,
    get_sales,
    get_strategic_planning,
    get_hr,
    get_finance,
)

app = Flask(__name__)


@app.route("/")
def index():
    """메인 대시보드 페이지"""
    data = get_all_dashboard_data()
    return render_template("dashboard.html", data=data)


@app.route("/api/overview")
def api_overview():
    """회사 전체 현황 API"""
    return jsonify(get_company_overview())


@app.route("/api/business-ops")
def api_business_ops():
    """사업수행팀 현황 API"""
    return jsonify(get_business_ops())


@app.route("/api/sales")
def api_sales():
    """영업팀 현황 API"""
    return jsonify(get_sales())


@app.route("/api/strategic-planning")
def api_strategic_planning():
    """전략기획실 현황 API"""
    return jsonify(get_strategic_planning())


@app.route("/api/hr")
def api_hr():
    """인사팀 현황 API"""
    return jsonify(get_hr())


@app.route("/api/finance")
def api_finance():
    """재무팀 현황 API"""
    return jsonify(get_finance())


@app.route("/api/all")
def api_all():
    """전체 데이터 API"""
    return jsonify(get_all_dashboard_data())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
