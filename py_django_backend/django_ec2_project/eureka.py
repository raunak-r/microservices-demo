# from py_eureka_client.eureka_client import EurekaClient
#
# import logging
#
# logging.basicConfig()
# APP_NAME = "pydjango"
#
# ec = EurekaClient(
#     eureka_server="http://localhost/8081",
#     app_name=APP_NAME,
#     instance_port=8000)
#
# result = ec.do_service(APP_NAME, "/context/path", return_type="json")

import py_eureka_client.eureka_client as eureka_client

your_rest_server_port = 8000
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init(eureka_server="http://localhost:8081",
                   app_name="pydjango",
                   instance_port=your_rest_server_port)