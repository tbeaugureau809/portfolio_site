from flask import Blueprint, redirect, jsonify, url_for

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return redirect(url_for('navigation.get_homepage'))

@bp.route('/health')
def health():
    return jsonify({"status": "ok"})