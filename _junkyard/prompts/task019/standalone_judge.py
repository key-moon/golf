
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJzVXWmS6yAOvs5MFT8SZz/LK9//GtOxDdInfQK8JN1TqfeaRRIChCRW//vPv3+nNP3G9BO6TaGf4L/nT0j9k9yUoVIHzPjftJRwX/KlrHspa8lPAvdM8CvwzwXyuZSu0ipYhb7iZ+bhKlypv1fTCs+lxAk+ZSyb91TtUOAsX5upKM4XXgfNNYSi/huWthgKXx4GfgHMejqZ+4vlNQhfSHrGnSXmUqgLzcyDcJOpmBxdTtIlSi2eCvb5k5uxL4VulPoZHliNQSZMW57V2NJl29InyKSx0gaczMl1hpmlfAnPXLyl+Cq1K+NgS1ou7VFKe2S+ocyf1AlGxt6UskBJ70pJfRhWqidtF47EJT9pOBgxQUoPFh9li5QEoyxK1/IC0kYkAkd5P+x+Cutgw9YpMA/Sbw/Sg0y/PRLCb4P5BGVr517EzjH79poovqhl0jKzDa9w9ZNeNLwJS5tnCpck9qCWpntxKy6OoGvXSLkmD79O+vspBBIN+nbyG7QPYHRo1mzXJD4I+iYcLvbl7qZV0Jfzeuu+xO6g/yQ1wipUSe3PSoIkfCYt8bZdZ6P3JS3XekpxrbMOt9gplB8IPUgaSlkZ5zD2UB/oNEU1aeoWhtH5VFlccovVnP6/lfBtqfvb/t1cH0ypkHb7+XszoRbGTDnyoO4Q8xrgXsmTnnMelC8h2dJMizs9avCIvgj9A+D1r/JmeqRAmhYPwneqpUGXqtKFX6EewUb6WNGowv4uD23Lu9XmrsPQvaus65jnupGWzLlid7PNvC7U5afgk6bqdZJNuS7hq2phFT+8LI0lLfPC2ofhl0t/mVZ6Fbl4OT5Qp9ekS1EZwbvLoVL2s8A/i/V4Fdrf4QHgl1a1s8N5vvhuJT67y6HHT+hhQhxuplJmwcJ77mkVn6V2LLNi44Ul8bpkBUmkLrfrVUnkLJ9rqYj0XQM7+IIYlccp9lKxUa09YY/aPkL6NRySbsvVdEsrnJKq8Vc5yO15dj1ffMYSnyVhXlE5K06ydGGsBnkEFTZLHkK9PCRdB+YXqLVC70NQzQiriyHWEZRR6qGWWFODLzUGeo6Kk6iqLA0qdaA4g8LZW47j3OmAR6M1JhjSGjKLsFQMn8YWWIs508lpD4ID+TvLMbybFRSYwam/D1V7vXL/EFpF72pe+iC3UelZ5+KzTl0bGD1CBXrVekJ+Jvh0MH1zzM+UxVvmBa3wMrk59Gq0TNb+L8ptyVU0mU5TcI7O84NlScsUr9x5LDY9t0b2IaQcHHPe2/gOZPkttbuQWuW/l6k288qywNnxhnxcpvh7DXre/bnQkem5WkoJfK4BYqeO2GBr2/DAqP4f6/6PS3WtDFSrOH+Xt579E7szOVb3TMT7xBFs9/xqsPvp5lrOo5+N9fZYjvL4es1LUTXlI0wS6LQClo2dc7Jc+NgZuLIyYKgkS9FYKtCmBr54+BHOkeVYu6Y9ZwwNxFOPfW5rTRXEMo4szBY6lnu39rqE/AkSLbu2Rna3ILKCrb0KJUeUzifLQh8UznsQn3OQdqVWqAeSeUgv2saxx1KHmUuoj9VzkPfmIh43tTk/xariHF0Ot1+5vZd1W/X/fWnzt8zchYIJvffM7ibk4TKVXNpQyhmgzJwyl/yWj2HUuyZDMrNtCOncrbi4p8f4HM1uXl9JazHsOKitTnP907cq3NYtW+gI94OFKJZefKLB0bXWtw/WS5fYG2lzkc73asZgQraXIn1Ua/1+zbQea+bnrls1j68w/uZw1vwZz87pSu7o1+kwT+MdRVPy5tpxWZczkV4i2cxb76VkOc7xZxWr0K6eb7smI/nEVjh9Cz2t6uAo1nDYqP1GOdIaZWZi/vr03Ap5zun9eox9G9LWLj4NYc9k8VMHzNNcu47URwc0Q2DHx6YFZ7m2v914xHEAO0lK1nBsq1bP8WvJ0btI739Xw6ml4KX6Cpa7aGj1/8vsML/1LOhY0wZTPljpPgyQo7DVUIbUCnChjn5alLqOQmVMz/rctNEkG6bGOc1L3N21ulAUKdPWw9LmJW/FjU5yXBu9gi2HWhGk3IzDqgZtwG6nW9YWS6tflnrwExHTWXEI6dwZY6YZrUSXMUZz82yttQrMU/rWjp8/+XPKa8HKMe5b7SmLr1Or3S9j68rcdrR+j/WCYkg6QtMyyk2+jT3CvDEBncRocn8AUnhZyZYLLWla9HsceBxsT35ea8pJHgZGpMJccf5pwsOVFP13cPLUu8KyRrqOpqnb9GY0wk3XEdKktcs9A7Goiovee19z7Aa8l9RdlDWM0gBYsyBsdvVBS5SWh7Kt3ootAVAB7nHEfaY0BstsrvOpS/hB0/WefsSl83vEP1jqr31FA12B5XR/m4dolY75VyK3ufe4LxXDsVnvHWInF8MT+JG2Jud6Cw1mLwx1jVfFObIce8dhTNG9BpumMa+q1/CWmvW5W7cijO2BHlyLKz19VlborHt5+utPi5XzW8VmZPkt57pAxjMveOoL846hya2SqpmVYZBZJbEa3uwIMNi9FDS3Z9O/OnTGHiw2NNPPuNaKgcxDe+u9Qt8nR1HWMHAbl9Z1hDu2Gc5bZ2av21gyyn3bD5W2j3KlF3B3kpXLOPlbWLRlRnvH9aHCVofJqWYtS3K3tabD1uKqW2Ggs+SvT8/9taxDKwlFmZaSvgtJJXPJGaA28TzUUhxKr9sx3jcPZVzupTnXjp44ImG/l6R826nWzs9t6mvIgVrpEiNPTU7Jil89FKol9AUeFA6M2WItzAiV24Vab8e5fh/MzuvGzW92bMHia3tcQmyYz8j6eyKGNelO59ZmTuuk4TM8cG0f6XYmOT6358yrDumTW9w64enTHmmClb4A5gjK0S23fL5T2knWZrXWnFIhrQbnbUNp1cAGvFTt6raJQ/q+hJ1oEsIzU5GOwDdy2rd+e88zfa8suGmNLUFiI9yrfv80nrIRxl7EOVuoKY70z8iVP7WsTqCSNUo8w2z9gpJL/IL9VNStJ1vHMZr9eUvg5myFg1Phw1DsmB86fb3Afqa0er+eoT8V9WB2j5pCeuk8hc8q7zzltfFKGd0jx60VbhxVke53eM5GMlvAWv47HJAeNr2coc6BNYj7WPLMDTU6cqw/5UdUgTN0jE+rKSZL24yfAgvpquzPlBa2tan5jZ7/QQ5vSaBbtdGw9k7xGNwjjn2xmtXmp5/1W3lrLaiiqlZvYa1pSYF3WYKUY8pqvctnT6pLb8icN87TfqA+4YqnXQfjE7Jzo5JmZ9ftM6c1XH7OdQzPthq9R3NbaxWlDVJ7jaJmPdiO5T4qdcuIb9lFWtN6M4slLHmLrezC87cqzL7/Evb7Z6J1YBcJ2ylpeWA7UzHsfrrGX6lamLr1WKP7LWz0dlP9vaZcu9bbTBaO2Qnywo+ru2sto7tQx3FY96vA7qML73N5OPc6l4WkPtWYNuCgJtKebeSF9niougWvEDuFMdFzKIOOSrIUIxzS8k2cI8upnYkeGq2RrUbcUpYT633JyMbSGA6VDctFQo5qOH+VN/amsGgP4bL26q/kRf1L5tTV2Jn2b22Mk7tLTb1A2he5SJwjhvNXeVvzMpM7lRn4B713XyPt7186imEZ3W/z4H52rYjKsuSNZmWo73bdO+escs6dObFu4BzgmH3RungZwD5AvFjP1TTgempxv9RvHUj4WmoU30Bg8mByCizcQlh0Y4a9Ev3dpgs8JatlzRkIGq7D5P4073NXxl40Iv+/KMSyM+PBDmX56/3AeW3lpkqjpbi8Xjxrn9mbXMxe197Z0lxtw6vNScaD5h4elnsXqGfX67/9OjP3BD+RasN2Nm59G5SDvnlwXXv4WTeH/W0earOD+t2FR+cMIL43UPZKEq5YOKwunCPK6ZWxo+RnH4XMbX4HeeZK3i4WijYNV1MuCl9jye52TqvlsrZj+3o1XcX31hjsXgr8lIO6XSL6UKVliX8m22NqfVqVqGF6VuE/Q5mP8b6dbz/ia5p7+562gajqAlM/aItvcGBlB1/R1Vyp3Oq9OgvDpBPekSKhCyn/KbhJ02AwTPIKXvGXcF//CMo1CyS1aveR+KH4Elc/DufkDjHOpRmr1nNrjBp6+6EpsyTXaQzLEcf5u7zVzp1HZ9FV33efSu8/g65HxFY6W8o6GZh4JxvW8UIr7L0Z7AMcKcqqjjBHyaGV1lskwHP0mzwoecsQWc+Z+PvvRbUennDiWpK/fCG9vrwPmbLmzK9E7qWZJa2uaYduTQvr3Z2aFnHKGaIZpvxvbyyM5YSQvUuQ7Qu7fTC9vL5gSKgPN5cGa7hEy7DzsDptNOu2a95n5dogfsOV3Xs/sqxI85gT5S5czsCU1lCnYgq8G50l1VqWW4nfDOytwG6jC1wlM1bG+P43po8feWHvE5CxJmCn9kYz67FtWvCSpxHjHEVtTU99qoe2USkr54vOG8uqeO/3DHPtnIUP5iLqlp/i1drF9VhKJ0Db32hfLF9SAp2gvrZUtFVZrx3B3rvYaRn/Ajnrh/00zTef5nRjs/LZQd1ffg2mntuH0fvuKeZySWi9QMpTerCOoaxOPlIJim8J1t6xK/FMIwklnWfxjqApGq2974HjRr++Ee9n1CVd59X2QY6gaeU0fqMth2ClOZBY/u5aTa7subZHCPOtstpv2fa8SZ1PiLdehD5pjj39AAfXy5HaWVE7K2pPRc3iHMMBwSin3eXOpNjRtfcllfTp/WwnlfjeJJ+7t2DKa13GkuiXuOy7dRJ6v5n1MiEOZ95PVqWdaUvpkb7+DCX3TOaQXpN5h/zaDX6r27fpRCUJNdbufl1F/1Qp8FVxC/Opsqy3J/+3/D8rW+0vYNdyzSnlUM/UZgLb7r78RZy6JT7iRMInTiusP8mAFtZqtbU2st+ywq/7XPV4yHmGvRTsOZALcCZ1rN2RlLzydoIa7fVbIOg1nBJ9w0z1ITmHCr3iW2Itjtfu8srzFkvoYdRLlmrc2bjUu3xHnIyEWl4/ZJ2KlW38Pur6b5z6/r2YcmzsEuaNneu5a3bOnEx4LpLlKML5u7zZ21Zjat2zcve0XD1lpBD+od7u9H+HzfM45owp6FceRhgtPfg1Vdtimg+euobCd0prvR7+Dul3DdfPCGcKc+xRSemjg6WXd/fH7EXmU7XyopxonPcp2KsJ6VxzwnWMXr8bN757tw6D33QUDlrjMPdPH1xd9766dSicpO7UbYjTsvJH2fzjvAHn3wl33e+O2BNXUjvmK/SdocITU6cARrfs98qC1xMCveNzR3gp4RFyxHhsY32Kcn0N927iuqb19VbhocAR38ziHUEzlPHmHY53TL4dzW1r+w4GHYeKek57ERyTv6scx3v4qt/d9a1eIbfry9hHdu+6F0/6Nn7fyVoz5qnrvuuBW6fBUwXy72j33+SgdT/ZxuI3j1HyTsnSrNcGUn1Zh76MfBwHHke93qjGqD/DsHWne1seWzF+4PjM/yQ3ZSjX3gRmLoHbm2yH3qXVNT/aiHfsTmN1PCmhvR6s9dTaVeE9uSgvumfMe40yqkOPLY94+yomanYFFcCsp9N3hlqf4WNyhOebWan1nYCtdIR7sw81ha8J61ULX4v2M/ct1djBXnP3MkGrWH8A055AV93NXGDN3cyP8mDw9Qvv9O1h/WZS/V1g1AQnGPv3Ka+N5zXB4lW70a/HU+1N5j44PS6cbCXtmx6zDhXj2Hr31FWfzvSnnt6hs0kb1U65fbEP9/0AisJspYN6EWcOF9cDUX+Y1VAq+6i9ajlbqLkfneONzTlc01+nJ0LWW34Pw/en66/EW5s2YSTEZDC2R/fT4atVN1NOFLtpSo07KQoW6NdwSLotV9Mto+e0SMDz6xzsvxnnVpC7WnfLLTWaZ2TechTh/F3eonstMiMwln7DnWsPa+VgIP2pchOHNDUCGr04al8CPJSHiWd7+ZDajH5dpOSSvOeUO9+OmHcjHgvXa6iU3PANRWm/3ANs11v3dw8c0+PsSyvMQtS/dRLZlb4vpFi5NdbdhaNzT7bG8MpGKNsmxZYidMArsTU9vjQtGzcnD9PpZtPPOY2vWcjfPPesrT1oD2PGeRbJGqa8QfV8DW8pg/b2jfYwtc3V8y3uNoqyk8pKjvzeSjRH+mZp0S06jOM75SO5RYetH9+w2/6CeS9NLRf87YREv+gqsqTfS9BlxKdDbB36cctLWaB97UnNRNKwbi/Q4XI+VVOQry5LWuZHzrHquvRgRGtj+HZUe5+5Dy7akxs7d936d8L8tzWd1jAhffbff2PFzj0Bgtgpzr/66mYl5Ziyoq9zSs3lmxioG8rYzXBJoG2e1U9r8fQ4KDNbCI9gwd7zWfjORJC2FsOsAno+3coeQiqtbPT+Wpzo/V1JsZrB65t6bh+G1W3+i0n7X/9l7e9GJ3qb0BukDREvMRoxzjHU7EjzMwp+uhW9f8zT7bINj7fwBWKs9XXsQvLGxgycnglUGovh0LGBXCTPEcf5u7zxFTJ5gyuntU6UW72/4ChqYFOEatLUwYJgH5N6fLYsPseL33h9pZOZhVou+Yuqxv/W9AS6CruHbvv23uhm1gpu9QnJFpa2POdkLS+7yWVfce9/wacNeS8crH8ZpzZ+69Tc/4raXVG7K2ou/4u8OejccjvWr1safct6Mf01cI4rB1vjNjIdckonWH3s/wYNT133FRvGrd1f0yG2I5fTxDt7/6K9MaYjel4tyDdTz4qOTju6LA0ztwzeFXvXdtsNrvhlp3soITl8T5HkRD2s7kJVpcFYMF1ismVHsL/Jg25Vf+b4Dm2FJ3qZ55B1qp6tlbQqVilN7jmFo4nnyvc2e14W9Ckey8/t5bToS2HleDR29pRVoNw8BU8XSc/LamzXSu0YfdkJ/Ym+G3mt3NodvlyvWI9qS6d1VY/uhF8As54OmxNcE/MEn5KbMlTkW2sYvw4kX3Ya6frP8mq2oo5y2YKs3/ywX8PIsbODxFLQWhufAEtIvrSn/4clJ8uFePUqjBxpbGwD/f8f4A10YtjOEoshtXZ8/yyk6pMSrudsofbbHIDHFrYn98+gj5Tehr4s2oO8A1I0zVNRezap1WWj0O1YbbQrhvCqTlK+fGB9ce0d1q2dHXsKfNLr83a0sPGT366b/i4wKu3wsgRr+9vvGHuMfvR5edSafykhsdJqODV9al+JbuH8Rd7auyHbvxi+/2vitTzvIZh1sbHtzzKJ9V+Ct/7jFh+Tj47PlKVbxtwSU+HofnZ0J9uvBWpNiut7e29fR3S/yYOFhfdZaauKXDlejU+KUjC9qbSkvpqpjIIvbfsux2X3TgaTdAef6EtHgHNcOfyMGz/zNrozbqciXwWrcv7tmbIGX067pVOZv/VTWXLp2gy5wefCGQb7soQ0TNIUOex+Cp8pzdsAdqKCycmn7h+P/wNxI5BW')).decode())

