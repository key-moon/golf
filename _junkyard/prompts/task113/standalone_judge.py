
import ast
import zlib
import base64
cases = ast.literal_eval(zlib.decompress(base64.b64decode(b'eJzVXVuSLKkN3Y4dwYc9c8cer2VC+9+G+041oMcRiExeNzqiK5MC6YgEIQkl9dc//vrrt/T1R6l8/p6+/r4+/5W+/oY/vy4eU8z1ZHv6Z8oov8v/TN9/uS2nM/W6SLOQM6dZeX2k/rtHUu6XP1L5M3eFoqQ/7e5nT6xH06LJuX96p/Rc4n3I6jG0jA/mflXpz97+1aTDyJAUn6f3v/T191Ujf+Y5JrgM6Z2nFHM92Z7pna+yf6evv6/P/6SvvynacZRirpfbcT3xd1n+y3Xzn35i2+9/Sn0aoeYn8RhtW8YvKvtvUn9oThwrU5r6uCSIRwzf56nI5/b33Ex5psox5WKZuAauRyOpSA6cu+idulpWnVspv7piUr/kUltUKlKaYgV9an/9/5F+fGh0/lOKtf6U6JrKxiz2Xnd2HC6hdB9qy10jZCOX6qor5s3wZxmlDyiKuZbHpB0T2/WN1T670UgO9hl+nu/n248W//RgodWcr5HWn5LPt5+aP1sZq4e0t+BazcuezQo0ri1tOFhrRnvheXT3ZgP+JODXRylqe1yNIGAfCOsMrYVsTWT9gD1QX1stLf0e4celwxQwN4wMSWFss2/daz1WW3JyfaK0F7VtFeGlEX56u8RBKFswhWtA28ZbFy31GT3f3L8sp/qnRxAp+12PO9030+9/Srgaoa6v6Wl+Eg/oRYSTxyBU2T1+p+ntjZKgtlG+FrO0RfXKJkbG0Fo5SlHoZdaOz/+qkWuPV2vQ9NqDK0qzuNQWlYq0T5SO++4vvGLeusb7K/+90mFuGBmSQsXKeFtiFgTnP+2a0hrO0NrhGp7HrJEWIx2pcZ/EpDtKO9BEOcD4CY5GfLfGpe9H95pSsnGWi6QbwYCkAJ6Y1hOa9/Z70t7UAYRNnak1BMmdXbjXMVUvruAMfSQ+952x0/QrSVvGJ8bObIS6ftO7d8aOH9HRkSAX28TVZQUaWVNS8eNnNgOEj0sY1Zg6s2Zx5nV4W07TyQAhvnsy3+afw6W2MLFOO8K7sSi8fhkPzs5OPEcXl6oZc0w6TAFzw8iQFCDLwGoCHAexFqgvwZYy0tkIhyVBPBAWi1noxfqUJ+kFqSFmczEWKc7psmPX9uLhErK5WsdRW+44B0v6MlICOTtcjpPuyOxurkAjqUgO1iPSmlw/Y+0L7s1pMivOAoS6vqan+aFVQ9dp6jrw/fpeXI1wlB6aqfVb8/QmavnZXEymVEDvuDthR/TOUzTu/mJA77S8pPk90Oud3Wh835L1Tl7jaEbe0FOKImKcsSqUwv/Pz/4VyihFoc1YO45SjMHH6DjKpxRxO7wONz0WcM/G16Z1eDbCXvs2Py+70ZYIvldY1reh7uMp859yhmmhFfr/PdeHWv+Wd1qD8djeeFt7T4F47GpEzXgMiOVzv4Ffw3H46prSPM68jken8kJ7nKsjzT3rYzcaN58l6M3s3dlAM2s3Qk0v4s3wcelFwqE2eD2zZnHmdbw9Ab0m6JVDRyD32i1o7OxGqOlpfmhlLbGb4NpY/1Mab12iT438PRStFZIi6Y+WkZO/d5MkCIvFzN9DKD764JiIty7ePDnvIaDYYtHE9zx/b0zcLgnC4u2LzIkP5E9K7ynKeEFZEyi/2VJ8u/DIjbTm5UWruvn73ZxF+2S2lhDM39+J2lLu45ExIWF5vRqRbynK9ij66Npy5ju33x7fkYk+zkETp2JXGpQpYfi8uiInH+MN7UpF5mOEcgUIrbsgk/DYukCONbNDEtT2ORbjgaMdI2SVXaCVb0PdzebQayDXBZTcGAzkOnwt1rGXnHE0x8sCRTtwsp/cmbBMy69HE+UA9SKhNd6O93VjuV8CdOBm1Jay5Y71na1nvRA7m0/apQSt0HWobatufhjofx4/KVQo4mtUjyPeushLPH5iPLjGqVZmfbwk1xOX0uCZXXulw9wwMiQFfwM56qHqsTPautaXHr2I39JT74fSOMVcLiK8JD16rgHhPiF/Gvx5vbqmNI8ztI3VtbaiuhYvmcxiOruXS3DFXIfatrKUuz5CIH/qtPW2Ak2UAzjHjfq7GE0vZfo96fPZFiDU9Xv7LLI+2gduPQF3T2jiGFuBRtZsjVvHaySbA/YsNkxpnKJXz0Qc84lnqexbyLhl7ZcHV0yLPuJiIraCitR6tUYduajVO2necEHyWypelCfiv1krX8z95SvmTtR9jwZxx1Ge8h1lu7J4X53/lGKti7VQakIPl85n9O5GIzlYjzSyoxIZC6vGPZ4JO1E/o6wRypxfoccef1J6T1G2BzEhUj4p2TdRmn04/Z50/GcDQk1P80OxHpEvTG/3wik9pygs2/LJowplzyCklatujrcuuwDEowq8D+f75d41pfWcOU0dyemNXr2qNuNUR+bXW4S99pH5ZVY1SqzMxHgfXFF6x8VEjCEVOxPgir1lJsziDG0cMBMikfT79nrOoraU+3sf+gw7s0/5ap7IGTOHS21h5PROvCK80696EPXqwTJCp1tdJgnCYjGL98UmaWBvjM3mYiLObmQ9Eknu9upi/XQWdSRmjyPr/Qj82b7FvX0bassd+6Jllae4zV8t/9HWxRZwfjXnPht4NcJRG1jisfudcC4vuaa0njOn6cX/s/WVcQhLK/xJaZyi/l7YzGrHXIyHx5+U3lMU+sCs12bHqz6RV1eUZnExe2qk12s+X7lG5vNo1git10JbTOTM23KaWgvY6KNdA6zP0rUvF5aQjjEsRm1bWcqWu0bo/1KZ0NX6afvIDpaR80tlN0mCsFjMZQ4Q3/sZs2birX+w3ag6JpRP7p6zr2xjfNb40TFxkySIB8JiMXMLt2AbHBOjrcuqZk6NmhtjkSvrbC427tI/H9e1e5fcUed83DloJBXJgXPHEX09g7SWbY7+6fcEIvqrEWp6mh9aWaG3RXIvZb6vQWkeZ14H+nLUtd6+nw8uNRrxF/0tjhukw9zieOO5t9aKWRd965dQMPd2FmrbylLux9D0ebtmb3/imjqbi6XnnF2Ackn0DtzkWbCmlHT87BeQDiNDUngz347rri91wczfiTrCC8/8yK5n1zPY3ts7UXf9Nsgde05G5xPPpTUoHurZOVyMXV5HlcldrvN6rk9GaRaX2qJSkfs2djfNPnm75tonv3cm7ERtW1nKlntzP7vdGs9SjO+aUhr81YzziMd/NaNrycPR0rVPFs+VnaifUca+kLvHL9ciiWPJndI4i9C4HguhN+PQTEMR+NBsOFYGtcZlkiAsnoZAdZHfguLOdz2VmyRBPBAWbzenzKgP/YH/lMZbF53g5iGd9COiq8ZtqPv+SOyE+fNvm+xG2LSUtS5r2qk4pmH2VfEu7/V26g3SYW4YmW+nNv0VrSe3zwkC2XCzEer6zfVbryZWb8snY+5cO2XSndLH09C4uRrmzupZsyY3fqkYzzcVmUN5jhNnVrwUrH5HpMMUMLc43pZ+x1SMVYWt8ev1+w3SYW7xcYXO85C0WpkGLsJXmmkFGllTUnEzAbxzybTNY5E2/LqTPtgpSVBbxANhsZj1XqtpTzw6bZCFryi941K/NT1Leq81f59HqLBLhj/LLHpAMdcTOzC8z/PzZHXFeBhCOUrRq8f7Uo8qfa9XwGYMf/o9gTOeZiPU9TW9Nn9vH8fqDlunqw8WlhDcx9mJ+gl3Zf2SzKWHFiDn/eqa0jzO0KZUNGNWo4nEoZ01/AyuKSXXarxXOozMtxqhd6eeOOT6esyu4Ay9YXHNT4sqUZuB/5TGW/+Zc04aGWbIzjAyhq/IyTCLckHWkaVn4+hlHoT7Mt66rILE4+hlzNBoLP97DAZbV76f54lzsrWeaMbGl98TyMlejbAdR27mZNf5SzhH5d18eMPFRH4FFRkhrDUqRzQD30nzhgua05WK1JRu3Jv03vSOqMIKNO7OpeHQzEbAeQCe/X+VzYBKCZ0Zco10mBtGhqTgv8311AoYbV08B5jJIu/caOSymbUCjRvPNBzssxFeS25Nb6IUoxSF78Paces54xfxtWF0HOVTiiIiRzKWIrWmn0Ok9d2akbYCjeudGw5Wh+dvhMXy6hk+pShssjLiwJsAdNqyRJbmaYSan8QjZkL9lrA1ZLiEr9gIf8QF2XCWSux8m/Nj4jRCzU/iae1Z47iPoI+5XlRK7p71vdJhZEgKGH3Uz3jzWwiRErJRxeOouxFDEOGGVuCSa0rrOUNL1fktiFxPaLHwZ1khBijm8lwvt+OrQaYpPP/HnxzlU4qyPf91svLsBv5TGm9deuuBv65mCZ4715TSoL9+HvG4v272OolH4Qy3B1eUZnEx2opdlWyBFzNhtHXJeniQ64WjLbfGs2gw12uVdCN041YaP1F/bL+jjp3R1iXu4ZyNmFcnoVvCnwTORuxRzOV6XeQrDepRlK+E6oU05pYyQjb8JklQ2+dYUJaiGzGQiJbckclSXIEmyoF59I9nEppZbynmdtxjFjsurI6wyYdQjlIUOVasHd+5ElqU3trFZR4+oCj2Xgva1slM99ps8VLSu8+/gHQYGZICns/i6Uj8/uMlz8l/er+adBgZkgK9yyPXL6m3XVknrkUr0Miabn64qmky5qm9M7Njf3IFGlkzysGeig5nh7qGKIavKc3j7NWHFgqyqUlZfnpebr8nbSsfQNi0g03+X+3pGXtP9YrSLC4tKvKtB5ExmGkMf5YR/oBirifbs9gRvd3d5SjfUpQ79v4Zz8iCEqMOjcSjZZTulwRhsZidMxSd9ijmdI/MhM5L3CTJGx4Ws4rlc61L8r0FiOvVNaU1nHlbTlPHwKWV4npQG+7IWGXr0UgOrlVGa38ZbDYXY6GbvGgTw54ozRwutYXZ01a5cjoa8sxeKPNwgKJXz8+Vc/fEN82v9WjcLASpjQMn9K/OHbS9sx6Nmz2keu79OV+hiNiWMnp5ztcbSULxJgeLxax3jc1KNVGLzuFi1jbSu8bFKvi0G/hPabx1sXHEnnXRnoPc462Lnia+Z43zG0ayHkQ+IM5C9MfnwlJyszf2SocpYG5xvHI/RuyoPf6k9J6isOKsDidtb+5f/9ejkVQkB6tLjYeMTxq5+iwgfwb+atJhZEgK/vtlT9eO0dbFNtczi2SMGco57VrMokWc4ZyxO4S0/h3Jnj7ZjUZy4NyRtyVtvNV7brZ31qNp0bTeFlqLUYQMrc4hnbWljJwzq3ZIgtoiHgiLxTyeOYnrYnvK4D+yBt4gHabwFpmfFYjK1s+Lt3Pqdkli+JzICT6t7pq3lOKlhKIpl0uHkSEpdITF5DlXHq+uKM3igtpKaf7Iv+5D/J39qJUcaV1ySsr/qp/KeqT+x7hHWttvqz3WyqtxR86SOzJnEqxH42cA4TMJtUXTnOF6tk2/N5pmAcKmTujy81dgpG9C2vFYGTkr8ClJony9FZjrrcLlkdaLtANaT1p54spI/uCK0iwuqK30apG3E909OTOavRF+kySIB8Li+W2tlX/OjhCld1yMz0vIXuGn7o3twdT5Otq6RETU6TxCLnYvZOt+Uhqn6NXjvl7JAnzUR6Ota32535HjCTmeLCyYoT4apZjLdR4l1/sik7h8N4qOo3xKMdfL7XjkWlqCfpbCibOy5qCRNVt5H9YulfsVMmoisboaemLvrEAja7p7oYTeqYPWGbF1gnObdk1pDWfeFtp1wp4rK8eg7ou35nWq5i0jlbiPGeUeac093TIPhex/lOyBJ7JHWvN8hir77yzHYrzn4615L4noBbD68V49m2N45l1VSm50+l7pMDIkhXh6VY8Rzqw0fMNXrBcfcTEaR1CR0rj5WXRid289GklFcuDc0d6nrC3X0B2r9go0sqabVUFo79Pux9l51PU5t5aoXjyA2lK23DXCftbz/PE2NhZ3ZynY3hERaJrh7Y5S1N6uiFF7bynhaAj+vSj06/TXrKNKex+TDlPA3DAyJAV+s7a5+60RLr8n8GbtaoSanuYn8cB9ZPscDq8ReNW4DbXlrhGCfGzzROzvrTbn3pIxuxphr32bn797bji+umJjbBoXG93232BWdombqRLKG9pSRs4bzDskQW2jfL3MX71uarl643ztvVnfDyDU/NAa3bQotN40NHb04mqETfsL8ENj0WjDJfpuNhej09VZiMK/yi2HPyk9p4jbgR1psC41ddWWkbsbYdua1CMbvf3q6qcNd2Tefl2PRnKwsUsb+7Al4ilcYXvfhrqPR//KmME5UYvO5lKpyJmFPWvldVyfN4tKyX2z8wbpMDeMDEnROgURR0B+vad3r3SYG0aGpGg9vfgYuPsk8BukwxRGtAJ+evR/BPw6UQ==')).decode())

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
