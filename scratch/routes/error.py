import traceback

from app import logger
from flask_smorest import Blueprint
from models.error import ResourceNotFoundError, ScratchError
from schemas.error import ResourceNotFoundSchema, ScratchErrorSchema

error_bp = Blueprint("error", __name__, description="handles all error handling")


@error_bp.app_errorhandler(Exception)
@error_bp.response(500, ScratchErrorSchema)
def generic_exception_handler(e: Exception) -> ScratchError:
    logger_bind_error(e)
    return ScratchError(str(e))


@error_bp.app_errorhandler(ResourceNotFoundError)
@error_bp.response(ResourceNotFoundError.status_code, ResourceNotFoundSchema)
def resource_not_found_handler(e: ResourceNotFoundError) -> ResourceNotFoundError:
    logger_bind_error(e)
    return e


def logger_bind_error(e):
    stacktrace = " | ".join(traceback.format_exc().splitlines()[-5:])
    stacktrace = stacktrace.replace("\n", " ").replace("  ", "").replace('"', "'")
    logger().bind(error_message=str(e), error_stacktrace=stacktrace)
