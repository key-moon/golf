
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJzlXW2S7CgOvM5OBD+qu6urus/ygvtfY8dVtvlKCWRAwLzoH28nK1dOZBuwEOLP//78+TDb383/s+bP9i+FBvwdjfgBevI91OPbf+EJVMToix+hOx+iHwB9te4f86+Xt//9BVvSHt38qXk9XfTw52fiaUOgG/ZZyO1j4X1HVlIsseCe8O3vEfEjLHh7xnGPd2QdxaLW7Xfk5/UXW9kQhNZw3/7Uu54u9+3Pu4+d/D7o5k/N6+mib3/+QH4fdPOn5vV0UdcDox67B3r0n1rX00UPfybPLvmUa3Lfvp9TWz3XPcsfBs/mPxLbo7nH27COYlHrvPkd9dXl/X88KxpcN5ObT1s91/k+eldO/t3/xbOCUY8foDcC3fmnl8eqSL+wMfovDlHMdV7+hvwe6NufetfTRcMvwl/g/9/EymiuNaspFrVuvyNRNG3n90Df/tS7ni7qP+GfCT/Bs6iHF6AnTqDuWZ5PW9wDfwrQF777/hnfkxe/D7r5U/N6uqh7lr8TPtXnJ+wdRRYSNmsh+uV8lmfUxlsIfqFa5/UjuHdvjbq+Qed6uujbnwHm8ROcRDUtbHdkLcUSC2FsCo0wnwCl4zQaFqxZTbHEwvuOJH3ni98H3fypeT1dNNeH/yZWjv8tmeN7v2QsBL9k+vux2nIWvF+o1nm+p0bs8tFdx4K7I6sollhwa4+38O/F74Fao3s9XdQ94b+m/K1szz2e2rEqurXO60cecIUdrbs/iDV6HQuuH1lFscRCGEP0ZjveDAhZCfgBSsUrdn6CfkZeHqki5VJoaoHmOi8/zZPgPwn0Sdh+EuiT0PEk0Ofp+zm1IX8+BWhupExwFkXZLTQa4ATKjaqjtfn+/BGgJ55Z8ZFFm9pzLbM6NFpbPTfs2b0RIjuWePwAPfnwTXsAC4+oZx+nory3Ti3QXN/Lj4T/iDFvbNbhHr6fUVs9N3zC0y+pbya6jCLGHh/c7W9g4Zvg3qLnfjZtyML3hec+mTPsfArFMwwKpeYdsZfHq8jNiSiUmimFXn7/1y8Z6UljOq251sygolvrXl5O+pedn/Q8ZB/1/l/lX2gRP3rTDnTz/azaSsdaagR+BE94kPW08++Gy25KUY+fXPEO0J0P1aHsJj9Lax3F12Y0uH0RnkVxqynU+YL3spaKEhTfJwrdnyEv3oj7KBxl0+FaM6+2ei6/mvENv7r0uJZZtxitrZ4b+p7K50jnujpc3/ezaavnvn2f7Czc+eV7Frd/Jfs+4ujt5uXxKnj0eu6eHxFAEXhqxqbDtWZebfXcuTOi7V+R+7z94RlbazQ3Q1wb9f2JYvjR/tnTig7X+X4+bfVcfqcnNRrhsYQajah8M8zFK5pUNt0ain0uzlxHoyq1Y781ao3u9XRRbu/t9i/egUbvSytHS77bLbn3drw2//m8GNk4swHS9lGxbByflq3Zx7Fsa2ZQ4XyEouSyLIMnjJ1T2ZeS/Hcqz7I8Eh2i1syrLXxqURYphR5ZpIfvtz6nfI4f8T3bdHwarRBz8elXzNnMqy1Gudg5Qv2cCxynwTkF7bnWzKCiW+uC+gkx/yPGvXtFVQJId64H/AA9+eAZ+PB6lxm1xeiLTzzLCP0I5oJfkN8adXNBnevpomHU5KvYykiuNaspFrXOuyOy/IOrqPOnzvV00Wt7b2fIThytolvrvBliyu+BulmfzvV00XylhNao6zF0rqeLHv6M9rXsfIzirzk9C+87spJiiYXjjkSVand+D/TtT73r6aJX83x0uPZS9s8q3LDWW8rH1bjbc52XR6ro1rqLs2gqEqlh4do8fKRiiYWr9ZxGcnPznPkUi1oX7RJCOy/pNTu0b/LkJ9zXr8DCpwm/58epQNxSCzQ39fJXwv+CUYGR3PCOrKBY1LrMeRHY9ljucUfWUSxqXdF8NF1b1eGWzEdHaavn8tkAPVDLrPCvj+Zyt9qjls3HWh2dpQ7otblgaxUlKFXRIl/x80Bqs0N1LNiGObXzWfBXmXEdc3olF5/ERa/k4pO46JXcD2+VeT5taB4uWWWefVXU/gXrn3fhKCzJC7wT8yIKjbMTZ9Xmz+8wmstZfPs+qcX94vdBrdG9ni6a3/FG1ftry3U9xkgV3Vp39hilb1of7tE3jFXRrXXns1xeQ0OSSdzDwvHcr6NYYiGXC0fFXmQjNoqnYQvBL5m8ubHacha8X6jWsV+lnxCNItmebR0LlvmCnVOxxAK3s6IPask9FP8F9NgxXr7/WpNrzbza6rl8zmIP1DIZh+ujV0fK1txrY+IqXC5LK8HYK+I8JpmXR6voNaOJ15PTvXD0vrmTH6B0dd7Xr8DC09yiNeJRKhC31ALNjVdxpJVxfwjbPwT6Q+j4EaDhOtAaiuV3ZHsTJO9qxM++fx6feCs3L49XkX6VfAHPoS+YG8F94dnTPqj6T6jOKRXTCX7JWAh+ISxYs5ri2PeoXuthgTtLCO/E6MO15AlDmiq6tW7qKv14PLN/Re3+7a9054BsT317C64nWkWxxMKVCHAdasXx25VQvtKQJHKWsL13ikJz+SeH72fUFqKS3JjjvJgrNXB6cK242s1KXO6s0D6oJU/6/C+gx/o8PkMb7Zjpw7VmBhXdWndGviX11D6JXo7OFsQ9V9gDj1eR9p9otwSdW4h3S3xmIyzUSUcB30OpiMfJj1Aq4vH6DaA/JhdhmVExnlvnZtwzRpcx97gj6ygWtS5zBoh0Nq9hwZrVFEss5N6R9ij/hK+O5r7y8R2M2AEqqXB3sjNf7loqwn6ZQn8BeiPR38jLKGpJn0ilwbVmXm313OO0rFv89+LLTqSio3d0TA9H7w7Umnm1xc8yFVlkIqReJRekuT6eVrbDw5oZVOTQq9VBSypalO4Rac91vct82uq5ud4lRTFX0wLf58yoWGKBOxWUqunVg3s892NVdGtdwQkJKdqea80MKrq1bvdyEoV68akYVMT3UMQN+BGKuCcfoO6OrKQYzV34qJlkDbx+FV07c2C8YomFWWpXuJ5olcoTota9vBz1Tyc/wUlU08J2R9ZSLLFwfY90+a6d1hasWU2xxIKrq4vOUL/Ff6cVdDIwdRJCwPdQ6iSEk3/W4J1RW4hSpzS8fgPoo2AUqD+3pr0FfsSYUbHEgssXviX8Pqg1utfTReP+Pu2N6GzmUdywv19Bsah1mfwxOhsrRbUsWDarbEbFEgvhO0JVCMZVONwZYT568sG4cwfoiw9HrvBtmE0bQiXceI8fmllJ3j8dC+6OrKJYYiGXL4wz1LW4ls0tHqutnnv4Pjrd9ORzUUG0R4zbT4b2iHH7yX5238+pLe1dZHvdcjkiyd6xE0Wt1rJgmSyTORVLLPBvww984ujoiI4F7h2ZU7HEwtynMh1vw4za6rn56hK46ha139HjRz0ihb74oPek0O9sfYr5FF+bu1J9H7LSnpsbBXRUdGvdXicu9f/Gl9R0bBHbQlXGZ9XmnlpJvcm0smRS4Wnno3XZ8VxrVlMsah0TH42+5E6Uy1unvh0R6vGZqKmmirBfxujOB304Rm9RPQWUH0l9zQV8D+VrqqSZkH6e53gVyEdo/7essovLgivPWO3DtWYGFd1adz7LY6sUh+gRmTye8Bm1hU8theJY6j3xPbpX7VHnT53r6aJ8lmYP1DL5mOuj12K9FEqNMPnKJfZCVLe9ijxKjYl8rZWys1Ak1RNcRYT4ityOXjebGKkCzQVkZ7Nxs4n3f0lWZwN+MqP8glfE6ItPzSjZGpJjtbX1vWRPy0iuuyOrKBa1jqnhQe1p0tvpZMl6H+O18b4v2YWVn3GjmaoWNzfjHqmtnhvmcqAxX1ZJ7SmaCeSqrlkzr7bYAq4Th7/y99qy7GzyGeOZuVnAL2pf7OWxKko9h2Mp2IK/OzapjPPi42o5ety37+fUVs+9Vt1QMu60t8DPc2ZULJpJnHekfF27B/fw8lgV3VqXqS/cHnVPrc71dNFrT60s7wpnWOGzW4NfLj3LWtp4C8EvVOuYGGKyzyWwgva0PAiuxw8snHwmsqipIp1joJ01D4JLWXgE56BiPj6BFNdUCPjRFTF6I04gffG9c1Dn04a8fOUcVLw/qw+6+VPzerqon+dDR+8wSkfvMEpH7zBKRe+sWU2x/Akff7oi5tq/5ERJPLq3R7n5yPooX+2qB2qZulbro7OcAm7NDCq6tc6rMZPele1PVlNeWieeWmN81zm2Zl5taESTrYpy531TsSy9ua4lzwYfr61+Hs7NrXGdhO1fqvYBqpMQ8QMdrk4CPePWVJH70vT4wJ8YvQVfj5L1vRr06K21rqeL5uqu0bGX8jhNawtu/FxFscSCf0dQ9IZ+V0vR9hbcHVlFscTC1XqoAT8ao+hxJ0V3/sXKp61V4NGvfKSk0FwuHDVjw6cOcZX+yiwEv2Qy5MZqy89Hz1+o1l3M0mpeefhS5lVrFSUoXZ8dobfKqu0e30M9PrhiupNx51+uz95WRWnfcH3vpawCRoBHtumMSlksM8z2nE2bxMu87+mdjGmmlh7XZs5mG6mtnhv2LouMO2Y1xelzT5+elavtm+5978O1bL1eLRXdWnfuRE75fVBrdK+ni7qTk1P+9u8TZEnqca2ZV1s9NxdDLEdlu7+SL142hqilgkepKCQdmwy9LDkXog+XfpY1VXRrXUHUJEW1uDYbSxmnrZ57VFfHNZ3Q+rMm15p5tdVz3frnDfJxrEhyukV7C9asplhiwfX3qFrCLeEfb5pOZY1jFJhRW4heqfqRP01DUplIx4IbG1ZRLLFw3BG65pwke52O/1FRwTAKOVpF/NRSsUkqCknFJlvW8o7wLEpnpZzqmlXtbq8t9CeOu/DZNb7vS0eYpM6WeIyqs+DuyCqKJRb4OVEPlJvRrI/6WTDSlTLp6he7omVmUIHQX6JflqD5M2BQtSlJXcb2Fvi5y4yKJRa4jGiqagTOhKKqRkh2zo5Wwb9l1BuJ17/TCiGS+A8X4SxHy6o5WeFps5ranD8v17ti68JRa4HUm4a5ku+M4Be2htxobbyF4BeqdUHEUpJLRecX41wqOr/4lUlsZlBRjl4bVekVA+kqAN6zSu1kPfasWjODithH1H7aBzypDp9f53t59Jkc9i85GYQ7QUdy2k5LrjXzaqvnuhrB8V2hxnFNrjXzaqvnctXfcaYB/rbVtGDJ6u+zKpZYyO38SlFNrmV3fo3VVs/Nz9lLZ8A9uLk5+0ht9Vwusih9p7S4loxNzqpY1LqiarvlKFXnVlqNwvf9nNriOaa0im+cA4yjQpK9ErI47ckO8nrHqYh9hGLIssjyb7SPo7SOYLK7+bStZeG4I+solljInaYgi0G15nIj8Ght9Vw/0oD4M1RfnFNbPTefY4nQiH2ismijx85mU+qoCHtrFAmVxUd3drQ7snzk0uE638+nrZ6bjxanqB7XZmLII7XVc8tOJ0nR1lz3hI9U0a11F/e963B534/VVs+V5yVJvo77WLDCzKbxiiUWcicFlK/Z13GP536sim6tY7NT8X1N2Jn3T9YjlmanjtbGWwh+oVqXOUH0+CVGR3LdKLCKYlHrmP0hEfdEe3AtuRNEU0W31mWqb0rqEbfnWjOvtnquOxnmFv7tfGntxXKUqkmV/8a3ZjXFedSrhRm8DbKe6+RH/Zlsfxba4RX6fk5tZRZobho1K40rteZaM4OKbq27WI8myG64NGO7bsF/7tdQLLHAReoT7LSiddaLJSP147VxFqJfqNax5yShCjjuv9I9jAE/6eXSPYwnH/aI3+yZSqO1pRbSmnLU1fbWsad0fDFWynMTA36AehmLzMkbeipSH6GKcFSWAYV+Zasb0nt38S5d+ilCzwtdgxDt6D0s+P39GopT36O3Yd9hnVm3ok/X0+Badt1qrLZ6LncOTbJTZkf1uJY8h2a8tnouF0N+MvEKtD/ryX7roJoa3LeOq/cxp7bYguw77OmdQUuvPJZW567jHl4eq6Jb69gafZL9jnoWLFO5b07FEgvXZz9tuVdnNGtwr9e4/az8vr5uwV6KKYxULLEwd/YC5tq/Iqdh+5PEva+jls3+Wx0N+xw033r6eICmXB0Lfp+zhmKJBT//vvwcMC2uNfNqq+fmK/yn6GiuzdT9n0+xqHVBZJmKQVHV8ai4ElUdj4q9CqvjmdUUS9BjLy4605DaVUq9f9SKdsBn3+uIn6DujqylOPX9B3kOVfyOlNaKHMkN35EVFItax+b1y86plNVqCc+0tEwGv54K5yMKlVSX8c4CDfI88ZdfirbnWjODim6tC74Q8MzqBqwE/KifxNydD/pJ38tjVZSOlLi3pi3Mfb6RvRjl0dCWt3D+QrXurAhYGk/V5Fozr7Z6Lre3OVkRC+4gqrJJV9JD1fE8Pnhe7t5zP6O22MKd4FIW7l7GFHX2Q2lOkZ4Fa1ZTLLHg3gb6nErJmZZtucfbMKO2eq6/rl6+D2As15rVFItalznJqnwXRxSPjXrENE4b8DMnWWmpiPvwNA/95MNRIH+GSZSl9+J/xfhuZSzXmtUUi1oXfAtIMnXbcq2ZQUW31nlepuMVKAaBuDoW3B1ZRbHEwtxn6mGuZVeHZ1Qsat3rjvzG+Z8nP80hHc/d7sh4Fd1aF4wN6CuR/85MvxL578x7gt5PL49XgeY5GE0t0Nx8lcdozD6ttOY6L49U0a11TWtp6ljg78iMiiUW4gqbqKoVrnWFdWhY8HuiNRRLLHAridQZ1rK6WGWZ2pZcSdRUkZtNYi5eScQzT1wVsr6uZHsLloxNz6pYYuHaTouIHzwZ9FklKXrywfzgAdAX/9KujLGKy+dEj+h7OeVT76oO15p5tdVz4yxdSWbpKK41qykWtS6TFUGh9VVZrluwbAbFjIolFuw/9v9osqJ5')).decode())

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
