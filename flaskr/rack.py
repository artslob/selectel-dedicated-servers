from flask import Blueprint
from flask import jsonify

from flaskr.models import Rack

bp = Blueprint('rack', __name__, url_prefix='/rack')


@bp.route('/all', methods=('GET',))
def all_racks():
    rows = Rack.query.all()
    return jsonify([rack.as_dict() for rack in rows])


@bp.route('/<int:id>', methods=('GET',))
def get_rack(id):
    rack = Rack.query.get(id)
    if not rack:
        return jsonify({}), 404

    return jsonify(rack.as_dict())
