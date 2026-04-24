from flask import jsonify

def register_error_handlers(app):
    
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify({
            "status": "error",
            "message": "Resource not found",
            "error": str(e.description)
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({
            "status": "error",
            "message": "Method HTTP tidak diizinkan untuk route ini"
        }), 405

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({
            "status": "error",
            "message": "Terjadi kesalahan internal pada server",
            "error": "Silakan hubungi administrator"
        }), 500

    @app.errorhandler(Exception)
    def handle_unexpected_error(e):
        # Menangkap error database atau error coding lainnya
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred",
            "details": str(e)
        }), 500
