# from opentelemetry import trace
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# # setup (one time)
# trace.set_tracer_provider(TracerProvider())
# tracer = trace.get_tracer(__name__)

# trace.get_tracer_provider().add_span_processor(
#     SimpleSpanProcessor(ConsoleSpanExporter())
# )

# # normal function
# def add_employee():
#     with tracer.start_as_current_span("add_employee"):
#         print("Employee added")
# add_employee()

from opentelemetry import metrics

meter = metrics.get_meter(__name__)

request_counter = meter.create_counter("requests")

request_counter.add(1)
print("Request recorded")  