import base64
import gzip
import json
import os
import urllib.error
import urllib.parse
from pprint import pprint

import mitmproxy
from mitmproxy import ctx

from garbevents.settings import Settings as ST


class GetData:
    """
    A garbevents HTTP request class.
    """

    events_list = []

    @staticmethod
    def chunks(arr, n):
        """

        :param arr:
        :param n:
        :return:
        """
        return [arr[i : i + n] for i in range(0, len(arr), n)]

    @staticmethod
    def gzip_decompress(data):
        """
        解密上报数据
        :param data:
        :return:
        """
        try:
            return gzip.decompress(data)
        except AttributeError:
            from io import StringIO

            buf = StringIO()
            buf.write(data)
            fd = gzip.GzipFile(fileobj=buf, mode="r")
            fd.rewind()
            value = fd.read()
            fd.close()
            return value

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """

        :param flow:
        :return:
        """

        request_data = flow.request
        self.request_url = request_data.url

        if ST.url in self.request_url:
            ctx.log.info(
                f"Get the complete URL after splitting ====>{self.request_url}"
            )
            api = self.request_url.split("/")[3]
            ctx.log.error(f"Get API address after splitting ====>{api}")

            request_content = str(flow.request.content).split("&")[2].split("=")[1]
            ctx.log.info(f"Get encrypted data after splitting ====>{request_content}")

            gzip_data = urllib.parse.unquote(request_content)
            data_list = json.loads(
                self.gzip_decompress(base64.b64decode(gzip_data)).decode("utf8")
            )

            for result_list in data_list:
                ctx.log.error("Get JSON string after decrypting data ====>")
                pprint(result_list)

                try:
                    event = result_list["event"]
                    ctx.log.error(
                        f"Get the event name after decrypting the data ====>{event}"
                    )
                    self.events_list.append(event)
                except KeyError:
                    ctx.log.warn("No events！")
                event_list = list(set(self.events_list))

                if not os.path.exists(ST.report_path):
                    os.mkdir(ST.report_path)
                    ctx.log.info(ST.report_path + "Successfully created！")

                file = open(f"{ST.report_path}/now_event.txt", "w")
                for line in event_list:
                    file.write(line + "\n")
                ctx.log.warn(f"Current event name collection ====>{event_list}")
                lost_list = list(set(ST.all_events).difference(set(event_list)))
                ctx.log.warn(f"Missing event name collection ====>{lost_list}")
                file = open(f"{ST.report_path}/lost_event.txt", "w")
                for line in lost_list:
                    file.write(line + "\n")