def get_cases(case_path: str) -> list[list[list[int]]]:
  return ast.literal_eval(zlib.decompress(open(case_path, "rb").read()))

if __name__ == "__main__":
  import sys
  import warnings
  warnings.filterwarnings("ignore", category=SyntaxWarning)
  warnings.filterwarnings("ignore", category=FutureWarning)
  if len(sys.argv) < 4:
    print(f"usage: {sys.argv[1]} [path to your code] [path to case data]")
    exit(1)
  
  env = {}
  exec(open(sys.argv[1]).read(), env)
    
  if "p" not in env:
    print("'p' not found in provided file.")
    exit(1)
  if not callable(env["p"]):
    print("'p' is not callable.")
    exit(1)
  p = env["p"]

  total = len(cases)
  wrong_cases = []
  for i, (inp, ans) in enumerate(cases):
    try:
      out = p(inp)
      if out == ans: continue
      wrong_cases.append((inp, ans, out))
    except Exception as e:
      wrong_cases.append((inp, ans, [[str(e)]]))

  wrong = len(wrong_cases)
  if wrong == 0:
    print("correct!")
  else:
    print(f"Wrong: failed {wrong} cases out of {total} cases")
    print(f"<failed_cases>")
    print("<note>only first 8 cases are shown</note>")
    for i, (inp, ans, out) in enumerate(wrong_cases[:8]):
      print(f"<case{i}>")
      print("<input>")
      print("\n".join([" ".join(map(str, row)) for row in inp]))
      print("</input>")
      print("<expected>")
      print("\n".join([" ".join(map(str, row)) for row in ans]))
      print("</expected>")
      print("<actual>")
      print("\n".join([" ".join(map(str, row)) for row in out]))
      print("</actual>")
      print(f"</case{i}>")
    print("</failed_cases>")
