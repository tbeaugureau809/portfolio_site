from flask import Blueprint, redirect, jsonify

bp = Blueprint('main', __name__)

@bp.route('/', __name__)
def index():
    return redirect("/")

@bp.routes('/health')
def health():
    return jsonify({"status": "ok"})