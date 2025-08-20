
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJytXFmu47gO3U43oA87ntdS0P630THHQ4pOUg8PF8kVB9myRHESnT///PnzanOjT29/5iZ/7zbipzYZ/m4z/g38Md7e/23vq51tf9P3N25vd/t8t+h/wN09T+nxel9ta/JN14rw1uCvoD/zv0ca6Dd835mvc3PrmOf3uM6bTj0Ymg1m6ARYOU56PoBoNgCS50d+nrVTKNrj5tTRTG/s8sYu93/hWxLuvsoiPfb3s+02Fy9q7fS8iLt77HaP1/s6TKU23cNxE+FwlUwyaLzzewzyIQjlgyGnPfVz6VlAehaaqUXmZ2nwV8Df+HkkEXZ+mkO9jozgIPmd2iHyytBO0E2Tj9Dk7yPtvoth5S5Xk7839npz0Yfa990uaCte+e+rMf2m6A7yNSTpSet62tP6nltIKhaRFmvf3wQvBC8AIz/Pq/MrXPPfd9b7uMzqzMnz+6wJbpK506dc5Hp4h0V2pNJ0xxsv0GK/l0ig8dj6059J7kRrG3Ezy265M3SlVJPIVQiyVaT1q/vFNZ5hZ5ygM7g1DThc41sDzk2+Sd8ZRLDoN4JnojPs/E7fZLxbm4Efr8+7WSmz9Lh78mhkF9kKs5zv9MR7fH6R7ri/hPNHftJ12s9mcHvP0UazNdm8OW6cwaWtTT4kIyN0P8UTVPW7r76SxK22E1aSrsl6Z/iGVoEPo8t3AQNU8PMIDqdoD7DGakF07h034fzGHWP7g2RGrqpjRkl3frcABJn+ZU26y9h24t5hrDvMBnNG+AgwXMH49fqsmw/T4KbJTQLQ8oo1sfYZbVJvwF/blrMd7EfQfSroILn8FeLxC9bu8mryobUzmLi+0SbzGg7WpzJLxpNX3Wb5V4it6wjJWgRpiM/tV4kzJ5Jm+DwzR7a6YlOPJp9BN1c00lhG85nhHofpmeitzuyHmk7dRMcqbQZ9m/vNUbcyT9yntFY4csSLL0F49trVGhuvyfnW6GN6n0exSHvB8RFe+Tv408vDPOM4MhQ5nyAf8xXmWWd3AnvkXrzZ3kDH+UYY7PGDfQuWVHvYeni0FNu8+mNbeXh1Ofp6RWtv9v3Fvrl56NaOPh7w63orP+urmp/39xkkgvtTZCHSg/ZgB1q00880vkv0g8n68ofm9ZT1e4IiZwXdd1GLvmUtnmME1NhGQy1/CpT7uXZfmnsLOU5R3zS3UywTrraMEhDXa4A0pqmgvMqGzVoEI8UEeRQ9QmO/Dr7+yzyc7e1/3GuyNvqjFuIm9UxMg9w6YqX9vj62sMf5xpymYS55TsdRO3h313sE8iEZukTXMf8mekpp8hFa7Kc01hHCYzN80cxc41w9wBX/BHY5wxfAMvvOqRxRRklOdCUcp6uD8/rJlpvtLqDnfr2w81nvu62N7cE2lJaBpIM//lQmd59ovOZKIw/cZuQSnjV4c6qfzAuRJys9ly803qFxZqKdZ618oYYnPEtBtP8sC9HO33kw+ZDsfoL4+jXknHwXzsupzGO+R2PojIsxNK+IfMd1gVVD+jd+XrurhH01r7ZGCaS5Jw/PpUxwk0jbYU+50pOs8lwrteVbxjRL5LbSc68N46MnfvoG/tVma9V+Q6x28N7z9XfJSmP2VXgVK+MeiUrMbbu3Jt+9DfBGkHwXdG6xfnJ+yTQM9N7kjsqpHOaVJOtZtjrkRrNcPEO22wsIOXkloi5Au858o+3He0XbbzgY89Hku5Ruywd8gZ0/X89h1ser5A7geR9zhYvm2swXiPDiNgr4PTc45hpjrjBkETtn8FAeMYekZwzmoXY7byB89D/P5H9GzRwtcaZ5BJWj2Nr/cR0+zr9BDxmbb/x6d+VXaYX15H6g3SyD1jXnKt+ds2u75KE1u1bx65oqv8LKzzDvYs9uW5bXtBBmCGeIkxGH9iF6vPkMINPcg9dTnbFfh/wMZkw5lvWVjudOr6QdPXvirWnAYY8Yq4vl7tHTeUk7xvYd4vbL5BdkpZAc1QJHgJ1/CpJT5RLx+h1yh6gp3FeRMySLWTFiYFodP1T9cjThJ1F49qQrqjE/01K0JSdRVb8oC7Pp4P9HLPQ9MvKzD2xNCdch21r6sqDzFe/tym5d0R9IeVk40UNt0zGP24vc7UqSKt9d4zT5Flk2DIwTYz2F0fufgN+vz/th9Ssrh+1mijE7xjqOC7NiVlw0B8mCnfzRWkRZijmPZ5pLFtqci+b5sp10scfZrhwrGf0bf8ypao7tKdq65+OkWTg/tDrEyntDW5uhaG9/g7pZ4zNngzqeyzhuEhyOy6Py2JoC7u6xmYzik7JsnV1taJgBweN8rDK6NXsj8iRoib7RRLqSlep2cuV2aXnz0Yd6CkRyF/HqYy9y9UWuxvput9WfJBvSQluyJR/avGYX40yaF5K8ZYz0BV6IRt8CqxVC6Z2Af5J9qLBfX6SZnkjvQFePnoXlb2M23fPAWhvi/J3zuz3m2FfS3evPuRvVVhHOdIfx+ixfOXeDsTueFWCbdfXYHs8PZnu2k/Qf1rSM8FnQ12Z7YIBP2SsjXWyP7CjfWW7TedxHqCFB2zQrVewQYPqYu//Mz1Ik/WyPkW9A8lS1qKLlw7n/CLkFHaG6Xzeb6uOyXEuSXMajRFtVk/B3O5nxzAzqCz9Zp6cDXA/+xgS+5QrxCOI65BgsG28a9pQsPbfhtD1m70OGeis8FDtLwzkNu3j0ULYwmzuNV747+r9r8Jcj7PxVJI5wvL5KvUfUwhEqWuQ76JPsvyr8xP+SODmfbSB/N//TMw3fq3AujefgfP7WvHoen+s0VJcrvYZz3RSe7yPMOxUqAfSOQ9Yut6DeJlQRmV7pWtV4Jrnher4Rj7vzhPlzOx5Pd+O8xNPdZ1o3+7/Brs2VMF4xFmeTIaU99/O7YFTO+9P171nMRtXmfSt1jDGyaUO1jstam3CVDHrqR6uo2DG79xhx4J2f+eNYdDSRvxdnDdkf0Lg9twefoYwHcb1QIjESQQmOkYb1g9kxjURPsxO8C2xtuXLmV224B9j5XVvu5h+rVLm+3Ed7KfJzUft6sOF2dg/8Ec70wpYaxSruoE451ScXbX7e2OaZlngGtAqeg2kdKHrCWB9anYZ51dGr5YpmwBTwd37WSs6vXuiW5HAzG066rGN2Has/PG+C9X2qe1w2sl3w+r2cccx2JNf7Rf4uGUbrqT1ifXPT6od4es409WtP9XOBNvZjHSdYONfmjMIG2QW3AOavCVzzy3e0AwU/zbb0c++Iz87RO+MTo5zjwAprrnfAyvJYQW08tm7O7/AJsPPH6/OsLUaxO0Dt4zfvcgo5mqzBc+68yqVbftzok3m1Nf+YM/PsSYxvt/d/+fR8LrAJtLUUGad+rgMOsPl2ilbuD6WSdBGdMZoDeOKnb+DfkvXYKn3dIZosYpiR5lpZ4m6LsQ0bKvxonmzHkYR1qOYDmu/iJ1q3yj/M7B+iz4YVAFyHKOagXSffwrO1w/owdbL5P2yvT8DvMFwN+PX6vLf1TptwHEEfx95xNA57RGgj+si/FaPj0UR5/LVSb/TnKuipcgN0UdA+Z9I2qlMcVu2TT4NAHwns12ftBJzKYc9c1VXkeguxpR3rM9CmeqaM8g+9lS3JfgQZZBvu0b7YaPAC1H7Xq3SP5no/7WVzhau0AC2voNN4lZYefV7wMGwk8h3gSU5IlB9zFxW/5Svg+h3yGH5u4lUaqFX5GQ97esU7Pz9PzIezJtOxzc2zg4WO608xoWfWXP5wbCMePZBJ7JzxRnvX1a5DVNLd1qOFPCTfegznXO0jjedLaWrV1c+zHn+1NzwG0io13BsX5DY9f4U6aTP/dUv62fPTl+X7Iy5H/uzXu21BSxPPKXKu/onW4QzjzN6B7+5o/QWPdoLb3bKSLpm4KzEnb3u5xxx+pV09Vx89ghhp/0KLEbpKrPUIkYBnzRUmTPeo8SUyXGXZV+AXzgd+lqbVe2qPkMM3LOTdFad1k2uWbButSzTPu9KMT6Tv9UDrVonnEu972GOtjNuCbqc34pq+2/nU6lWtQZENinY5r/BTP5cqz8Gh544VR+sQg6ymb60yzjlM5zItRDBR2xU01sOxJuvv3qvE9zDxKfNJebQMyU58ye9/z/ajjlBfbxpwqAdvDb01+e6hHiLkkBHeCnqqoQuwX79LdZZxdnkXxHYbWxE/7UpvGj22Wftx3VSS395E9mOeN6yW7ZH5jYPMGLUUV729lrN38S3qkKszeXc9op4f4sYeMg/yzKoNX/q0YT5eP9F8ttwnMtveo3/B+AmjHzhZXUL8ueS64671eVOaF3+DdkmWT+/Eti/dN9rFWHcy0HxcB9S8qv8bz10jDvVmXWOjv1KANTYehcCptc2Un3EDFKIQ5Zeoz/idrl4UXp/31OF30juYvO2Sl3VbrFE+44uY32ixX84V783zKrfunpPunhOujzV53d7G623A5Zg65UJ99Q03hR4TjAVzyhGHtoWzOWuxC9aHXaD8Lm1YNxnfA/w7SH28/Magxi3p/f02vJvVuTaONYa/3z8Bre5H2iflQNDKcuVYtL9VRVnOgnm9fI4rcE5/ocWVUF/SesS4wPa2RhOWV+0x+ojnaIYLOTU4Me+aB4Psa8pq61vcPkfLgEMtmM9Y1NvdpbfD9RkLnMCUZzYR7nLmYhT77x7/3OS7sy0kawiw8YiWyPw8wgw7v9NJO4D9Zd/GRzPWMmi17WR4yZaXtQxxNfn80eM5/YWWcDYJtOHccqB1O8f0E958Cle1Sw+v9O+Q8+msDz1x9zJdZ89tfP9Dqgb6N99FPN+GZ8d+Wnz9DxCPK/rK8X059rz1fTle3+/v0kVaJ49ceEw3L+QLLuIPAiT5qkiv+CeJC5Rf4WuAeQSL+aCL/dd9r1U0rvnkdx96PDFbo27r7UNrSrWLHhN7pOW4MdIa3vzv7HNPAYcSIu91t/jOt+bGLHbAHaxvfxf9TJ+mN8Rj7lEgWRPHs9fEeF0nthKyPvaU+r7xy/y6iHvp+8fWw38RBt8XeEk7VNN0+NUYsFL+mzGST7CcAlrUzzTLhPTxfUNb1b+I5itazPuK7n6M5s/mb+hzRsk8DpP9s8l356yUYYSfM1W/8PMIpMoUTl48+o1S9onGPrdHzVOQQOsxnuKVFYW5gvBXfszrxdzenHJ7spfCrpc91GtvJPqt2JZc99AOJ1sp64011np/xk0P9xfL1NEbH+KNKro2iyRvGLbZpB9juAloT/26+XX+awn6Dr9mNCpIz55/g3iXCxZmH88U3Bf332XhqOcsJQaoP/Djip3Bf4rnQWML9RxqG4wGEc8aweshXQOpXxnfsZfvcu9PQVecZj+V3+xpqSvi9buczmlmX/PbZ9aHdue5yPVxfdH4zrjhYvakY0QqmRPAdfD0P+1axk2yf5ZoJ9wqFK1Y7eBxctWSusqw4zCWq351YSIc7mrdW3Vms/x1SHxbuKDx/ArWVgtjy3ze+JnG66m06JGtaRV99dBSZLzGjlFDb4OG9GzGWWQ44BTIVtg1WGxNgOuQRXny/aZHK8CnYZ/kbhl65GtPZTuNJPluW9aDYf6yRaratRXC2KyGJvjVzQyN/Xobq1E9Bx5+naU4Bf0V6m38zZbxN+pU22mE5BHX02/a7YE/18ghP8t/PHuL441+4C+08TTIn9N9xE+Z8jruHKrv0k6iLFfqEet7/hZSKXGI5UJ4wIZYVNjrmJFjkgVsywT8mtu9EgyRol2/QwzpUegCeUA8Txz9djxrRB2ZzyGrU2CvQ7H6rM5vuOg+QN0ef911zGj4L7ZWbydGGDAlPcL81M6vHtf4NqPXgM8SOY3VZ3ZeWJzFPdN609/awFzL0xzjb/DA+wdt+mltXsF+4blItLV+lhLtczwriWP2311G+xVx0X5ZpUNxnlDR9OSB8dU5RIezBqyWjnFbkReESqDvNLdT+K4Txroe5++gAZcm33HU8Hblr/z4nP4bXvgLzp63x18VizWNGH+cEH/0/wDWXn6d')).decode())

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
