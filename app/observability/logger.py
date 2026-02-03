import logging
import logging.config
import json
from contextvars import ContextVar
import uuid
from pathlib import Path

correlation_id_ctx: ContextVar[str] = ContextVar("correlation_id", default="-")

class ContextFilter(logging.Filter):
    def filter(self, record):
        from opentelemetry import trace
        record.correlation_id = correlation_id_ctx.get()
        
        # Extract OTEL trace context if available
        span = trace.get_current_span()
        if span.is_recording():
            span_context = span.get_span_context()
            record.otelTraceID = trace.format_trace_id(span_context.trace_id)
            record.otelSpanID = trace.format_span_id(span_context.span_id)
        else:
            record.otelTraceID = "-"
            record.otelSpanID = "-"
        return True


class LevelFilter(logging.Filter):
    def __init__(self, levels):
        super().__init__()
        self.levels = set()
        for level in levels:
            if isinstance(level, int):
                self.levels.add(level)
                continue
            name = str(level).upper()
            if name not in logging._nameToLevel:
                raise ValueError(f"Unknown log level: {level}")
            self.levels.add(logging._nameToLevel[name])

    def filter(self, record):
        return record.levelno in self.levels


def setup_logging():
    # Ensure log directory exists
    log_dir = Path("app/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    with open("app/config/logging_config.json") as f: 
        config = json.load(f)

    logging.config.dictConfig(config)

    root_logger = logging.getLogger()
    # Add filter to ALL handlers BEFORE logging starts
    context_filter = ContextFilter()
    for handler in root_logger.handlers:
        handler.addFilter(context_filter)
    
    # Force flush on all file handlers to ensure immediate writes
    for handler in root_logger.handlers:
        if isinstance(handler, logging.FileHandler):
            handler.flush()


def get_logger(name: str):
    return logging.getLogger(name)


def set_correlation_id(cid: str):
    correlation_id_ctx.set(cid)


def generate_correlation_id():
    return str(uuid.uuid4())
    