"""
Package responsible for handle requests from a frontend.
"""
from flask import Flask
from app.views.candidates import get_candidates, get_candidate
from app.views.hiring_stages import get_hiring_stages
from app.views.offices import get_offices
from app.views.benefits import get_benefits
from app.views.hiring_types import get_hiring_types
from app.views.job_postings import get_job_postings, get_job_posting, export_job_posting
def add_views(app: Flask):
    """
    Maps urls and functions to the Flask application.
    Args:
        app (Flask): the rh-backend app
    """
    app.add_url_rule('/api/v1/hiring_stages', view_func=get_hiring_stages)
    app.add_url_rule('/api/v1/candidates', view_func=get_candidates)
    app.add_url_rule('/api/v1/candidates/<candidate_id>', view_func=get_candidate, methods=['GET', 'PATCH'])
    app.add_url_rule('/api/v1/job_postings', view_func=get_job_postings, methods=['GET', 'PATCH', 'POST'])
    app.add_url_rule('/api/v1/job_postings/<job_posting_title>', view_func=get_job_posting, methods=['GET', 'PATCH'])
    app.add_url_rule('/api/v1/job_postings/import/<stage>', view_func=export_job_posting, methods=['GET', 'PATCH'])
    app.add_url_rule('/api/v1/offices', view_func=get_offices, methods=['GET', 'PATCH'])
    app.add_url_rule('/api/v1/benefits', view_func=get_benefits, methods=['GET', 'PATCH'])
    app.add_url_rule('/api/v1/hiring_types', view_func=get_hiring_types, methods=['GET', 'PATCH'])
    