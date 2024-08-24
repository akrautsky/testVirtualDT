from .users_route import user_bp
from .get_my_order import get_my_order_bp
from .get_order_summary import get_Order_Summary_bp
from .save_order import save_order_bp
from .process_my_order import process_my_order_bp
from .process_my_tip import process_my_tip_bp

def register_blueprint(app):
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(get_my_order_bp, url_prefix='/api/myOrder')
    app.register_blueprint(get_Order_Summary_bp, url_prefix='/api/orderSummary')
    app.register_blueprint(save_order_bp, url_prefix='/api/saveOrder')
    app.register_blueprint(process_my_order_bp, url_prefix='/api/processMyOrder')
    app.register_blueprint(process_my_tip_bp, url_prefix='/api/processMyTip')