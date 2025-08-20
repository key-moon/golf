
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJylm0uO3EgMRK8zBrjRF9JZGrz/NaZKDDJCDXJhePWMRqVSyT+Z8s9/Pz+bLba6/eLnHz+7HXZ+/vGm/7HPqtU2uz5/e/O76rTd7s8/3oxVh13Pk978rlrsfnZ/M1bdnyd8//bmd9X12fX7nDdj1fU5x/b8TflddX/OsT/PUeZeqx3P35Sx12nL8xxlrDo/T7iesyq/q9bPrvcjH2XutTy/fjP2Op5fvxmrNuz/Zugr3vlNnuvEecg814rzkCnD7XnSmyHD/dn9zZTGBikoQxo7pKCkNHZIgUxpbJACmdKIX7+Z1rvBakm+4YE3I/MNF7wZyb0u7EHmXjf2IGmHK+yPTDs8YX9krPrY6nOeN7+rPrb6nOfNXHU+53kzVq3Ped6k9e6wWjKtd4PVkqmvEx6iDH2t8BBlrPpKZoWEyO+qrzRPSJXMVecj8Tdj1fpI/M081wLtKuNcB7SrpL4O6IlMfS3QE5l7hTbejL1Cg2/SK3d4I5leucEbyVzVxi8bYx4idujpTX8idujpzZT8De9RhuQveJwyZRhv9mbIMN7szVx1QuLKWLVC4srMKeFXb/qTU8Kv3mT+OqEN0pG/VmiQzL1CT2/GXqGnN/NcK6K4Ms51IvIrmStvt1905MrL7RczAtw4qzIiwAX5KFMaO7K4MqSxIYsr6V87/IpM/9rgV2Sea0cEUsa5NkQtJW2+iZU2xldE7ANRQelPxF4QSZQpjRs2oQxpXLAJJSPbgohGZmQ7ENFI1jZNHrUx90KGN2K/MmR4IV8o81wLtKuMcx3QrpIyXCE7MmV4QnZkSuNCJlSGNG5kTyWtt7FsG72h9jqwB5l7LdiDTK/cIVdleOUGXShThheipzJkeCN6KhmjLsQmMmPUjdhE5rkWyE4Z5zogO2WuWmHRylh1wguUlOEJ2ZEpwxWyIxk3mmrJxgqr7LCpKmysRKruXfHWpKPuPXFSkl7ZVGY2VnMlw+aJNr4FznWgqlXGuRZUwkpWDiEhpaNyCKkqmVMiwysdOSWqAiUj9or9SUfEPvHOJK13h9WSab0brJZkbRM5TemobSIPKlmlRGxSOqqUiE3Kf+n1ht7Mxn6uuoAb9kI6uoALNkbSUzZ4CJmessNDSOrrhp7I1NcFPZGs2cJqlY6aLaxWmTK80UMrQ4YX+m5l7rUh2yljrx3ZTpkybGOKjXGoutGm27dxQlDSOCAFMqWxQApkWu8Ge1GG9e6wMSVXXfg1matu/JpM/9owDVGGf+2YhijZE0VEUzp6oohoSkabprq1sSL+pwlMO1mwcRpRtU1IQemobUIKSubKphaxsX5BvXEhbind4i127E6mNFp/sNGHsFerSxv1X2/YnNlGOVUmaqK5jRkAttFWtzZWxGXzJ2ydTJtfYeskc0q8tdKRU+KkynzDFfFYGW94IoYrea4D5yHzXAvOQ2aMuhC3lBGjbsQ6ZerrQN2tDH0tqNWVnMDE1EDpmMDE1EDJ/HXib6Qjf614DskZUdOp2tjdluSb7Gtjxi6bP2DrZNr8AlsnGQFWWDSZEeCEF5DsEJvpjI0TncpfMYdSOvJXzKGUlOEK2ZEpwxOyIxkPm7rHxloJ0jhhL8qQxgobU9IOm8rMxmqueqImS9mY2UpfF/REpr5u6IlkNo+ooHRk84gkSkpjhxTIlMYGKZDpyyt0qAxfPqF3JeN8TDaVjjgfk00lY29TmdlYzdXELJ6kdEzMYnclp1hNh2BjV1HSaOoDG2uKmkeFpyod86jwbiVtfoetk2nzG2ydTOttLdtGb8C5Wo+10ctrHhVRRumYR0WUUbIiumCbpKMiumHPJGfmcValY2Ye8lGyBmhmOjbOgarSu6B50lHp3bAWkv1Xk0dtzL01FQn7UzqmImF/ynzDdmJi45SlcmWT22zMhyX5FRInU/InJE7SDk/YH5l2uML+SObKDRIiHblyh1RJekoz8bfxlqA6qahOlI5OKqoTJbvR5h7Oxru70lejSxv1XzdZF7yHdNxk3fA4kjPY6JOVjhls9MlK2uGO/cm0ww3vTHJ6EJpXOqYHYS1K7rVhDzL32rEHSdvYYRNk2sYGmyDZ3UTcUjq6m4h1Ss6IGsu20Rsq60X9pHRkvaiflOyyY+ahdHTZMSdRMmJHT6Z0ROzo45SsAW74HOmoAS74KcmZXtxgKR0zvbjBUnJ+2Nwi23jzXHObsDKlY24TlqlkNv/7byqGGxobb3Vq5tDU3zbW7DX7au5obbzXrbixwg/IjBsnfIdkBNjh+WRGgA2eTzKyHTgrmZFtgXxIWlQTzW3MADWRPmAvpGMivcDGSMaNG2clM25ckA/JLjs8VenossO7ley/LuiQdPRfN/ROMqeEdpWOnBLaVbI+/PtvexZo903Hjc+G55CsvqJ+Ujqqr6iflPSv5ibextv7qhyaebqNM/iq2ZrOx8ZuqWYOzZ26jffwkPyKJylD8id2V3J6EB6idEwPwkOUrJabnG1jni/rbW7UbLyFK9vYYBNk2sYOmyDZVzb1t401e8nwhuzIlOEF2ZGcYsWvlY4pVvxayRog6ielowaI+knJON/ELxtjXllUk31tzNjVIYb9KR0dYtifktXyjRhJOqrlC3GVZG0Tc3mlo7aJubySVUp4vtJRpYTnKxnZmrtnG++rq0oJ2SkdVUrITsnq60BUIB3V14JIQlKGTQVjY9VTezXdo40dZ9VsKzRPOmq2E9ZCsp6/4d+ko56/EBNI6uuEnsjU1wo9kbyTanRpo/4rsjUzUxvnrBU3msxhY7apN2ze3sYTV6/XfEtq4/enlb+avt3GXh+SX1AxKEPyByoGJaepcValY5oa8lFSGk2HYGNXUXtd2IPMvW7sQbJmW+AHpKNmO+A7JON88x2kjd9OVrUcdaHSUS1HXahkZNsQ0ciMbDsiGsk+pakdbaw3a364QoekY354Qu8ks3njsTZ6ec2ImixlY2aruNF83WXjF2EVDxtd2qj/qntvaIN01L0XNEgywzY38Tbe3tdeG/Ygc68de5D0lGaCbOPUueyweXsbT1wdR9Nl2diZ1Ry76VRt7G4rV0ZmVTpyZWRWJX25qQ9srClqwrkg2pGOCeeBCEmmf7U9jI19T92nNN+S2vj9afWw0XkrHT1sdOtK+nLzvbuN38iXf63wKzL964RfkZTGBimQKY0dUiAp+WYeYeMMoyLbjYhGZmS7ENFIxqjme3cbv5GvrNdEPRsjJc7VThZsnEbUjKj57sfGb4XKUxZ4CJmecsBDyDxXe2ti400L3rB9oo1vUdbb3I7beKNedtjcmth401IdR/Mdv43f/ldv3lTSNlbf8K92YmLjlKUmSxE9lY7JUkRPZVpv+x2Jjd+e1KoFvyZz1YFfk5zOrf73/5OrvZOw8R6jetjm/wzY+P8Myg6bfsnGHqvs8ID9kWmHC+yPzL1O1E/K2GtF/aTkzKG5y7Tx/rNmX808wsYZRtUAEd+Vjhog4ruS9UZTcdpYpdassplx2zgXL09Z4CFkesoBDyH9j/8Pc6Ft3w==')).decode())

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
