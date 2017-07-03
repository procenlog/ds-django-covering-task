from .models import RequestRecord


class RequestKeeperMiddleware:
    def process_view(self, request, view, args, kwargs):
        record = RequestRecord(path=request.path)
        record.save()