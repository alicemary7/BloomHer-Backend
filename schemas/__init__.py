# INFO:     Will watch for changes in these directories: ['C:\\Full stack project\\fastapi']
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [15376] using StatReload
# Process SpawnProcess-1:
# Traceback (most recent call last):
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\Lib\multiprocessing\process.py", line 313, in _bootstrap
#     self.run()
#     ~~~~~~~~^^
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\Lib\multiprocessing\process.py", line 108, in run
#     self._target(*self._args, **self._kwargs)
#     ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\uvicorn\_subprocess.py", line 80, in subprocess_started
#     target(sockets=sockets)
#     ~~~~~~^^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\uvicorn\server.py", line 67, in run
#     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\Lib\asyncio\runners.py", line 195, in run
#     return runner.run(main)
#            ~~~~~~~~~~^^^^^^
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\Lib\asyncio\runners.py", line 118, in run
#     return self._loop.run_until_complete(task)
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\Lib\asyncio\base_events.py", line 725, in run_until_complete
#     return future.result()
#            ~~~~~~~~~~~~~^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\uvicorn\server.py", line 71, in serve
#     await self._serve(sockets)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\uvicorn\server.py", line 78, in _serve
#     config.load()
#     ~~~~~~~~~~~^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\uvicorn\config.py", line 439, in load
#     self.loaded_app = import_from_string(self.app)
#                       ~~~~~~~~~~~~~~~~~~^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\uvicorn\importer.py", line 19, in import_from_string
#     module = importlib.import_module(module_str)
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py", line 88, in import_module
#     return _bootstrap._gcd_import(name[level:], package, level)
#            ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
#   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
#   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
#   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
#   File "<frozen importlib._bootstrap_external>", line 1027, in exec_module
#   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
#   File "C:\Full stack project\fastapi\main.py", line 3, in <module>
#     from models import (
#     ...<2 lines>...
#     )
# ImportError: cannot import name 'Payment' from 'models' (C:\Full stack project\fastapi\models\__init__.py)
# WARNING:  StatReload detected changes in 'models\__init__.py'. Reloading...
#  INFO:     Started server process [9860]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
# INFO:     127.0.0.1:61345 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61345 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61345 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61345 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61345 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:56653 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61035 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61035 - "GET /openapi.json HTTP/1.1" 200 OK
# WARNING:  StatReload detected changes in 'models\users.py'. Reloading...
#  INFO:     127.0.0.1:58779 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61187 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61187 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:58777 - "GET /address/ HTTP/1.1" 200 OK
# INFO:     127.0.0.1:51768 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:51768 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:62932 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:62932 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:62680 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:62680 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:63010 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:63010 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57478 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57478 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61964 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61964 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61964 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:58382 - "GET /products/ HTTP/1.1" 200 OK
# INFO:     127.0.0.1:49291 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:49291 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:51976 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:56116 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:56116 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:50241 - "GET /products/ HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57037 - "POST /products/ HTTP/1.1" 422 Unprocessable Content
# INFO:     127.0.0.1:53420 - "POST /products/ HTTP/1.1" 422 Unprocessable Content
# INFO:     127.0.0.1:64896 - "POST /products/ HTTP/1.1" 422 Unprocessable Content
# INFO:     127.0.0.1:57768 - "POST /products/ HTTP/1.1" 201 Created
# INFO:     127.0.0.1:49708 - "POST /products/ HTTP/1.1" 201 Created
# INFO:     127.0.0.1:63007 - "POST /products/ HTTP/1.1" 201 Created
# INFO:     127.0.0.1:61488 - "POST /users/signup HTTP/1.1" 200 OK
# INFO:     127.0.0.1:53192 - "POST /users/signup HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57445 - "POST /orders/?user_id=2 HTTP/1.1" 500 Internal Server Error
# ERROR:    Exception in ASGI application
# Traceback (most recent call last):
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1967, in _exec_single_context
#     self.dialect.do_execute(
#     ~~~~~~~~~~~~~~~~~~~~~~~^
#         cursor, str_statement, effective_parameters, context
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 951, in do_execute
#     cursor.execute(statement, parameters)
#     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
# psycopg2.errors.NotNullViolation: null value in column "product_id" of relation "orders" violates not-null constraint
# DETAIL:  Failing row contains (1, 2, null, null, 2990, pending, 2025-12-28 16:18:22.480098).


# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\uvicorn\protocols\http\h11_impl.py", line 403, in run_asgi
#     result = await app(  # type: ignore[func-returns-value]
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         self.scope, self.receive, self.send
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\uvicorn\middleware\proxy_headers.py", line 60, in __call__
#     return await self.app(scope, receive, send)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\applications.py", line 1134, in __call__
#     await super().__call__(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\applications.py", line 113, in __call__
#     await self.middleware_stack(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\middleware\errors.py", line 186, in __call__
#     raise exc
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\middleware\errors.py", line 164, in __call__
#     await self.app(scope, receive, _send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\middleware\exceptions.py", line 63, in __call__
#     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
#     raise exc
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
#     await app(scope, receive, sender)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\middleware\asyncexitstack.py", line 18, in __call__
#     await self.app(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\routing.py", line 716, in __call__
#     await self.middleware_stack(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\routing.py", line 736, in app
#     await route.handle(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\routing.py", line 290, in handle
#     await self.app(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\routing.py", line 125, in app
#     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
#     raise exc
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
#     await app(scope, receive, sender)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\routing.py", line 111, in app
#     response = await f(request)
#                ^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\routing.py", line 391, in app
#     raw_response = await run_endpoint_function(
#                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     ...<3 lines>...
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\routing.py", line 292, in run_endpoint_function
#     return await run_in_threadpool(dependant.call, **values)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\concurrency.py", line 38, in run_in_threadpool
#     return await anyio.to_thread.run_sync(func)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\anyio\to_thread.py", line 56, in run_sync
#     return await get_async_backend().run_sync_in_worker_thread(
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         func, args, abandon_on_cancel=abandon_on_cancel, limiter=limiter
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\anyio\_backends\_asyncio.py", line 2485, in run_sync_in_worker_thread
#     return await future
#            ^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\anyio\_backends\_asyncio.py", line 976, in run
#     result = context.run(func, *args)
#   File "C:\Full stack project\fastapi\routers\order.py", line 42, in create_order
#     return orders
#     ^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2030, in commit
#     trans.commit(_to_root=True)
#     ~~~~~~~~~~~~^^^^^^^^^^^^^^^
#   File "<string>", line 2, in commit
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
#     ret_value = fn(self, *arg, **kw)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1311, in commit
#     self._prepare_impl()
#     ~~~~~~~~~~~~~~~~~~^^
#   File "<string>", line 2, in _prepare_impl
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
#     ret_value = fn(self, *arg, **kw)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1286, in _prepare_impl
#     self.session.flush()
#     ~~~~~~~~~~~~~~~~~~^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4331, in flush
#     self._flush(objects)
#     ~~~~~~~~~~~^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4466, in _flush
#     with util.safe_reraise():
#          ~~~~~~~~~~~~~~~~~^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 224, in __exit__
#     raise exc_value.with_traceback(exc_tb)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4427, in _flush
#     flush_context.execute()
#     ~~~~~~~~~~~~~~~~~~~~~^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 466, in execute
#     rec.execute(self)
#     ~~~~~~~~~~~^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 642, in execute
#     util.preloaded.orm_persistence.save_obj(
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
#         self.mapper,
#         ^^^^^^^^^^^^
#         uow.states_for_mapper_hierarchy(self.mapper, False, False),
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         uow,
#         ^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 93, in save_obj
#     _emit_insert_statements(
#     ~~~~~~~~~~~~~~~~~~~~~~~^
#         base_mapper,
#         ^^^^^^^^^^^^
#     ...<3 lines>...
#         insert,
#         ^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1233, in _emit_insert_statements
#     result = connection.execute(
#         statement,
#         params,
#         execution_options=execution_options,
#     )
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1419, in execute
#     return meth(
#         self,
#         distilled_parameters,
#         execution_options or NO_OPTIONS,
#     )
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
#     return connection._execute_clauseelement(
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
#         self, distilled_params, execution_options
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1641, in _execute_clauseelement
#     ret = self._execute_context(
#         dialect,
#     ...<8 lines>...
#         cache_hit=cache_hit,
#     )
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1846, in _execute_context
#     return self._exec_single_context(
#            ~~~~~~~~~~~~~~~~~~~~~~~~~^
#         dialect, context, statement, parameters
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1986, in _exec_single_context
#     self._handle_dbapi_exception(
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
#         e, str_statement, effective_parameters, cursor, context
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2355, in _handle_dbapi_exception
#     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1967, in _exec_single_context
#     self.dialect.do_execute(
#     ~~~~~~~~~~~~~~~~~~~~~~~^
#         cursor, str_statement, effective_parameters, context
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 951, in do_execute
#     cursor.execute(statement, parameters)
#     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
# sqlalchemy.exc.IntegrityError: (psycopg2.errors.NotNullViolation) null value in column "product_id" of relation "orders" violates not-null constraint
# DETAIL:  Failing row contains (1, 2, null, null, 2990, pending, 2025-12-28 16:18:22.480098).

