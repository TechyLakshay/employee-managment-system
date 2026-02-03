from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor


def setup_observability(app):
    

    # 1. Setup tracer
    trace.set_tracer_provider(TracerProvider())

    tracer_provider = trace.get_tracer_provider()
    tracer_provider.add_span_processor(
        SimpleSpanProcessor(ConsoleSpanExporter())
    )

    # 2. Auto-instrument FastAPI
    FastAPIInstrumentor.instrument_app(app)

    # 3. Auto-instrument logging - DO NOT override format (set_logging_format=False)
    # This allows your custom logging config to work with OTEL trace context
    LoggingInstrumentor().instrument(set_logging_format=False)

    return app

