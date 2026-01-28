# INFO:     Will watch for changes in these directories: ['C:\\Full stack project\\fastapi']
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [13324] using StatReload
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
#  Process SpawnProcess-2:
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
# psycopg2.errors.UniqueViolation: duplicate key value violates unique constraint "pg_class_relname_nsp_index"
# DETAIL:  Key (relname, relnamespace)=(payments_id_seq, 2200) already exists.


# The above exception was the direct cause of the following exception:

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
#   File "C:\Full stack project\fastapi\main.py", line 17, in <module>
#     Base.metadata.create_all(bind=engine)
#     ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\schema.py", line 5928, in create_all
#     bind._run_ddl_visitor(
#     ~~~~~~~~~~~~~~~~~~~~~^
#         ddl.SchemaGenerator, self, checkfirst=checkfirst, tables=tables
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 3252, in _run_ddl_visitor
#     conn._run_ddl_visitor(visitorcallable, element, **kwargs)
#     ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2459, in _run_ddl_visitor
#     ).traverse_single(element)
#       ~~~~~~~~~~~~~~~^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\visitors.py", line 661, in traverse_single
#     return meth(obj, **kw)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\ddl.py", line 984, in visit_metadata
#     self.traverse_single(
#     ~~~~~~~~~~~~~~~~~~~~^
#         table,
#         ^^^^^^
#     ...<2 lines>...
#         _is_metadata_operation=True,
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\visitors.py", line 661, in traverse_single
#     return meth(obj, **kw)
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\ddl.py", line 1022, in visit_table
#     )._invoke_with(self.connection)
#       ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\ddl.py", line 321, in _invoke_with
#     return bind.execute(self)
#            ~~~~~~~~~~~~^^^^^^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1419, in execute
#     return meth(
#         self,
#         distilled_parameters,
#         execution_options or NO_OPTIONS,
#     )
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\ddl.py", line 187, in _execute_on_connection
#     return connection._execute_ddl(
#            ~~~~~~~~~~~~~~~~~~~~~~~^
#         self, distilled_params, execution_options
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\AliceMarySureshKumar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1530, in _execute_ddl
#     ret = self._execute_context(
#         dialect,
#     ...<4 lines>...
#         compiled,
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
# sqlalchemy.exc.IntegrityError: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "pg_class_relname_nsp_index"
# DETAIL:  Key (relname, relnamespace)=(payments_id_seq, 2200) already exists.

# [SQL: 
# CREATE TABLE payments (
# 	id SERIAL NOT NULL, 
# 	order_id INTEGER NOT NULL, 
# 	amount FLOAT NOT NULL, 
# 	payment_method VARCHAR NOT NULL, 
# 	status VARCHAR, 
# 	created_at TIMESTAMP WITHOUT TIME ZONE, 
# 	PRIMARY KEY (id), 
# 	FOREIGN KEY(order_id) REFERENCES orders (id)
# )

# ]
# (Background on this error at: https://sqlalche.me/e/20/gkpj)
# WARNING:  StatReload detected changes in 'models\product.py'. Reloading...
#  INFO:     Started server process [13868]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
# WARNING:  StatReload detected changes in 'main.py'. Reloading...
 