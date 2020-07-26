import base64
import gzip
import json
import urllib.parse
import urllib.error
import zlib

ss = 'H4sIAAAAAAAAAO2VXWvbMBSG/8pQepkYyZZsKXdlH5CLscLYB4whFFuOtdqSseRkofS/T3KSNWnaQqGFXvjK8qsj6Zz36EG/bgB3ncivuSrAfIYooVkKaQqnwKlGgjkijKQpYTiFCfbitvUiGJaAKSiUdUrnblgNUIIykhFM/UytlmB+Ay6GL7jURWd8zHQQ+Fp2VhntJ5IojkL4hWjbIxnBCEfZIbyRrjLhgNwU8iAW0glVD2ITWamt6WwhnIiEFvXWqdz60XBqZIvr6Osu4oOPuLxaTCZDBR/XUrvJ5HQu+iPWYjJJECTgdgpkiPHHGP3Nyu59rYbC2860snNK2oerNPaoGhaUQq5VLndGlSiOlxmlNKMSCgSf8KXxJYcqPy/esd3GpwfZvJNS840qXOW7BSm8EyupVpXPPU5wUBuh+1Lkru9k5zf5qYRp1BPee3kxtBVCGPv/vBJay3rQcFi3UaUCc9f10v9o6Tamu+b7G/Jj8WkB9u4dtHxv3rJ3zmiuRbhgYNWZjeZ9G1wVK3mQK9OEXvv6+/q/uDW9q/jgCW9NOyzyaX4/Sh5iGJLf2b3LlQhMU0lnGU7kzA+LGSOwnMUMEpJiyJZZsLYW1vG7bl+F7b+0Uh+mQnJ3eV0oy0vVeb0Q250J/rLwsu5txU/RSRGC7HZ6QhrKUMZIwjA9A41igkbQRtBeHDQnfIft6mHOlC7kX1/BfeKWxm/RvB5mx71+ecySmDDKUnb2nBGEcDpSNlL2OpTJJyEjbwWyRlobsqz9vefeD/ds4hC8/7BBTGkCSYbPkEsoGZEbkXsd5PaEPQ4deivQ9V7nvvulqp//wiF0j7dZDGF4+ShDZ8BROAI3Avdc4B7G4ZS4gBZf+Xu7fgS6N0vP73/fsTAK8hAAAA=='
aa = 'H4sIAAAAAAAAAO2Yz2vUQBTH%2FxXJ9rgbJvMjmfRWsIU9iEVBBZEwm8w2Y5OZMMluW0qvnjwoeBe8ePIgnvx%2FVOx%2F4ZvZFrvdWrpdEKULgSTfeW9m3rzvZ1ny%2FDjIOivy%2FUwVwWZEMCecYZz0g07VEhSWsjimnDFCIxCPGhADnxH0g0K1ndJ555ODiEQJSxjlMFKpUbB5HGz4e7ClC2sgpu%2BFbCptq4yGARLi0IVviKa5IEcopGFyHl7LrjRugdwU8lwsZCdU5cU6bKVujW0L0YlQaFEddSpv4cmvGrbFfvh4FnEfIrZ2h72er2B7KnXX682PhS%2FFVPR6JEIsOOkH0sXAMlbuQbG7Yk%2FuKK3aUrpqGmsaaTsl26uLNe2FolKnFHKqcjk7r3GE8SjhnCdcIhGha46nhspdsQ%2BG99LZxPMLtbmVUmcHquhKaBri6LdYSrVXQgmYUKfWQk%2FGIu8mVlqY5JkSplbXtADkoe8uQgjDe14KrWXlNeryDtRYBZudnUh40bI7MHY%2FOzPK0%2BHO0PnEVz1LYYLyWPJBQokcwGMxSBkaD3CKGIspSkeJq9C5L2vBWzKrjIBEnMTUb%2BbJhS0iitwWK9F22XmjKjHReemaA73KtHAuDkpTe%2BeoNhsrC9GFOJrtGVqcjatJW2bzho95jPFJfw6PAaYxQnCxRTxSSu4yHmDQSSW3DxvTgrHWaNwYDWtMfeYPFFFCCWgjN43101zysY%2BuwFaZU2FQ6UIewoBbftaD81Doi7SZlWCAWuriEWR6VEb%2BtH5%2BfHX64W3wJ6KWB3aOwSt%2FLJeEj1yGj6GUU8RxdAV8DK3hW8O3Enwp4QTdDj7yT8G34IYVwSMxI468%2BAruUr7mbs3dStzhlKPodtyxJbk7ff%2Fl29c3%2Fwt3gwglPGacU75AXoyieE3emrxVyMM8IYTdjrx4SfK%2Bv%2Fv849Pr%2F4a8JGZJFGG2CB4nd%2FuvptG7ppk0Dxup19TdmLrGNJe%2BRDjlLObITLoy8xVmjTvcv4bJ6l9IyMmLX%2F2am4FCFAAA'
result = urllib.parse.unquote(ss)
print(result)
# if ss.find('%') == 0:
#     result = urllib.parse.unquote(ss)
# else:
#     url_content = urllib.parse.unquote(ss)
#     ace = base64.b64decode(url_content)
#     result = zlib.decompress(ace,).decode('utf-8')
# result_list = json.loads(result)
# print(result_list)
#
# self.gzip_decompress(base64.b64decode(gzip_data)).decode('utf8')


def gzip_decompress(request_data):
    try:
        return gzip.decompress(request_data)
    except AttributeError:
        from io import StringIO

        buf = StringIO()
        buf.write(request_data)
        fd = gzip.GzipFile(fileobj=buf, mode="r")
        fd.rewind()
        value = fd.read()
        fd.close()
        return value


gzip_data = result
data_list = json.loads(gzip_decompress(base64.b64decode(gzip_data)).decode('utf8'))

for data in data_list:
    print(data)


    def mock_request(self, msg):
        if 'data' in msg:
            gzip_data = msg['data']
            print(gzip_data)
            data = json.loads(self.gzip_decompress(base64.b64decode(gzip_data)).decode('utf8'))
            print(data)
            data_list = [data]
        else:
            gzip_data = msg['data_list']
            data_list = json.loads(self.gzip_decompress(base64.b64decode(gzip_data)).decode('utf8'))

        for data in data_list:
            self.assertEqual(data['distinct_id'], '1234')
            self.assertTrue(data['time'] is not None)
            self.assertTrue(data['type'] is not None)
            self.assertTrue(isinstance(data['properties'], dict))
            self.msg_counter += 1