# [SQL: INSERT INTO orders (user_id, total_amount, status, order_date) VALUES (%(user_id)s, %(total_amount)s, %(status)s, %(order_date)s) RETURNING orders.id]
# [parameters: {'user_id': 2, 'total_amount': 2990.0, 'status': 'pending', 'order_date': datetime.datetime(2025, 12, 28, 16, 18, 22, 480098)}]
# (Background on this error at: https://sqlalche.me/e/20/gkpj)
# INFO:     127.0.0.1:57543 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:53154 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:53154 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:53154 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:54667 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:54667 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:51890 - "GET /products/ HTTP/1.1" 200 OK
# INFO:     127.0.0.1:63071 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57330 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57330 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:50761 - "POST /orders/?user_id=2 HTTP/1.1" 500 Internal Server Error
# ERROR:    Exception in ASGI application
# Traceback (most recent call last):
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1967, in _exec_single_context
#     self.dialect.do_execute(
#     ~~~~~~~~~~~~~~~~~~~~~~~^
#         cursor, str_statement, effective_parameters, context
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 951, in do_execute
#     cursor.execute(statement, parameters)
#     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
# psycopg2.errors.NotNullViolation: null value in column "product_id" of relation "orders" violates not-null constraint
# DETAIL:  Failing row contains (2, 2, null, null, 598, pending, 2025-12-29 02:14:12.732279).


# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\uvicorn\protocols\http\h11_impl.py", line 403, in run_asgi
#     result = await app(  # type: ignore[func-returns-value]
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         self.scope, self.receive, self.send
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\uvicorn\middleware\proxy_headers.py", line 60, in __call__
#     return await self.app(scope, receive, send)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\applications.py", line 1134, in __call__
#     await super().__call__(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\applications.py", line 113, in __call__
#     await self.middleware_stack(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\middleware\errors.py", line 186, in __call__
#     raise exc
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\middleware\errors.py", line 164, in __call__
#     await self.app(scope, receive, _send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\middleware\exceptions.py", line 63, in __call__
#     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
#     raise exc
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
#     await app(scope, receive, sender)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\middleware\asyncexitstack.py", line 18, in __call__
#     await self.app(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\routing.py", line 716, in __call__
#     await self.middleware_stack(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\routing.py", line 736, in app
#     await route.handle(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\routing.py", line 290, in handle
#     await self.app(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\routing.py", line 125, in app
#     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
#     raise exc
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
#     await app(scope, receive, sender)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\routing.py", line 111, in app
#     response = await f(request)
#                ^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\routing.py", line 391, in app
#     raw_response = await run_endpoint_function(
#                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     ...<3 lines>...
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\fastapi\routing.py", line 292, in run_endpoint_function
#     return await run_in_threadpool(dependant.call, **values)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\starlette\concurrency.py", line 38, in run_in_threadpool
#     return await anyio.to_thread.run_sync(func)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\anyio\to_thread.py", line 56, in run_sync
#     return await get_async_backend().run_sync_in_worker_thread(
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         func, args, abandon_on_cancel=abandon_on_cancel, limiter=limiter
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\anyio\_backends\_asyncio.py", line 2485, in run_sync_in_worker_thread
#     return await future
#            ^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\anyio\_backends\_asyncio.py", line 976, in run
#     result = context.run(func, *args)
#   File "C:\Full stack project\fastapi\routers\order.py", line 42, in create_order
#     return orders
#     ^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2030, in commit
#     trans.commit(_to_root=True)
#     ~~~~~~~~~~~~^^^^^^^^^^^^^^^
#   File "<string>", line 2, in commit
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
#     ret_value = fn(self, *arg, **kw)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1311, in commit
#     self._prepare_impl()
#     ~~~~~~~~~~~~~~~~~~^^
#   File "<string>", line 2, in _prepare_impl
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
#     ret_value = fn(self, *arg, **kw)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1286, in _prepare_impl
#     self.session.flush()
#     ~~~~~~~~~~~~~~~~~~^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4331, in flush
#     self._flush(objects)
#     ~~~~~~~~~~~^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4466, in _flush
#     with util.safe_reraise():
#          ~~~~~~~~~~~~~~~~~^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 224, in __exit__
#     raise exc_value.with_traceback(exc_tb)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4427, in _flush
#     flush_context.execute()
#     ~~~~~~~~~~~~~~~~~~~~~^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 466, in execute
#     rec.execute(self)
#     ~~~~~~~~~~~^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 642, in execute
#     util.preloaded.orm_persistence.save_obj(
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
#         self.mapper,
#         ^^^^^^^^^^^^
#         uow.states_for_mapper_hierarchy(self.mapper, False, False),
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         uow,
#         ^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 93, in save_obj
#     _emit_insert_statements(
#     ~~~~~~~~~~~~~~~~~~~~~~~^
#         base_mapper,
#         ^^^^^^^^^^^^
#     ...<3 lines>...
#         insert,
#         ^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1233, in _emit_insert_statements
#     result = connection.execute(
#         statement,
#         params,
#         execution_options=execution_options,
#     )
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1419, in execute
#     return meth(
#         self,
#         distilled_parameters,
#         execution_options or NO_OPTIONS,
#     )
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
#     return connection._execute_clauseelement(
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
#         self, distilled_params, execution_options
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1641, in _execute_clauseelement
#     ret = self._execute_context(
#         dialect,
#     ...<8 lines>...
#         cache_hit=cache_hit,
#     )
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1846, in _execute_context
#     return self._exec_single_context(
#            ~~~~~~~~~~~~~~~~~~~~~~~~~^
#         dialect, context, statement, parameters
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1986, in _exec_single_context
#     self._handle_dbapi_exception(
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
#         e, str_statement, effective_parameters, cursor, context
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2355, in _handle_dbapi_exception
#     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1967, in _exec_single_context
#     self.dialect.do_execute(
#     ~~~~~~~~~~~~~~~~~~~~~~~^
#         cursor, str_statement, effective_parameters, context
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 951, in do_execute
#     cursor.execute(statement, parameters)
#     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
# sqlalchemy.exc.IntegrityError: (psycopg2.errors.NotNullViolation) null value in column "product_id" of relation "orders" violates not-null constraint
# DETAIL:  Failing row contains (2, 2, null, null, 598, pending, 2025-12-29 02:14:12.732279).

# [SQL: INSERT INTO orders (user_id, total_amount, status, order_date) VALUES (%(user_id)s, %(total_amount)s, %(status)s, %(order_date)s) RETURNING orders.id]
# [parameters: {'user_id': 2, 'total_amount': 598.0, 'status': 'pending', 'order_date': datetime.datetime(2025, 12, 29, 2, 14, 12, 732279)}]
# (Background on this error at: https://sqlalche.me/e/20/gkpj)
# INFO:     127.0.0.1:52519 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:58439 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:58439 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:64489 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:64489 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:55036 - "GET /products/ HTTP/1.1" 200 OK
# INFO:     127.0.0.1:52846 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:52846 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:52846 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57759 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57759 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60424 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:62990 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:62990 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61465 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:59093 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:59093 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60934 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60934 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60934 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60913 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60913 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:63351 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:55253 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:55253 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:62756 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60674 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60674 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60674 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60674 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60674 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60674 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:54006 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:54006 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:51849 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:51849 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:54440 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:54440 - "GET /favicon.ico HTTP/1.1" 404 Not Found
# INFO:     127.0.0.1:50583 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:50583 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:59171 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:59171 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:59171 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:50941 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:53114 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:53114 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:52379 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:52379 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:52379 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:65518 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:65518 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:65518 - "GET /openapi.json HTTP/1.1" 200 OK
