class ScratchError(Exception):
    def __init__(
        self,
        message: str,
        error_type: str = "internal_server_error",
        status_code: int = 500,
    ):
        self.status_code = status_code
        self._message = message
        self._error_type = error_type

    def __str__(self):
        return self.message

    @property
    def message(self):
        return self._message

    @property
    def error_type(self):
        return self._error_type


class ResourceNotFoundError(ScratchError):
    status_code = 404

    def __init__(
        self,
        resource_id,
        message="Resource not found",
        error_type="not_found_error",
    ):
        super().__init__(
            message=message,
            error_type=error_type,
            status_code=self.status_code,
        )
        self._resource_id = resource_id

    @property
    def resource_id(self):
        return self._resource_id


class CustomerNotFound(ResourceNotFoundError):
    def __init__(self, customer_id):
        super().__init__(
            message="A matching customer could not be found",
            error_type="customer_not_found",
            resource_id=customer_id,
        )
