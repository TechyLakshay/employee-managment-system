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

    # 3. Auto-instrument logging
    LoggingInstrumentor().instrument()

# import json
# import logging
# from opentelemetry import trace
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
# from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
# from opentelemetry.instrumentation.logging import LoggingInstrumentor


# def setup_observability(app):
#     # 1. Load config
#     with open("app/config/observability.json") as f:
#         config = json.load(f)

#     # 2. Set log level
#     logging.getLogger().setLevel(config.get("log_level", "INFO"))

#     # 3. Enable tracing only if config says so
#     if config.get("enable_tracing"):
#         trace.set_tracer_provider(TracerProvider())

#         tracer_provider = trace.get_tracer_provider()
#         tracer_provider.add_span_processor(
#             SimpleSpanProcessor(ConsoleSpanExporter())
#         )

#         FastAPIInstrumentor.instrument_app(app)
#         LoggingInstrumentor().instrument()
#         logging.info("Observability setup complete with tracing enabled.")
#     else:
#         logging.info("Observability setup complete with tracing disabled.")