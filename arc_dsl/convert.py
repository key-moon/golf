import re
from const import task2arc, consts

def extract_functions(file_path):
  with open(file_path, 'r') as file:
    code = file.read()
  function_pattern = re.compile(r'(def (\w+)\s*\([^)]*?\):\n(?:    [^\n]*\n)+)')
  functions = function_pattern.findall(code)
  return functions

dsl_funcs = extract_functions("arc_dsl/dsl.py")
solver_funcs = extract_functions("arc_dsl/solvers.py")

dep_re = r"(?<!\.)(\w+)"

def resolve_dependencies(impl: str):
  dependencies = set()
  queue = [impl]
  impls = [impl]

  while queue:
      current_impl = queue.pop()
      matches = re.findall(dep_re, current_impl)
      for func_impl, name in dsl_funcs:          
          if name in matches and name not in dependencies:
              dependencies.add(name)
              queue.append(func_impl)
              impls.append(func_impl)

  return dependencies, impls

for i in range(1,401):
  task = f"task{i:03}"
  arc = task2arc[task]
  solver = [impl for impl, name in solver_funcs if arc in name][0]
  solver = solver.replace(f"solve_{arc}", "p")
  solver=solver.replace(":", ":\n    I=tuple(map(tuple,I))")
  solver=solver.replace("return O", "return [*map(list,O)]")

  deps, impls = resolve_dependencies(solver)
  impl = "\n".join(impls[::-1])
  for dep in deps:
    impl = re.sub(rf"(?<!\.){dep}", f"val_func_{dep}", impl)
  for name, val in reversed(consts.items()):
    impl = impl.replace(name, repr(val))
  open(f"base_arcdsl/{task}.py", "w").write(impl)